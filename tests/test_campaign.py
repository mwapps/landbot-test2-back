import pytest
from app.core.use_cases.campaign_service import CampaignService
from app.core.exceptions import BusinessException


class DummyRepository:
    def create_campaign(self, name, steps): pass
    def get_all(self): return []
    def get_by_id(self, campaign_id): return None


def test_create_campaign_with_invalid_data():
    service = CampaignService(DummyRepository())

    with pytest.raises(BusinessException) as excinfo:
        service.create_campaign({"name": "", "steps": []})

    assert "Name and steps are required" in str(excinfo.value)
