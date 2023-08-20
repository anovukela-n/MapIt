from django.urls import path
from tracking import views

urlpatterns = [
    path("", views.home, name="home"),#replace with load
    path("hello/<name>", views.hello_there, name="hello_there"),#remove
    path('load/records',views.load_csv_data,name='load'),#use the home path ie the first url for the load
    path('api/records/', views.get_records, name='get_records'),#might need to be removed
    path('api/create/', views.create_record, name='create_record'),
    path('api/json',views.GetDataAsJson,name="json"),
    path('table',views.getTable,name="table"),
    path('delete/<int:id>',views.delete,name="delete"),
    path("update/<int:id>",views.updateRecord,name="update"),
]
 #   path('pullData/', views.fetchData, name='pullData'),
 #   path('saveData/',views.SaveData,name ='saveData'),
 #   path('queryDb/',views.GetData,name='queryDB'),
  #  path('table/delete/<int:id>',views.delete,name ='delete'),
  #  path('table/',views.getTable,name='table'),
   # path('table/update/<int:id>',views.update,name='update'),
   # path('table/update/updaterecord/<int:id>', views.updaterecord, name='updateRecord'),