"""myobject URL Configuration

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
from django.urls import path

from web.views import index

urlpatterns = [
    path('', index.login, name="web_login"),
    path('login', index.login, name="web_login"),
    path('dologin', index.dologin, name="web_dologin"),
    path('logout', index.logout, name="web_logout"),
    path('buy', index.inbuy, name="web_buy"),
    path('order', index.inorder, name="web_order"),
    path('sheet', index.insheet, name="web_sheet"),
    path('modify', index.modify, name="web_modify"),
    path('sheetout', index.sheetout, name="web_sheetout"),
]
