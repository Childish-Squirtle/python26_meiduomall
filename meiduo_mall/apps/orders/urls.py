from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^orders/settlement/$', views.SettlementView.as_view()),
    url(r'^orders/commit/$', views.CommitView.as_view()),
    url(r'^orders/success/$', views.SuccessView.as_view()),
    url(r'^orders/info/(?P<page_num>\d+)/$', views.InfoView.as_view()),
    url(r'^orders/comment/$', views.CommentView.as_view()),
    url(r'^comment/(?P<sku_id>\d+)/$', views.CommentSKUView.as_view()),
]
