from django.urls import path
from .views import StoryView, RecipeView, CreateStoryView, CreateRecipeView, StoryDetailView, RecipeDetailView

urlpatterns = [
    path('stories/', StoryView.as_view(), name = 'stories'),
    path('recipes/', RecipeView.as_view(), name = 'recipes'),
    path('create_story/', CreateStoryView.as_view(), name = 'create_story'),
    path('create_recipe/', CreateRecipeView.as_view(), name = 'create_recipe'),
    path('single_story/<int:pk>/', StoryDetailView.as_view(), name = 'single_story'),
    path('single_recipe/<int:pk>/', RecipeDetailView.as_view(), name = 'single_recipe'),

]