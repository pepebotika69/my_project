from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse


# TODO это чисто для того чтобы понять как все это работает, на самом деле можно удалить
@permission_required('core.view_pet', raise_exception=True)
def index(request):
    return HttpResponse("DONE")
