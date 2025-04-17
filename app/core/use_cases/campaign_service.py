import logging

from app.adapters.repositories.campaign_repository import CampaignRepository
from app.core.exceptions.exceptions import BusinessException


class CampaignService:
    def __init__(self, repository: CampaignRepository):
        self.repository = repository
        self.logger = logging.getLogger(self.__class__.__name__)

    def list_campaigns(self):
        self.logger.info("list campaigns")
        return self.repository.get_all()

    def create_campaign(self, data):
        self.logger.info(f"Create campaign {data.get('name')}")

        name = data.get('name')
        steps_data = data.get('steps', [])
        if not name or not steps_data:
            raise BusinessException("Name and steps are required")

        campaign = self.repository.create_campaign(name, steps_data)
        return campaign

    def get_campaign(self, campaign_id):
        self.logger.info(f"get campaign {campaign_id}")
        campaign = self.repository.get_by_id(campaign_id)
        if not campaign:
            raise BusinessException("Campaign not found")
        return campaign

    def complete_step(self, campaign_id, step_id):
        self.logger.info(f"Complete step {campaign_id}, {step_id}")
        campaign = self.repository.get_by_id(campaign_id)
        if not campaign:
            raise BusinessException("Campaign not found")

        # Validate the previous step was completed
        step = next((s for s in campaign.steps if s.id == step_id), None)
        if not step:
            raise BusinessException("Step not found")

        if step.order > 1:
            prev_step = next((s for s in campaign.steps if s.order == step.order - 1), None)
            if not prev_step or not prev_step.completed:
                raise BusinessException("Previous step must be completed")

        updated_campaign = self.repository.mark_step_complete(campaign_id, step_id)
        return updated_campaign
