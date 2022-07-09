# Create a list called fav_songs
# Each item on the list will be a dictionary with the following keys: artist, song_name, genre, release_year
# Recap or research to add, remove and update some of the dictionaries.

# fav_song is the variable - 
fav_songs = [{
    "artist":"Evanescence",
    "song_name":"Bring Me To Life",
    "genre":"Metal",
    "release_year":"2003"
},
{
    "artist":"Manic Street Preachers",
    "song_name":"You Stole The Sun From My Heart",
    "genre":"Indie",
    "release_year":"1998"
},
{   
    "artist":"Savage Garden",
    "song_name":"Crash And Burn",
    "genre":"Pop",
    "release_year":"1999"
},
{
    "artist":"The Who",
    "song_name":"Behind Blue Eyes",
    "genre":"Rock",
    "release_year":"1971"
}]

print(fav_songs)

# .append method is to add a new dictionary to the current dictionaries
fav_songs.append({ 
    "artist":"Guns N Roses",
    "song_name":"November Rain",
    "genre":"Rock",
    "release_year":"1991"
})

print(fav_songs)

# Delete methods
del (fav_songs[1])
print(fav_songs)

# Pop method delete the last one in the list unless you add the index position in the end brackets
# fav_songs.pop()
# fav_songs.pop(0)

# Update using the index position
fav_songs[2].update({"song_name":"Won't Get Fooled Again"})
print(fav_songs)