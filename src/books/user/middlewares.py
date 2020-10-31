# from time import time
from user.models import GclidClick


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # start = time()
        response = self.get_response(request)
        # end = time()
        # print(f'Path: {request.path}, Time: {end - start}')
        return response


class GoogleLead:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        gclid = request.GET.get('gclid')
        if gclid:
            if not GclidClick.objects.filter(value=gclid).exists():
                GclidClick.objects.create(value=gclid)
        response = self.get_response(request)
        return response
