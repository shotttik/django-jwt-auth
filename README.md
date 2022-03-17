# django-jwt-auth
### About
>In this project User model overrided and customized User model

>Created user login,registration,update and token refresh views. 

>Using RESTful API

>Using PyJWT

>Using `MySQL` database, If you want to use default database `sqlite` Go to the **jwtproject/settings.py** and uncomment 80-87 lines and comment 88-97.


# Running the Project Locally

First, clone the repository to your local machine:

```
git clone https://github.com/shotttik/django-jwt-auth
```

Second, create virtual environment
```
python3 -m venv env
```

Third, activate virtual environment
```
source env/bin/activate
```

Install the requirements:

```
python3 -m pip install -r requirements.txt

```

Apply the migrations:

```
python3 manage.py migrate
```

Finally, run the development server:

```
python3 manage.py runserver
```