from django.contrib.auth import authenticate, login,  logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
import json
from itertools import chain
from django.contrib import messages
import itertools
from .models import *
from django.db.models import Q
from django.db.models import Count
from django.utils import timezone
from django.db.models import Q, Count
import datetime
from django.db.models import F
from django.contrib.auth.hashers import make_password
from django.db.models import Avg

import datetime

from datetime import datetime, timedelta
import requests


from decimal import Decimal





def home(request):
    return render(request,"home.html")


def companyprofile(request):
    return render(request,"companyprofile.html")


def test(request):
    return render(request,"test.html")


def travelagency(request):
    return render(request,"travelagency.html")
