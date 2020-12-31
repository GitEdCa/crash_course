def make_album(artist, title, tracks=''):
    album = {'artist': artist, 'title': title}
    if tracks:
        album['tracks'] = tracks
    return album

a1 = make_album("Pink Floyd", "Animals")
a2 = make_album("The Doors", "Light my Fire")
a3 = make_album("Luis Miguel", "Mexico en la piel")
a4 = make_album("Linking Park", "Metamorphosis", 20)

print(a1)
print(a2)
print(a3)
print(a4)
