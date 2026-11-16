
from fastapi import HTTPException

from app.schemas import StoryCreate, StoryUpdate, StoryPatch


# CREATE
def create_story(store: dict, story: StoryCreate):
    story_id = max(store.keys(), default=0) + 1

    new_story = {
        "id": story_id,
        **story.model_dump()
    }

    store[story_id] = new_story

    return new_story


# READ ALL
def get_all_stories(store: dict):
    return list(store.values())


# READ ONE
def get_story_by_id(store: dict, story_id: int):
    if story_id not in store:
        raise HTTPException(
            status_code=404,
            detail="Story not found"
        )

    return store[story_id]


# UPDATE (PUT)
def update_story(
    store: dict,
    story_id: int,
    story: StoryUpdate
):
    if story_id not in store:
        raise HTTPException(
            status_code=404,
            detail="Story not found"
        )

    updated_story = {
        "id": story_id,
        **story.model_dump()
    }

    store[story_id] = updated_story

    return updated_story


# PARTIAL UPDATE (PATCH)
def patch_story(
    store: dict,
    story_id: int,
    story: StoryPatch
):
    if story_id not in store:
        raise HTTPException(
            status_code=404,
            detail="Story not found"
        )

    update_data = story.model_dump(exclude_unset=True)

    store[story_id].update(update_data)

    return store[story_id]


# DELETE
def delete_story(store: dict, story_id: int):
    if story_id not in store:
        raise HTTPException(
            status_code=404,
            detail="Story not found"
        )

    del store[story_id]

    return None
