from rest_framework import serializers
from .models import  Quote, Author

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ('id','quote','date')

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id','name')