from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer


# # Create your views here.
# @api_view(['POST'])
# def signup(request):
#     password = request.data.get('password')
#     password_confirm = request.data.get('password2')

#     # if password != password_confirm:
#     #     error_msg = {
#     #         'error' : '비밀번호 불일치',
#     #     }
#     #     return Response(error_msg, status=status.HTTP_400_BAD_REQUEST)
    
#     # serializer = UserSerializer(data=request.data)

#     # if serializer.is_valid(raise_exception=True):
#     #     user = serializer.save()
        