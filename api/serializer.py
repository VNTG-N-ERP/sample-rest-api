from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Codes


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class CodesSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)

    class Meta:
        model = Codes
        fields = (
            'id',
            'code_type',
            'code',
            'code_name',
            'sort_seq',
            'use_yn',
            'remark',
        )
        read_only_fields = ('code_type', 'code')
