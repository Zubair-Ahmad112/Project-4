from django.urls import path
from . import views
from .views import login_view,logout_view

urlpatterns = [
    path('home/', views.main, name='index'),
    path('<int:id>', views.view, name='view_employee'),
    path('add/', views.adding, name='add'),
    path('edit/<int:id>/', views.update, name='edit'),
    path('delete/<int:id>/', views.destroy, name='delete'),
    path('info/', views.info, name='info'),
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    

]
