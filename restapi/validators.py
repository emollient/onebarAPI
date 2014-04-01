import json
from .models import DBSession, CSH_Services
from pyramid.security import authenticated_userid
from pyramid.httpexceptions import HTTPUnauthorized, HTTPExpectationFailed
from re import compile as re_compile


def JSON(request):
    data = json.loads(request.body);
    request.validated['json'] = data


def ValidFields(*fields):
    def validator(request):
        data = json.loads(request.body)
        for key in fields:
            if key not in data:
                return HTTPExpectationFailed()
    return validator


