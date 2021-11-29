from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Page
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
# Create your views here.
def page(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    return render(request, 'pages/sample.html',{'page':page})

@method_decorator(staff_member_required,name='dispatch')
class PageDeleteView(DeleteView):
    model = Page
    success_url = reverse_lazy('pages')

@method_decorator(staff_member_required,name='dispatch')
class PageCreateView(CreateView):
    model = Page
    fields = ['title', 'content', 'order']
    success_url = reverse_lazy('pages')

@method_decorator(staff_member_required,name='dispatch')
class PageUpdateView(UpdateView):
    model = Page
    fields = ['title', 'content', 'order']
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse_lazy('update_page', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required,name='dispatch')
class PageDetailView(DetailView):
    model = Page

@method_decorator(staff_member_required,name='dispatch')
class PageListView(ListView):
    model = Page