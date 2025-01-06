from django.db import models


# Create your models here.

class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(decimal_places=2, max_digits=10)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(decimal_places=2, max_digits=10)
    size = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title


'''
Список QuerySet запросов в порядке вызовов, которые использовались для внесения изменений в БД
from task1.models import Game
Game.objects.create(title='Game_1 without age_limited', cost=1500, size=234132, description='description for game_1  without age_limited', age_limited=False)
Game.objects.create(title='Game_2 with age_limited', cost=2100, size=344522, description='description for game_2  with age_limited', age_limited=True)
Game.objects.create(title='Game_3 with age_limited', cost=2120, size=574753, description='description for game_3 with age_limited', age_limited=True)
from task1.models import Buyer
Buyer.objects.create(name='Buyer 22 yo', balance=1500, age=22)
Buyer.objects.create(name='Buyer 30 yo', balance=2500, age=30)
Buyer.objects.create(name='Buyer 17 yo', balance=1100, age=17)
buyer_1 = Buyer.objects.get(id=1)
buyer_2 = Buyer.objects.get(id=2)
buyer_3 = Buyer.objects.get(id=3)
Game.objects.get(id=1).buyer.set((buyer_1, buyer_2, buyer_3))
Game.objects.get(id=2).buyer.set((buyer_1, buyer_2))
Game.objects.get(id=3).buyer.set((buyer_1, ))
'''
