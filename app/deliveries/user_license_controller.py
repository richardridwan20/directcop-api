from fastapi import Depends, APIRouter, HTTPException, status
from typing import List
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session
from app.schemas import user_license_schema, token_schema
from app.usecases.user_license_service import UserLicenseService as usecase
from app.middlewares import deps, di, auth

router = APIRouter()
local_prefix = "/user_licenses/"

class UserLicenseController():

    @router.post("/users/{user_id}"+local_prefix,
                response_model=user_license_schema.UserLicense)
    def create_user_license_for_user(
                user_id: str,
                user_license: user_license_schema.UserLicenseCreate,
                db: Session = Depends(deps.get_db)
            ):
        return usecase.create(db=db, user_license=user_license, user_id=user_id)

    @router.put(local_prefix+"{user_license_id}",
                response_model=user_license_schema.UserLicense)
    def update_user_license(
                user_license_id: str,
                user_license: user_license_schema.UserLicenseUpdate,
                db: Session = Depends(deps.get_db)
            ):
        db_user_license = usecase.read(db, user_license_id=user_license_id)
        if db_user_license is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User License not found")
        return usecase.update(db=db, user_license=user_license, user_license_id=user_license_id)

    @router.get(local_prefix,
                response_model=List[user_license_schema.UserLicense])
    def read_user_licenses(
                commons: dict = Depends(di.common_parameters),
                db: Session = Depends(deps.get_db)
            ):
        user_licenses = usecase.reads(
                db,
                skip=commons['skip'],
                limit=commons['limit']
            )
        return user_licenses

    @router.get(local_prefix+"{user_license_id}",
                response_model=user_license_schema.UserLicense)
    def read_user_license(user_license_id: str, db: Session = Depends(deps.get_db)):
        db_user_license = usecase.read(db, user_license_id=user_license_id)
        if db_user_license is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User License not found")
        return db_user_license

    @router.delete(local_prefix,
                    response_model=user_license_schema.UserLicense)
    def delete_user_license(
                user_license: user_license_schema.UserLicenseId,
                db: Session = Depends(deps.get_db)
            ):
        db_user_license = usecase.read(db, user_license_id=user_license.id)
        if db_user_license is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User License not found")
        return usecase.delete(db=db, user_license_id=user_license.id)

    @router.get(local_prefix+"validate/",
                response_model=user_license_schema.UserLicense)
    def validate_license(user_license_id: str, db: Session = Depends(deps.get_db)):
        db_user_license = usecase.read(db, user_license_id=user_license_id)
        if db_user_license is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User License not found")
        date = datetime.fromisoformat(db_user_license.end_date)
        if datetime.now() > date:
            raise HTTPException(status_code=400, detail="Expired license, please contact admistrator for further details")
        
        return db_user_license
