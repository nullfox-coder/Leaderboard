## Setup and Installation

1. Clone the repository
2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Start the development server:
```bash
python manage.py runserver
```

7. In a separate terminal, start Redis (required for Celery):
```bash
redis-server
```

8. In another terminal, start Celery worker:
```bash
celery -A leaderboard worker -l info
```

9. In another terminal, start Celery beat:
```bash
celery -A leaderboard beat -l info
```


# Test - 

# Create game -

curl --location 'http://localhost:8000/api/games/' \
--header 'Content-Type: application/json' \
--data '{"name":"SnakeAndLadder"}'


# Create contestant - 

curl --location 'http://localhost:8000/api/contestants/' \
--header 'Content: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name":"Anil",
    "email":"anil@abc.com"
}'

# Create Game Sessions - 

curl --location 'http://localhost:8000/api/game-sessions/' \
--header 'Content: application/json' \
--header 'Content-Type: application/json' \
--data '{
    "game":3,
    "contestant":3,
    "score":0
}'

# Update Scores - 

curl --location --request PUT 'http://localhost:8000/api/game-sessions/3/update_score/' \
--header 'Content: application/json' \
--header 'Content-Type: application/json' \
--data '{
    "score":55
}'

# End Game sessions -

curl -X PUT "http://localhost:8000/api/game-sessions/1/end/"

# Upvote Games -

curl -X POST "http://localhost:8000/api/games/1/upvote/"

# View leaderboards -

# Global leaderboard
curl "http://localhost:8000/api/leaderboard/global/"

# Game-specific leaderboard
curl "http://localhost:8000/api/leaderboard/game/1/"

# Game Popularity 

curl "http://localhost:8000/api/game/popularity/"