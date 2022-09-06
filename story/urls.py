from django.urls import path
from .views import stories, story, create_story, recipes

urlpatterns = [
    path('stories/', stories, name = 'stories'),
    path('story/', story, name = 'story'),
    path('create_story/', create_story, name = 'create_story'),
    path('recipes/', recipes, name = 'recipes'),
]