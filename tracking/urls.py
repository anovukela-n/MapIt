from django.urls import path
from tracking import views

urlpatterns = [
    path("", views.home, name="home"),#replace with load
    path('load/records',views.load_csv_data,name='load'),#use the home path ie the first url for the load
    path('api/create/', views.create_record, name='create_record'),
    path('api/json',views.GetDataAsJson,name="json"),
    path('table',views.getTable,name="table"),
    path('delete/<int:id>',views.delete,name="delete"),
    path("update/<int:id>",views.updateRecord,name="update"),
    path("map/",views.getMap,name='map')
]
 