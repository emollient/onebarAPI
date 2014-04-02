from restapi.services import Faves, AllFaves
from restapi.validators import JSON, ValidFields
from sqlalchemy import desc
from restapi.models import DBSession, Favorites, CSH_Services
from pyramid.httpexceptions import HTTPForbidden
import json




@Faves.get(renderer='json')
def getFavoriteByRank(request):
    """
    ->
    {
        'rank'
    }
    <-
    {
        'service_id': <>
        'rank': <>
    }
    """
    for favorite in DBSession.query(Favorites).order_by(Favorites.rank):
        if favorite.rank == int(request.GET['rank']):
        #if favorite.rank is request.validated['favorite'].rank:
            return {'service_id': favorite.service_id,
                    'rank': favorite.rank
                   }
    return HTTPForbidden()

@AllFaves.get(renderer='json')
def getOrderedFavorites(request):
    """
    <-
    {
        all favorites objects ordered by rank
        {
            'service_id': <>
            'rank': <>
        }
    }
    """
    arr = []
    for favorite in DBSession.query(Favorites).order_by(Favorites.rank):
        obj = {}
        obj['service_id'] = favorite.service_id
        obj['rank'] = favorite.rank
        arr.append(obj)
    return json.load(arr)

@Faves.post(validators=[JSON, ValidFields('rank','service_id')])
def addFavorites(request):
    """
    ->
    {
        'rank'
        'service_id'
    }
    <-
    {
        'success': True
        'service_id': <>
        'rank': <>
    }
    """
    if (len(DBSession.query(Favorites).order_by(desc(Favorites.id)).all()) == 0):
        uid = 0
    else:
        uid = DBSession.query(Favorites).order_by(desc(Favorites.id)).first().id + 1
    new_fav = Favorites(
            id = uid,
            service_id = request.json_body['service_id'],
            rank = request.json_body['rank']
    )

    DBSession.add(new_fav)
    #DBSession.commit()
    return {
            'success': True,
            'id': new_fav.id,
            'service_id': new_fav.service_id,
            'rank': new_fav.rank
            }

@Faves.delete()
def removeFavorites(request):
    """
    does it's own thing
    """
    pass

