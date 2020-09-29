from django.urls import path
from . import views


urlpatterns = [


    path('', views.index,name="index"),

    path('login/', views.loginPage, name='login'),
    path('logout/',views.logoutUser,name ='logout'),


    path('produse',views.produse,name='produse'),

    path('felul_principal', views.felul_principal, name='felul_principal'),
    path('crearefelul_principal', views.crearefelul_principal, name='crearefelul_principal'),
    path('modificafelul_principal/<str:pk>/', views.felul_principal, name='modificafelul_principal'),
    path('stergerefelul_principal/<str:pk>/', views.stergerefelul_principal, name='stergerefelul_principal'),

    path('bauturi', views.bauturi, name='bauturi'),
    path('crearebauturi', views.crearebauturi,name= 'crearebauturi'),
    path('modificabauturi/<str:pk>/', views.modificabauturi, name='modificabauturi'),
    path('stergerebauturi/<str:pk>/', views.stergerebauturi, name='stergerebauturi'),

    path('desert', views.desert, name='desert'),
    path('crearedesert', views.crearedesert,name= 'crearedesert'),
    path('modificadesert/<str:pk>/', views.modificadesert, name='modificadesert'),
    path('stergeredesert/<str:pk>/', views.stergeredesert, name='stergeredesert'),





]




