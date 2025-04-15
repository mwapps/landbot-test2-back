# Landbot Backend Challenge – Implementation

This repository contains an implementation of the technical challenge described in the original Landbot backend test repository:

🔗 https://github.com/enocmatz/landbot-test2-back

The project is built with Flask, using **Hexagonal Architecture** to keep core logic framework-agnostic and easy to migrate if necessary.

---

## 🧱 Architecture

The core principles applied include:

- **Hexagonal Architecture (Ports and Adapters)**: The domain logic remains isolated from external frameworks and infrastructure.
- **Dependency Injection**: Managed via [`dependency_injector`](https://python-dependency-injector.ets-labs.org/).
- **Pydantic Entities**: Used for strict data validation in the domain layer.
- **Custom Business Exceptions**: `BusinessException` handles domain errors gracefully.
- **Logging**: Configurable logging levels based on environment.
- **Testing**: Unit and functional tests using `pytest`.

---

## 📂 Folder Structure

```
.
├── app/
│   ├── main.py                       # App factory & Flask setup
│   ├── config.py                     # Centralised configuration
│   ├── container.py                  # Dependency Injection container
│   ├── adapters/
│   │   ├── controllers/
│   │   │   └── campaign_controller.py
│   │   ├── db/
│   │   │   └── models.py             # SQLAlchemy models
│   │   └── repositories/
│   │       └── campaign_repository.py
│   ├── core/
│   │   ├── entities/
│   │   │   └── campaign.py           # Domain models (Pydantic)
│   │   ├── exceptions/
│   │   │   └── exceptions.py         # BusinessException
│   │   └── use_cases/
│   │       └── campaign_service.py
│   └── utils/
│       └── logging_config.py         # Logging initialisation
├── tests/
│   ├── test_campaign.py              # Unit tests
│   └── test_functional.py            # Endpoint tests (with Flask client)
├── docker-compose.yml
├── Dockerfile
├── .env.dev
├── pyproject.toml
├── README.md
└── tests/postman/
    ├── landbot_campaign_api.postman_collection.json
    └── landbot_env.json
```

---

## 🐳 Running the Project Locally (Dev Mode)

You can build and run the service locally using Docker Compose.

### 1️⃣ Start the service:

```bash
docker-compose up --build
```

By default, the service will be available at:  
👉 http://localhost:8090

---

## 🧪 Running Tests

From your local terminal (outside Docker):

```bash
pytest tests/
```

This will run both:
- Unit tests for the business logic
- Functional tests for the REST API

---

## 📮 Postman

To test the API manually:

1. Start the service with Docker (`localhost:8090`)
2. Import the collection:
   - `tests/postman/landbot_campaign_api.postman_collection.json`
   - Optional: Use `landbot_env.json` to define `{{base_url}}` as `http://localhost:8090`
3. Run the requests: list, create, get, complete steps.

---

## ⚙️ Environment Variables

Dev mode expects an `.env.dev` file like:

```
DEBUG=True
LOGGING_LEVEL=DEBUG
DATABASE_URL=sqlite:///campaigns.db
```

You can override logging level to `INFO`, `WARNING`, etc.

---

## ℹ️ Notes

- All logic errors raise custom `BusinessException`, properly handled in controllers.
- SQLAlchemy is used with SQLite for persistence in development.

---

Built with ❤️ by Omar Manrique  
For questions or feedback, feel free to reach out.
