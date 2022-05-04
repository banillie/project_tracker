from rest_framework import permissions

from .permissions import IsStaffEditorPermission


class StaffEditorPermissionMixin():
    permission_classes = [
        permissions.IsAdminUser,
        # permissions.IsAuthenticatedOrReadOnly,
        IsStaffEditorPermission
    ]

