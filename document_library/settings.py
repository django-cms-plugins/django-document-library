"""Default settings for the document_library app."""
from django.conf import settings


LOGIN_REQUIRED = getattr(settings, 'DOCUMENT_LIBRARY_LOGIN_REQUIRED', False)
