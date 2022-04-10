from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse


@permission_required('core.view_animal', raise_exception=True)
def index(request, response=HttpResponse("Hello, world. You're at the polls index.")):
    return response
