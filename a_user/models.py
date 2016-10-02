#coding=utf-8

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models
from django.conf import settings
import os.path
import urllib, hashlib, traceback, json
from .model.MenuUser import MenuUser
from .model.Menu import Menu

class Extra(models.Model):
    user = models.OneToOneField(User)
    permission_str = models.CharField(max_length=500, blank=True, default=1)
    role = models.IntegerField(blank=True, default=1)

    def get_menus(self, menu_ids):
        menu_tree = Menu.where(status=1).where(parent_id=0).select().execute().all()
        menus = Menu.where(status=1).where(Menu.parent_id.__gt__(0)).select().execute().all()
        print(menu_tree)
        print()
        print()

        for item in menu_tree:
            item['sub'] = []
            for item1 in menus:
                if item1['parent_id'] == item['id']:
                    item['sub'].append(item1)

        return menu_tree

    def get_menu(self):
        try:
            menus = MenuUser.where(user_id=self.user.id).select().execute().all()
            menu_ids = [item['m_id'] for item in menus]
            user_menus = self.get_menus(menu_ids)
            return user_menus
        except:
            print(traceback.format_exc())
            return {}

def create_user_extra(sender, instance, created, **kwargs):
    if created:
        Extra.objects.create(user=instance)

def save_user_extra(sender, instance, **kwargs):
    instance.extra.save()

post_save.connect(create_user_extra, sender=User)
post_save.connect(save_user_extra, sender=User)
