# API reference — Majid Al-Sakani | ماجد السكني

Reviewed 2026-11-16 from the actual source. This repository currently implements a demonstration scaffold, NOT production authentication. Earlier production-readiness claims describe goals rather than verified capabilities.

## Run / Swagger

```sh
pip install -r requirements.txt
uvicorn app.main:app --reload
curl -i http://127.0.0.1:8000/docs
curl -i http://127.0.0.1:8000/redoc
curl -fsS http://127.0.0.1:8000/openapi.json > openapi.json
```

`/docs` is Swagger UI, `/redoc` is ReDoc and `/openapi.json` is the generated contract. These are GET endpoints.

## GET /

No parameters, body or authentication. HTTP 200, static service information, NOT database readiness.

```sh
curl -i http://127.0.0.1:8000/
```
```json
{"status":"running","project":"enterprise backend system","author":"Majid Al-Sakni","message":"Welcome to the Enterprise Backend API"}
```
Author spelling above matches the current source.

## POST /api/login

No body or credential validation is implemented. Always HTTP 200:

```sh
curl -i -X POST http://127.0.0.1:8000/api/login
```
```json
{"message":"login success","token":"example_jwt_token_for_demonstration","status":"authorized"}
```

This literal placeholder is NOT a signed JWT. Do not protect resources with it or submit production passwords. GET on this path returns 405; unknown routes return 404. A credential-related 401 is NOT implemented.

## Security gates

Database and user model files are empty; persistence, user isolation and real authentication are not implemented. Before production: implement credential validation, maintained password hashing, token signature and expiry validation, owner/other-user access tests, HTTPS, restricted CORS, input limits and abuse protection. Keep secrets outside source. Report vulnerabilities privately to majidalsakani@gmail.com without disclosing secrets publicly.

## Tests

```sh
pip install pytest httpx ruff
pytest -q tests
ruff check --isolated app api tests
```

Five contract tests passed on 2026-11-16. See [performance evidence](PERFORMANCE.md). These tests establish current behavior, not security certification or production capacity.
