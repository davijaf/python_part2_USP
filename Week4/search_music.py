class Music:
    def __init__(self, title, interprete, compositor, year):
        self.title = title
        self.interprete = interprete
        self.compositor = compositor
        self.year = year

class Search:
    def search_by_title(self, playlist, title):
        for i in range(len(playlist)):
            if playlist[i].title == title:
                return i
        return -1

    def lets_search(self):
        playlist = [
                    Music("Baby","Gal Costa","Caetano Veloso",1969),
                    Music("Ponta de Areia","Milton", "Milton Nascimento", 1975),
                    Music("Podres Poderes","Caetano Veloso","Caetano Veloso",1984)
                    ]

        where_found = self.search_by_title(playlist,"Podres Poderes")

        if where_found == -1:
            print("Your music not found on playlist")
        else:
            prefered = playlist[where_found]
            print(prefered.title, prefered.interprete, prefered.compositor,prefered.year,sep=", ");

#b = Search()
#b.lets_search()