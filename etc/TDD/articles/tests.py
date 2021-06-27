from django.test import TestCase
from django.test import Client
from .models import Article
from django.contrib.auth import get_user_model

# Create your tests here.
class ArticleTest(TestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user(username='test', password='123')
        Article.objects.create(title='hello', content='content', user=user)

    def test_article_title(self):
        article = Article.objects.get(pk=1)
        self.assertEqual(article.title, 'hello')
    
    def test_article_create(self):
        c = Client()
        # 0. 로그인 확인
        res = c.get('/articles/create/')
        self.assertEqual(res.status_code, 200)
        
        # 1. /articles/create/ 로 GET요청
        # 200 OK
        c.login(username='admin', password='admin')
        res = c.get('/articles/create/')
        self.assertEqual(res.status_code, 200)

        # 2. /articles/create/ 로 POST요청 (invalid)
        # 400 bad request 에러 발생
        res = c.post('/articles/create/')
        self.assertEqual(res.status_code, 400)
        
        # 3. /articles/create/ 로 POST요청 (valid)
        # 201 create 
        before = Article.objects.last()
        res = c.post('/articles/create/', {'title': 'hi', 'content': 'content', 'user': '1'})
        after = Article.objects.last()
        self.assertEqual(res.status_code, 201)
        self.assertNotEqual(before, after)