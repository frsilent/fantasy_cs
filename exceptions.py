"""
Global exception and warning classes.
"""


class RosterFullException(Exception):
    """Roster is already filled"""
    pass


class ObjectDoesNotExist(Exception):
    """The requested object does not exist"""
    silent_variable_failure = True


class InvalidRosterException(Exception):
    """Roster is invalid"""
    pass


#
#
# class MultipleObjectsReturned(Exception):
#     """The query returned multiple objects when only one was expected."""
#     pass
#
#
# class SuspiciousOperation(Exception):
#     """The user did something suspicious"""
#
#
# class SuspiciousMultipartForm(SuspiciousOperation):
#     """Suspect MIME request in multipart form data"""
#     pass
#
#
# class SuspiciousFileOperation(SuspiciousOperation):
#     """A Suspicious filesystem operation was attempted"""
#     pass
#
#
# class DisallowedHost(SuspiciousOperation):
#     """HTTP_HOST header contains invalid value"""
#     pass
#
#
# class DisallowedRedirect(SuspiciousOperation):
#     """Redirect to scheme not in allowed list"""
#     pass
#
#
# class PermissionDenied(Exception):
#     """The user did not have permission to do that"""
#     pass
#
#
# class MiddlewareNotUsed(Exception):
#     """This middleware is not used in this server configuration"""
#     pass
#
#
# class ImproperlyConfigured(Exception):
#     """Django is somehow improperly configured"""
#     pass
#
#
# class FieldError(Exception):
#     """Some kind of problem with a model field."""
#     pass
