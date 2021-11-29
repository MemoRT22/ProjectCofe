from django.urls import path
from . import views

urlpatterns = [
    path('',views.PageListView.as_view(), name="pages"),
    path('<int:page_id>/',views.page, name="page"),
    path('<int:pk>/<slug:page_slug>',views.PageDetailView.as_view(), name="page_detail"),
    path('create_page/',views.PageCreateView.as_view(), name="create_page"),
    path('update_page/<int:pk>',views.PageUpdateView.as_view(), name="update_page"),
    path('delete_page/<int:pk>',views.PageDeleteView.as_view(), name="delete_page"),
]