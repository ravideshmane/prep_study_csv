from  django.urls import path
from . import views
urlpatterns =[
    path('csv/', views.uploadCSV),
    path('download/', views.download),

]