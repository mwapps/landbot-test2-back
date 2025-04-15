from app.main import create_app


def test_endpoints():
    app = create_app()
    client = app.test_client()

    # Create campaign
    response = client.post('/campaigns/', json={
        "name": "Test Campaign",
        "steps": [{"name": "Step 1"}, {"name": "Step 2"}]
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data["name"] == "Test Campaign"

    # List campaigns
    response = client.get('/campaigns/')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

    # Get campaign
    response = client.get('/campaigns/1')
    assert response.status_code == 200
    assert response.get_json()["id"] == 1

    # Complete first step
    response = client.put('/campaigns/1/steps/1')
    assert response.status_code == 200
    assert response.get_json()["steps"][0]["completed"] is True

    # Attempt to complete second step (now valid)
    response = client.put('/campaigns/1/steps/2')
    assert response.status_code == 200
    assert response.get_json()["steps"][1]["completed"] is True


def test_create_campaign_with_invalid_payload():
    app = create_app()
    client = app.test_client()

    response = client.post("/campaigns/", json={"name": "", "steps": []})
    assert response.status_code == 400
    assert "error" in response.get_json()
