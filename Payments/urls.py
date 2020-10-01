from django.conf.urls import url
from Payments import views

urlpatterns = [
    url(r'^validate/$', views.validator),
    # url(r'^confirm/$', views.Confirm.as_view(), name=views.Confirm.name),
    url(r'^confirm/$', views.confirm),

]
