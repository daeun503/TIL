from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED

from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentListSerializer, CommentSerializer
from django.contrib.auth import get_user_model

# swagger
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(methods=['post'], request_body=ArticleSerializer)
@api_view(['GET', 'POST'])
def create(request):
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)

def detail(request, pk):
    pass

def delete(request, pk):
    pass

def update(request, pk):
    pass


def comments_create(request, pk):
    pass

def comments_delete(request, article_pk, comment_pk):
    pass