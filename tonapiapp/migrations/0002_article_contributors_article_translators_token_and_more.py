# Generated by Django 4.1.7 on 2023-03-16 10:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tonapiapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='contributors',
            field=models.ManyToManyField(related_name='contributors', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='article',
            name='translators',
            field=models.ManyToManyField(related_name='translators', to=settings.AUTH_USER_MODEL),
        ),
        
        # igrations.CreateModel(
            #name='Token',
            #fields=[
                #('key', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='Key')),
                #('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                #('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            #],
        #),

        
    ]
