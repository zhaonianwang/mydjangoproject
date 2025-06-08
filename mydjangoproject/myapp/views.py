#from django.shortcuts import render
#from .models import Item

#def index(request):
#    items = Item.objects.all()
#    return render(request, 'myapp/index.html', {'items': items})
	
	
	
from django.shortcuts import render

def item_list(request):
    items = [
        {'name': 'Item 1', 'description': 'First item description'},
        {'name': 'Item 2', 'description': 'Second item description'},
    ]
    return render(request, 'myapp/index.html', {'items': items})
