

from django.conf.urls import url, include
from django.contrib import admin
from .views import JSONWebTokenAPIView,UserTotalCountView,UserDayIncreCountView,UserActiveCountView,UserOrderCountView,\
    UserMonthCountView,GoodsDayView
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    # url(r'authorizations/$', JSONWebTokenAPIView.as_view()),
    url(r'authorizations/$', obtain_jwt_token),
    url(r'statistical/total_count/$', UserTotalCountView.as_view()),
    url(r'statistical/day_increment/$', UserDayIncreCountView.as_view()),
    url(r'statistical/day_active/$', UserActiveCountView.as_view()),
    url(r'statistical/day_orders/$', UserOrderCountView.as_view()),
    url(r'statistical/month_increment/$', UserMonthCountView.as_view()),
    url(r'statistical/goods_day_views/$', GoodsDayView.as_view()),

]