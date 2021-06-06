from sqlalchemy.orm import Session

from app.interfaces.api_interfaces import ServiceInterface
from app.repositories.user_license_repository import UserLicenseRepository as repository
from app.schemas import user_license_schema as schema


class UserLicenseService(ServiceInterface):

    def reads(db: Session, skip: int = 0, limit: int = 100, order: str = 'asc', sort: str = 'id'):
        return repository.reads(db, skip=skip, limit=limit, order=order, sort=sort)

    def read(db: Session, user_license_id: str):
        return repository.read(db, user_license_id=user_license_id)
    
    def read_by_user_id(db: Session, user_id: str):
        return repository.read_by_user_id(db, user_id=user_id)

    def create(db: Session,
               user_license: schema.UserLicenseCreate,
               user_id: str):
        return repository.create(
            db=db,
            user_license=user_license,
            user_id=user_id)

    def update(db: Session, user_license: schema.UserLicenseUpdate, user_license_id: str):
        return repository.update(db=db, user_license=user_license, user_license_id=user_license_id)

    def delete(db: Session, user_license_id: str):
        return repository.delete(db=db, user_license_id=user_license_id)
