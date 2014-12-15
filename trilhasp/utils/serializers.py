# -*- coding: utf-8 -*-

from rest_framework import serializers
from django.contrib.auth.models import User

###############################################################################
##                     Classes for the Users                                 ##
###############################################################################


class UserSerializer(serializers.ModelSerializer):
    answers = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = User
        fields = ('id','username', 'password', 'first_name', 'last_name', 'email')
        write_only_fields = ('password',)
        lookup_field = 'username'

    def restore_object(self, attrs, instance=None):
        # call set_password on user object. Without this
        # the password will be stored in plain text.
        user = super(UserSerializer, self).restore_object(attrs, instance)
        user.set_password(attrs['password'])
        return user
