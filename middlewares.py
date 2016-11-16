import json

class BodyPostMiddleware(object):

    def process_request(self, request):
        try:
            if request.method != 'GET' and request.body:
                request.POST = request.POST.copy()
                request.POST.update(json.loads(request.body.decode()))
        except Exception as e:
            pass
