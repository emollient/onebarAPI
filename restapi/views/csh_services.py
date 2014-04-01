from restapi.validators import JSON, ValidFields
from restapi.services import cshServices
from restapi.models import DBSession, CSH_Services
from pyramid.httpexceptions import HTTPForbidden
import json

@cshServices.get(validators=[JSON], renderer='json')
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
        if service.id is request.validated['csh_services'].id:
            return{
                    'id': service.id,
                    'icon': service.icon,
                    'name': service.name,
                    'url': service.url
                    }
    return HTTPForbidden()

@cshServices.get(validators=[JSON], renderer='json')
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
    return json.load(arr)

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
    service_id = request.validated['services'].id
    new_service = CSH_Services(
            id = service_id,
            icon = request.validated['json']['icon'],
            name = request.validated['json']['name'],
            url = request.validated['json']['url']

            )
    DBSession.add(new_service)
    DBSession.commit()
    return {
            'success': True,
            'id': new_service.id,
            'icon': new_service.icon,
            'name': new_service.name,
            'url': new_service.url
            }









