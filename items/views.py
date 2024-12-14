from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Item
import json

@csrf_exempt
def item_list(request):
    if request.method == 'POST':
        items = Item.objects.all().values('item_id', 'name', 'price')
        return JsonResponse(list(items), safe=False)

@csrf_exempt
def item_add(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        item = Item(item_id=data['item_id'], name=data['name'], price=data['price'])
        item.save()
        return JsonResponse({'message': 'Item added successfully!'})

@csrf_exempt
def item_delete(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        item = Item.objects.get(id=data['id'])
        item.delete()
        return JsonResponse({'message': 'Item deleted successfully!'})

@csrf_exempt
def item_edit(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        item = Item.objects.get(id=data['id'])
        item.item_id = data['item_id']
        item.name = data['name']
        item.price = data['price']
        item.save()
        return JsonResponse({'message': 'Item updated successfully!'})
