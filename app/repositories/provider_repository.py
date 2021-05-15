from sqlalchemy.orm import Session

from app.interfaces.api_interfaces import RepositoryInterface
from app.models import provider_model
from app.schemas import provider_schema
from app.utils.uuid import generate_uuid

class ProviderRepository(RepositoryInterface):

    def reads(db: Session, skip: int = 0, limit: int = 100):
        return db.query(
            provider_model.Provider
        ).offset(skip).limit(limit).all()

    def read(db: Session, provider_id: int):
        return db.query(
            provider_model.Provider
        ).filter(provider_model.Provider.id == provider_id).first()

    def create(
            db: Session,
            provider: provider_schema.ProviderCreate,
            user_id: str):
        uuid = generate_uuid()
        db_provider = provider_model.Provider(**provider.dict(), id=uuid)
        db.add(db_provider)
        db.commit()
        db.refresh(db_provider)
        return db_provider

    def update(db: Session, provider: provider_schema.ProviderUpdate, provider_id: str):
        db.query(
            provider_model.Provider
        ).filter(
            provider_model.Provider.id == provider_id
        ).update({
            provider_model.Provider.name: provider.name,
            provider_model.Provider.slug: provider.slug,
            provider_model.Provider.url: provider.url
        })

        db.commit()
        return db.query(
            provider_model.Provider
        ).filter(provider_model.Provider.id == provider_id).first()

    def delete(db: Session, provider_id: str):
        db_provider = db.query(
            provider_model.Provider
        ).filter(provider_model.Provider.id == provider_id).first()
        # use this one for hard delete:
        # db.delete(db_provider)
        # use this one for soft delete (is_active)
        db.query(
            provider_model.Provider
        ).filter(
            provider_model.Provider.id == provider_id
        ).update({
            provider_model.Provider.is_active: 0,
        })

        db.commit()
        return db_provider
