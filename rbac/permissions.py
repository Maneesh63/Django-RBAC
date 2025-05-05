from rest_framework.permissions import BasePermission
from .models import GroupPermission

class HasPermission(BasePermission):
    """
    Custom permission to check if the user has a specific permission.
    """
    def has_permission(self, request, view):
        required_permissions = getattr(view, 'required_permissions', {})
        required_permission = required_permissions.get(request.method)

        if not required_permission:
            return True  #
        
         
        if not request.user.is_authenticated:
            return False
        
        
        try:
            group_ids = request.user.groups.values_list('id', flat=True)
            return GroupPermission.objects.filter(
                group_id__in=group_ids,
                permission__name=required_permission
            ).exists()
        
        except Exception as e:
            import traceback;
            traceback.print_exc()
            return False

     