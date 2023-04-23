# This is data access library - Could be another API or database
import httpx
from typing import Optional
from Schema.schema import MovieSchema

async def get_movie(title_subtext: str) -> Optional[MovieSchema]:
    url = f"https://movieservice.talkpython.fm/api/search/{title_subtext}"

    async with httpx.AsyncClient() as client:
        response: httpx.Response = await client.get(url)
        response.raise_for_status()
        data = response.json()
    
    results = data["hits"]
    if not results:
        return None 
    
    movie = MovieSchema(**results[0])
    return movie
