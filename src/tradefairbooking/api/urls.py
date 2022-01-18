from django.urls import path, include
from .views import (
    # Goods
    GoodsListView,
    GoodsMasterCreateView,
    GoodsMasterRUDView,

    # Goods Booking
    GoodsRegisterListView,
    GoodsRegisterMasterListView,
    GoodsRegisterMasterCreateView,
    GoodsRegisterMasterRDView,

    # Extra
    ExtraListView,
    ExtraMasterCreateView,
    ExtraMasterRUDView,

    # Extra Register
    ExtraRegisterListView,
    ExtraRegisterMasterListView,
    ExtraRegisterMasterCreateView,
    ExtraRegisterMasterRDView
)

app_name = 'tradefair-api'

urlpatterns = [
    # Goods
    path("goods/", GoodsListView.as_view(), name="goods"),

    # Goods Register
    path("goods/register/", GoodsRegisterListView.as_view(), name="goods-register"),


    # Master Series

    # Goods
    path("goods/master/create/", GoodsMasterCreateView.as_view(),
         name="goods-master-create"),

    path("goods/master/<int:id>/",
         GoodsMasterRUDView.as_view(), name="goods-master-rud"),

    # Goods Register
    path("goods/master/register/", GoodsRegisterMasterListView.as_view(),
         name="goods-register-master-list"),

    path("goods/master/register/create/", GoodsRegisterMasterCreateView.as_view(),
         name="goods-register-master-create"),

    path("goods/master/register/<int:id>/",
         GoodsRegisterMasterRDView.as_view(), name="goods-register-master-rud"),



    # Extra
    path("extra/", ExtraListView.as_view(), name="extra"),

    # Extra Register
    path("extra/register/", ExtraRegisterListView.as_view(), name="extra-register"),


    # Master Series

    # Extra
    path("extra/master/create/", GoodsMasterCreateView.as_view(),
         name="extra-master-create"),

    path("extra/master/<int:id>/",
         ExtraMasterRUDView.as_view(), name="extra-master-rud"),

    # Extra Register
    path("extra/master/register/", ExtraRegisterMasterListView.as_view(),
         name="extra-register-master-list"),

    path("extra/master/register/create/", ExtraRegisterMasterCreateView.as_view(),
         name="extra-register-master-create"),

    path("extra/master/register/<int:id>/",
         ExtraRegisterMasterRDView.as_view(), name="extra-register-master-rud"),
]
