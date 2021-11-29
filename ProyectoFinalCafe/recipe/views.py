from typing import List
from django.shortcuts import render
from django.views.generic.list import ListView
from .forms import PedidoForm
from .models import Recipe
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
# Create your views here.

class RecipeCreatePedido(CreateView):
    form_class = PedidoForm
    template_name = 'recipe/pedido_cliente.html'
    success_url = reverse_lazy('recipes:success_pedido')
    def form_valid(self, form):
        # guardar datos del pedido 
        pedido = form.save(commit = False)
        pedido.save()
        return super().form_valid(form)
    
    def get_form_kwargs(self):
        # coloca el request disponible para el forms 
        kwargs = super(RecipeCreatePedido,self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

class PedidoSuccess(TemplateView):
    template_name = 'recipe/pedido_success.html'


class RecipeListView(ListView):
    model = Recipe

class RecipeDetailView(DetailView):
    model = Recipe

@method_decorator(staff_member_required,name='dispatch')
class RecipeCreateView(CreateView):
    model = Recipe
    fields = ['title', 'content', 'order']
    success_url = reverse_lazy('recipes:recipes')

class RecipeUpdateView(UpdateView):
    model = Recipe
    fields = ['title', 'content', 'order']
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse_lazy('recipes:update', args=[self.object.id]) + '?ok'
    
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    

@method_decorator(staff_member_required,name='dispatch')
class RecipeDeleteView(DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipes:recipes')

def crea_diccionario(datos_pedido):
    diccionario = {}
    datos_pedido = datos_pedido[:-1]
    productos = datos_pedido.split("|")
    for producto in productos:
        detalle = producto.split('-')
        diccionario[detalle[0]] = int(detalle[1])
    return diccionario


def realizar_pedido(request):
    pedido = list()
    if request.method == 'POST':
        datos_pedido = request.POST['datos_pedido']
        productos = crea_diccionario(datos_pedido)
        total = 0
        for codigo_barrra in productos.keys():
            cantidad = productos[codigo_barrra]
            if cantidad > 0:
                dict_productos = {}
                receta = Recipe.objects.get(pk = codigo_barrra)
                dict_productos['id'] = receta.id
                dict_productos['descripcion'] = receta.title
                dict_productos['cantidad'] = cantidad
                dict_productos['precio'] = "100"
                total += cantidad *100
                pedido.append(dict_productos)
        # se guarda el total en una variable de sesión
        request.session['total']= float(total)
    return render(request, "recipe/detalle_pedido.html",{'pedido': pedido,'total':total})
