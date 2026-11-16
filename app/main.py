
from typing import Annotated

from fastapi import FastAPI, Depends, status, Response

from app.schemas import (
    StoryCreate,
    StoryUpdate,
    StoryPatch,
    StoryResponse
)

from app.dependencies import get_story_store

from app import crud


app = FastAPI(
    title="GolpoJolpo Story Catalog API",
    description="A RESTful API for managing stories",
    version="1.0.0"
)


# Shared dependency
StoryStore = Annotated[dict, Depends(get_story_store)]


# HOME
@app.get("/")
def home():
    return {
        "message": "Welcome to GolpoJolpo Story Catalog API"
    }


# CREATE STORY
@app.post(
    "/stories",
    response_model=StoryResponse,
    status_code=status.HTTP_201_CREATED
)
def create_new_story(
    story: StoryCreate,
    store: StoryStore
):
    return crud.create_story(store, story)


# GET ALL STORIES
@app.get(
    "/stories",
    response_model=list[StoryResponse]
)
def read_all_stories(store: StoryStore):
    return crud.get_all_stories(store)


# GET ONE STORY
@app.get(
    "/stories/{story_id}",
    response_model=StoryResponse
)
def read_story(story_id: int, store: StoryStore):
    return crud.get_story_by_id(store, story_id)


# UPDATE STORY (PUT)
@app.put(
    "/stories/{story_id}",
    response_model=StoryResponse
)
def replace_story(
    story_id: int,
    story: StoryUpdate,
    store: StoryStore
):
    return crud.update_story(store, story_id, story)


# PARTIAL UPDATE STORY (PATCH)
@app.patch(
    "/stories/{story_id}",
    response_model=StoryResponse
)
def partially_update_story(
    story_id: int,
    story: StoryPatch,
    store: StoryStore
):
    return crud.patch_story(store, story_id, story)


# DELETE STORY
@app.delete(
    "/stories/{story_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def remove_story(story_id: int, store: StoryStore):
    crud.delete_story(store, story_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
