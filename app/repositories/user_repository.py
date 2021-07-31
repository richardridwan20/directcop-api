from sqlalchemy.orm import Session

from sqlalchemy_filters import apply_pagination, apply_sort, apply_filters

from app.interfaces.api_interfaces import RepositoryInterface
from app.models import user_model
from app.schemas import user_schema
from app.utils.hash import create_hashing
from app.utils.uuid import generate_uuid

class UserRepository(RepositoryInterface):

    def read(db: Session, user_id: int):
        return db.query(
            user_model.User
        ).filter(user_model.User.id == user_id).first()

    def read_by_email(db: Session, email: str):
        return db.query(
            user_model.User
        ).filter(user_model.User.email == email).first()

    def reads(db: Session, skip: int = 1, limit: int = 100, order: str = 'asc', sort: str = 'id', filter_field: str = None, filter_value: str = None,):
        #Begin SQLAlchemy Query
        query = db.query(
            user_model.User
        )
        
        #Begin Filter Function
        filter_spec = [
            {'field': 'is_active', 'op': '==', 'value': True}
        ]
        
        #If filter_field and filter_value is not None
        if filter_field and filter_value:
            filter_spec.append({'field': filter_field, 'op': 'like', 'value': f'%{filter_value}%'})
            pass
        
        filtered_query = apply_filters(query, filter_spec)
        
        #Begin Sort Function
        sort_spec = [
            {'field': sort, 'direction': order}
        ]
        sorted_query = apply_sort(filtered_query, sort_spec)
        
        #Begin Pagination Function
        sorted_query, pagination = apply_pagination(sorted_query, page_number=skip, page_size=limit)

        #Return with Data and Meta
        return {
            'data': sorted_query.all(),
            'meta': {
                'page_size': pagination.page_size,
                'page_number': pagination.page_number,
                'num_pages': pagination.num_pages,
                'total_results': pagination.total_results
            }
        }

    def create(db: Session, user: user_schema.UserCreate):
        uuid = generate_uuid()
        hashpass = create_hashing(user.password)
        db_user = user_model.User(
            id=uuid,
            full_name=user.full_name,
            email=user.email,
            hashed_password=hashpass)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def update(db: Session, user: user_schema.UserCreate, user_id: str):
        hashpass = create_hashing(user.password)
        db.query(
            user_model.User
        ).filter(
            user_model.User.id == user_id
        ).update({
            user_model.User.full_name: user.full_name,
            user_model.User.email: user.email,
            user_model.User.hashed_password: hashpass,
            user_model.User.is_active: user.is_active
        })
        db.commit()
        return db.query(
            user_model.User
        ).filter(user_model.User.id == user_id).first()

    def delete(db: Session, user_id: str):
        db_user = db.query(
            user_model.User
        ).filter(user_model.User.id == user_id).first()
        # use this one for hard delete:
        # db.delete(db_user)
        # use this one for soft delete (is_active)
        db.query(
            user_model.User
        ).filter(
            user_model.User.id == user_id
        ).update({
            user_model.User.is_active: 0,
        })

        db.commit()
        return db_user
