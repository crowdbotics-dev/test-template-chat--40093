from rest_framework import authentication
from chat_user_profile.models import Contact,Profile,VerificationCode
from .serializers import ContactSerializer,ProfileSerializer,VerificationCodeSerializer
from rest_framework import viewsets

class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Profile.objects.all()

class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Contact.objects.all()

class VerificationCodeViewSet(viewsets.ModelViewSet):
    serializer_class = VerificationCodeSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = VerificationCode.objects.all()