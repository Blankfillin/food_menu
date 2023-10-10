from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Item
from .forms import ItemForm

# Create your views here.


def index(request):
    item_list = Item.objects.all()
    context = {"item_list": item_list}
    return render(request, "food/index.html", context)


def item(request):
    return HttpResponse("<h1>This is an item view<h1>")


def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {"item": item}
    return render(request, "food/detail.html", context)


def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        item = form.save(commit=False)
        item.added_by = request.user
        item.save()
        return redirect("food:index")

    content = {"form": form}
    return render(request, "food/item-form.html", content)


def update_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect("food:index")

    content = {"form": form}
    return render(request, "food/item-form.html", content)


def delete_item(request, item_id):
    item = Item.objects.get(id=item_id)

    if request.method == "POST":
        item.delete()
        return redirect("food:index")

    content = {"item": item}
    return render(request, "food/item-delete.html", content)
