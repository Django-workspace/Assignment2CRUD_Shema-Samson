from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage,name="save"),
    path('retrieve/', views.showdata),
    path('delete/<int:id>', views.deletedata),
    path('edit/<int:id>', views.editdata),
    path('update/<int:id>', views.updatedata)
]