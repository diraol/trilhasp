#-*- coding: utf-8 -*-

from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .serializers import *
from .util import IsStaffOrTargetUser


###############################################################################
##                     Classes for the Users                                 ##
###############################################################################


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    model = User
    lookup_field = 'username'
    permission_classes = (IsStaffOrTargetUser,)

    def get_permissions(self):
        # allow non-authenticated user to create via POST
        return (AllowAny() if self.request.method == 'POST'
                else IsStaffOrTargetUser()),

