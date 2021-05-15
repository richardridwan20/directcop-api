from fastapi import Depends, APIRouter, HTTPException, status
from typing import List
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session
from app.schemas import provider_schema, token_schema
from app.usecases.provider_service import ProviderService as usecase
from app.middlewares import deps, di, auth

router = APIRouter()
local_prefix = "/providers/"

class ProviderController():

    @router.post("/users/{user_id}"+local_prefix,
                response_model=provider_schema.Provider)
    def create_provider_for_user(
                user_id: str,
                provider: provider_schema.ProviderCreate,
                db: Session = Depends(deps.get_db)
            ):
        return usecase.create(db=db, provider=provider, user_id=user_id)

    @router.put(local_prefix+"{provider_id}",
                response_model=provider_schema.Provider)
    def update_provider(
                provider_id: str,
                provider: provider_schema.ProviderUpdate,
                db: Session = Depends(deps.get_db)
            ):
        db_provider = usecase.read(db, provider_id=provider_id)
        if db_provider is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Provider not found")
        return usecase.update(db=db, provider=provider, provider_id=provider_id)

    @router.get(local_prefix,
                response_model=List[provider_schema.Provider])
    def read_providers(
                commons: dict = Depends(di.common_parameters),
                db: Session = Depends(deps.get_db)
            ):
        providers = usecase.reads(
                db,
                skip=commons['skip'],
                limit=commons['limit']
            )
        return providers

    @router.get(local_prefix+"{provider_id}",
                response_model=provider_schema.Provider)
    def read_provider(provider_id: str, db: Session = Depends(deps.get_db)):
        db_provider = usecase.read(db, provider_id=provider_id)
        if db_provider is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Provider not found")
        return db_provider

    @router.delete(local_prefix,
                    response_model=provider_schema.Provider)
    def delete_provider(
                provider: provider_schema.ProviderId,
                db: Session = Depends(deps.get_db)
            ):
        db_provider = usecase.read(db, provider_id=provider.id)
        if db_provider is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Provider not found")
        return usecase.delete(db=db, provider_id=provider.id)
