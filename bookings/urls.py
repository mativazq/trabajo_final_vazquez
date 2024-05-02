from django.urls import path

from .views import (
    home_view,
    SalaListView,
    SalaDetailView,
    SalaDeleteView,
    SalaUpdateView,
    SalaCreateView,
)




urlpatterns = [
    path('', home_view),
    path('sala/list/', SalaListView.as_view(), name='sala-list'),
    path('sala/create/', SalaCreateView.as_view(), name='sala-create'),
    path('sala/<int:pk>/detail/', SalaDetailView.as_view(), name='sala-detail'),
    path('sala/<int:pk>/delete/', SalaDeleteView.as_view(), name='sala-delete'),
    path('sala/<int:pk>/update/', SalaUpdateView.as_view(), name='sala-update'),
    
]