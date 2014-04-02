from restapi.validators import JSON, ValidFields
from restapi.services import cshServices, allcshServices
from restapi.models import DBSession, CSH_Services
from sqlalchemy import desc
from pyramid.httpexceptions import HTTPForbidden
import json

@cshServices.get(renderer='json')
def getServiceByID(request):
    """
    <-
    {
        'id': <>
        'icon': <>
        'name': <>
        'url': <>
    }
    """
    for service in DBSession.query(CSH_Services).order_by(CSH_Services.id):
        if service.id == int(request.GET['id']):
            return{
                    'id': service.id,
                    'icon': service.icon,
                    'name': service.name,
                    'url': service.url
                    }
    return HTTPForbidden()

@allcshServices.get(renderer='json')
def getServices(request):
    """
    <-
    {
    all service objects
        {
            'id': <>
            'icon': <>
            'name': <>
            'url': <>
        }
    }
    """
    arr = []
    for csh_service in DBSession.query(CSH_Services).order_by(CSH_Services.id):
        service_wrapper = {}
        service_wrapper['id'] = csh_service.id
        service_wrapper['icon'] = csh_service.icon
        service_wrapper['name'] = csh_service.name
        service_wrapper['url'] = csh_service.url

        arr.append(service_wrapper)
    return arr

@cshServices.delete()
def deleteService(request):
    pass

@cshServices.post(validators=[JSON, ValidFields('name','icon','url')])
def addService(request):
    """
    ->
    {
        'name'
        'icon'
        'url'
    }
    <-
    {
        'success': True
        'id': <>
        'icon': <>
        'name': <>
        'url': <>
    }
    """
    if (len(DBSession.query(CSH_Services).order_by(desc(CSH_Services.id)).all()) == 0):
        service_id = 0
    else:
        service_id = DBSession.query(CSH_Services).order_by(desc(CSH_Services.id)).first().id + 1

    new_service = CSH_Services(
            id = service_id,
            icon = request.json_body['icon'],
            name = request.json_body['name'],
            url = request.json_body['url']

            )
    DBSession.add(new_service)
    return {
            'success': True,
            'id': new_service.id,
            'icon': new_service.icon,
            'name': new_service.name,
            'url': new_service.url
            }









