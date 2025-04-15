
from app.core.entities.campaign import CampaignEntity, StepEntity
import itertools


class CampaignRepository:
    def __init__(self):
        self.campaigns = []
        self.step_id_counter = itertools.count(1)
        self.campaign_id_counter = itertools.count(1)

    def get_all(self):
        return self.campaigns

    def get_by_id(self, campaign_id):
        return next((c for c in self.campaigns if c.id == campaign_id), None)

    def create_campaign(self, name, steps_data):
        campaign_id = next(self.campaign_id_counter)
        steps = []
        for i, step in enumerate(steps_data):
            step_entity = StepEntity(
                id=next(self.step_id_counter),
                name=step['name'],
                order=i + 1,
                completed=False
            )
            steps.append(step_entity)
        campaign = CampaignEntity(id=campaign_id, name=name, steps=steps)
        self.campaigns.append(campaign)
        return campaign

    def mark_step_complete(self, campaign_id, step_id):
        campaign = self.get_by_id(campaign_id)
        if campaign:
            for step in campaign.steps:
                if step.id == step_id:
                    step.completed = True
                    return campaign
        raise ValueError("Step not found")
