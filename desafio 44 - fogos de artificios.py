from time import sleep
import emoji
festa = str(input("Qual comemoração? ")).upper()

for c in range(10, 0, -1):
    print(c)
    sleep(1)
print("FELIZ {} !!".format(festa))
print(emoji.emojize("BUM! BUM! POOOW!:fireworks::sparkler::tada:", use_aliases=True))