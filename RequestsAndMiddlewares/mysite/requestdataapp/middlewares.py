import time

from django.http import HttpRequest, HttpResponse

def setup_useragent_on_request_middleware(get_response):

    print("initial call")
    def middleware(request: HttpRequest):
        print("before get response")
        request.user_agent = request.META["HTTP_USER_AGENT"]
        response = get_response(request)
        print("after get response")
        return response

    return middleware

class CountRequestsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.request_time = {}
        self.requests_count = 0
        self.responses_count = 0
        self.exceptions_count = 0

    def __call__(self, request: HttpRequest):
        ip_address = request.META.get('REMOTE_ADDR')
        time_delay = 10
        if self.request_time:
            if (round(time.time()) - self.request_time['time'] < time_delay and
                    self.request_time['ip_address'] == ip_address):
                return HttpResponse("A repeat request is only possible after 10 seconds.")

        self.request_time = {'time': round(time.time()), 'ip_address': ip_address}

        self.requests_count += 1
        print("requests count", self.requests_count)
        response = self.get_response(request)
        self.responses_count += 1
        print("responses count", self.responses_count)
        return response

    def process_exception(self, request: HttpRequest, exceprion: Exception):
        self.exceptions_count += 1
        print("got", self.exceptions_count, "exceptions so far")