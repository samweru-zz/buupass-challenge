# from ninja_auth.api import router as auth_router
# from ninja.security import django_auth

from ninja.security import HttpBearer
from ninja import NinjaAPI, Form
from ninja import Schema

# from ninja.security import django_auth
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# api = NinjaAPI(csrf=False)

api = NinjaAPI()
# api.add_router('/auth', auth_router)

class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        if token == "supersecret":
            return token

@api.post("/bearer", auth=AuthBearer())
def bearer(request):
    return {"token": request.auth}

@api.get("/hello")
def hello(request):
    return "Hello world"

class UserIn(Schema):
    username: str
    password: str

@api.post("/login")
def login(request, data: UserIn):
    user = authenticate(request, username=data.username, password=data.password)
    if user is not None:
        login(request, user)
        return {'success': True}
    return {'success': False}

# @api.post("/user/{user_id}",  auth=django_auth)
@api.post("/user/{user_id}")
def user(request, user_id:int):
    try:
        user = User.objects.get(id=user_id)
        if user:
            return {'username': user.username}
    except:
        return {"success": False}

@api.post("/current/user")
def current(request):
    if request.user.is_authenticated:
        user = request.user
        return {"username": user.username}
    return {"message": "No authd user!"}

@api.post("/add/user")
def addUser(request, data:UserIn=Form(...)):
    try:
        user = User.objects.create(username=data.username, password=make_password(data.password))
        return {"success": True, "message":"Created user successfully."}
    except:
        return {"success": False, "message":"Failed to create user!"}

class SubUserIn(UserIn):
    user_id: str

@api.post("/add/sub/user")
def addSubUser(request, data:SubUserIn = Form(...)):
    return {"username":data.username, "password":data.password, "user_id":data.user_id}