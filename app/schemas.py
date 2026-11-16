
from pydantic import BaseModel, Field


# Schema for creating a story
class StoryCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    author: str = Field(min_length=2, max_length=50)
    description: str = Field(min_length=5)
    category: str
    published: bool = False


# Schema for updating a story
class StoryUpdate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    author: str = Field(min_length=2, max_length=50)
    description: str = Field(min_length=5)
    category: str
    published: bool


# Schema for partially updating a story
class StoryPatch(BaseModel):
    title: str | None = Field(default=None, min_length=3, max_length=100)
    author: str | None = Field(default=None, min_length=2, max_length=50)
    description: str | None = Field(default=None, min_length=5)
    category: str | None = None
    published: bool | None = None


# Schema for returning a story
class StoryResponse(BaseModel):
    id: int
    title: str
    author: str
    description: str
    category: str
    published: bool
