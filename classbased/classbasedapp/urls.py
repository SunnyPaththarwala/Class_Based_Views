from django.urls import path
from classbasedapp import views

urlpatterns = [
    path('myviews',views.Myview.as_view()),
    path('addstudent',views.Addstudent.as_view()),
    path('allstudents',views.StudentList.as_view()),
    path('delete/<sid>',views.Deletestu.as_view()),
    path('update/<sid>',views.Updatestu.as_view()) 


]
