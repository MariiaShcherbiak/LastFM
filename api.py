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

def artist_by_genre():
    print("Enter the genre\n")
    genre = input("<")
    tag = network.get_tag(genre)
    band = tag.get_top_artists()
    print("Found:\n")
    for str in band:
        print(str[0])

    print("\n")
    print("Choose an artist\n")
    artist = input("<")
    artist = network.get_artist(artist)
    print("\n")
    print("Choose the option\n1.Get similar artists\n2.Get albums\n3.Get top tracks\n")
    opt = input()
    if opt == "1":
        similar = artist.get_similar()
        for i in similar:
            print(i[0])
    elif opt == "2":
        album = artist.get_top_albums()
        for i in album:
            print(i[0])
    elif opt == "3":
        track = artist.get_top_tracks()
        for i in track:
            print(i[0])
    else:
        print("Error!")



def our_tracks():
    #print("Type the name of the user:")
    #user_name=input(">")
    my_user_name = "MSbts"
    #user1=network.get_user(user_name)
    user1 = network.get_user("aidihou")
    user2=network.get_user(my_user_name)
    my_loved=user2.get_loved_tracks()
    user_loved=user1.get_loved_tracks()
    same_track=[]
    if len(user_loved) >= len(my_loved):
        for i in my_loved:
            for j in user_loved:
                if i[0] == j[0]:
                    print(i[0])
                    same_track.append(i[0])
    else:
        for i in user_loved:
            for j in my_loved:
                if i[0] == j[0]:
                    print(i[0])
                    same_track.append(i[0])
    return str(same_track)


def our_artists():
    # print("Type the name of the user:")
    # user_name=input(">")
    my_user_name = "jonnek_m"
    # user1=network.get_user(user_name)
    user1 = network.get_user("aidihou")
    user2 = network.get_user(my_user_name)
    my_artists=user2.get_top_artists()
    user_artists=user1.get_top_artists()
    same_artist = []
    if len(user_artists) >= len(my_artists):
        for i in my_artists:
            for j in user_artists:
                if i[0] == j[0]:
                    print(i[0])
                    same_artist.append(i[0])
    else:
        for i in user_artists:
            for j in my_artists:
                if i[0] == j[0]:
                    print(i[0])
                    same_artist.append(i[0])
    return str(same_artist)

def genre_country():
    # print("Type the name of the user:")
    # user_name=input(">")
    #country = network.get_country("Russian Federation")country=network.get_country("Russian Federation")
    #country = network.get_country("Australia")
    country = network.get_country("Japan")
    top=country.get_top_artists(5)
    artists=[]
    g=[]
    for i in top:
        artists.append(str(i[0]))

    for i in range(len(artists)):
        g.append([])
        genre=network.get_artist(artists[i])
        genre=genre.get_top_tags(5)
        for k in genre:
            g[i].append(str(k[0]))
    #for i in g:
        #print(i)
    same=[]
    for i in range(len(g)):
        for j in range(len(g[i])):
            if g[i][j] not in same:
                same.append(g[i][j])
    print(same)

genre_country()











