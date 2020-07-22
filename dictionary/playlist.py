custom_playlist = {
    'name': 'Hindi Melody',
    'artist': 'Kumar Sanu',
    'songs': [
        {'title': 'Ek ladki ko dekha to aisa laga', 'movie': '1942 a love story', 'duration': 5.3},
        {'title': 'Ashiquee ke liye', 'movie': 'Ashiquee', 'duration': 4.7},
        {'title': 'Ae kash kahi aisa hota', 'movie': 'Mohra', 'duration': 4.9}
    ]
}

total_duration = 0
for song in custom_playlist['songs']:
    total_duration += song['duration']

print(f"Total duration of this playlist is: {total_duration}")