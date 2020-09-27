import base64
import json

import jwt
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


def decode_jwt(jwt_value):
    """
    :type jwt_value: str
    simple JWT에서 제공하는 메소드가 안될 시, 사용 방안.
    """
    try:
        headers_enc, payload_enc, verify_signature = jwt_value.split(".")
    except ValueError:
        raise jwt.InvalidTokenError()

    payload_enc += '=' * (-len(payload_enc) % 4)  # add padding
    payload = json.loads(base64.b64decode(payload_enc).decode("utf-8"))

    algorithms = getattr(settings, 'JWT_JWS_ALGORITHMS', ['HS256', 'RS256'])
    public_key_name = 'JWT_PUBLIC_KEY_{}'.format(payload['iss'].upper())
    public_key = getattr(settings, public_key_name, None)
    if not public_key:
        raise ImproperlyConfigured('Missing setting {}'.format(
                                   public_key_name))

    decoded = jwt.decode(jwt_value, public_key, algorithms=algorithms)
    return decoded