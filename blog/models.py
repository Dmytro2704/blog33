from django.db import models
from django.contrib.auth.models import User
from django.forms import forms


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name="Назва")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

class Post(models.Model):
    title = models.CharField(max_length=30, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Опис")
    published_date = models.DateTimeField(auto_created=True, verbose_name="Дата та час")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    poster = models.URLField(default='https://upload.wikimedia.org/wikipedia/commons/0/09/POL_2007_08_04_Jaroslawiec_zachodniopomorskie_02.JPG', verbose_name="Постер")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Пости"

class Comment(models.Model):
    content = models.TextField(verbose_name="Коментар")
    published_date = models.DateTimeField(auto_created=True, verbose_name="Дата та час")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="До посту")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор коментаря")
    poster = models.URLField(default='https://i.pinimg.com/564x/92/c5/11/92c511eb998b41b3d6c78fc9522f5927.jpg', verbose_name="Постер")

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "Коментар"
        verbose_name_plural = "Коментари"

class ToContact(models.Model):
    login = models.CharField(max_length=10, verbose_name="Login")
    email=models.EmailField(max_length=30, verbose_name="Email")

    def __str__(self):
        return self.email

class Sign_up(models.Model):
    login = models.CharField(max_length=10, verbose_name="Login")
    email=models.EmailField(max_length=30, verbose_name="Email")
    poster=models.URLField(default='https://i.pinimg.com/564x/92/c5/11/92c511eb998b41b3d6c78fc9522f5927.jpg', verbose_name="Poster")
    date_of_birth = models.DateTimeField(default='2000-01-01T00:00:00Z', verbose_name="Date of birth")

    def __str__(self):
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    login = models.CharField(default='login', max_length=10, verbose_name="Login")
    email=models.EmailField(default='login@mail.com', max_length=30, verbose_name="Email")
    poster=models.ImageField(upload_to='uploads/', default='https://i.pinimg.com/564x/92/c5/11/92c511eb998b41b3d6c78fc9522f5927.jpg', verbose_name="Poster")
    date_of_birth=models.DateTimeField(default='2000-01-01T00:00:00Z', verbose_name="Date of birth")

    def __str__(self):
        return self.login

