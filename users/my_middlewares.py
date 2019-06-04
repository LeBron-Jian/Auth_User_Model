from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse

class CustomerMiddleware(MiddlewareMixin):

    def process_request(self, request):
        print("Customer 1111111111middle ware ......")

    def process_response(self, request, response):
        print("Customer 111111111process_response...........")
        return response

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("process view 111111111111")

    def process_exception(self, request, exception):
        print("process exception 111111111111")

class CustomerMiddleware2(MiddlewareMixin):

    def process_request(self, request):
        print("Customer 2222222222middle ware ......")

    def process_response(self, request, response):
        print("Customer process_222222222response...........")
        return response

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("process view 222222222")

    def process_exception(self, request, exception):
        print("process exception 2222222222")
        return HttpResponse(exception)