from django.test import TestCase
from django.test import Client
from .models import Article
from django.contrib.auth import get_user_model

# Create your tests here.
class ArticleTest(TestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user(username='test', password='123')
        Article.objects.create(title='hello', user=user)

    def test_article_title(self):
        article = Article.objects.get(pk=1)
        self.assertEqual(article.title, 'hello')
    
    def test_article_create(self):
        c = Client()
        # 0. 로그인 확인
        res = c.get('/articles/create/')
        self.assertEqual(res.status_code, 302)
        
        # 1. /articles/create/ 로 GET요청
        c.login(username='test', password='123')
        res = c.get('/articles/create/')
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'articles/article_form.html')
        self.assertContains(res, '<h1>form</h1>')

        # 2. /articles/create/ 로 POST요청 (invalid)
        res = c.post('/articles/create/')
        self.assertContains(res, 'This field is required.')
        self.assertEqual(res.status_code, 200)
        
        # 3. /articles/create/ 로 POST요청 (valid)
        before = Article.objects.last()
        res = c.post('/articles/create/', {'title': 'hi'})
        after = Article.objects.last()
        self.assertEqual(res.status_code, 302)
        self.assertEqual(res.url, '/articles/2/')
        self.assertNotEqual(before, after)


    def test_article_list(self):
        c = Client()
        res = c.get('/articles/')
        context_articles = res.context.get('articles')
        queryset_articles = Article.objects.all()

        self.assertEqual(list(context_articles), list(queryset_articles))
        self.assertTemplateUsed(res, 'articles/article_list.html')