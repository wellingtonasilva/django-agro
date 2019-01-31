from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('listagem', views.listagem, name='listagem'),
    path('novo', views.cliente_novo, name='novo'),
    path('cliente/add', views.cliente_add, name='cliente_add'),
    path('cliente/edit/<int:id>', views.cliente_edit, name='cliente_edit'),
    path('cliente/delete/<int:id>', views.cliente_delete, name='cliente_delete'),
    path('cliente/view/<int:id>', views.cliente_view, name='cliente_view'),
    path('cliente/save/<int:id>', views.cliente_save, name='cliente_save'),
    path('<int:question_id>', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('api/get_endereco', views.get_endereco, name='get_endereco'),
    path('check_login', views.check_login, name='check_login')
]

