from django.shortcuts import render

def stories(request):
    return render(request, 'stories.html')

def story(request):
    return render(request, 'single.html')

def create_story(request):
    return render(request, 'create_story.html')

def recipes(request):
    return render(request, 'recipes.html')