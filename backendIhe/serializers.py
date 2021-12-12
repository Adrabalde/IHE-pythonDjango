from rest_framework import serializers
from .models import Auditeur, Evenement, Institut, Accueil, Experience, Pedagogie, AutreTexte

class AuditeurSerializer(serializers.ModelSerializer):

    class Meta:
        model = Auditeur
        fields = ['id_auditeur', 'photo', 'nom_prenom', 'poste', 'annee_formation', 'avis']
    


class EventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Evenement
        fields = ['id_event', 'nom', 'descriptif', 'date_event', 'image']
    


class InstitutSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Institut
        fields = ['id_institut', 'sigle', 'nom_complet', 'logo', 'presentation', 'descriptif_formation', 'website', 'social_media']



class AccueilSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Accueil
        fields = ['id_accueil', 'titre', 'sous_titre', 'texte', 'image']



class ExperienceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Experience
        fields = ['id_experience', 'titre', 'texte', 'image']



class PedagogieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Pedagogie
        fields = ['id_pedagogie', 'titre', 'sous_titre', 'texte']



class AutreTexteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AutreTexte
        fields = ['id_autre', 'titre', 'sous_titre']