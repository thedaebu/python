from django.urls import path
from . import views


app_name = 'reading'
urlpatterns = [
    path('', views.index, name='index'),  # path, index method from views file, name of url
    path('<int:book_id>', views.info, name='info')
]
