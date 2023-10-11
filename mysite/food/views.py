from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)
from .models import Item
from .forms import ItemForm

# Create your views here.


def index(request):
    item_list = Item.objects.all()
    context = {"item_list": item_list}
    return render(request, "food/index.html", context)


class IndexListView(ListView):
    model = Item
    template_name = "food/index.html"
    context_object_name = "item_list"


def item(request):
    return HttpResponse("<h1>This is an item view<h1>")


def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {"item": item}
    return render(request, "food/detail.html", context)


class FoodDetailView(DetailView):
    model = Item
    template_name = "food/detail.html"
    context_object_name = "item"


def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        item = form.save(commit=False)
        item.added_by = request.user
        item.save()
        return redirect("food:index")

    content = {"form": form}
    return render(request, "food/item-form.html", content)


class FoodCreateView(CreateView):
    model = Item
    fields = ["item_name", "item_desc", "item_price", "item_image"]
    template_name = "food/item-form.html"
    success_url = reverse_lazy("food:index")

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super(FoodCreateView,self).form_valid(form)
    


def update_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect("food:index")

    content = {"form": form}
    return render(request, "food/item-form.html", content)

class FoodUpdateView(UpdateView):
    model = Item
    fields = ["item_name", "item_desc", "item_price", "item_image"]
    template_name = "food/item-form.html"
    success_url = reverse_lazy("food:index")

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super(FoodUpdateView,self).form_valid(form)

def delete_item(request, item_id):
    item = Item.objects.get(id=item_id)

    if request.method == "POST":
        item.delete()
        return redirect("food:index")

    content = {"item": item}
    return render(request, "food/item-delete.html", content)


class FoodDeleteView(DeleteView):
    model = Item
    template_name = "food/item-delete.html"
    success_url = reverse_lazy("food:index")