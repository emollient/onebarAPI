from cornice import Service


Faves = Service("favorites", "/favorites", description = "user favorites api")


cshServices = Service("csh_favorites", "/csh_favorites", description = "csh services api")



