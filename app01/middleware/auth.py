from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect

class AuthMiddleWare(MiddlewareMixin):

    def process_request(self,request):

        # 0. set the allowed URL, when without sesson
        if request.path_info in ['/account/login/','/check/code/']:
            return

        # 1. if session exists, then run view. when without session, reponse
        info_dict = request.session.get("info")

        if info_dict:
            return

        return redirect("/account/login/")
