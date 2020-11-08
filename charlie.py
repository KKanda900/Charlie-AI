import pygame, sys, random, os, re, pyttsx3, threading, random, curses, nltk
from pygame.locals import *
from time import *
from curses.ascii import isdigit
from nltk.corpus import cmudict
import Speech2Text as s2t

d = cmudict.dict()

def nsyl(word):
    return [len(list(y for y in x if isdigit(y[-1]))) for x in d[word.lower()]]

def animate(lastImage):
    workingSentence = " "
    # s2t.speak(sentence)
    for word in sentence.split():
        ipa = d[word.lower()]
        ipa = ipa[0]
        syl = nsyl(word)
        syl = syl[0]
        timePerChar = 0.244/float(len(ipa))
        for char in ipa:
            windowSurface.fill(WHITE)
            if "m" in char.lower() or "b" in char.lower() or "p" in char.lower():
                img = pygame.image.load('animate/face_mbp.png')
            elif "th" in char.lower():
                img = pygame.image.load('animate/face_th.png')
            elif "ee" in char.lower():
                img = pygame.image.load('animate/face_ee.png')
            elif "oo" in char.lower():
                img = pygame.image.load('animate/face_oo.png')
            elif "l" in char.lower():
                img = pygame.image.load('animate/face_l.png')
            elif "f" in char.lower() or "v" in char.lower():
                img = pygame.image.load('animate/face_fv.png')
            elif "g" in char.lower() or "sh" in char.lower() or "ch" in char.lower():
                img = pygame.image.load('animate/face_gshch.png')
            elif "s" in char.lower() or "d" in char.lower() or "t" in char.lower() or "r" in char.lower() or "k" in char.lower() or "c" in char.lower():
                img = pygame.image.load('animate/face_sdtrck.png')
            elif "a" in char.lower():
                img = pygame.image.load('animate/face_a.png')
            elif "o" in char.lower():
                img = pygame.image.load('animate/face_o.png')
            else:
                img = lastImage
            windowSurface.blit(img, (0, 0))
            pygame.display.update()
            workingSentence += char[0]
            pygame.display.update()
            sleep(timePerChar)
            lastImage = img
        workingSentence += " "
        windowSurface.fill(WHITE)
        img = pygame.image.load('animate/face_normal.png')
        lastImage = img
        windowSurface.blit(img, (0, 0))
        pygame.display.update()
        pygame.display.update()
        # sleep(0.04)
    windowSurface.fill(WHITE)

    img = lastImage
    windowSurface.blit(img, (0, 0))
    pygame.display.update()
    # sleep(0.4)

# This is where the program starts up
pygame.init()
windowSurface = pygame.display.set_mode((259, 271), 0, 32)
pygame.display.set_caption("Charlie")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

info = pygame.display.Info()
sw = info.current_w
sh = info.current_h
y = 0
windowSurface.fill(WHITE)
img = pygame.image.load('animate/face_normal.png')
windowSurface.blit(img, (0, 0))
pygame.display.update()
# sleep(0.2)
clientString = ""
i = 0
while "that is all charlie" not in clientString.lower():
    if i == 0:
        paragraph = "Hello my name is Charlie! How can I assist you?"  # response from robot
        paragraph = re.sub('[!,;?]', '.', paragraph)
        lastImage = img
        for sentence in paragraph.split("."):
            x = threading.Thread(target=s2t.speak, args=(sentence,)) 
            x.start()
            y = threading.Thread(target=animate, args=(lastImage,))
            y.start()
            x.join()
            y.join()
        i = i + 1
    else:
        clientString = s2t.convertClientAudio()
        robotResponse = s2t.response(clientString)
        paragraph = robotResponse  # response from robot
        paragraph = re.sub('[!,;?]', '.', paragraph)
        lastImage = img
        for sentence in paragraph.split("."):
            x = threading.Thread(target=s2t.speak, args=(sentence,)) 
            x.start()
            y = threading.Thread(target=animate, args=(lastImage,))
            y.start()
            x.join()
            y.join()
