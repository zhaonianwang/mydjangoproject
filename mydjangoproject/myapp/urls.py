#from django.urls import path
#from .views import index

#urlpatterns = [
#   path('', index, name='index'),
#]


from django.urls import path
from .views import item_list

urlpatterns = [
    path('items/', item_list, name='item-list'),
]
