from django.shortcuts import render
from django.views import View


class TweeterView(View):
    template_name = 'tweeter/tweeter.html'

    def get(self, request, *args, **kwargs):
        return render(request,  self.template_name, {})
