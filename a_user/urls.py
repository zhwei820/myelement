#coding=utf-8

from django.conf.urls import include, url
from a_user import views

urlpatterns = [
    url(r'^code/', views.code, name='code'),
    url(r'^login/', views.user_login, name='login'),
    url(r'^logout/', views.user_logout, name='logout'),
    url(r'^user_extra/(\d+)?$', views.user_extra),
    url(r'^get_menus/', views.get_menus, name='get_menus'),
    url(r'^get_user_group/', views.get_user_group, name='get_user_group'),
    url(r'^get_user_group_detail/', views.get_user_group_detail, name='get_user_group_detail'),

    url(r'^a_user_list/(\d+)?$', views.user_list),
    url(r'^a_user_list_index/', views.user_list_index),
    url(r'^a_user_open/(\d+)?$', views.user_open),
    url(r'^a_user_shut/(\d+)?$', views.user_shut),
    # url(r'^a_user_permission_update/', views.user_permission_update),

    url(r'^a_menus/(\d+)?$', views.menus),
    url(r'^a_menus_index/?$', views.menus_index),
    url(r'^a_menus_data/(\d+)?$', views.menus_data),
    url(r'^a_menu_open/(\d+)?$', views.menu_open),
    url(r'^a_menu_shut/(\d+)?$', views.menu_shut),
]
