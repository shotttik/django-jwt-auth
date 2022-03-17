import jwt
from django.conf import settings
from django.middleware.csrf import CsrfViewMiddleware
from rest_framework import authentication, exceptions

from .models import User

# class CSRFCheck(CsrfViewMiddleware):
#     def _reject(self, request, reason):
#         # Return the failure reason instead of an HttpResponse
#         return reason


class JWTAuthentication(authentication.BaseAuthentication):
    authentication_header_prefix = 'Token'

    def authenticate(self, request):
        """
        The `authenticate` method is called on every request regardless of
        whether the endpoint requires authentication. 
        """

        request.user = None
        auth_header = authentication.get_authorization_header(request).split()
        auth_header_prefix = self.authentication_header_prefix.lower()

        if not auth_header:
            return None

        if len(auth_header) == 1:
            return None

        elif len(auth_header) > 2:
            return None

        prefix = auth_header[0].decode('utf-8')
        token = auth_header[1].decode('utf-8')

        if prefix.lower() != auth_header_prefix:
            return None

        return self._authenticate_credentials(request, token)

    def _authenticate_credentials(self, request, token):

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, 'HS256',)

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('access_token expired')
        except IndexError:
            raise exceptions.AuthenticationFailed('Token prefix missing')
        except:
            msg = 'Invalid authentication. could not decode token.'
            raise exceptions.AuthenticationFailed(msg)

        try:
            user = User.objects.get(pk=payload['id'])
        except User.DoesNotExist:
            msg = 'No user matching this token was found.'
            raise exceptions.AuthenticationFailed(msg)

        if not user.is_active:
            msg = "This user has been deactivated"
            raise exceptions.AuthenticationFailed(msg)

        # self.enforce_csrf(request)

        return (user, token)

    # def enforce_csrf(self, request):
    #     """
    #     Enforce CSRF validation
    #     """
    #     check = CSRFCheck()
    #     # populates request.META['CSRF_COOKIE'], which is used in process_view()
    #     check.process_request(request)
    #     reason = check.process_view(request, None, (), {})
    #     print(reason)
    #     if reason:
    #         # CSRF failed, bail with explicit error message
    #         raise exceptions.PermissionDenied('CSRF Failed: %s' % reason)
