

from django.conf.urls import url, include
from .views.user_login_views import *
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import SimpleRouter
from meiduo_admin.views.home_views import *
from rest_framework.routers import SimpleRouter
from meiduo_admin.views.user_views import *
from meiduo_admin.views.sku_views import *

from meiduo_admin.views.spu_views import *
from meiduo_admin.views.spec_views import *
from meiduo_admin.views.option_views import *
from meiduo_admin.views.channel_views import *
from meiduo_admin.views.brand_views import *
from meiduo_admin.views.image_views import *



urlpatterns = [
    # url(r'^authorizations/$', UserLoginView.as_view())

    # obtain_jwt_token给我们返回给前端的数据只有token，没有额外的数据
    url(r'^authorizations/$', obtain_jwt_token),
    # url(r'^statistical/total_count/$', HomeView.as_view({"get":"total_count"})),

    # 用户数据展示和新增用户
    url(r'^users/$', UserView.as_view()),

    # sku商品表增删改查
    url(r'^skus/$', SKUView.as_view({"get":"list", "post":"create"})),
    url(r'^skus/(?P<pk>\d+)/$', SKUView.as_view({"delete":"destroy", "get":"retrieve", "put":"update"})),
    # sku三级分类
    url(r'^skus/categories/$', GoodsCategoryView.as_view()),
    # sku所属spu
    url(r'^goods/simple/$', SPUSimpleView.as_view()),
    # sku商品规格
    url(r'^goods/(?P<pk>\d+)/specs/$', SpecOptView.as_view()),

    #spu商品所有数据，新建单一资源
    url(r'^goods/$', SPUViewSet.as_view({'get': 'list', 'post':'create'})),
    #spu商品单一对象删除，获得单一对象数据
    url(r'^goods/(?P<pk>\d+)/$', SPUViewSet.as_view({'delete':'destroy', 'get':'retrieve', "put":'update'})),

    #获得spu商品对应可选品牌信息
    url(r'^goods/brands/simple/$', BrandSimpleView.as_view()),
    #获得一级分类信息
    url(r'^goods/channel/categories/$', GoodsCategoryView.as_view()),
    #获得二级或三级分类信息
    url(r'^goods/channel/categories/(?P<pk>\d+)/$', GoodsCategoryView.as_view()),

    # 获得规格所有数据
    # url(r'^goods/specs/$', SpecViewSet.as_view({"get":"list", "post":"create"})),
    # 单一规格资源的删除,获得单一资源,更新单一资源
    # url(r'^goods/specs/(?P<pk>\d+)/$', SpecViewSet.as_view({'delete':'destroy',
    #                                                         'get':'retrieve',
    #                                                         'put':'update'})),

    # 获得规格选项所有数据，新建单一资源
    url(r'^specs/options/$', OptionViewSet.as_view({"get":"list", 'post':'create'})),
    # 删除规格选项的单一数据
    url(r'^specs/options/(?P<pk>\d+)/$', OptionViewSet.as_view({'delete': 'destroy',
                                                                'get':'retrieve',
                                                                'put':'update'})),

    # 获得规格所有的信息
    url(r'^goods/specs/simple/$', SpecSimpleView.as_view()),

    #获得频道的所有数据
    url(r'^goods/channels/$', ChannelViewSet.as_view({'get':'list', 'post':'create'})),
    #获得单一频道数据
    url(r'^goods/channels/(?P<pk>\d+)/$', ChannelViewSet.as_view({'get':'retrieve',
                                                                  'put':'update',
                                                                  'delete':'destroy'})),
    #获得频道所有分组数据
    url(r'^goods/channel_types/$', ChannelViewSet.as_view({'get':'channel_types'})),
    #获得频道可选的一级分类
    url(r'^goods/categories/$', ChannelViewSet.as_view({'get':'categories'})),

    #获得品牌所有信息，数据新建
    url(r'^goods/brands/$', BrandViewSet.as_view({'get': 'list', 'post':'create'})),
    #删除对象
    url(r'^goods/brands/(?P<pk>\d+)/$', BrandViewSet.as_view({'delete': 'destroy',
                                                              'get':'retrieve',
                                                              'put':'update'})),
    #获得图片所有数据
    url(r'^skus/images/$', ImageViewSet.as_view({'get':'list', 'post':'create'})),
    #单个图片操作
    url(r'^skus/images/(?P<pk>\d+)/$', ImageViewSet.as_view({'get':'retrieve',
                                                             'put':'update',
                                                             'delete':'destroy'})),
    #获得新建图片可选sku商品
    url(r'^skus/simple/$', ImageViewSet.as_view({'get':'simple'})),

]


router = SimpleRouter()
router.register(prefix="statistical", viewset=HomeView, base_name="home")
router.register(prefix='goods/specs', viewset=SpecViewSet, base_name='specs')
urlpatterns += router.urls