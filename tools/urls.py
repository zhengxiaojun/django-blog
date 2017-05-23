from django.conf.urls import url

from . import views

app_name = 'tools'
urlpatterns = [
    url(r'^qrcode1/(.+)$', views.generate_qrcode, name='qrcode'),
]
