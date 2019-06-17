

from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from .views.skus import *
from .views.users import *
from .views.spus import *
from .views.specs import *
from .views.options import *
from .views.channels import *
from .views.brands import *
from .views.orders import *

urlpatterns = [
    url(r'^authorizations/', obtain_jwt_token),
    url(r'^users/$', UserView.as_view()),

    url(r'^skus/$', SKUView.as_view({"get":"list",
                                    "post":"create"})),

    url(r'^skus/(?P<pk>\d+)/', SKUView.as_view({"delete":"destroy",
                                               "put":"update",
                                               "patch":"partial_update",
                                               "get":"retrieve"})),

    # 获得所有分类
    url(r'^skus/categories/$', SKUCategorieView.as_view()),
    url(r'^goods/simple/$', SPUSimpleView.as_view()),
    url(r'^goods/(?P<pk>\d+)/specs/$', SPUSpecView.as_view()),

    # spu商品
    url(r'^goods/$', SPUGoodsView.as_view({"get":"list", "post":"create"})),


    url(r'^goods/brands/simple/$', SPUBrandView.as_view()),
    url(r'^goods/channel/categories/$', ChannelCategorysView.as_view()),
    url(r'^goods/channel/categories/(?P<pk>\d+)/$', ChannelCategorysView.as_view()),

    # 获得spu商品
    url(r'^goods/(?P<pk>\d+)/$', SPUGoodsView.as_view({"get":"retrieve", "put":"update", "delete":"destroy"})),

    # 获得所有spu规格
    url(r'^goods/specs/$', SPUSpecificationView.as_view({"get":"list", "post":"create"})),
    url(r'^goods/specs/(?P<pk>\d+)/$', SPUSpecificationView.as_view({"get":"retrieve",
                                                                     "delete":"destroy",
                                                                     "put":"update",
                                                                     "patch":"partial_update"})),


    url(r'^specs/options/$', OptionsView.as_view({"get":"list", "post":"create"})),
    url(r'^specs/options/(?P<pk>\d+)/$', OptionsView.as_view({"get":"retrieve",
                                                              "put":"update",
                                                              "patch":"partial_update",
                                                              "delete":"destroy"})),
    url(r'^goods/specs/simple/$', OptionSpecSimple.as_view({"get":"list"})),

    url(r'^goods/channels/$', GoodsChannelView.as_view({"get":"list",
                                                        "post":"create"})),

    url(r'^goods/channels/(?P<pk>\d+)/$', GoodsChannelView.as_view({"get":"retrieve",
                                                                    "put":"update",
                                                                    "patch":"partial_update",
                                                                    "delete":"destroy"})),

    url(r'^goods/channel_types/$', GoodsChannelGroupView.as_view()),
    url(r'^goods/categories/$', GoodsChannelCategoriesView.as_view()),

    url(r'^goods/brands/$', GoodsBrandsView.as_view({"get":"list", "post":"create"})),
    url(r'^goods/brands/(?P<pk>\d+)/$', GoodsBrandsView.as_view({"get":"retrieve",
                                                                 "put":"update",
                                                                 "patch":"partial_update",
                                                                 "delete":"destroy"})),


    url(r'^orders/$', OrdersView.as_view({"get":"list"})),
    url(r'^orders/(?P<order_id>\d+)/$', OrdersDetailView.as_view()),
    url(r'^orders/(?P<order_id>\d+)/status/$', OrdersDetailView.as_view()),
]