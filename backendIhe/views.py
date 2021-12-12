from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from openpyxl import load_workbook
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AuditeurSerializer, EventSerializer, InstitutSerializer, AccueilSerializer, ExperienceSerializer, PedagogieSerializer, AutreTexteSerializer
from .models import Auditeur, Evenement, Institut, Accueil, Experience, Pedagogie, AutreTexte

# Create your views here.

class ListAuditeurs(APIView):

    parser_classes = [MultiPartParser,]

    # Retrieve & display auditeurs
    def get(self, request, format = None):
        auditeurs = Auditeur.objects.all()
        serializer = AuditeurSerializer(auditeurs, many = True, context = {'request':request})
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    # Create new auditeur
    def post(self, request, format = None):

        serializer = AuditeurSerializer(data = request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class DetailAuditeur(APIView):

    parser_classes = [MultiPartParser,]
    
    # Search 1 auditeur database
    def get_object(self, id_auditeur):
        try:
            return Auditeur.objects.get(id_auditeur = id_auditeur)
        except ObjectDoesNotExist:
            raise Http404
 
    # Retrieve 1 auditeur 
    def get(self, request, id_auditeur, format = None):
        auditeur = self.get_object(id_auditeur)
        serializer = AuditeurSerializer(auditeur, many = False, context = {'request':request})
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    # Update 1 auditeur
    def put(self, request, id_auditeur, format = None):
        auditeur = self.get_object(id_auditeur)
        serializer = AuditeurSerializer(auditeur, data = request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    # Delete 1 auditeur 
    def delete(self, request, id_auditeur, format = None):
        auditeur = self.get_object(id_auditeur)
        auditeur.delete()
        return Response(status = status.HTTP_200_OK)



class ListEvents(APIView):

    # Retrieve & display events
    def get(self, request, format = None): 
        events = Evenement.objects.all()
        serializer = EventSerializer(events, many = True, context = {'request':request})
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    # Create new event
    def post(self, request, format = None):
        serializer = EventSerializer(data = request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
           return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class DetailEvent(APIView):

    # Search an event in database  
    def get_object(self, id_event):
        try:
            return Evenement.objects.get(id_event = id_event)
        except ObjectDoesNotExist:
            raise Http404
    
    # Retrieve an event
    def get(self, request, id_event, format = None):
        event = self.get_object(id_event)
        serializer = EventSerializer(event, many = False, context = {'request':request})
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    # Update an event
    def put(self, request, id_event, format = None):
        event = self.get_object(id_event)
        serializer = EventSerializer(event, data = request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status = status.HTTP_200_OK)
        else:
           return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    # Delete an event
    def delete(self, request, id_event, format = None):
        event = self.get_object(id_event)
        event.delete() 
        return Response(status = status.HTTP_200_OK)



class ListInstituts(APIView):

    # Retrieve & display institutes
    def get(self, request, format = None):
        instituts = Institut.objects.all()
        serializer = InstitutSerializer(instituts, many = True, context = {'request':request})
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    # Create new institute 
    def post(self, request, format = None):
        serializer = InstitutSerializer(data = request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
           return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class DetailInstitut(APIView):

    # Search an institute in database  
    def get_object(self, id_institut):
        try:
            return Institut.objects.get(id_institut = id_institut)
        except ObjectDoesNotExist:
            raise Http404
    
    # Retrieve an institute
    def get(self, request, id_institut, format = None):
        institut = self.get_object(id_institut)
        serializer = InstitutSerializer(institut, many = False, context = {'request':request})
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    # Update an institute 
    def put(self, request, id_institut, format = None):
        institut = self.get_object(id_institut)
        serializer = Institut(institut, data = request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status = status.HTTP_200_OK)
        else:
           return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    # Delete an institute  
    def delete(self, request, id_institut, format = None):
        institut = self.get_object(id_institut)
        institut.delete() 
        return Response(status.HTTP_200_OK)



class DetailAccueil(APIView):

    parser_classes = [MultiPartParser,]
    
    # Search home page 
    def get_object(self, id_accueil):
        try:
            return Accueil.objects.get(id_accueil = id_accueil)
        except ObjectDoesNotExist:
            raise Http404
 
    # Retrieve home page  
    def get(self, request, id_accueil, format = None):
        accueil = self.get_object(id_accueil)
        serializer = AccueilSerializer(accueil, many = False, context = {'request':request})
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    # Update home page 
    def put(self, request, id_accueil, format = None):
        accueil = self.get_object(id_accueil)
        serializer = AuditeurSerializer(accueil, data = request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    # Delete home page 
    def delete(self, request, id_accueil, format = None):
        accueil = self.get_object(id_accueil)
        accueil.delete()
        return Response(status = status.HTTP_200_OK)



class DetailExperience(APIView):

    parser_classes = [MultiPartParser,]
    
    # Search experience page 
    def get_object(self, id_experience):
        try:
            return Experience.objects.get(id_experience = id_experience)
        except ObjectDoesNotExist:
            raise Http404
 
    # Retrieve experience page  
    def get(self, request, id_experience, format = None):
        experience = self.get_object(id_experience)
        serializer = ExperienceSerializer(experience, many = False, context = {'request':request})
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    # Update experience page 
    def put(self, request, id_experience, format = None):
        experience = self.get_object(id_experience)
        serializer = ExperienceSerializer(experience, data = request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    # Delete experience page 
    def delete(self, request, id_experience, format = None):
        experience = self.get_object(id_experience)
        experience.delete()
        return Response(status = status.HTTP_200_OK)



class DetailPedagogie(APIView):
    
    # Search pedagogie page 
    def get_object(self, id_pedagogie):
        try:
            return Pedagogie.objects.get(id_pedagogie = id_pedagogie)
        except ObjectDoesNotExist:
            raise Http404
 
    # Retrieve pedagogie page  
    def get(self, request, id_pedagogie, format = None):
        pedagogie = self.get_object(id_pedagogie)
        serializer = PedagogieSerializer(pedagogie, many = False)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    # Update pedagogie page 
    def put(self, request, id_pedagogie, format = None):
        pedagogie = self.get_object(id_pedagogie)
        serializer = PedagogieSerializer(pedagogie, data = request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    # Delete pedagogie page 
    def delete(self, request, id_pedagogie, format = None):
        pedagogie = self.get_object(id_pedagogie)
        pedagogie.delete()
        return Response(status = status.HTTP_200_OK)


class DetailAutreTexte(APIView):
    
    # Search 
    def get_object(self, id_autre):
        try:
            return AutreTexte.objects.get(id_autre = id_autre)
        except ObjectDoesNotExist:
            raise Http404
 
    # Retrieve   
    def get(self, request, id_autre, format = None):
        autre = self.get_object(id_autre)
        serializer = AutreTexteSerializer(autre, many = False)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    # Update 
    def put(self, request, id_autre, format = None):
        autre = self.get_object(id_autre)
        serializer = AutreTexteSerializer(autre, data = request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    # Delete home page 
    def delete(self, request, id_autre, format = None):
        autre = self.get_object(id_autre)
        autre.delete()
        return Response(status = status.HTTP_200_OK)