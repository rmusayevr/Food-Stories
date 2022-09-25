from django.contrib import admin
from .models import tag, category, recipe, story, comment

admin.site.register(tag)
admin.site.register(category)
admin.site.register(recipe)
admin.site.register(story)
admin.site.register(comment)
