from fastapi import Depends, APIRouter, HTTPException, status
from typing import List
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session
from app.schemas import user_profile_schema, token_schema
from app.usecases.user_profile_service import UserProfileService as usecase
from app.middlewares import deps, di, auth

router = APIRouter()
local_prefix = "/user_profiles/"

class UserProfileController():

    @router.post("/users/{user_id}"+local_prefix,
                response_model=user_profile_schema.UserProfile)
    def create_user_profile_for_user(
                user_id: str,
                user_profile: user_profile_schema.UserProfileCreate,
                db: Session = Depends(deps.get_db)
            ):
        return usecase.create(db=db, user_profile=user_profile, user_id=user_id)

    @router.put(local_prefix+"{user_profile_id}",
                response_model=user_profile_schema.UserProfile)
    def update_user_profile(
                user_profile_id: str,
                user_profile: user_profile_schema.UserProfileUpdate,
                db: Session = Depends(deps.get_db)
            ):
        db_user_profile = usecase.read(db, user_profile_id=user_profile_id)
        if db_user_profile is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User Profile not found")
        return usecase.update(db=db, user_profile=user_profile, user_profile_id=user_profile_id)

    @router.get(local_prefix+"filter/"+"{user_id}",
                response_model=List[user_profile_schema.UserProfile])
    def read_user_profiles(
                user_id: str,
                commons: dict = Depends(di.common_parameters),
                db: Session = Depends(deps.get_db)
            ):
        user_profiles = usecase.reads(
                db,
                skip=commons['skip'],
                limit=commons['limit'],
                user_id=user_id
            )
        return user_profiles

    @router.get(local_prefix+"{user_profile_id}",
                response_model=user_profile_schema.UserProfile)
    def read_user_profile(user_profile_id: str, db: Session = Depends(deps.get_db)):
        db_user_profile = usecase.read(db, user_profile_id=user_profile_id)
        if db_user_profile is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User Profile not found")
        return db_user_profile

    @router.delete(local_prefix,
                    response_model=user_profile_schema.UserProfile)
    def delete_user_profile(
                user_profile: user_profile_schema.UserProfileId,
                db: Session = Depends(deps.get_db)
            ):
        db_user_profile = usecase.read(db, user_profile_id=user_profile.id)
        if db_user_profile is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User Profile not found")
        return usecase.delete(db=db, user_profile_id=user_profile.id)
