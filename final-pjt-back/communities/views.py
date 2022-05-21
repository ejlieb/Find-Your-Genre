from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash


from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# @api_view(['GET'])