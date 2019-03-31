from pygame import mixer

mixer.init()
mixer.music.load("jazz.mp3")
mixer.music.play()
input('Ouça a musica!')