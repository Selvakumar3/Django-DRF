from django.urls import path
from app import views
from .views import *


urlpatterns = [
    path("create/" ,views.add, name='add'),
    path("view/" ,views.view, name='view'),
    path("view/" ,views.view, name='view'),
    
    path("update/<int:pk>/",views.update, name="update"),
    path("delete/<int:pk>/",views.delete, name="delete"),
    
 ###################################################################################
 
    path("",views.booklist, name="booklist"),
    path("d/<int:pk>/",views.bookdetails, name="bookdetail"),
    path("c/",views.bookcreate, name="bookcreate"),
    path("u/<int:pk>/",views.bookupdate, name="bookupdate"),
    path("del/<int:pk>/",views.bookdelete, name="bookdelete"),
    
###################################################################################
              #class based views

    path('books/', views.BooksList.as_view()),
    path('books/<int:pk>/', views.BooksDetail.as_view()),
    

    ###################################################################################
              # generic  views
     
  path('students/', views.StudentsList.as_view()),
  path('students/<int:pk>/', views.Studentsdetail.as_view()),

]
