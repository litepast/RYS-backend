from flask import Flask, jsonify, request
from search_album import Search
from insert_album import Album 
from delete_album import DeleteAlbum
from search_library import Library  
from update_ratings import UpdateRatings
from get_album_on_library import AlbumInLibrary
from edit_album import EditAlbum
from flask_cors import CORS


# this launches the RESTFUL Flask api
# this is the Api that feeds the data to the RYS Vue.Js frontend


app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})


# search albums from spotify
@app.route('/api/v1/search-spotify', methods=['GET'])
def search_from_spotify():
    if request.method == 'GET':
        p1 = int(request.args.get('p1'))
        p2 = str(request.args.get('p2'))
        search = Search()          
        albums_result=search.search_album(p1,p2)
        if albums_result:
            results = jsonify({
                'status' : 200,
                'msg': 'Showing Results',
                'albums' : albums_result
            })
        else:
            results = jsonify({
                'status' : 400,
                'albums' : [],
                'msg': 'No results'
            })
        return results

#inserts an spotify album data to the rys database
@app.route('/api/v1/insert-album-catalog/<string:id_album>', methods=['PUT'])
def insert_album_library(id_album):
    if request.method == 'PUT':
        insert_album = Album(id_album)
        status, msg = insert_album.insert_album_data()
        if status:
            status_request = 200
        else:
            status_request = 400
        result = jsonify({
                'status' : status_request,
                'msg': msg
            })
        return result
    
#searches library, given parameters sent from the frontend, it returns the matches
@app.route('/api/v1/search-album-catalog', methods=['GET'])
def search_from_catalog():
    if request.method == 'GET':
        query = request.args.to_dict(flat=False)
        lib = Library(query)
        albums_result = lib.search_album()
        if albums_result:
            results = jsonify({
                'status' : 200,
                'msg': 'OK Query',
                'albums' : albums_result
            })
        else:
            results = jsonify({
                'status' : 400,
                'albums' : [],
                'msg': 'No results'
            })
        return results

#returns the data from one specific album, to be shown on the album view on the front end
@app.route('/api/v1/get-album-data/<string:id_album>', methods=['GET'])
def search_album_from_catalog(id_album):
    if request.method == 'GET':
        AlbumLib = AlbumInLibrary(id_album)
        album_data = AlbumLib.search_album()
        if album_data:
            results = jsonify({
                'status' : 200,
                'msg': 'OK Query',
                'album' : album_data
            })
        else:
            results = jsonify({
                'status' : 400,
                'album' : False,
                'msg': 'No results'
            })
        return results
    

#given the ratings recieved from the frontend album page, this will update them on the db
@app.route('/api/v1/update-album-ratings/', methods=['PUT'])
def update_album_ratings():
    if request.method == 'PUT':
        params = request.get_json()
        
        update_ratings = UpdateRatings(params)
        result = update_ratings.update_ratings()

        if result:
            results = jsonify({
                'status' : 200,
                'msg': result                
            })
        else:
            results = jsonify({
                'status' : 400,
                'msg': result                               
            })
        return results
    

#it edits certain album data, given the parameters from the web app
@app.route('/api/v1/edit-album-catalog', methods=['PUT'])
def edit_album_catalog():
    if request.method == 'PUT':
        params = request.get_json()
        print(params['params'])
        edit_album = EditAlbum(params)
        result = edit_album.edit_album()
        if result:
            results = jsonify({
                'status' : 200,
                'msg': 'Album edited'                
            })
        else:
            results = jsonify({
                'status' : 400,
                'msg': 'Album not edited'                               
            })
        return results


#deletes an album from the database, given the album id sent from the web app frontend
@app.route('/api/v1/delete-album-data/<string:id_album>', methods=['DELETE'])
def delete_album_from_catalog(id_album):
    print('deleting?')
    if request.method == 'DELETE':
        del_album = DeleteAlbum(id_album)
        result = del_album.delete_album()
        if result:
            results = jsonify({
                'status' : 200,
                'text': 'Sucess deleting album',
                'msg': result                
            })
        else:
            results = jsonify({
                'status' : 400,
                'text': 'Error deleting album',
                'msg': result                               
            })
        return results





if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=5000)