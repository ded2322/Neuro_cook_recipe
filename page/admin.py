from django.contrib import admin
from .models import Category, Recipe, Commentary, Generate_recipe
# Register your models here.

# Подключение катергории в админ. панель
admin.site.register(Category)
# Подключение рецептов в админ. панель
admin.site.register(Recipe)
# Подключение комментарий в админ. панель
admin.site.register(Commentary)
# Подключение созданных рецептов gpt админ. панели
admin.site.register(Generate_recipe)
