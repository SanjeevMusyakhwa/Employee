
from django.urls import path
from app import views
urlpatterns = [
   path('', views.EmployeeListView.as_view(), name='listView'),
   path('create/', views.CreateEmployee.as_view(), name='create'),
   path('update/<int:pk>/', views.UpdateEmployee.as_view(), name='update'),
   path('delete/<int:pk>/', views.deleteEmployee.as_view(), name='delete'),
]
