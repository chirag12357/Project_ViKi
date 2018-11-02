import spotipy
sp = spotipy.Spotify()

results = sp.search(q='weezer', limit=20)
for i, t in enumerate(results['ed sheeran']['items']):
    print (' ', i, t['name'])
