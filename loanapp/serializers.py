from django.contrib.auth.models import User
from rest_framework import serializers
from loanapp.models import Application


class ApplicationSerializer(serializers.HyperlinkedModelSerializer): # new
    owner = serializers.ReadOnlyField(source='owner.username')


    class Meta:
        model = Application
        fields = ('url', 'id', 'title', 'code', 'linenos',
                    'owner',) # new


class UserSerializer(serializers.HyperlinkedModelSerializer): # new
    applications = serializers.HyperlinkedRelatedField( # new
        many=True, view_name='application-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'applications') # new