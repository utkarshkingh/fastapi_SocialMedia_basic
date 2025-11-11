from fastapi import FastAPI,HTTPException
from app.schema import PostCreate,PostResponse
from app.db import Post,create_db_and_tables,get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager  

@asynccontextmanager
async def lifespan(app:FastAPI):
    await create_db_and_tables()
    yield

app=FastAPI()

text_posts = {
    1: {"title": "new post", "content": "cool post"},
    2: {"title": "Random Idea", "content": "Just a thought that crossed my mind today."},
    3: {"title": "Quick Update", "content": "Checking in with a brief message."},
    4: {"title": "Late Night Musings", "content": "Thinking about the universe and everything."},
    5: {"title": "Project Status", "content": "Making good progress on the current task."},
    6: {"title": "Weekend Vibes", "content": "Ready for some relaxation and fun!"},
    7: {"title": "Coding Challenge", "content": "Trying to solve a difficult programming problem."},
    8: {"title": "Travel Dreams", "content": "Where should I go for my next vacation?"},
    9: {"title": "Book Recommendation", "content": "Highly recommend the latest sci-fi novel."},
    10: {"title": "Daily Reflection", "content": "What did I learn today?"}
}


@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit:
        # Return a list of the first 'limit' post values
        return list(text_posts.values())[:limit]
    
    # If no limit, return the whole dictionary
    return text_posts


@app.get("/posts/{id}") # path parameter
def get_post(id:int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(id)


@app.post("/posts")
def create_post(post:PostCreate) -> PostResponse:
   new_post={"title":post.title, "content":post.content}
   new_post = text_posts[max(text_posts.keys())+1]=new_post
   return new_post

    