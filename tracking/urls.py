from django.urls import path
from tracking import views

urlpatterns = [
    path("", views.home, name="home"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path('load/records',views.load_csv_data,name='load'),
    path('api/records/', views.get_records, name='get_records'),
    path('api/create/', views.create_record, name='create_record'),
]