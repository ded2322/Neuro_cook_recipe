from django.urls import path

from . import views

urlpatterns = [
    # Предоставляет главную страницу
    path("", views.render_index, name='index'),
    # Предоставляет странцу отдельно взятого поста
    path("recipe/<int:id>", views.render_post, name="recipe_post"),
    # Предоставляет страницу с возможность генерировать рецпты
    path("generate/", views.render_gpt,name="generate"),
    # Предоставляет страницу о нас
    path("about-us/", views.render_about,name='about'),
    # Предоставляет страницу ошибки
    path("404/", views.render_error,name='error')
]
