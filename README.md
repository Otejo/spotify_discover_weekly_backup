# spotify_discover_weekly_backup
A python script that will backup Discover Weekly track names so they are not lost forever 


# Requirements
You will need to get a client_id, and client_secret from Spotify. This can be done by creating an APP for yourself at https://developer.spotify.com/dashboard/applications

This uses the Tekore package - https://tekore.readthedocs.io/en/stable/
You can use their [example](https://github.com/felix-hilden/tekore/blob/0e2aa312e1bec8033092d6daf08f2fe92daffbcf/docs/src/getting_started.rst#saving-the-configuration) provided to create the tekore.cfg file that is used for authentication in this script. 
(I will create a small file to do this later)

You will need to get the 'id' for your discover weekly playlist. You can get this by going to open.spotify.com in your browser and navigating to your 'Discover Weekly' playlist. The id is the last part of the url. https://open.spotify.com/playlist/<PLAYLIST_ID>

You will need to create a new playlist to keep last weeks Discover Weekly playlist songs. Grab the id from that playlist to.

# Using the scripts. 

After running spotifyweekly.py you will have a file spotifysongs.txt will the artist/song names from your Discover Weekly.  It will add to the file everytime you run script. Ideally you schedule the script to run every Sunday or something like that
It will also add the songs to the new playlist you created. For now that playlist will grow forever. Later I may update the code to remove tracks added more than 30 days prior.
