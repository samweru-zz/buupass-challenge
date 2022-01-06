Buupass Challenge
====

This project uses a expirable bearer token which is received after login.
The token is used for every request that requires authorization. 
Permissions are used to enforce role based access on routes (RBAC)

# Sample Code

```python
# Found in rbac/api.py

@api.post("/user/{user_id}", auth=AuthBearer())
@permissions("view_user")
def user(request, user_id:int):
    try:
        user = User.objects.get(id=user_id)
        if user:
            return {'username': user.username}
    except Exception as e:
        logger.critical(e)

        return {"success": False}
```

## Environment

To start you'll need to install `python 3.8` , `git` and `pip`

```sh
sudo apt update
sudo apt install git python3.8 python3-pip
```
Clone the project then run `pip` for requirements inside project folder:

```sh
git clone https://github.com/samweru/buupass-challenge
cd buupass-challenge
````
## Setup

Setting up the `logs` and `sqlite` database

```sh
./bin/starter
```

This script will create `logs/app.log` file, create migration and execute them.
It will also prompt for `superuser` so, please comply. (Smiley Face).
It will also install `requirements.txt`

## Seeding Database

To create subordinate users under `superuser` run the script below: 

```sh
python seeder.py
```

## Run Project

To server the project:

```sh
python manage.py runserver
```

The project will run under django's default port `localhost:8000`

You can interogate all routes under `http://localhost:8000/api/docs` to test the various APIs.
You may also view Admin database at `http://localhost:8000/api/admin` for users.

## Existing Routes

> - /api/bearer
> - /api/hello
> - /api/login
> - /api/user/{user_id}
> - /api/current/user
> - /api/add/user
> - /new/sub/to/user/{sup_id}
> - /for/user/{sup_id}/subs/all

### Login

In this route `/api/login` username and password fields are required which can will return
a `bearer` token that can be used to authenticate on the `http://localhost:8000/api/docs` in browser
via route `/api/bearer` ensure to click on the `Authorize` button first.

-OR-

You can use `httpie` to authenticate your requests. For example:

```sh
http POST :8000/api/current/user "Authorization: Bearer <place_secret_token_here>"
```

You may install `httpie` via pip.

```sh
pip install httpie
```

### Note

Route `/api/hello` require no bearer.

Route `/new/sub/to/user/{sup_id}` adds a new surbordinate to a single supervisor. It also 
requires parameters for username and password.

Route `/for/user/{sup_id}/subs/all` lists all surborinates under a single supervisor
You may find code for all routes and permissions under `rbac/api.py`

***Decorators are used in code for permission, routes and http methods, it is an elegant method
of keeping code clean and understanable.***