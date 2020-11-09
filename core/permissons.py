# from rest_framework.permissions import BasePermission, SAFE_METHODS

# class IsOwnerOrReadOlny(BasePermission): 
#     message = 'you must be the owner of this object'
#     my_safe_method = ['GET', 'PUT']
#     def has_permission(self, request, view):
# 		# check if user who launched request is object owner 
#         if request.method in self.my_safe_method: 
#             return True
#         else:
#             return False

#     def has_object_permission(self, request, view, obj):
#         if request.method in SAFE_METHODS:
#             return True
#         return obj.user == request.user