from django.urls import path
from .views import index, get_visit, export_excel, list_visit_day, add_visit

urlpatterns = [
    path('', index, name='index'),
    path('visit/<str:slug>', get_visit, name='visit'),
    path('export/excel/', export_excel, name='export_excel'),
    path('list-visit-day/', list_visit_day, name='list_visit_day'),
    path('add_visit/', add_visit, name='add_visit'),

]

