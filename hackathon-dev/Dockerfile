FROM python:3.12 as build

RUN apt update

# Set Poetry environment variables
ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.8.2

# Create working directory
WORKDIR /hackathon

# System dependencies
RUN pip install "poetry==$POETRY_VERSION"

# Copy Poetry requirements to cache them in Docker layer
COPY poetry.lock pyproject.toml /hackathon//

# Project initialization
RUN poetry config virtualenvs.create false \
    && poetry install

# Copy files to image
COPY . .

CMD ["python", "main.py"]