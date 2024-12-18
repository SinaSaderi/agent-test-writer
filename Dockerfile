
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy poetry files
COPY poetry.lock pyproject.toml ./

# Install Poetry and dependencies
RUN pip install --upgrade pip &&     pip install poetry &&     poetry config virtualenvs.create false

# Install project dependencies
ARG DEV=true
RUN if [ "$DEV" = "true" ]; then poetry install --with dev; else poetry install --only main; fi

# Copy the application code
COPY . .

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]    
    
