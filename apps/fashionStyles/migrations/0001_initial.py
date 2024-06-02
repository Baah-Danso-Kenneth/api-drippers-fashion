# Generated by Django 3.2.7 on 2024-06-02 18:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0002_auto_20240601_1142'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FashionInspo',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('tags', models.CharField(blank=True, max_length=200)),
                ('source_link', models.URLField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FashionInspoImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('front_image', models.ImageField(default='fashion_inspo_images/default_front.png', upload_to='fashion_inspo_images/')),
                ('back_image', models.ImageField(default='fashion_inspo_images/default_back.png', upload_to='fashion_inspo_images/')),
                ('caption', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='UserFashionInspoInteraction',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('fashion_inspo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fashionStyles.fashioninspo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'fashion_inspo')},
            },
        ),
        migrations.CreateModel(
            name='Styles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('style_image', models.ImageField(upload_to='style_images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='styles', to='profiles.category')),
            ],
        ),
        migrations.AddField(
            model_name='fashioninspo',
            name='images',
            field=models.ManyToManyField(to='fashionStyles.FashionInspoImage'),
        ),
        migrations.AddField(
            model_name='fashioninspo',
            name='styles',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fashionStyles.styles'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('text', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('userfashioninspointeraction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fashionStyles.userfashioninspointeraction')),
                ('value', models.PositiveSmallIntegerField()),
                ('ratings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='fashionStyles.fashioninspo')),
            ],
            options={
                'abstract': False,
            },
            bases=('fashionStyles.userfashioninspointeraction',),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('userfashioninspointeraction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fashionStyles.userfashioninspointeraction')),
                ('likes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='fashionStyles.fashioninspo')),
            ],
            options={
                'abstract': False,
            },
            bases=('fashionStyles.userfashioninspointeraction',),
        ),
    ]
