from restapi.services import Favorites
from restapi.validators import JSON, ValidFields
from restapi.models import DBSession, Favorites, CSH_Services




@Favorites.get(validators=[ValidJSON], renderer='json')
def getFavorite(request):
    for favorite in request.validated['favorites']:
        if favorite is request:
            return {'service_id': favorite.service_id,
                    'rank': favorite.rank
                   }
    return

@Favorites.get(validators=[ValidJSON], renderer='json')
def getOrderedFavorites(request):
    arr = []
    for favorite in request.validated['favorites']:
        obj = {}
        obj['service_id'] = favorite.service_id
        obj['rank'] = favorite.rank
        arr.append(obj)
    return json.load(arr)

@Favorites.post(validators=[ValidJSON, ValidFields('rank','service_id')])
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

@Favorites.delete()
def removeFavorites(request):
    """
    does it's own thing
    """
    pass

