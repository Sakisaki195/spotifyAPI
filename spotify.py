import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'
client_id = 'facaaab57e79437ba29f054c777e254b'
client_secret = '8348fa05f31845789a8a4c9c11e7352c'

spotify_client_credentials = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=spotify_client_credentials)

name = 'boston'
result = spotify.search(q='artist:' + name, type='artist')
artist_id = result['artists']['items'][0]['id']#検索結果内で名前が最も一致するバンドのid

lz_uri = 'spotify:artist:' + artist_id

results = spotify.artist_albums(lz_uri, album_type='album')
album_id = 'spotify:album:' + results['items'][-1]['id']
results = spotify.album(album_id)['tracks']['items'][1]
track_id = 'spotify:album:' + results['id']
results = spotify.audio_features(track_id)

# results = spotify.artist_top_tracks(lz_uri)

# for track in results['tracks'][:10]:
#     print('track    : ' + track['name'])
#     print('audio    : ' + track['preview_url'])
#     print('cover art: ' + track['album']['images'][0]['url'])
#     print()