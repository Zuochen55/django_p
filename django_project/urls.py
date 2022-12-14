"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app01.views import department,user,vip_number,admin,account,task

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('department/list/', department.department),
    path('department/add/', department.add_department),
    path('department/delete/', department.delete_department),
    path('department/<int:nid>/edit/', department.edit_department),

    path('user/list/', user.user_list),
    path('user/add/', user.user_add),
    path('user/<int:nid>/edit/', user.user_edit),
    path('user/delete/', user.user_delete),

    path('vip/number/list/', vip_number.vipnumber),
    path('vip/number/add/', vip_number.vipnumber_add),
    path('vip/number/<int:nid>/edit/', vip_number.vipnumber_edit),
    path('vip/number/<int:nid>/delete/', vip_number.vipnumber_delete),

    path('admin/list/', admin.admin_list),
    path('admin/add/', admin.admin_add),
    path('admin/<int:nid>/edit/', admin.admin_edit),
    path('admin/<int:nid>/delete/', admin.admin_delete),
    path('admin/<int:nid>/reset/', admin.admin_reset),

    path('account/login/', account.account_login),
    path('account/logout/', account.account_logout),
    path('check/code/', account.image_code),

    path('task/list/',task.task_list),
    path('task/add/', task.task_add),




]
