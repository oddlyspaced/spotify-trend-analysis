
# Tiny - GeneralizedSpotifyAnalyser
 
 This is a stripped down version of [OleAd's Generalized Spotify Analyser](https://github.com/OleAd/GeneralizedSpotifyAnalyser)
 More info can be found on the [source repository](https://github.com/OleAd/GeneralizedSpotifyAnalyser) and [here](https://oleheggli.medium.com/easily-analyse-audio-features-from-spotify-playlists-part-1-3b004cd406b3).

This variant of the GSA project contains enough code to Authenticate with Spotify API and fetch information regarding any Spotify Playlist.
 
 
## Requirements
 pandas
 requests
 tqdm
joblib
spotipy
 
## Usage

### Step 1
Visit [Spotify Developer Dashboard](https://developer.spotify.com/dashboard) and create a New App.

### Step 2
Once done, open the Project page for your newly created App, and click on 'Edit Settings'.
Under Edit Settings, look for 'Redirect URIs' and add the following link:
http://example.com/callback/

### Step 3
Now, open the file `spotifyConstants_template.py` and add your Cliend ID in `myClientID` and Client Secret in `myClientSecret` from your App Page.
Also copy your Username from your [Profile](https://www.spotify.com/us/account/overview/) page, and add it to the `myUser` field in the constants file. Finally add `http://example.com/callback/` in `myRedirect` field.
 
### Step 4
Rename the file `spotifyConstants_template.py` to `spotifyConstants.py`
 
### Step 5
Install the dependencies by running

    pip install -r requirements.txt

### Step 6
Copy the URI of your target playlist. See [this post](https://community.spotify.com/t5/Spotify-for-Developers/Get-Playlist-URI-with-updated-Desktop-Look/td-p/5185605) for more information.
### Step 7
Run `GSA_FetchPlaylistPickle.py`, and authenticate if prompted.
Paste the URI you copied previously, and wait for the script to fetch metadata.

The output Pickle dataset file would be located in Playlists folder.