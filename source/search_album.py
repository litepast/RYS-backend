import config

class Search():

    results = None

    def __init__(self):
       self.sp = config.sp
    
    def search_album(self,search_string,type_search):
                
        if (type_search):
            self.string_search=search_string
        else:
            self.string_search='artist:'+search_string
        

        results_columns = ['name', 'artist', 'album_id', 'release_date', 'cover_url']        
        results_rows = { column: [] for column in results_columns} 
        
        results_albums = self.sp.search(q=self.string_search , type='album', limit=10, market='MX')
        if results_albums:
            albums = results_albums['albums']['items'] 
            for album in albums:
                results_rows['name'].append(album['name'])
                results_rows['artist'].append(album['artists'][0]['name']) 
                results_rows['album_id'].append(album['id']) 
                results_rows['release_date'].append(album['release_date']) 
                results_rows['cover_url'].append(album['images'][1]['url'])
            self.results = results_rows
        return self.results 
    
    def get_album_id(self,index):
            return self.results['album_id'][index]



        



