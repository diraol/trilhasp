# -*- coding: utf-8 -*-
from rest_framework import permissions


class IsStaffOrTargetUser(permissions.BasePermission):
    def has_permission(self, request, view):
        # allow user to list all users if logged in user is staff
        return view.action == 'retrieve' or request.user.is_staff

    def has_object_permission(self, request, view, obj):
        # allow logged in user to view own details, allows staff to view all records
        return request.user.is_staff or request.user == obj


#def welcome_new_user(backend, *args, **kwargs):
#    print(kwargs)
#    pass
