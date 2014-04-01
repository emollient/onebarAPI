from restapi.services import Faves
from restapi.validators import JSON, ValidFields
from restapi.models import DBSession, Favorites, CSH_Services
from pyramid.httpexceptions import HTTPForbidden
import json



@Faves.get(validators=[JSON], renderer='json')
def getFavoriteByRank(request):
    for favorite in DBSession.query(Favorites).order_by(Favorites.rank):
        if favorite.rank is request.validated['favorite'].rank:
            return {'service_id': favorite.service_id,
                    'rank': favorite.rank
                   }
    return HTTPForbidden()

@Faves.get(validators=[JSON], renderer='json')
def getOrderedFavorites(request):
    arr = []
    for favorite in DBSession.query(Favorites).order_by(Favorites.rank):
        obj = {}
        obj['service_id'] = favorite.service_id
        obj['rank'] = favorite.rank
        arr.append(obj)
    return json.load(arr)

@Faves.post(validators=[JSON, ValidFields('rank','service_id')])
def addFavorites(request):
    uid = request.validated['services'].id
    new_fav = Favorites(
            service_id = request.validated['csh_services'],
            rank = request.validated['json']['rank']
    )
    new_fav.service_mapper = request.validated['json']['service_mapper']
    DBSession.add(new_fav)
    DBSession.commit()
    return {
            'success': True,
            'service_id': new_fav.service_id,
            'rank': new_fav.rank
            }

@Faves.delete()
def removeFavorites(request):
    """
    does it's own thing
    """
    pass

