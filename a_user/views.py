#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-06-09

@author: zw
'''

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from mydecorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from config.global_conf import USER_TYPE, RESULT_404, NO_PERMISSION
from DjangoCaptcha import Captcha
import utils
import logging
import random
import traceback
import json
import copy
from .model.Menu import Menu

from peewee import *

from model.pw_model import AuthGroup
from model.pw_model import AuthUserGroups
from model.pw_model import AuthUser

from .model.UserExtra import UserExtra
from .model.Menu import Menu
from .model.AdminUser import AdminUser
from .model.MenuUser import MenuUser
from config import global_conf
from django.views.decorators.csrf import csrf_exempt

logger = logging.getLogger('mall_admin')
logger_error = logging.getLogger('mall_admin_error')

def code(request):
    # 生成验证码
    figures = [1,2,3,4,5,6,7,8,9]
    ca =  Captcha(request)
    ca.words = [''.join([str(random.sample(figures,1)[0]) for i in range(0,4)])]
    ca.type = 'word'
    return ca.display()

@csrf_exempt
def user_login(request):
    # 用户登录
    if request.method == 'GET':
        return render(request, 'cover.html')
    else:
        try:
            result = {"status": 1, "message": ""}
            print(request.POST)
            code = request.POST.get('code') or ''
            if not code:
                return JsonResponse({"status": 1, "message": "请填写验证码"})
            ca = Captcha(request)
            if not ca.check(code):
                return JsonResponse({"status": 1, "message": "验证码错误"})
            username, password = request.POST['email'], request.POST['password']

            # 验证用户信息有效性
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    user_role = utils.get_user_role(user.id)
                    result['data'] = {'username':user.username, 'role': user_role}
                    logger.info('%s login' % user.username)
                    return JsonResponse({"status": 0, "data": {'email': username, 'password': password, 'logged_in': True}})
                else:
                    return JsonResponse({"status": 1, "message": "用户被禁用"})
            else:
                return JsonResponse({"status": 1, "message": "用户名或密码错误"})
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse(RESULT_404)

@login_required
def user_logout(request):
    # 用户登出
    if request.method == 'GET':
        try:
            result = {"status": 1, "message": ""}
            logout(request)
            return redirect('/user/login')
        except Exception as e:
            return JsonResponse(RESULT_404)

@login_required
def user_list(request, param):
    permission_keys = ['permission_1', 'permission_2', 'permission_3', 'permission_4', 'permission_20']
    if not utils.check_permission(request.user, 'a_user_list_index'):
        return JsonResponse(NO_PERMISSION)
    if request.method == 'GET':
        try:
            query_filter = {}
            query_filter['email'] = request.GET.get('email', '')
            users = User.objects.filter(email__contains=query_filter['email'])
            user_list = utils.objects_to_dict(list(users))

            option = {'is_staff': global_conf.yes_no,
                      'is_superuser': global_conf.yes_no,
                      'is_active': global_conf.public_status,
                      'role': global_conf.admin_role,
                      }
            user_list = utils.prepare_table_data(user_list, option)
            return JsonResponse(user_list, safe = False)
        except Exception as e:
#            logger_error.error(e)
            print(traceback.format_exc())
            return JsonResponse(RESULT_404)
    elif request.method == "PUT":
        user_id = int(param)
        try:
            par = utils.get_post_parameter(request, permission_keys)
            par = dict(filter(lambda x: x[1], par.items()))
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse({"status": 1, "message":"参数错误"})
        res = Menu.where().select().execute().all()
        menus = {}
        for item in res:
            menus[str(item['id'])] = item
        permission_str = get_permission_str(menus, par, permission_keys);
        user_extra = UserExtra.where(user_id=user_id).select().execute().one()
        user_extra.permission_str = permission_str
        try:
            user_extra.save()
        except Exception as e:
            return JsonResponse({"status": 1, "message":"编辑失败"})
        return JsonResponse({"status": 0, "message":"编辑成功"})

def get_permission_str(menus, par, permission_keys):
    permission = {"menu": []}
    for key in permission_keys:
        if key not in par.keys():
            continue
        item = par[key]
        parent_id = key.split('_')[1]
        menu_group = {"name": menus[parent_id]['name'], "icon": menus[parent_id]['icon'], "sub": [], "id": parent_id}
        for id in item:
             menu_group['sub'].append({"name": menus[str(id)]['name'], "url": "/" + menus[str(id)]['type'] + "/" + menus[str(id)]['action'], "id": id})
        permission['menu'].append(menu_group)
    return json.dumps(permission)

@login_required
def user_extra(request, id):
    id = int(id) if id else 0
    if not utils.check_permission(request.user.extra, 'a_user_list_index'):
        return JsonResponse(NO_PERMISSION)

    if request.method == 'GET':
        user_extra = UserExtra.where(user_id=id).select().execute().one()
        return JsonResponse(json.loads(user_extra['permission_str'], ) if user_extra and user_extra['permission_str'] else {})


@login_required
def user_list_index(request):
    if not utils.check_permission(request.user.extra, 'a_user_list_index'):
        return JsonResponse(NO_PERMISSION)
    return render(request, 'a_user_list.html', {"breadcrumb1" : "设置", "breadcrumb2" : "管理员管理"})

@login_required
def user_open(request, id):
    id = int(id) if id else 0
    if not utils.check_permission(request.user.extra, 'a_user_list_index'):
        return JsonResponse(NO_PERMISSION)
    a_user = AdminUser.where(id=id).select().execute().one()
    a_user.is_active = True
    try:
        a_user.save()
    except Exception as e:
        return JsonResponse({"status": 1, "message":"编辑失败"})
    return JsonResponse({"status": 0, "message":"编辑成功"})

@login_required
def user_shut(request, id):
    id = int(id) if id else 0
    if not utils.check_permission(request.user.extra, 'a_user_list_index'):
        return JsonResponse(NO_PERMISSION)
    a_user = AdminUser.where(id=id).select().execute().one()
    a_user.is_active = False
    try:
        a_user.save()
    except Exception as e:
        return JsonResponse({"status": 1, "message":"编辑失败"})
    return JsonResponse({"status": 0, "message":"编辑成功"})

@login_required
def user_permission_update(request):
    if not utils.check_permission(request.user.extra, 'a_user_list_index'):
        return JsonResponse(NO_PERMISSION)
    user_extras = UserExtra.where().select().execute().all()
    try:
        for user_extra in user_extras:
            user_extra1 = UserExtra.where(id=user_extra['id']).select().execute().one()
            user_extra1.permission_str = get_updated_permission_str(user_extra['permission_str'])
            user_extra1.save()
    except Exception as e:
        return JsonResponse({"status": 1, "message":"编辑失败"})
    return JsonResponse({"status": 0, "message":"编辑成功"})

def get_updated_permission_str(permission_str):
    try:
        permission = json.loads(permission_str)
        menu_actions = get_menu_actions()
        for ii in range(len(permission['menu'])):
            for jj in range(len(permission['menu'][ii]['sub'])):
                if permission['menu'][ii]['sub'][jj]['name'] not in menu_actions:
                    del permission['menu'][ii]['sub'][jj]
        return json.dumps(permission)
    except Exception as e:
        raise
        return None

@login_required
def menus(request, id):
    id = int(id) if id else 0
    if not utils.check_permission(request.user.extra, 'a_user_list_index'):
        return JsonResponse(NO_PERMISSION)
    if request.method == 'GET':
        menus = Menu.where(status=1).select().execute().all()
        menu_tree = {}
        for item in menus:
            if item['parent_id'] != 0:
                if str(item['parent_id']) in menu_tree:
                    menu_tree[str(item['parent_id'])]['sub'].append(item)
                else:
                    menu_tree[str(item['parent_id'])] = {'sub': [item]}
            else:
                if str(item['id']) in menu_tree:
                    menu_tree[str(item['id'])]['name'] = item['name']
                    menu_tree[str(item['id'])]['icon'] = item['icon']
                else:
                    menu_tree[str(item['id'])] = {'name': item['name'], 'icon': item['icon'], 'sub': []}

        return JsonResponse(menu_tree)


@login_required
def menus_index(request):
    if not utils.check_permission(request.user.extra, 'a_menus_index'):
        return JsonResponse(NO_PERMISSION)
    return render(request, 'a_menus.html', {"breadcrumb1" : "设置", "breadcrumb2" : "菜单管理", 'parent_menus': get_parent_menus()})

def get_parent_menus():
    res = Menu.where(parent_id=0).select().execute().all()
    a_parent_menus = {}
    for item in res:
        a_parent_menus[str(item['id'])] = item['name']
    return a_parent_menus

def get_menu_actions():
    res = Menu.where(status=1).select().execute().all()
    menu_actions = []
    for item in res:
        menu_actions.append(item['name'])
    return menu_actions


@login_required
def menus_data(request, id):
    menus_keys = ['type', 'action', 'name', 'parent_id', 'icon',]
    id = int(id) if id else 0
    if not utils.check_permission(request.user.extra, 'a_menus_index'):
        return JsonResponse(NO_PERMISSION)
    if request.method == 'GET':
        menus = Menu.where().select().execute().all()
        option = {'status': global_conf.public_status,
                  'parent_id': get_parent_menus(),
                  }
        menus = utils.prepare_table_data(menus, option)
        return JsonResponse(menus, safe = False)
    elif request.method == "PUT":
        try:
            par = utils.get_post_parameter(request, menus_keys)
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse({"status": 1, "message":"参数错误"})
        a_menu = Menu.where(id=id).select().execute().one()
        a_menu = utils.model_set(a_menu, par)
        try:
            a_menu.save()
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse({"status": 1, "message":"编辑失败"})
        return JsonResponse({"status": 0, "message":"编辑成功"})
    elif request.method == "POST":
        try:
            par = utils.get_post_parameter(request, menus_keys)
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse({"status": 1, "message":"参数错误"})
        a_menu = Menu()
        a_menu.status = 1
        a_menu = utils.model_set(a_menu, par)
        try:
            a_menu.save()
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse({"status": 1, "message":"新增失败"})
        return JsonResponse({"status": 0, "message":"新增成功"})

@login_required
def menu_open(request, id):
    id = int(id) if id else 0
    if not utils.check_permission(request.user.extra, 'a_menus_index'):
        return JsonResponse(NO_PERMISSION)
    a_menu = Menu.where(id=id).select().execute().one()
    a_menu.status = 1
    try:
        a_menu.save()
    except Exception as e:
        return JsonResponse({"status": 1, "message":"编辑失败"})
    return JsonResponse({"status": 0, "message":"编辑成功"})

@login_required
def menu_shut(request, id):
    id = int(id) if id else 0
    if not utils.check_permission(request.user.extra, 'a_menus_index'):
        return JsonResponse(NO_PERMISSION)
    a_menu = Menu.where(id=id).select().execute().one()
    a_menu.status = 0
    try:
        a_menu.save()
    except Exception as e:
        return JsonResponse({"status": 1, "message":"编辑失败"})
    return JsonResponse({"status": 0, "message":"编辑成功"})

def _get_menus(menu_ids):
    menu_tree = Menu.where(status=1).where(parent_id=0).select().execute().all()
    menus = Menu.where(status=1).where(Menu.parent_id.__gt__(0)).select().execute().all()

    for item in menu_tree:
        item['sub'] = []
        for item1 in menus:
            if item1['parent_id'] == item['id']:
                item1['route_url'] = '/' + item1['action'] + '_' + item1['type']
                item['sub'].append(item1)

    return menu_tree

@login_required
def get_menus(request):
    menus = MenuUser.where(user_id=request.user.id).select().execute().all()
    menu_ids = [item['m_id'] for item in menus]
    user_menus = _get_menus(menu_ids)
    return JsonResponse(user_menus, safe = False)

@login_required
def get_user_group(request):
    user_group_keys = ['name', 'id']
    if request.method == 'GET':
        user_group = AuthGroup.select().dicts()
        user_group = utils.pw_objects_to_dict(user_group)
        return JsonResponse(user_group, safe = False)
    elif request.method == "PUT":
        try:
            par = utils.get_post_parameter(request, user_group_keys)
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse({"status": 1, "message":"参数错误"})
        user_group = AuthGroup.get(AuthGroup.id==par['id'])
        user_group = utils.model_set(user_group, par)
        try:
            user_group.save()
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse({"status": 1, "message":"编辑失败"})
        return JsonResponse({"status": 0, "message":"编辑成功"})
    elif request.method == "POST":
        try:
            par = utils.get_post_parameter(request, user_group_keys)
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse({"status": 1, "message":"参数错误"})
        user_group = AuthGroup()
        user_group = utils.model_set(user_group, par)
        user_group.id = None
        try:
            user_group.save()
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse({"status": 1, "message":"新增失败"})
        return JsonResponse({"status": 0, "message":"新增成功"})


@login_required
def get_user_group_detail(request):
    user_group_keys = ['name', 'id']
    if request.method == 'GET':
        g_id = request.GET.get('id', '')
        res = (AuthUser.select().join(AuthUserGroups, JOIN.LEFT_OUTER, on=(AuthUser.id == AuthUserGroups.group).alias('user_group')))
        for item in res:
            print(item)

        group_user = utils.pw_objects_to_dict(res, ['log'])
        print(res)

        print(group_user)
        for ii in range(len(group_user)):
            if group_user[ii]['group_id'] == g_id:
                group_user[ii]['status'] = 1
            elif group_user[ii]['group_id']:
                group_user[ii]['status'] = -1
            else:
                group_user[ii]['status'] = 0

        return JsonResponse(group_user, safe = False)
    elif request.method == "PUT":
        try:
            par = utils.get_post_parameter(request, user_group_keys)
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse({"status": 1, "message":"参数错误"})
        user_group = UserGroup.where(id=par['id']).select().execute().one()
        user_group = utils.model_set(user_group, par)
        try:
            user_group.save()
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse({"status": 1, "message":"编辑失败"})
        return JsonResponse({"status": 0, "message":"编辑成功"})
    elif request.method == "POST":
        try:
            par = utils.get_post_parameter(request, user_group_keys)
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse({"status": 1, "message":"参数错误"})
        user_group = UserGroup()
        user_group = utils.model_set(user_group, par)
        try:
            user_group.save()
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse({"status": 1, "message":"新增失败"})
        return JsonResponse({"status": 0, "message":"新增成功"})
