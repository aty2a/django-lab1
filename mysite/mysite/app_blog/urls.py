from django.urls import path
from .views import HomePageView, ArticleDetail, ArticleList, ArticleCategoryList

urlpatterns = [
  path('', HomePageView.as_view(), name='home'),
  path('articles/', ArticleList.as_view(), name='articles-list'),
  path('article/<slug:slug>/', ArticleDetail.as_view(), name='article-detail'),
    path('articles/', ArticleList.as_view(), name='articleslist'),  # List of articles
    path('articles/category/<slug>/', ArticleCategoryList.as_view(), name='articles-category-list'),  # Category view
    path('articles/<int:year>/<int:month>/<int:day>/<slug>/', ArticleDetail.as_view(), name='news-detail'),  # Article detail
]
