from sqlalchemy.orm import Session
from sqlalchemy import desc, asc

from app.interfaces.api_interfaces import RepositoryInterface
from app.models import user_license_model
from app.schemas import user_license_schema
from app.utils.uuid import generate_uuid

class UserLicenseRepository(RepositoryInterface):

    def reads(db: Session, skip: int = 0, limit: int = 100, order: str = 'asc', sort: str = 'id'):
        if order == 'asc':
            return db.query(
                user_license_model.UserLicense
            ).filter(user_license_model.UserLicense.status != 'inactive').order_by(asc(sort)).offset(skip).limit(limit).all()
            pass
        else:
            return db.query(
                user_license_model.UserLicense
            ).filter(user_license_model.UserLicense.status != 'inactive').order_by(desc(sort)).offset(skip).limit(limit).all()
            pass

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
