from django.contrib import admin
from pizzas.models import (Pizza,Topping)
#后台管理文件
admin.site.register(Pizza)
admin.site.register(Topping)