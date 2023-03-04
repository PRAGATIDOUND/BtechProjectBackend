
from django.urls import path,include
from .views import ArticleViewSet,UserViewSet,ImagesViewSet
from .create import createImage
from rest_framework.routers import DefaultRouter
from . import create
#from .views import article_details, article_list

router = DefaultRouter()
router.register('articles',ArticleViewSet,basename='articles')
router.register('users',UserViewSet)
router.register('images',ImagesViewSet,basename='images')



urlpatterns = [
    path('api/',include(router.urls)),
    path('api/create/', create.createImage, name = 'create')
    
 
    
]
