#Create a list called fav_songs
#Each item on the list will be a dictionary with the following keys: artist, song_name, genre, release_year
#Recap or research to add, remove and update some of the dictionaries.

fav_songs = {
    "artist":"Evanescence",
    "song_name":"Bring Me To Life",
    "genre":"Metal",
    "release_year":"2003"
}

# for i in fav_songs.keys():
#     print(i)
    
#Add
fav_songs.update({"Album":"Fallen"})
print(fav_songs)

#Remove
del fav_songs["genre"]
print(fav_songs)

#update
fav_songs.setdefault("genre", "rock")
print(fav_songs)