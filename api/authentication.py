from rest_framework.authentication import TokenAuthentication as BaseTokenAuth


# No expiration by default.
# Can use other authentication packages.
# Can create custom authentication class via from rest_framework.authtoken.models import Token
# if just receiving data don't need to change authentications often.


class TokenAuthentication(BaseTokenAuth):
    keyword = 'Bearer'