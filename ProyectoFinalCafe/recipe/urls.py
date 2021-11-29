from django.urls import path
from .import views

recipe_patterns = ([
    path('',views.RecipeListView.as_view(), name="recipes"),
    path('<int:pk>/<slug:recipe_slug>',views.RecipeDetailView.as_view(), name="recipe_detail"),
    path('create/',views.RecipeCreateView.as_view(), name="create"),
    path('update/<int:pk>',views.RecipeUpdateView.as_view(), name="update"),
    path('delete/<int:pk>',views.RecipeDeleteView.as_view(), name="delete"),
    path('pedido/',views.realizar_pedido, name="detalle_pedido"),
    path('create_pedido/',views.RecipeCreatePedido.as_view(), name="create_pedido"),
    path('success_pedido/',views.PedidoSuccess.as_view(), name="success_pedido"),
], 'recipes')

