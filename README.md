# Vehicle Valuation Microservice (CSY3056 AS1)

A small Python vehicle valuation component built to demonstrate DevOps CI/CD practices, automated testing with `pytest`, Jenkins pipeline automation, and Docker containerisation.

## Setup
Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running Automated Tests
Run the unit, integration, and regression test suite locally:
```bash
python -m pytest -v
```

## Running with Docker
Build and run the containerised test suite:
```bash
docker build -t vehicle-valuation:latest .
docker run --rm vehicle-valuation:latest
```