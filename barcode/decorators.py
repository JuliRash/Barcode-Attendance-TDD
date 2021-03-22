from django.core.exceptions import PermissionDenied

from barcode.models import Setup


def setup_is_configured(function):
    def wrap(request, *args, **kwargs):
        setup = Setup.objects.exists()
        if setup:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied("Application Not Configured yet contact the system administrator")
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
