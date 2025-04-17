import logging

from dependency_injector.wiring import inject, Provide
from flask import Blueprint, request, jsonify

from app.container import Container
from app.core.exceptions.exceptions import BusinessException
from app.core.use_cases.campaign_service import CampaignService

bp = Blueprint('campaign', __name__, url_prefix='/campaigns')
logger = logging.getLogger(__name__)


@bp.route('/', methods=['GET'])
@inject
def list_campaigns(service: CampaignService = Provide[Container.campaign_service]):
    logger.info("GET /campaigns - List all campaigns")
    campaigns = service.list_campaigns()
    return jsonify([campaign.model_dump() for campaign in campaigns]), 200


@bp.route('/', methods=['POST'])
@inject
def create_campaign(service: CampaignService = Provide[Container.campaign_service]):
    data = request.get_json()
    logger.info("POST /campaigns - Create campaign with payload: %s", data)
    try:
        campaign = service.create_campaign(data)
        logger.info("Campaign created successfully: ID=%s", campaign.id)
        return jsonify(campaign.model_dump()), 201
    except BusinessException as be:
        logger.warning("Business error creating campaign: %s", be)
        return jsonify({'error': str(be)}), 400


@bp.route('/<int:campaign_id>', methods=['GET'])
@inject
def get_campaign(campaign_id: int, service: CampaignService = Provide[Container.campaign_service]):
    logger.info("GET /campaigns/%s - Retrieve campaign", campaign_id)
    try:
        campaign = service.get_campaign(campaign_id)
        return jsonify(campaign.model_dump()), 200
    except BusinessException as be:
        logger.warning("Business error retrieving campaign %s: %s", campaign_id, be)
        return jsonify({'error': str(be)}), 404


@bp.route('/<int:campaign_id>/steps/<int:step_id>', methods=['PUT'])
@inject
def complete_step(campaign_id: int, step_id: int, service: CampaignService = Provide[Container.campaign_service]):
    logger.info("PUT /campaigns/%s/steps/%s - Complete step", campaign_id, step_id)
    try:
        campaign = service.complete_step(campaign_id, step_id)
        logger.info("Step %s completed successfully in campaign %s", step_id, campaign_id)
        return jsonify(campaign.model_dump()), 200
    except BusinessException as be:
        logger.warning("Business error completing step %s for campaign %s: %s", step_id, campaign_id, be)
        return jsonify({'error': str(be)}), 400
