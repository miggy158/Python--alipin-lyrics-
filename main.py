import time 
import sys


def printlyrics():
    print("\n\n")

lyrics = [
     
     ("Ako'y alipin mo kahit hindi batid", 1.60, 0.13),
     ("Aamin ko minsan ako'y manhid",  2.0, 0.15),
     ("Sana ay",  2.1, 0.18),
     ("Iyong naririnig", 0.7, 0.15),
     ("Sa yong yakap ako'y nasasabik", 2.0, 0.15),
     ("Pagkat ikaw lang nais magkatabi", 2.1, 0.15),
     ("Malamig man o mainit ang gabi", 0.12, 0.15),
     ("Nais ko sana", 2.1, 0.18),
     ("Iparating", 2.1, 0.18),
     ("Na ikaw lamang", 2.1, 0.18),
     ("Ang siyang aking", 2.0, 0.15),
     ("IIBIGIN", 2.0, 0.18),

]

def type_out(text, char_delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(char_delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def play_lyrics(lyrics):
    for line, line_delay, char_delay in lyrics:
        type_out(line, char_delay)
        time.sleep(line_delay)

if __name__ == "__main__":
    print("Now playing: Alipin\n")
    print("\n\n")
    play_lyrics(lyrics)