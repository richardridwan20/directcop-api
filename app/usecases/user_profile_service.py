from sqlalchemy.orm import Session

from app.interfaces.api_interfaces import ServiceInterface
from app.repositories.user_profile_repository import UserProfileRepository as repository
from app.schemas import user_profile_schema as schema


class UserProfileService(ServiceInterface):

    def reads(db: Session, skip: int = 0, limit: int = 100, user_id: str = None):
        return repository.reads(db, skip=skip, limit=limit, user_id=user_id)

    def read(db: Session, user_profile_id: str):
        return repository.read(db, user_profile_id=user_profile_id)

    def create(db: Session,
               user_profile: schema.UserProfileCreate,
               user_id: str):
        return repository.create(
            db=db,
            user_profile=user_profile,
            user_id=user_id)

    def update(db: Session, user_profile: schema.UserProfileUpdate, user_profile_id: str):
        return repository.update(db=db, user_profile=user_profile, user_profile_id=user_profile_id)

    def delete(db: Session, user_profile_id: str):
        return repository.delete(db=db, user_profile_id=user_profile_id)
