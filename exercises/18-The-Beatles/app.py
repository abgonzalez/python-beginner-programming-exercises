# ✅↓ Write your code here ↓✅
# ✅↓ Write your code here ↓✅

def sing():
    lyrics_string = ''
    for i in range(4):
        lyrics = 'let it be,\n'
        lyrics_string += lyrics
    lyrics_string += "there will be an answer,\n"
    for i in range(5):
        lyrics = 'let it be,\n'
        lyrics_string += lyrics
    lyrics_string += "whisper words of wisdom, let it be"
    return lyrics_string

print(sing())