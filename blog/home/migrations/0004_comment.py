# Generated by Django 4.2.1 on 2023-05-14 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_blog_approved'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('body', models.TextField(null=True)),
                ('date', models.DateField(auto_now=True, null=True)),
                ('comment_on', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='home.blog')),
            ],
        ),
    ]