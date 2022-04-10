from django.contrib.auth.decorators import permission_required
from django.shortcuts import render


@permission_required('core.view_animal', raise_exception=True)
def index(request):
    return render(request, 'index.html', {})
