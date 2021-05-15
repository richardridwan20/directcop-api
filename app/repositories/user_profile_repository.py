from sqlalchemy.orm import Session

from app.interfaces.api_interfaces import RepositoryInterface
from app.models import user_profile_model
from app.schemas import user_profile_schema
from app.utils.uuid import generate_uuid

class UserProfileRepository(RepositoryInterface):

    def reads(db: Session, skip: int = 0, limit: int = 100):
        return db.query(
            user_profile_model.UserProfile
        ).offset(skip).limit(limit).all()

    def read(db: Session, user_profile_id: int):
        return db.query(
            user_profile_model.UserProfile
        ).filter(user_profile_model.UserProfile.id == user_profile_id).first()

    def create(
            db: Session,
            user_profile: user_profile_schema.UserProfileCreate,
            user_id: str):
        uuid = generate_uuid()
        db_user_profile = user_profile_model.UserProfile(**user_profile.dict(), id=uuid)
        db.add(db_user_profile)
        db.commit()
        db.refresh(db_user_profile)
        return db_user_profile

    def update(db: Session, user_profile: user_profile_schema.UserProfileCreate, user_profile_id: str):
        db.query(
            user_profile_model.UserProfile
        ).filter(
            user_profile_model.UserProfile.id == user_profile_id
        ).update({
            user_profile_model.UserProfile.user_id: user_profile.user_id,
            user_profile_model.UserProfile.provider_id: user_profile.provider_id,
            user_profile_model.UserProfile.first_name: user_profile.first_name,
            user_profile_model.UserProfile.last_name: user_profile.last_name,
            user_profile_model.UserProfile.address: user_profile.address,
            user_profile_model.UserProfile.postal_code: user_profile.postal_code,
            user_profile_model.UserProfile.city: user_profile.city,
            user_profile_model.UserProfile.phone_number: user_profile.phone_number,
            user_profile_model.UserProfile.email: user_profile.email
        })

        db.commit()
        return db.query(
            user_profile_model.UserProfile
        ).filter(user_profile_model.UserProfile.id == user_profile_id).first()

    def delete(db: Session, user_profile_id: str):
        db_user_profile = db.query(
            user_profile_model.UserProfile
        ).filter(user_profile_model.UserProfile.id == user_profile_id).first()
        # use this one for hard delete:
        # db.delete(db_user_profile)
        # use this one for soft delete (is_active)
        db.query(
            user_profile_model.UserProfile
        ).filter(
            user_profile_model.UserProfile.id == user_profile_id
        ).update({
            user_profile_model.UserProfile.is_active: 0,
        })

        db.commit()
        return db_user_profile
