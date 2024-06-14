from rest_framework import serializers
from LibApp.models import LibraryDB

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryDB
        fields = (
            'BookID',
            'BookName',
            'AuthorName',
            'Pub_Date',
            'Price',
            'Image',
        )