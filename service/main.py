import fastapi
import uvicorn
import movie_data as movie_data
from Schema.schema import MovieSchema

# Initiate the instance of fastapi 
app = fastapi.FastAPI()

@app.get("/")
def index():
    message="""
<p><h2 style="color:red;">Welcome to Movie Search API.</h2></p>
<p><h3>This API allows you to search for a movie title and returns the 1st matching movie title along with the keywords associated with the movie, the director of movie and the year in which the movie was released.<p></h3>
<p><h4 style="font-weight:bold;">To use this API: Use http://127.0.0.1:8000/api/movie/{Title}</h4></p>"""
    return fastapi.responses.HTMLResponse(message)


@app.get("/api/movie/{title}", response_model=MovieSchema)
async def movie_search(title: str):
    movie = await movie_data.get_movie(title)
    if not movie:
        raise fastapi.HTTPException(status_code=404)
    return movie.dict()


if __name__ == "__main__":
    uvicorn.run(app)