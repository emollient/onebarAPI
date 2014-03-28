from restapi.services import Favorites
from restapi.validators import JSON, ValidFields
from restapi.models import DBSession




@Favorites.get(renderer='json')
def getFavorites(request):
    pass

@Favorites.get(renderer='json')
def orderFavorites(request):
    pass

@Favorites.post(validators=[ValidJSON, ValidFields('rank','service_id')])
def addFavorites(request):
    pass

@Favorites.delete()
def removeFavorites(request):
    """
    does it's own thing
    """
    pass

