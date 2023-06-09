from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)


class FullDjangoModelPermission(permissions.DjangoModelPermissions):
    def __int__(self) -> None:
        self.perms_map['GET'] = ['%(app_label)s.add_%(model_name)s']


class ViewCustomerHistoryPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perms('store.view.history')
