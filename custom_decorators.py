from django.shortcuts import redirect

def guest_only(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            # Redirect logged-in users to a different page.
            return redirect('jobboard:home')  
        return view_func(request, *args, **kwargs)

    return _wrapped_view
