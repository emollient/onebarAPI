from cornice import Service


Faves = Service("favorites", "/favorites", description = "user favorites api")

AllFaves = Service("allFavorites", "/allfavorites", description= "all the favorites")

cshServices = Service("csh_services", "/csh_services", description = "csh services api")

allcshServices = Service("allcsh_services", "/allcsh_services", description =" all csh services")


