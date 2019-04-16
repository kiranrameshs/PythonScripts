from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    #url(r'^$', views.HomeView.as_view(), name='home'),
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('charts/', views.ChartsPageView.as_view(), name='charts'),
    path('result/', views.ResultPageView.as_view(), name='result'),
    path('update/', views.UpdatePageView.as_view(), name='update'),
    url(r'^submit', views.submit),
    url(r'^update', views.update),
    url(r'^charts/get_charts', views.get_charts),
]

