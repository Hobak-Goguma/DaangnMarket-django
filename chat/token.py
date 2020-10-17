from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from jwt import decode as jwt_decode
from django.conf import settings
from django.contrib.auth import get_user_model
from common.models.member_model import Member
from asgiref.sync import sync_to_async


class TokenAuthMiddleware:
    """
    Custom token auth middleware
    """

    def __init__(self, inner):
        # Store the ASGI application we were passed
        self.inner = inner

    def __call__(self, scope):

        # Get the token
        token = ''
        try:
            token = dict(scope['headers'])[b'authorization'].decode('utf8').split(' ')[1]
        except KeyError as e:
            return self.inner(dict(scope, user='Anonymous'))

        # Try to authenticate the user
        try:
            # This will automatically validate the token and raise an error if token is invalid
            UntypedToken(token, 34)
        except (InvalidToken, TokenError) as e:
            # Token is invalid
            return self.inner(dict(scope, user='Anonymous'))
        else:
            #  Then token is valid, decode it
            decoded_data = jwt_decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            # Will return a dictionary like -
            # {
            #     "token_type": "access",
            #     "exp": 1568770772,
            #     "jti": "5c15e80d65b04c20ad34d77b6703251b",
            #     "user_id": 6
            # }

            # Get the user using ID
        # Return the inner application directly and let it run everything else
            user = Member.objects.get(auth=decoded_data['user_id'])
            print(user, 3324)
        return self.inner(dict(scope, user=decoded_data['user_id']))
