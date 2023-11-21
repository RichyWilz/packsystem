from functools import wraps
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.cache import never_cache

def custom_admin_only(view_func):
    view_func = never_cache(view_func)
    view_func = login_required(login_url='login/')(view_func)
    view_func = user_passes_test(lambda u: u.is_superuser)(view_func)
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        return view_func(request, *args, **kwargs)
    return wrapped_view


def custom_authorised_user(view_func):
    view_func = never_cache(view_func)
    view_func = login_required(login_url='login/')(view_func)
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        return view_func(request, *args, **kwargs)
    return wrapped_view