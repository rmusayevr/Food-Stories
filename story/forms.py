from django import forms
from .models import recipe, story, comment, tag

class recipeForm(forms.ModelForm):

    class Meta:
        model = recipe
        fields = ['name', 'cover_image', 'text', 'category', 'tag']
    
class storyForm(forms.ModelForm):
    
    class Meta:
        model = story
        fields = ['name', 'cover_image', 'text', 'category', 'tag']
    
class commentForm(forms.ModelForm):

    class Meta:
        model = comment
        fields = ['message']

