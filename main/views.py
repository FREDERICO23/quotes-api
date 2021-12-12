from . import models
from rest_framework import viewsets
from . import serializers

class QuotesViewSet(viewsets.ModelViewSet):
    queryset = models.Quote.objects.all()
    serializer_class = serializers.QuoteSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer