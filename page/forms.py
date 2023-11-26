from django import forms
from .models import Commentary, Generate_recipe
# Форма комментариев
class CommentForm(forms.ModelForm):
    class Meta:
        model=Commentary
        fields=['name_user','text_comment']

# Форма комментариев
class GenerateForm(forms.ModelForm):
    class Meta:
        model = Generate_recipe
        fields = ['name_recipe', 'ingredients', 'prompt']