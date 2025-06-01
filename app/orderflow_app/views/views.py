from datetime import datetime
from pathlib import Path

from django.shortcuts import render

template_path = Path("orderflow_app")


def index(request):
    context = {"now": datetime.now()}
    return render(request, template_path/"index.html",  context=context)
