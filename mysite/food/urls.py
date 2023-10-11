from django.urls import path
from . import views

app_name = "food"

urlpatterns = [
    path("", views.IndexListView.as_view(), name="index"),
    path("item/", views.item, name="item"),
    path("<int:pk>/", views.FoodDetailView.as_view(), name="detail"),
    path("delete/<int:pk>/", views.FoodDeleteView.as_view(), name="delete_item"),
    path("update/<int:pk>/", views.FoodUpdateView.as_view(), name="update_item"),
    path("add/", views.FoodCreateView.as_view(), name="create_item"),
]
