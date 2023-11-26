from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse



from .models import Recipe
from .forms import CommentForm, GenerateForm, Generate_recipe
from .service import GPTService
# Create your views here.


def render_index(request):
    """
    Функция вытягивает из БД параметры. Параметры задавались в models,
    используемый класс 'Recipe'
    """
    recipes = Recipe.objects.all()

    return render(request,'core/index.html', {'recipes' : recipes})

def render_post(request, id):
    """
    Функция для отображение отдлено взятого поста и комментарии к нему
    """

    recipe = get_object_or_404(Recipe, id=id)

    comments = recipe.post_comments.filter(active=True)

    if request.method == "POST":

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post_comment = recipe
            new_comment.save()

    else:
        comment_form = CommentForm()

    return render(request, 'addition/page.html', {
        "recipe" : recipe,
        "comments" : comments,
        "comment_form" : comment_form
    })


#Функция для объединения всех данных в единый промпт
def prompt(name_recipe, ingredients, prompt):

    final_prompt = (f"Я хочу что бы сгенирировал блюдо под названием {name_recipe},"+
                    f"в нем должны быть такие ингридиенты как {ingredients},"+
                    f"готовиться это блюдо должно {prompt}. "+
                    f"Исходя из этих данных сгенрируй рецепт, будто бы это рецепт из поваренной книги. И предоставь рецепт на русском")
    return final_prompt

def render_gpt(request):
    """
    Функция которая генерирует рецепт
    """
    if request.method == 'POST':
        form = GenerateForm(request.POST)
        if form.is_valid():
            #Для получения отдлеьно полученных данных
            name_recipe=form.cleaned_data['name_recipe']
            ingredients=form.cleaned_data['ingredients']
            text_prompt=form.cleaned_data['prompt']

            #создание одной переменной с промптом
            text_recipe=prompt(name_recipe, ingredients, text_prompt)

            #генерация рецепта
            generated_recipe=GPTService.generate_recipe(text_recipe)

            #Сохранение данных для в администраторскую панель
            ready_recipe = Generate_recipe(name_recipe=name_recipe, ingredients=ingredients,prompt = text_prompt, text_recipe = generated_recipe)

            ready_recipe.save()
            #Передача данных для генерации
            return render(request,'addition/test.html',{'recipe': generated_recipe})
    else:
        form = GenerateForm()

    return render(request, 'addition/generate_recipe.html', {'form': form  })


# Рендер страница о нас
def render_about(request):
    return render(request,"addition/about.html")
# Рендер страници ошибки
def render_error(request):
    return render(request,"addition/error.html")