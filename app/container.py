
from dependency_injector import containers, providers
from app.adapters.repositories.campaign_repository import CampaignRepository
from app.core.use_cases.campaign_service import CampaignService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=["app.adapters.controllers"])

    campaign_repository = providers.Singleton(CampaignRepository)
    campaign_service = providers.Factory(
        CampaignService,
        repository=campaign_repository
    )
