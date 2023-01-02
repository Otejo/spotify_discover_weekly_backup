
import tekore as tk
import datetime
today = datetime.date.today().ctime()


DiscoverWeekly_id = '{{enter Discover Weekly playlist id}}'
LastWeeksPlaylist_id = '{{Newly created Playlist ID}}'


file = 'tekore.cfg'
conf = tk.config_from_file(file, return_refresh=True)
token = tk.refresh_user_token(*conf[:2], conf[3])

spotify = tk.Spotify(token)
tracks = spotify.current_user_top_tracks(limit=10)

discover = spotify.playlist(DiscoverWeekly_id)
songs = discover.tracks.items
song_list = {}
uris = []
for item in songs:
    artist = item.track.artists[0].name
    song_name = item.track.name
    uri_s = item.track.uri
    comb = {artist: song_name}
    song_list.update(comb)
    uris.append(uri_s)


with open('spotifysongs.txt', 'a', newline='') as file:
    file.write(today+'\n')
    for artist, song_name in song_list.items():
        info = (artist," | ",song_name)
        file.write(''.join(info)+'\n')
    file.write('\n')
file.close()

spotify.playlist_add(LastWeeksPlaylist_id, uris)


#spotify.playlist_remove(LastWeeksPlaylist_id, uris)

#### Need to update to remove tracks added 30+ days before the script is run. For now the "Last Weeeks playlist" will grow forever
