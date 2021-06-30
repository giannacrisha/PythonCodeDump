print('\n--- DICTIONARY OF ARTISTS ---\n')

print("Enter 'q' to quit.\n")

def make_album(artist, album, tracks = ""):
    """Builds a dictionary describing a music album"""
    dictionary = {}
    dictionary['artist'] = artist.title()
    dictionary['album'] = album.title()
    if tracks:
        dictionary['tracks'] = tracks
    return dictionary

while True:
    artist = input('\nEnter an artist: ')
    if artist == 'q':
        break
    album = input('\nEnter an album of the artist: ')
    if album == 'q':
        break
    tracks = input('\n(Optional) Enter the number of tracks: ')
    if tracks == 'q':
        break
    
    print(make_album(artist, album, tracks))
    
print('\nThank you for using our program!')