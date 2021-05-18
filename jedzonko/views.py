from datetime import datetime
from django.http import HttpResponse

from django.shortcuts import render
from django.views import View


class IndexView(View):

    def get(self, request):
        ctx = {"actual_date": datetime.now()}
        return render(request, "test.html", ctx)


def index_site(request):
    return render(request,"index.html")