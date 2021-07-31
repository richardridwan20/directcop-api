from sqlalchemy.orm import Session
from sqlalchemy import desc, asc

from sqlalchemy_filters import apply_pagination, apply_sort, apply_filters

from app.interfaces.api_interfaces import RepositoryInterface
from app.models import user_license_model
from app.schemas import user_license_schema
from app.utils.uuid import generate_uuid

class UserLicenseRepository(RepositoryInterface):

    def reads(db: Session, skip: int = 1, limit: int = 100, order: str = 'asc', sort: str = 'id', filter_field: str = None, filter_value: str = None,):
        #Begin SQLAlchemy Query
        query = db.query(
            user_license_model.UserLicense
        )
        
        #Begin Filter Function
        filter_spec = [
            {'field': 'status', 'op': '!=', 'value': 'inactive'}
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

    def read(db: Session, user_license_id: str):
        return db.query(
            user_license_model.UserLicense
        ).filter(user_license_model.UserLicense.id == user_license_id).first()
        
    def read_by_user_id(db: Session, user_id: str):
        return db.query(
            user_license_model.UserLicense
        ).filter(user_license_model.UserLicense.user_id == user_id).first()

    def create(
            db: Session,
            user_license: user_license_schema.UserLicenseCreate,
            user_id: str):
        uuid = generate_uuid()
        db_user_license = user_license_model.UserLicense(**user_license.dict(), id=uuid, status='active')
        db.add(db_user_license)
        db.commit()
        db.refresh(db_user_license)
        return db_user_license

    def update(db: Session, user_license: user_license_schema.UserLicenseUpdate, user_license_id: str):
        db.query(
            user_license_model.UserLicense
        ).filter(
            user_license_model.UserLicense.id == user_license_id
        ).update({
            user_license_model.UserLicense.user_id: user_license.user_id,
            user_license_model.UserLicense.license_type: user_license.license_type,
            user_license_model.UserLicense.start_date: user_license.start_date,
            user_license_model.UserLicense.end_date: user_license.end_date
        })

        db.commit()
        return db.query(
            user_license_model.UserLicense
        ).filter(user_license_model.UserLicense.id == user_license_id).first()

    def delete(db: Session, user_license_id: str):
        db_user_license = db.query(
            user_license_model.UserLicense
        ).filter(user_license_model.UserLicense.id == user_license_id).first()
        # use this one for hard delete:
        # db.delete(db_user_license)
        # use this one for soft delete (is_active)
        db.query(
            user_license_model.UserLicense
        ).filter(
            user_license_model.UserLicense.id == user_license_id
        ).update({
            user_license_model.UserLicense.status: 'inactive',
        })

        db.commit()
        return db_user_license
