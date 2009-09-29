import hashlib
from django.conf import settings


HIPPOCAMPUS_COOKIE_NAME = hashlib.md5('hippocampus' + settings.SECRET_KEY).hexdigest()
