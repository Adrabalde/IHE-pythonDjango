from django.contrib import admin
from .models import Auditeur, Evenement, Institut, Accueil, Experience, Pedagogie, AutreTexte

# Register your models here.
admin.site.register(Auditeur)
admin.site.register(Evenement)
admin.site.register(Institut)
admin.site.register(Accueil)
admin.site.register(Experience)
admin.site.register(Pedagogie)
admin.site.register(AutreTexte)