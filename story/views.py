from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.db.models import Count, Q
from .models import story, recipe, category, tag
from .forms import storyForm, recipeForm, commentForm

class StoryView(ListView):
    template_name = 'stories.html'
    model = story
    context_object_name = 'stories'
    paginate_by = 9

    def get_queryset(self):
        category = self.request.GET.get('category')
        if category != None:
            return story.objects.order_by("-date").filter(category__name=category).all()
        return story.objects.order_by("-date").all()

    def get_context_data(self, **kwargs):
        context = super(StoryView, self).get_context_data(**kwargs)
        context['categories'] =  story.objects.values_list('category', flat = True).distinct().values('category__name').annotate(count = Count('category'))
        return context

class RecipeView(ListView):
    template_name = 'recipes.html'
    model = recipe
    context_object_name = 'recipes'
    paginate_by = 6

    def get_queryset(self):
        category = self.request.GET.get('category')
        if category != None:
            return recipe.objects.order_by("-date").filter(category__name=category).all()
        return recipe.objects.order_by("-date").all()

    def get_context_data(self, **kwargs):
        context = super(RecipeView, self).get_context_data(**kwargs)
        context['categories'] = recipe.objects.values_list('category', flat = True).distinct().values('category__name').annotate(count = Count('category'))
        return context

class CreateStoryView(LoginRequiredMixin, CreateView):
    template_name = 'create_story.html'
    form_class = storyForm
    success_url = reverse_lazy('stories')

    def get_success_url(self):
        messages.success(self.request, 'Your story has been successfully created!')
        return super(CreateStoryView, self).get_success_url()

    def get_context_data(self, **kwargs):
        context = super(CreateStoryView, self).get_context_data(**kwargs)
        context['categories'] = category.objects.all()
        context['tags'] = tag.objects.all()
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.save()
        return super().form_valid(form)

class CreateRecipeView(LoginRequiredMixin, CreateView):
    template_name = 'create_recipe.html'
    form_class = recipeForm
    success_url = reverse_lazy('recipes')

    def get_success_url(self):
        messages.success(self.request, 'Your recipe has been successfully created!')
        return super(CreateRecipeView, self).get_success_url()

    def get_context_data(self, **kwargs):
        context = super(CreateRecipeView, self).get_context_data(**kwargs)
        context['categories'] = category.objects.all()
        context['tags'] = tag.objects.all()
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.save()
        return super().form_valid(form)

class StoryDetailView(CreateView, DetailView):
    template_name = 'single_story.html'
    form_class = commentForm

    def get_object(self, queryset=None):
        return story.objects.get(pk=self.kwargs.get("pk"))

    def get_context_data(self, **kwargs):
        context = super(StoryDetailView, self).get_context_data(**kwargs)
        context['categories'] =  story.objects.values_list('category', flat = True).distinct().values('category__name').annotate(count = Count('category'))
        context['blogs'] = story.objects.order_by('-date').filter(~Q(pk=self.kwargs.get('pk'))).all()[:3]
        context['count'] = self.get_object().comment_of_story.count()
        context['all_tags'] = tag.objects.all()
        context['story_tags'] = self.get_object().tag.all()
        context['comments'] = self.get_object().comment_of_story.all()
        return context

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
            form.instance.story = self.get_object()
            form.save()
            return redirect('single_story', pk=self.get_object().pk)
        else:
            return redirect('login')

class RecipeDetailView(CreateView, DetailView):
    template_name = 'single_recipe.html'
    form_class = commentForm

    def get_object(self, queryset=None):
        return recipe.objects.get(pk=self.kwargs.get("pk"))

    def get_context_data(self, **kwargs):
        context = super(RecipeDetailView, self).get_context_data(**kwargs)
        context['categories'] =  recipe.objects.values_list('category', flat = True).distinct().values('category__name').annotate(count = Count('category'))
        context['blogs'] = recipe.objects.order_by('-date').filter(~Q(pk=self.kwargs.get('pk'))).all()[:3]
        context['count'] = self.get_object().comment_of_recipe.count()
        context['all_tags'] = tag.objects.all()
        context['recipe_tags'] = self.get_object().tag.all()
        context['comments'] = self.get_object().comment_of_recipe.all()
        return context

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
            form.instance.recipe = self.get_object()
            form.save()
            return redirect('single_recipe', pk=self.get_object().pk)
        else:
            return redirect('login')