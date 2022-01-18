from django.contrib import admin

from .models import (
    Goods,
    GoodsRegister,
    Extra,
    ExtraRegister,
)

admin.site.register(Goods)
admin.site.register(GoodsRegister)
admin.site.register(Extra)
admin.site.register(ExtraRegister)