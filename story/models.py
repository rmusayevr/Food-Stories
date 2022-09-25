from email import message
from django.db import models
from django.urls import reverse
from account.models import user

class tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

class category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class recipe(models.Model):
    name = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to="recipe_cover_images")
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(category, on_delete=models.CASCADE, related_name='recipe_of_category')
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='recipe_of_user')
    tag = models.ManyToManyField(tag, related_name="tag_of_recipe")

    def __str__(self):
        return f"{self.user.first_name}'s {self.name} recipe"
    

    class Meta:
        verbose_name = "Recipe"
        verbose_name_plural = "Recipes"

class story(models.Model):
    name = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to="story_cover_images")
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(category, on_delete=models.CASCADE, related_name='story_of_category')
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='story_of_user')
    tag = models.ManyToManyField(tag, related_name="tag_of_story")

    def __str__(self):
        return f"{self.user.first_name}'s {self.name} story"
    
    
    class Meta:
        verbose_name = "Story"
        verbose_name_plural = "Stories"

class comment(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='comment_of_user')
    story = models.ForeignKey(story, on_delete=models.CASCADE, related_name='comment_of_story', null=True, blank=True)
    recipe = models.ForeignKey(recipe, on_delete=models.CASCADE, related_name='comment_of_recipe', null=True, blank=True)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name}'s comment"

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
