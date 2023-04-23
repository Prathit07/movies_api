## Dockerization of movies_api using FastAPI
Build a FastAPI to get the movies data and return the movies match based on movie title. Create and run the API in a docker container.

This API allows you to search for a movie title and returns the 1st matching movie title along with the keywords associated with the movie, the director of movie and the year in which the movie was released.

This is a great example to build a python API using FastAPI web framework and run the API within a docker container. 

I was inspired by this video: https://youtu.be/qQNGw_m8t0Y

Once the API is built, run the below line of code to build a docker image:
docker build -t movies_api  .

To run the container, run the below line of code in your terminal
docker run -p 127.0.0.1:8000:80/tcp movies_api

To use this API: Use http://127.0.0.1:8000/api/movie/{Title}

Kind regards,
Prathit

