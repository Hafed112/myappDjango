from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.stagiaire_form,name="stagiaire_insert"),
    path('<int:id>/',views.stagiaire_form,name="stagiaire_update"),
    path('<int:id>/delete',views.stagiaire_delete,name="stagiaire_delete"),
    path('list/',views.stagiaire_list,name="stagiaire_list")
]