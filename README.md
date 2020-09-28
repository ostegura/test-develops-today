## test-develops-today
### Step 1:
`git clone https://github.com/ostegura/test-develops-today.git`

### Step 2:
cd to repository directory and run `virtualenv --python=python venv` **install for python 3.7.x**

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
