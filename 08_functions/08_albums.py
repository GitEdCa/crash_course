def make_album(artist, title, tracks=''):
    album = {'artist': artist, 'title': title}
    if tracks:
        album['tracks'] = tracks
    return album

print("Make an album")
print("enter 'q' at any time to quit")
while True:
    artist = input("Artist's name? ")
    if artist == 'q':
        break
    title = input("Title's name? ")
    if title == 'q':
        break
    album = make_album(artist, title)
    print(album)
