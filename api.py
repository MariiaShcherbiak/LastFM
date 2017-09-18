import pylast

# You have to have your own unique two values for API_KEY and API_SECRET
# Obtain yours from http://www.last.fm/api/account/create for Last.fm
API_KEY = "72c6fd6d492eadb29a902e5f7edc7532"  # this is a sample key
API_SECRET = "0e137effc9d5c832f9a047dc1fa261bd"

# In order to perform a write operation you need to authenticate yourself
username = "MSbts"
password_hash = pylast.md5("rt7-qBH-PGn-VJq")

network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=username, password_hash=password_hash)


Artist = network.get_artist("System of")

