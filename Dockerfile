FROM python:3.11-slim
WORKDIR /app

# Copy requirements.txt and install dependencies listed in requirements.txt.
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application code to the container.
COPY src ./src
COPY tests ./tests

# Set the defult command to run and execute the application code and the automated tests.
CMD ["python", "-m", "pytest", "-v"]