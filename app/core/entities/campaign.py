
from pydantic import BaseModel
from typing import List


class StepEntity(BaseModel):
    id: int
    name: str
    order: int
    completed: bool


class CampaignEntity(BaseModel):
    id: int
    name: str
    steps: List[StepEntity]
