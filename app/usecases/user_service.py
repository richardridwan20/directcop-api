from sqlalchemy.orm import Session

from app.interfaces.api_interfaces import ServiceInterface
from app.repositories.user_repository import UserRepository as repository
from app.schemas import user_schema as schema


class UserService(ServiceInterface):

    def read(db: Session, user_id: int):
        return repository.read(db, user_id=user_id)

    def read_by_email(db: Session, email: str):
        return repository.read_by_email(db, email=email)

    def reads(db: Session, skip: int = 1, limit: int = 100, order: str = 'asc', sort: str = 'id', filter_field: str = None, filter_value: str = None,):
        return repository.reads(db, skip=skip, limit=limit, order=order, sort=sort, filter_field=filter_field, filter_value=filter_value)

    def create(db: Session, user: schema.UserCreate):
        return repository.create(db=db, user=user)

    def update(db: Session, user: schema.UserCreate, user_id: str):
        return repository.update(db=db, user=user, user_id=user_id)

    def delete(db: Session, user_id: str):
        return repository.delete(db=db, user_id=user_id)
