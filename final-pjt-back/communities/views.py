from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash


from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Review
from.serializers import ReviewSerializer, CommentCreateSerializer

# 리뷰는 어떻게 띄울 것?

@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all().order_by('-pk')
    serializer = ReviewSerializer(reviews, many=True)

    return Response(serializer.data)


# 각 리뷰의 디테일 정보 요청
@api_view(['GET'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ReviewSerializer(review)
    
    return Response(serializer.data)

@api_view(['POST'])
def comment_create(request, review_pk):
    if not request.user.is_authenticated:
        return redirect('http://127.0.0.1:8000/api/v1/accounts/login/')

    review = get_object_or_404(Review, pk=review_pk)
    serializer = CommentCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, review=review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def comment_delete(request, review_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    # comment = Comment.objects.get(pk=comment_id)

    if not request.user.comment_set.filter(pk=comment_id).exists():
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

    comment.delete()
    return Response({ 'id': comment_id }, status=status.HTTP_204_NO_CONTENT)



