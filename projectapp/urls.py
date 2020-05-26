from django.conf.urls import url
from projectapp import views

# TEMPLATE TAGGING
app_name = 'projectapp'

urlpatterns=[
    url(r'^index/$',views.index,name='index'),
    url(r'^gejala/$',views.gejala,name='gejala'),
    url(r'^daftarrsrujukan/$',views.daftarrsrujukan,name='daftarrsrujukan'),
    url(r'^coba/$',views.coba,name='coba'),
    url(r'^external/$',views.external),
]
