# carbon-credits-api

Steps to run the FastAPI server locally:

1. Clone the repository
2. `pip3 install -r requirements.txt`
3. Create a database named `CarbonCreditsDB` in your local MySQL service
4. Add the local MySQL url to `SQLALCHEMY_DATABASE_URL` variable in `./db/database.py`
5. `uvicorn app:app --reload` or alternatively you can use `gunicorn` as well.
6. Open `locahost:8000/docs` to access the Swagger UI (API documentation)
