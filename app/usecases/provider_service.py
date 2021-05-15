from sqlalchemy.orm import Session

from app.interfaces.api_interfaces import ServiceInterface
from app.repositories.provider_repository import ProviderRepository as repository
from app.schemas import provider_schema as schema


class ProviderService(ServiceInterface):

    def reads(db: Session, skip: int = 0, limit: int = 100):
        return repository.reads(db, skip=skip, limit=limit)

    def read(db: Session, provider_id: str):
        return repository.read(db, provider_id=provider_id)

    def create(db: Session,
               provider: schema.ProviderCreate,
               user_id: str):
        return repository.create(
            db=db,
            provider=provider,
            user_id=user_id)

    def update(db: Session, provider: schema.ProviderUpdate, provider_id: str):
        return repository.update(db=db, provider=provider, provider_id=provider_id)

    def delete(db: Session, provider_id: str):
        return repository.delete(db=db, provider_id=provider_id)
