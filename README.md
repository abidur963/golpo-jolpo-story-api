# GolpoJolpo Story Catalog API

A RESTful API built with FastAPI and Pydantic V2 for managing stories.

## Features

- Create a new story
- Retrieve all stories
- Retrieve a story by ID
- Replace an existing story using PUT
- Partially update a story using PATCH
- Delete a story
- Pydantic request validation
- HTTP status codes and error handling
- Dependency injection

## Technologies

- Python
- FastAPI
- Pydantic V2
- Uvicorn
- Postman

## Installation

Clone the repository:

    git clone YOUR_REPOSITORY_URL

Move into the project directory:

    cd golpo-jolpo-story-api

Create a virtual environment:

    python -m venv venv

Activate it on Windows PowerShell:

    .\venv\Scripts\Activate.ps1

Install dependencies:

    python -m pip install -r requirements.txt

## Run the application

    python -m uvicorn app.main:app --reload

## API Documentation

Open the following URL in your browser:

http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| POST | /stories | Create a story |
| GET | /stories | Get all stories |
| GET | /stories/{story_id} | Get one story |
| PUT | /stories/{story_id} | Replace a story |
| PATCH | /stories/{story_id} | Partially update a story |
| DELETE | /stories/{story_id} | Delete a story |

## Storage

This project currently uses in-memory storage.
Story data resets when the application restarts.