from django.contrib import admin
from .models import Article,Images
# Register your models here.
#admin.site.register(Article) #add model to admin.py
@admin.register(Article)
class ArticleModel(admin.ModelAdmin):
    list_filter =  ('title','description')
    list_display = ('title','description')

@admin.register(Images)
class ArticleModel(admin.ModelAdmin):
    list_filter =  ('url','user')
    list_display = (['user'])    
