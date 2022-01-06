# from django.shortcuts import render

# from django.http import JsonResponse, HttpResponse
# from django.views import View

# from django_request_mapping import request_mapping
# from django.contrib.auth.decorators import login_required, permission_required
# from django.contrib.auth import authenticate, login

# @request_mapping("/user")
# class UserView(View):
#     @request_mapping("/login", method="post")
#     def login(self, request):
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#         # data = request.POST
#             return HttpResponse("login:success")
#         return HttpResponse("login:failure")

#     @request_mapping("/signup/", method="post")
#     def signup(self, request):
#         return HttpResponse("user:signup")
    
#     @request_mapping("/<int:user_id>/role/")
#     def get_role(self, request, user_id):
#        return HttpResponse("user:role")

# @request_mapping("/")
# class HelloView(View):
#     # @permission_required("view_user")
#     @request_mapping("/", method="get")
#     def index(self, request):
#        return HttpResponse("Hello World!")