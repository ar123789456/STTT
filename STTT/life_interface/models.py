from django.db import models
from django.contrib.auth import get_user_model

Client = get_user_model()


class Aspects(models.Model):
    title = models.CharField(max_length=50, verbose_name='Аспект')
    description = models.TextField(max_length=300, verbose_name='Описание')



class Level(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название уровня')
    description = models.TextField(max_length=300, verbose_name='Описание уровня')
    exp = models.PositiveIntegerField(verbose_name="EXP", default=0)
    full_exp = models.PositiveIntegerField(verbose_name="FULL EXP")
    aspect = models.ForeignKey(Aspects, verbose_name='Аспект', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Verification(models.Model):
    quest_title = models.CharField(max_length=100, verbose_name='Название задания')
    slug = models.SlugField(max_length=100)
    quest = models.TextField(max_length=300, verbose_name='Задание')
    answer = models.CharField(max_length=50, verbose_name='Ответ')
    exp = models.DecimalField(max_digits=7, decimal_places=0)
    level = models.ForeignKey(Level, verbose_name="Категория Аспекта", on_delete=models.CASCADE)

    def __str__(self):
        return self.quest_title

    def check(self, inp):
        if self.answer == inp:
            return True
        else:
            return False


class Skill(models.Model):
    pass


class Profession(models.Model):
    pass


class User(models.Model):
    user = models.ForeignKey(Client, verbose_name="Пользователь", on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона', blank=True)
    info = models.TextField(max_length=300, verbose_name='О себе', blank=False)
