# Generated by Django 4.2.7 on 2023-11-24 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0004_alter_commentary_post_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentary',
            name='post_comment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='post_comments', to='page.recipe', verbose_name='Рецепт'),
            preserve_default=False,
        ),
    ]
