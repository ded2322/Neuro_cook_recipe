from django.db import models

# Create your models here.

class Category(models.Model):
    """
    Модель, для категорий рецептов
    """

    name_category = models.CharField(verbose_name='Название категории',max_length=255)

    class Meta:
        # Для единственного и множественного числа

        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name_category

class Recipe(models.Model):
    """
    Модель, для написания рецептов
    """
    # Используется для ссылки на категорию, что было проще сортировать \
    # Имя для доступа в шаблонах: category
    category = models.ForeignKey( Category,verbose_name = 'Категория',related_name='category' ,on_delete = models.CASCADE)

    name_recipe = models.CharField(verbose_name='Название рецепта', max_length=255)
    preview = models.TextField(verbose_name='Превью рецепта',max_length=380)
    text_post = models.TextField(verbose_name='Текст рецепта',max_length=4000)
    image_post = models.ImageField(verbose_name='Изображение рецепта', upload_to='image/%Y',blank=True,null=True)

    class Meta:
        # Для единственного и множественного числа

        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return f'Название рецепта: {self.name_recipe} Категория: {self.category}'

class Commentary(models.Model):
    """
    Модель, для написания комментария под постом
    """
    post_comment = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='post_comments',verbose_name='Рецепт')
    name_user = models.CharField(verbose_name='Имя пользователя',max_length=30)
    text_comment = models.TextField(verbose_name='Текст комментария', max_length=1000)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'Комментарий к рецепту: {self.post_comment.name_recipe}. Автор комментария: {self.name_user}'

class Generate_recipe(models.Model):
    """
    Модель, для генерации рецепта
    """
    name_recipe = models.TextField(verbose_name='Название рецепта',max_length=100)
    ingredients = models.TextField(verbose_name='Ингредиенты')
    prompt = models.TextField(verbose_name='Текст для генерации рецепта')
    text_recipe = models.TextField(verbose_name='Текст рецепта')
    class Meta:
        verbose_name_plural = 'Сгенерированный рецепт'

    def __str__(self):
        return f"{self.name_recipe}"