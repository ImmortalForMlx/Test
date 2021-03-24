from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse


class Mymidd1(MiddlewareMixin):
    def process_request(self,request):
        print('from md1')
        # return HttpResponse('no')

    def process_response(self,resquest,response):
        print('from response1')
        return response



class Mymidd2(MiddlewareMixin):
    def process_request(self,request):
        print('from md2')

    def process_response(self,resquest,response):
        print('from response2')
        print(resquest)
        print(self)
        print(response)
        return response
