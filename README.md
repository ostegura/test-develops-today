## API endpoints
`GET /posts` - **to get list of avalaible posts**
`CREATE /posts` - **to create new post**
`GET /posts/{int:pk}` - **to get post with exact id**
`PUT /posts/{int:pk}` - **to update post with exact id**
`PATCH /posts/{int:pk}` - **to update several fields in post with exact id**
`DELETE /posts/{int:pk}` - **to delete post with exact id**
`GET /posts/<int:pk>/upvote` - **to upvote exact post**

### And same endpoints for "Comments"

## test-develops-today
### Step 1:
`git clone https://github.com/ostegura/test-develops-today.git`

### Step 2:
cd to repository directory and run `virtualenv --python=python venv` **(install for python 3.7.x)**

### Step 3:
cd to root directory

### Step 4:
`pip install -r requirements.txt`

### Step 5:
Run PostgreSQL with your credentials and after change it in `newsBoard/settings.py`:
```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "posts",
        "USER": "YOUR_USERNAME",
        "PASSWORD": "YOUR_PASSWORD",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```

### Step 6:
cd to newsBoard directory and run `python manage.py makemigrations` and `python manage.py migrate`

### Step 7:
`python manage.py createsuperuser`

### Step 8:
`python manage.py runserver`

### Step 9:
Visit `http://127.0.0.1:8000/`
