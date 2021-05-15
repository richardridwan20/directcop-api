from fastapi import APIRouter, Depends
from app.deliveries import (
        item_controller,
        user_controller,
        user_profile_controller,
        user_license_controller,
        provider_controller,
    )
from app.middlewares import auth

api = APIRouter()


api.include_router(
    user_controller.router,
    tags=["users"])
api.include_router(
    item_controller.router,
    tags=["items"],
    dependencies=[Depends(auth.get_current_active_user)],
    responses={404: {"description": "Not found"}},
)
api.include_router(
    user_profile_controller.router,
    tags=["user_profiles"],
    dependencies=[Depends(auth.get_current_active_user)],
    responses={404: {"description": "Not found"}},
)
api.include_router(
    user_license_controller.router,
    tags=["user_licenses"],
    dependencies=[Depends(auth.get_current_active_user)],
    responses={404: {"description": "Not found"}},
)
api.include_router(
    provider_controller.router,
    tags=["providers"],
    dependencies=[Depends(auth.get_current_active_user)],
    responses={404: {"description": "Not found"}},
)
