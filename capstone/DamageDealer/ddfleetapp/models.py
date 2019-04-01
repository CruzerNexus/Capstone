from django.db import models
from django.urls import reverse

import math

class Card(models.Model):
    card_type = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    card_text = models.TextField(null=True, blank=True)
    point_value = models.CharField(max_length=3, default="0")
    anti_ship_lng_dice = models.IntegerField(null=True, blank=True)
    anti_ship_med_dice = models.IntegerField(null=True, blank=True)
    anti_ship_cls_dice = models.IntegerField(null=True, blank=True)
    unique = models.BooleanField(default=False)
    faction = models.CharField(max_length=9, null=True, blank=True)
    upgrade_type = models.CharField(max_length=200, null=True, blank=True)
    modification = models.BooleanField(default=False)
    ship_size = models.CharField(max_length=200, null=True, blank=True)
    flotilla = models.BooleanField(default=False)
    bomber = models.BooleanField(default=False)
    objective_type = models.CharField(max_length=200, null=True, blank=True)
    card_img = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name


class Fleet(models.Model):
    IMPERIAL = "Imperial"
    REBEL = "Rebel"
    FACTION_CHOICES = (
        (IMPERIAL, 'Imperial'),
        (REBEL, 'Rebel'),
    )
    admiral_name = models.CharField(max_length=200)
    faction = models.CharField(max_length=9, choices=FACTION_CHOICES, default=REBEL)
    list_name = models.CharField(max_length=200)
    point_total = models.IntegerField(default=0)
    cards = models.ManyToManyField('Card', through='CardAmount', related_name='fleets')

    def __str__(self):
        return self.list_name

    def get_absolute_url(self):
        return reverse("dd_detail", args=[str(self.id)])

    @property
    def get_point_total(self):
        cards_total = 0
        for card in self.cards.all():
            for cardb in card.card_amounts.filter(fleet=self):
                thiscard = cardb.amount
                cards_total += int(card.point_value) * thiscard
        return cards_total

    @property
    def get_dd_total(self):
        lng_dmg_total = 0
        med_dmg_total = 0
        cls_dmg_total = 0
        flt_dd_total = 0
        for card in self.cards.all():
            for carda in card.card_amounts.filter(fleet=self):
                thiscard = carda.amount
                if card.card_type == "ship":
                    lng_dmg_total = int(card.anti_ship_lng_dice) * 2
                    med_dmg_total = int(card.anti_ship_med_dice)
                    cls_dmg_total = int(card.anti_ship_cls_dice) * 2
                    print(lng_dmg_total, med_dmg_total, cls_dmg_total)
                    card_dd_avg = math.ceil((lng_dmg_total + med_dmg_total + cls_dmg_total) / 5)
                    print(card_dd_avg)
                    flt_dd_total += card_dd_avg
        return flt_dd_total




class CardAmount(models.Model):
    fleet = models.ForeignKey('Fleet', related_name='card_amounts', on_delete=models.SET_NULL, null=True)
    card = models.ForeignKey('Card', related_name='card_amounts', on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.IntegerField(default=1)

    def __str__(self):
        return self.fleet.list_name + ' <> ' + self.card.name
