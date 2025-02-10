## Setup and Installation

# I have deployed the backend in gcp - 

```bash
http://34.46.28.212:8000
```

# Or If you are on windows - Use my venv and .env.json file to use my configurations

# Or use the following command to install the required packages

1. Clone the repository
2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate 
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Redis check:
```bash
redis-cli ping
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

10 . Celery log
```bash
celery -A leaderboard worker --loglevel=info --pool=solo
````


# Test - 

# Create game -

## Local -
```bash
curl --location 'http://localhost:8000/api/games/' \
--header 'Content-Type: application/json' \
--data '{"name":"SnakeAndLadder"}'
```

## GCP

```bash
curl --location 'http://34.46.28.212:8000/api/games/' \
--header 'Content-Type: application/json' \
--data '{"name":"SnakeAndLadder"}'
```

# Create contestant - 

## Local

```bash
curl --location 'http://localhost:8000/api/contestants/' \
--header 'Content: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name":"Anil",
    "email":"anil@abc.com"
}'
```

## GCP

```bash
curl --location 'http://34.46.28.212:8000/api/contestants/' \
--header 'Content: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name":"Anil",
    "email":"anil@abc.com"
}'
```

# Create Game Sessions - 

## Local

```bash
curl --location 'http://localhost:8000/api/game-sessions/' \
--header 'Content: application/json' \
--header 'Content-Type: application/json' \
--data '{
    "game":3,
    "contestant":3,
    "score":0
}'
```

## GCP

```bash
curl --location 'http://34.46.28.212:8000/api/game-sessions/' \
--header 'Content: application/json' \
--header 'Content-Type: application/json' \
--data '{
    "game":3,
    "contestant":3,
    "score":0
}'
```

# Update Scores - 

## Local

```bash
curl --location --request PUT 'http://localhost:8000/api/game-sessions/3/update_score/' \
--header 'Content: application/json' \
--header 'Content-Type: application/json' \
--data '{
    "score":55
}'
```

## GCP

```bash
curl --location --request PUT 'http://34.46.28.212:8000/api/game-sessions/3/update_score/' \
--header 'Content: application/json' \
--header 'Content-Type: application/json' \
--data '{
    "score":55
}'
```

# End Game sessions -

## Local

```bash
curl -X PUT "http://localhost:8000/api/game-sessions/1/end/"
```

## GCP

```bash
curl -X PUT "http://34.46.28.212:8000/api/game-sessions/1/end/"
```

# Upvote Games -

## Local

```bash
curl -X POST "http://localhost:8000/api/games/1/upvote/"
```

## GCP

```bash
curl -X POST "http://34.46.28.212:8000/api/games/1/upvote/"
```

# View leaderboards -

## Global leaderboard

### Local

```bash
curl "http://localhost:8000/api/leaderboard/global/"
```

### GCP

```bash
curl "http://34.46.28.212:8000/api/leaderboard/global/"
```

## Game-specific leaderboard

### Local

```bash
curl "http://localhost:8000/api/leaderboard/game/1/"
```

### GCP

```bash
curl "http://34.46.28.212:8000/api/leaderboard/game/1/"
```

# Game Popularity 

## Local

```bash
curl "http://localhost:8000/api/game/popularity/"
```

## GCP

```bash
curl "http://34.46.28.212:8000/api/game/popularity/"
```
