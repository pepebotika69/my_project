from django.contrib.auth.decorators import permission_required
from django.shortcuts import render

from core.models import Pet


def index(request):
    return render(request, 'pet/index.html', {})


@permission_required('core.view_pet', raise_exception=True)
def get_all_pets(request):
    return render(request, 'pet/all_pets.html', {
        'pets': Pet.objects.all()
    })
