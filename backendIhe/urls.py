from django.urls import path 
from . import views

urlpatterns = [
    path('auditeurs/', views.ListAuditeurs.as_view(), name = 'auditeurs'),
    path('auditeur/<int:id_auditeur>/', views.DetailAuditeur.as_view(), name = 'auditeur'),
    path('evenements/', views.ListEvents.as_view(), name = 'evenements'),
    path('evenement/<int:id_event>/', views.DetailEvent.as_view(), name = 'evenement'),
    path('instituts/', views.ListInstituts.as_view(), name = 'instituts'),
    path('institut/<int:id_institut>/', views.DetailInstitut.as_view(), name = 'institut'),
    path('accueil/<int:id_accueil>/', views.DetailAccueil.as_view(), name = 'accueil'),
    path('experience/<int:id_experience>/', views.DetailExperience.as_view(), name = 'experience'),
    path('pedagogie/<int:id_pedagogie>/', views.DetailPedagogie.as_view(), name = 'pedagogie'),
    path('autre/<int:id_autre>/', views.DetailAutreTexte.as_view(), name = 'autre')
]