from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reagent/', views.ReagentListView.as_view(), name='reagent'),
    path('reagent/<int:pk>', views.ReagentDetailView.as_view(), name='reagent-detail'),
    path('reagentinstance/', views.ReagentInstanceListView.as_view(), name='reagentinstance'),
    path('reagentinstance/<pk>', views.ReagentInstanceDetailView.as_view(), name='reagentinstance-detail'),
    path('principal/', views.PrincipalListView.as_view(), name='principal'),
    path('principal/<int:pk>', views.PrincipalDetailView.as_view(), name='principal-detail'),
    path('location/', views.LocationListView.as_view(), name='location'),
    path('location/<int:pk>', views.LocationDetailView.as_view(), name='location-detail'),
    path('source/', views.SourceListView.as_view(), name='source'),
    path('source/<int:pk>', views.SourceDetailView.as_view(), name='source-detail'),
    path('chinese_name/', views.ChineseNameListView.as_view(), name='chinese_name'),
    path('chinese_name/<int:pk>', views.ChineseNameDetailView.as_view(), name='chinese_name-detail'),
    path('english_name/', views.EnglishNameListView.as_view(), name='english_name'),
    path('english_name/<int:pk>', views.EnglishNameDetailView.as_view(), name='english_name-detail'),


]