from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminCocktail(BasePermission):
    message = 'Вам запрещено выполнять данное действие'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        # if request.user.is_superuser:
        #     return True
        # elif request.user != obj.author:
        #     return False

        return True
