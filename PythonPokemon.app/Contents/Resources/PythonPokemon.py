
"""Pokemon Python Game For Senior Seminar"""
import math
import random
import time
import timeit
import pygame
import numpy as np
import sys
from numpy import newaxis, r_, c_, mat
import matplotlib.pyplot as plt
from sklearn import preprocessing
import warnings
warnings.filterwarnings("ignore")
#import subprocess
#playing_long=subprocess.Popen(["open", "/Users/phagmann/Desktop/115 Battle (VS Trainer).mp3"])
GLOBAL=[]
def feature_normalize(X):
    return preprocessing.scale(X)
def computeCostMulti(theta,X,y):
    #least squares
    m = X.shape[0]
    predictions = np.dot(X,theta)
    sqrErrors = (predictions - y) ** 2
    return 1./(2*m) * sqrErrors.sum()
def computeCostMulti_df(theta,X,y):
    #least squares dirrivative
    predictions = np.dot(X,theta)
    return np.dot(X.T,(predictions - y))

def power_element(L,p):
    return np.array([i ** p for i in L])
def superpower(x,P):
    fl=np.ones(len(x))
    fl=fl.reshape((len(x),1))
    x=np.append(fl,x,1)
    if P<2:
        return x
    for p in range(2,P+1):
        xx=[]
        xx=power_element(x[:,1],p)
        xx=xx.reshape((len(xx),1))
        x=np.append(x,xx,1)
    return x
#class that puts text on screen and have it be "highlighted" on screen
class Option:
    hovered = False
    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.set_rect()
        self.draw()
    def text(self):
        return self.text
    
    def draw(self):
        self.set_rend()
        screen.blit(self.rend, self.rect)
    
    def set_rend(self):
        self.rend = menu_font.render(self.text, True, self.get_color())
    
    def get_color(self):
        if self.hovered:
            return (255, 255, 255)
        else:
            return (0, 0, 0)
    
    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos
level=50 # made the pokemon's "level" a constant so both teams are balanced
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW= (252,252,0)
TEAL=(0,139,139)
BLUE=(0,0,255)
size = [700, 500]
pygame.display.init
pygame.init()
screen = pygame.display.set_mode(size)
red_square = pygame.Surface((15, 15))
red_square.fill(RED)
# makes a red square at last coordinates touched for debugging reasons
print "hiiiiii"




# Set the width and height of the screen [width,height]


pygame.display.set_caption("Pattymon")

done = False

clock = pygame.time.Clock()

pygame.mouse.set_visible(0)
screen.fill(TEAL)
menu_font = pygame.font.Font(None, 30)
pygame.display.update()
pygame.display.flip()
clock.tick(60)
def poke1(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, BLUE, [1 + x, y, 10, 10], 0)
    
    # Legs
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)
    
    # Body
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [5 + x, 7 + y], 2)
    
    # Arms
    pygame.draw.line(screen, BLACK, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(screen, BLACK, [5 + x, 7 + y], [1 + x, 17 + y], 2)
def poke2(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, RED, [1 + x, y, 10, 10], 0)
    
    # Legs
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)
    
    # Body
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [5 + x, 7 + y], 2)
    
    # Arms
    pygame.draw.line(screen, BLACK, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(screen, BLACK, [5 + x, 7 + y], [1 + x, 17 + y], 2)
def poke_master(l1,l2):
    #prints out how many pokemon are left
    r1=270
    r2=400
    for y in range(l1):
        poke1(screen, r1, 200)
        r1=r1-30
    for yy in range(l2):
        poke2(screen, r2, 200)
        r2=r2+30


def picachu(screen, x, y):
    #picachu mouse curser
    
    # Head
    pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)
    #Picachu's Face Fillings
    pygame.draw.circle(screen,RED,[x+3,y+5],2)
    pygame.draw.circle(screen,RED,[x+10,y+5],2)
    #Ears
    pygame.draw.polygon(screen, YELLOW, [[x-5, y+5], [x+5, y-5], [x-14, y-14]])
    pygame.draw.polygon(screen, YELLOW, [[x+15, y+5], [x+5, y-5], [x+24, y-14]])
    # Legs
    pygame.draw.line(screen, YELLOW, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen, YELLOW, [5 + x, 17 + y], [x, 27 + y], 2)
    
    # Body
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [5 + x, 7 + y], 2)
    
    # Arms
    pygame.draw.line(screen, YELLOW, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(screen, YELLOW, [5 + x, 7 + y], [1 + x, 17 + y], 2)
    #Tail
    pygame.draw.polygon(screen, YELLOW,[[x+6.5,y+18],[x+30,y+18],[x+25,y+13]])
def health_bar1(screen, x, y, left, total):
    #creates health bars, green if mostly full, yellow if about half left, and red mostly out.
    per=1.0*left/total
    pygame.draw.line(screen,BLACK,[x-4,y-5],[x-4,y+10],6)
    if per>0.66:
        pygame.draw.polygon(screen,GREEN,[[x,y],[x,y+10],[x+(100*per),y+10],[x+(100*per),y]])
    elif per<=0.66 and per>0.33:
        pygame.draw.polygon(screen,YELLOW,[[x,y],[x,y+10],[x+(100*per),y+10],[x+(100*per),y]])
    elif per<=0.33 and left>0:
        pygame.draw.polygon(screen,RED,[[x,y],[x,y+10],[x+(100*per),y+10],[x+(100*per),y]])
    else:
        pygame.draw.polygon(screen,BLACK,[[x,y],[x,y+10],[x+(100*per),y+10],[x+(100*per),y]])
    pygame.draw.line(screen,BLACK,[x,y-3],[x+100,y-3],6)

LETTERS="@ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
def drown(n):
    #rounds a number n to the nearest 4
    if n%4==0:
        return 4
    else:
        return n%4
def round4(n,e):
    #rounds a number n to the nearest e
    if n%e==0:
        return n
    return e*(int(n/e)+1)
def genius(L):
    i=1
    if ((int(L[-i][1:]))% 4 ==0):
        L[-i-1]=L[-i-1][0] + str(int(L[-i-1][1:])+1)
        L[-1]=L[-1][0] + str(int(L[-1][1:])+1)
        return L
    else:
        L[-1]=L[-1][0] + str(int(L[-1][1:])+1)
        return L
    L[-1]=L[-1][0] + str(int(L[-1][1:])+1)
    return L

def basic(vertical):
    L=[]
    for char in vertical:
        L=L+[char+"1"]
    return L
def stages(p):
    if p>0:
        return ((p+2)/2.0)
    elif p<0:
        return (2.0/(-p+2))
    else:
        return 1
def Value_List(L,i):
    if i==len(L)-1:
        return L[i]
    elif i==0:
        return (L[i]+np.mean(L[1:]))/2.0
    else:
        return ( L[i] +np.mean(L[(i+1):]))/2.0
def ave_list(L):
    total=0.0
    for i in range(len(L)):
        total=total + Value_List(L,i)
    return total/len(L)
#conditions pokemon will be under/ this part not coded yet
condition=['good',"frozen","burned","poisoned","sleeping","paralyzed"]
#
TYPES=['','normal','fire','water','electric','grass','ice','fighting','poison','ground','flying','psychic','bug','rock','ghost','dragon']
TYPE=['normal','fire','water','electric','grass','ice','fighting','poison','ground','flying','psychic','bug','rock','ghost','dragon']
#pokemon is a dictionary of pokemon and all their info such as [nature types, base stats, playable moves, and later other features will be added futher in code. see lines around 960
#pokemon["poke"]=[nature type1,nature type2,health,offense,defense, speed,special,moves]
pokemon={'bulbasaur':['grass','poison',45,49,49,45,65,["razorleaf","leechseed","bodyslam","growth"]]}
pokemon[ 'ivysaur']= [ 'grass','poison',60,62,63,60,80,["leechseed","razorleaf","growth","megadrain"]]
pokemon[ 'venusaur']= [ 'grass','poison',80,82,83,80,100,["leechseed","sleeppowder","growth","solarbeam"]]
pokemon[ 'charmander']= [ 'fire','',39,52,43,65,50,["seismictoss","flamethrower","dig","bodyslam"]]
pokemon[ 'charmeleon']= [ 'fire','',58,64,58,80,65,["slash","flamethrower","dig","submission"]]
pokemon[ 'charizard']= [ 'fire','flying',78,84,78,100,85,["fireblast","fly","firespin","swordsdance"]]
pokemon[ 'squirtle']= [ 'water','',44,48,65,43,50,["dig","surf","bodyslam","blizzard"]]
pokemon[ 'wartortle']= [ 'water','',59,63,80,58,65,["seismictoss","surf","toxic","dig"]]
pokemon[ 'blastoise']= [ 'water','',79,83,100,78,85,["tailwhip","hydropump","withdraw","skullbash"]]
pokemon[ 'caterpie']= [ 'bug','',45,30,35,45,20,["stringshot","tackle","stringshot","tackle"]]
pokemon[ 'metapod']= [ 'bug','',50,20,55,30,25,["stringshot","tackle","stringshot","tackle"]]
pokemon[ 'butterfree']= [ 'bug','flying',60,45,50,70,80,["stunspore","psychic","megadrain","swift"]]
pokemon[ 'weedle']= [ 'bug','poison',40,35,30,50,20,["stringshot","poisonsting","stringshot","poisonsting"]]
pokemon[ 'kakuna']= [ 'bug','poison',45,25,50,35,25,["stringshot","poisonsting","stringshot","poisonsting"]]
pokemon[ 'beedrill']= [ 'bug','poison',65,80,40,75,45,["focusenergy","twineedle","megadrain","hyperbeam"]]
pokemon[ 'pidgey']= [ 'normal','flying',40,45,40,56,35,["whirlwind","fly","sandattack","mirrormove"]]
pokemon[ 'pidgeotto']= [ 'normal','flying',63,60,55,71,50,["swift","fly","sandattack","toxic"]]
pokemon[ 'pidgeot']= [ 'normal','flying',83,80,75,91,70,["sandattack","quickattack","fly","mirrormove"]]
pokemon[ 'rattata']= [ 'normal','',30,56,35,72,25,["dig","superfang","bodyslam","toxic"]]
pokemon[ 'raticate']= [ 'normal','',55,81,60,97,50,["hyperfang","superfang","quickattack","toxic"]]
pokemon[ 'spearow']= [ 'normal','flying',40,60,30,70,31,["swift","drillpeck","doubleteam","fly"]]
pokemon[ 'fearow']= [ 'normal','flying',65,90,65,100,61,["growl","drillpeck","hyperbeam","mirrormove"]]
pokemon[ 'ekans']= [ 'poison','',35,60,44,55,40,["double-edge","earthquake","glare","megadrain"]]
pokemon[ 'arbok']= [ 'poison','',60,85,69,80,65,["strength","glare","dig","acid"]]
pokemon[ 'pikachu']= [ 'electric','',35,55,30,90,50,["reflect","thunderbolt","thunderwave","swift"]]
pokemon[ 'raichu']= [ 'electric','',60,90,55,100,90,["megakick","thunder","quickattack","thunderwave"]]
pokemon[ 'sandshrew']= [ 'ground','',50,75,85,40,30,["sandattack","earthquake","rockslide","slash"]]
pokemon[ 'sandslash']= [ 'ground','',75,100,110,65,55,["sandattack","dig","rockslide","strength"]]
pokemon[ 'nidoranF']= [ 'poison','',55,47,52,41,40,["blizzard","toxic","bodyslam","thunderbolt"]]
pokemon[ 'nidoranM']= [ 'poison','',46,57,40,50,40,["thunder","blizzard","horndrill","bodyslam"]]
pokemon[ 'nidorina']= [ 'poison','',70,62,67,56,55,["bubblebeam","toxic","bodyslam","thunder"]]
pokemon[ 'nidoqueen']= [ 'poison','ground',90,82,87,76,75,["earthquake","toxic","rockslide","doublekick"]]
pokemon[ 'nidorino']= [ 'poison','',61,72,57,65,55,["thunder","blizzard","horndrill","bodyslam"]]
pokemon[ 'nidoking']= [ 'poison','ground',81,92,77,85,75,["thunderbolt","icebeam","bodyslam","horndrill"]]
pokemon[ 'clefairy']= [ 'normal','',70,45,48,35,60,["bide","earthquake","hornattack","horndrill"]]
pokemon[ 'clefable']= [ 'normal','',95,70,73,60,85,["blizzard","thunderwave","bodyslam","metronome"]]
pokemon[ 'vulpix']= [ 'fire','',38,41,40,65,65,["toxic","flamethrower","confuseray","dig"]]
pokemon[ 'ninetales']= [ 'fire','',73,76,75,100,100,["tailwhip","fireblast","confuseray","quickattack"]]
pokemon[ 'jigglypuff']= [ 'normal','',115,45,20,20,25,["flash","sing","seismictoss","bodyslam"]]
pokemon[ 'wigglytuff']= [ 'normal','',140,70,45,45,50,["strength","sing","disable","hyperbeam"]]
pokemon[ 'zubat']= [ 'poison','flying',40,45,35,55,40,["swift","confuseray","haze","megadrain"]]
pokemon[ 'golbat']= [ 'poison','flying',75,80,70,90,75,["haze","hyperbeam","supersonic","megadrain"]]
pokemon[ 'oddish']= [ 'grass','poison',45,50,55,30,75,["double-edge","petaldance","megadrain","stunspore"]]
pokemon[ 'gloom']= [ 'grass','poison',60,65,70,40,85,["stunspore","petaldance","megadrain","acid"]]
pokemon[ 'vileplume']= [ 'grass','poison',75,80,85,50,100,["solarbeam","megadrain","acid","stunspore"]]
pokemon[ 'paras']= [ 'bug','grass',35,70,55,25,55,["megadrain","spore","dig","slash"]]
pokemon[ 'parasect']= [ 'bug','grass',60,95,80,30,80,["megadrain","spore","growth","slash"]]
pokemon[ 'venonat']= [ 'bug','poison',60,55,50,45,40,["toxic","psychic","double-edge","megadrain"]]
pokemon[ 'venomoth']= [ 'bug','poison',70,65,60,90,90,["flash","psychic","megadrain","sleeppowder"]]
pokemon[ 'diglett']= [ 'ground','',10,55,25,95,45,["fissure","earthquake","sandattack","slash"]]
pokemon[ 'dugtrio']= [ 'ground','',35,80,50,120,70,["growl","dig","rockslide","sandattack"]]
pokemon[ 'meowth']= [ 'normal','',40,45,35,90,40,["screech","slash","bubblebeam","thunderbolt"]]
pokemon[ 'persian']= [ 'normal','',65,70,60,115,65,["hyperbeam","thunder","screech","bite"]]
pokemon[ 'psyduck']= [ 'water','',50,52,48,55,50,["blizzard","hydropump","dig","disable"]]
pokemon[ 'golduck']= [ 'water','',80,82,78,85,80,["disable","icebeam","confusion","bubblebeam"]]
pokemon[ 'mankey']= [ 'fighting','',40,80,35,70,35,["thrash","submission","counter","dig"]]
pokemon[ 'primeape']= [ 'fighting','',65,105,60,95,60,["thrash","seismictoss","lowkick","counter"]]
pokemon[ 'growlithe']= [ 'fire','',55,70,45,60,50,["dig","flamethrower","doubleteam","bodyslam"]]
pokemon[ 'arcanine']= [ 'fire','',90,110,80,95,80,["leer","fireblast","agility","dig"]]
pokemon[ 'poliwag']= [ 'water','',40,50,40,90,40,["hydropump","amnesia","blizzard","psychic"]]
pokemon[ 'poliwhirl']= [ 'water','',65,65,65,90,50,["surf","icebeam","psychic","amnesia"]]
pokemon[ 'poliwrath']= [ 'water','fighting',90,85,95,70,70,["bubblebeam","amnesia","submission","hypnosis"]]
pokemon[ 'abra']= [ 'psychic','',25,20,15,90,105,["psychic","bodyslam","thunderwave","doubleteam"]]
pokemon[ 'kadabra']= [ 'psychic','',40,35,30,105,120,["psychic","reflect","dig","recover"]]
pokemon[ 'alakazam']= [ 'psychic','',55,50,45,120,135,["psybeam","reflect","hyperbeam","kinesis"]]
pokemon[ 'machop']= [ 'fighting','',70,80,50,35,35,["submission","focusenergy","bodyslam","seismictoss"]]
pokemon[ 'machoke']= [ 'fighting','',80,100,70,45,50,["submission","focusenergy","dig","seismictoss"]]
pokemon[ 'machamp']= [ 'fighting','',90,130,80,55,65,["focusenergy","lowkick","megapunch","leer"]]
pokemon[ 'bellsprout']= [ 'grass','poison',50,75,35,40,70,["razorleaf","double-edge","toxic","wrap"]]
pokemon[ 'weepinbell']= [ 'grass','poison' ,65,90,50,55,85,["razorleaf","stunspore","megadrain","growth"]]
pokemon[ 'victreebel']= [ 'grass','poison',80,105,65,70,100,["razorleaf","sleeppowder","acid","wrap"]]
pokemon[ 'tentacool']= [ 'water','poison',40,40,35,70,100,["surf","toxic","blizzard","megadrain"]]
pokemon[ 'tentacruel']= [ 'water','poison',80,70,65,100,120,["bubblebeam","toxic","wrap","screech"]]
pokemon[ 'geodude']= [ 'rock','ground',40,80,100,20,30,["rockslide","fireblast","earthquake","seismictoss"]]
pokemon[ 'graveler']= [ 'rock','ground',55,95,115,35,45,["rockslide","metronome","earthquake","fireblast"]]
pokemon[ 'golem']= [ 'rock','ground',80,110,130,45,55,["rockthrow","dig","defensecurl","fireblast"]]
pokemon[ 'ponyta']= [ 'fire','',50,85,55,90,65,["firespin","toxic","agility","horndrill"]]
pokemon[ 'rapidash']= [ 'fire','',65,100,70,105,80,["fireblast","tailwhip","stomp","reflect"]]
pokemon[ 'slowpoke']= [ 'water','psychic',90,65,65,15,40,["surf","thunderwave","psychic","amnesia"]]
pokemon[ 'slowbro']= [ 'water','psychic',95,75,110,30,80,["surf","megapunch","psychic","disable"]]
pokemon[ 'magnemite']= [ 'electric','',25,35,70,45,95,["thunderbolt","thunderwave","flash","swift"]]
pokemon[ 'magneton']= [ 'electric','',50,60,95,70,120,["thunderwave","supersonic","thunder","flash"]]
pokemon[ "farfetch'd"]= [ 'normal','flying',52,65,55,60,58,["slash","toxic","sandattack","fly"]]
pokemon[ 'doduo']= [ 'normal','flying',35,85,45,75,35,["drillpeck","bodyslam","doubleteam","reflect"]]
pokemon[ 'dodrio']= [ 'normal','flying',60,110,70,100,60,["triattack","agility","fly","growl"]]
pokemon[ 'seel']= [ 'water','',65,45,55,45,70,["surf","doubleteam","blizzard","bodyslam"]]
pokemon[ 'dewgong']= [ 'water','ice',90,70,80,70,95,["aurorabeam","horndrill","surf","headbutt"]]
pokemon[ 'grimer']= [ 'poison','',80,80,50,25,40,["sludge","acidarmor","bodyslam","thunderbolt"]]
pokemon[ 'muk']= [ 'poison','',105,105,75,50,65,["sludge","acidarmor","fireblast","screech"]]
pokemon[ 'shellder']= [ 'water','',30,65,100,40,45,["blizzard","supersonic","surf","swift"]]
pokemon[ 'cloyster']= [ 'water','ice',50, 95, 180,70,85,["icebeam","supersonic","bubblebeam","clamp"]]
pokemon[ 'gastly']= [ 'ghost','poison',30,35,30,80,100,["psychic","nightshade","hypnosis","confuseray"]]
pokemon[ 'haunter']= [ 'ghost','poison',45,50,45,95,115,["psychic","hypnosis","dreameater","confuseray"]]
pokemon[ 'gengar']= [ 'ghost','poison',60,65,60,110,130,["hypnosis","dreameater","nightshade","metronome"]]
pokemon[ 'onix']= [ 'rock','ground',35,45,160,70,30,["rockslide","self-destruct","earthquake","fissure"]]
pokemon[ 'drowzee']= [ 'psychic','',60,48,45,42,90,["hypnosis","psychic","dreameater","seismictoss"]]
pokemon[ 'hypno']= [ 'psychic','',85,73,70,67,115,["hypnosis","psychic","poisongas","headbutt"]]
pokemon[ 'krabby']= [ 'water','',30,105,90,50,25,["surf","guillotine","bodyslam","blizzard"]]
pokemon[ 'kingler']= [ 'water','',55,130,115,75,50,["crabhammer","toxic","strength","guillotine"]]
pokemon[ 'voltorb']= [ 'electric','',40,30,50,100,55,["thunderbolt","reflect","thunderwave","takedown"]]
pokemon[ 'electrode']= [ 'electric','',60,50,70,140,80,["thunder","thunderwave","swift","flash"]]
pokemon[ 'exeggcute']= [ 'grass','psychic',60,40,80,40,60,["leechseed","self-destruct","toxic","psychic"]]
pokemon[ 'exeggutor']= [ 'grass','psychic',95,95,85,55,125,["stomp","sleeppowder","psychic","solarbeam"]]
pokemon[ 'cubone']= [ 'ground','',50,50,95,35,40,["bonemerang","focusenergy","blizzard","thrash"]]
pokemon[ 'marowak']= [ 'ground','',60,80,110,45,50,["boneclub","focusenergy","headbutt","thrash"]]
pokemon[ 'hitmonlee']= [ 'fighting','',50,120,53,87,35,["rollingkick","focusenergy","jumpkick","highjumpkick"]]
pokemon[ 'hitmonchan']= [ 'fighting','',50,105,79,76,35,["megapunch","thunderpunch","firepunch","icepunch"]]
pokemon[ 'lickitung']= [ 'normal','',90,55,75,30,60,["bodyslam","blizzard","thunder","earthquake"]]
pokemon[ 'koffing']= [ 'poison','',40,65,95,35,60,["sludge","toxic","thunder","haze"]]
pokemon[ 'weezing']= [ 'poison','',65,90,120,60,85,["sludge","mimic","thunder","haze"]]
pokemon[ 'rhyhorn']= [ 'ground','rock',80,85,95,25,30,["bodyslam","fissure","earthquake","rockslide"]]
pokemon[ 'rhydon']= [ 'ground','rock',105,130,120,40,45,["hornattack","fissure","earthquake","thunder"]]
pokemon[ 'chansey']= [ 'normal','',250,5,5,50,105,["eggbomb","seismictoss","rest","metronome"]]
pokemon[ 'tangela']= [ 'grass','',65,55,115,60,100,["stunspore","solarbeam","megadrain","growth"]]
pokemon[ 'kangaskhan']= [ 'normal','',105,95,80,90,40,["dizzypunch","substitute","rockslide","surf"]]
pokemon[ 'horsea']= [ 'water','',30,40,70,60,70,["hydropump","smokescreen","icebeam","toxic"]]
pokemon[ 'seadra']= [ 'water','',55,65,95,85,95,["smokescreen","surf","double-edge","toxic"]]
pokemon[ 'goldeen']= [ 'water','',45,67,60,63,50,["surf","agility","horndrill","doubleteam"]]
pokemon[ 'seaking']= [ 'water','',80,92,65,68,80,["waterfall","furyattack","horndrill","supersonic"]]
pokemon[ 'staryu']= [ 'water','',30,45,55,85,70,["minimize","recover","surf","psychic"]]
pokemon[ 'starmie']= [ 'water','psychic',60,75,85,115,100,["bubblebeam","thunder","swift","minimize"]]
pokemon[ 'mr.mime']= [ 'psychic','',40,45,65,90,100,["barrier","hyperbeam","lightscreen","psychic"]]
pokemon[ 'scyther']= [ 'bug','flying',70,110,80,105,55,["focusenergy","doubleteam","hyperbeam","swift"]]
pokemon[ 'jynx']= [ 'ice','psychic',65,50,35,95,95,["lovelykiss","bodyslam","icepunch","psychic"]]
pokemon[ 'electabuzz']= [ 'electric','',65,83,57,105,85,["thunderpunch","metronome","thunderwave","reflect"]]
pokemon[ 'magmar']= [ 'fire','',65,95,57,93,85,["confuseray","firepunch","megapunch","psychic"]]
pokemon[ 'pinsir']= [ 'bug','',65,125,100,85,55,["slash","seismictoss","toxic","guillotine"]]
pokemon[ 'tauros']= [ 'normal','',75,100,95,110,70,["stomp","fireblast","skullbash","bide"]]
pokemon[ 'magikarp']= [ 'water','',20,10,55,80,20,["splash","tackle","splash","tackle"]]
pokemon[ 'gyarados']= [ 'water','flying',95,125,79,81,100,["bubblebeam","leer","bite","fireblast"]]
pokemon[ 'lapras']= [ 'water','ice',130,85,80,60,95,["bubblebeam","icebeam","mist","sing"]]
pokemon[ 'ditto']= [ 'normal','',48,48,48,48,48,["transform","transform","transform","transform"]]
pokemon[ 'eevee']= [ 'normal','',55,55,50,55,65,["double-edge","quickattack","focusenergy","sandattack"]]
pokemon[ 'vaporeon']= [ 'water','',130,65,60,65,110,["hydropump","quickattack","acidarmor","haze"]]
pokemon[ 'jolteon']= [ 'electric','',65,65,60,130,110,["thunder","quickattack","pinmissile","sandattack"]]
pokemon[ 'flareon']= [ 'fire','',65,130,60,65,110,["fireblast","quickattack","smog","sandattack"]]
pokemon[ 'porygon']= [ 'normal','',65,60,70,40,75,["psybeam","recover","triattack","conversion"]]
pokemon[ 'omanyte']= [ 'rock','water',35,40,100,35,90,["hydropump","toxic","bodyslam","icebeam"]]
pokemon[ 'omastar']= [ 'rock','water',70,60,125,55,115,["surf","toxic","spikecannon","horndrill"]]
pokemon[ 'kabuto']= [ 'rock','water',30,80,90,55,45,["surf","doubleteam","blizzard","slash"]]
pokemon[ 'kabutops']= [ 'rock','water',60,115,105,80,70,["hydropump","swordsdance","megakick","icebeam"]]
pokemon[ 'aerodactyl']= [ 'rock','flying',80,105,65,130,60,["supersonic","bite","fireblast","fly"]]
pokemon[ 'snorlax']= [ 'normal','',160,110,65,30,65,["takedown","bide","metronome","rest"]]
pokemon[ 'articuno']= [ 'ice','flying',90,85,100,85,125,["icebeam","agility","skyattack","mist"]]
pokemon[ 'zapdos']= [ 'electric','flying',90,90,85,100,125,["thunder","flash","skyattack","bide"]]
pokemon[ 'moltres']= [ 'fire','flying',90,100,90,90,125,["fireblast","reflect","skyattack","agility"]]
pokemon[ 'dratini']= [ 'dragon','',41,64,45,50,50,["blizzard","fireblast","thunderbolt","bodyslam"]]
pokemon[ 'dragonair']= [ 'dragon','',61,84,65,70,70,["bodyslam","thunderbolt","fireblast","icebeam"]]
pokemon[ 'dragonite']= [ 'dragon','flying',91,134,95,80,100,["thunder","fireblast","wrap","slam"]]
pokemon[ 'mewtwo']= [ 'psychic','',106,110,90,130,154,["psychic","metronome","megapunch","flash"]]
pokemon[ 'mew']= [ 'psychic','',100,100,100,100,100,["psychic","amnesia","thunderbolt","rest"]]
# dic pokenumber just relates a number to a pokemon just in case of numerical repherence
pokenumber={1: 'bulbasaur', 2: 'ivysaur', 3: 'venusaur', 4: 'charmander', 5: 'charmeleon', 6: 'charizard', 7: 'squirtle', 8: 'wartortle', 9: 'blastoise', 10: 'caterpie', 11: 'metapod', 12: 'butterfree', 13: 'weedle', 14: 'kakuna', 15: 'beedrill', 16: 'pidgey', 17: 'pidgeotto', 18: 'pidgeot', 19: 'rattata', 20: 'raticate', 21: 'spearow', 22: 'fearow', 23: 'ekans', 24: 'arbok', 25: 'pikachu', 26: 'raichu', 27: 'sandshrew', 28: 'sandslash', 29: 'nidoranF', 30: 'nidorina', 31: 'nidoqueen', 32: 'nidoranM', 33: 'nidorino', 34: 'nidoking', 35: 'clefairy', 36: 'clefable', 37: 'vulpix', 38: 'ninetales', 39: 'jigglypuff', 40: 'wigglytuff', 41: 'zubat', 42: 'golbat', 43: 'oddish', 44: 'gloom', 45: 'vileplume', 46: 'paras', 47: 'parasect', 48: 'venonat', 49: 'venomoth', 50: 'diglett', 51: 'dugtrio', 52: 'meowth', 53: 'persian', 54: 'psyduck', 55: 'golduck', 56: 'mankey', 57: 'primeape', 58: 'growlithe', 59: 'arcanine', 60: 'poliwag', 61: 'poliwhirl', 62: 'poliwrath', 63: 'abra', 64: 'kadabra', 65: 'alakazam', 66: 'machop', 67: 'machoke', 68: 'machamp', 69: 'bellsprout', 70: 'weepinbell', 71: 'victreebel', 72: 'tentacool', 73: 'tentacruel', 74: 'geodude', 75: 'graveler', 76: 'golem', 77: 'ponyta', 78: 'rapidash', 79: 'slowpoke', 80: 'slowbro', 81: 'magnemite', 82: 'magneton', 83: "farfetch'd", 84: 'doduo', 85: 'dodrio', 86: 'seel', 87: 'dewgong', 88: 'grimer', 89: 'muk', 90: 'shellder', 91: 'cloyster', 92: 'gastly', 93: 'haunter', 94: 'gengar', 95: 'onix', 96: 'drowzee', 97: 'hypno', 98: 'krabby', 99: 'kingler', 100: 'voltorb', 101: 'electrode', 102: 'exeggcute', 103: 'exeggutor', 104: 'cubone', 105: 'marowak', 106: 'hitmonlee', 107: 'hitmonchan', 108: 'lickitung', 109: 'koffing', 110: 'weezing', 111: 'rhyhorn', 112: 'rhydon', 113: 'chansey', 114: 'tangela', 115: 'kangaskhan', 116: 'horsea', 117: 'seadra', 118: 'goldeen', 119: 'seaking', 120: 'staryu', 121: 'starmie', 122: 'mr.mime', 123: 'scyther', 124: 'jynx', 125: 'electabuzz', 126: 'magmar', 127: 'pinsir', 128: 'tauros', 129: 'magikarp', 130: 'gyarados', 131: 'lapras', 132: 'ditto', 133: 'eevee', 134: 'vaporeon', 135: 'jolteon', 136: 'flareon', 137: 'porygon', 138: 'omanyte', 139: 'omastar', 140: 'kabuto', 141: 'kabutops', 142: 'aerodactyl', 143: 'snorlax', 144: 'articuno', 145: 'zapdos', 146: 'moltres', 147: 'dratini', 148: 'dragonair', 149: 'dragonite', 150: 'mewtwo', 151: 'mew'}
# dic movenumber just relates a number to a move just in case of numerical repherence
movenumber={'-': 137,
    'absorb': 145,
    'acid': 46,
    'acidarmor': 84,
    'agility': 105,
    'amnesia': 99,
    'aurorabeam': 2,
    'barrage': 92,
    'barrier': 59,
    'bide': 120,
    'bind': 155,
    'bite': 96,
    'blizzard': 82,
    'bodyslam': 6,
    'boneclub': 27,
    'bonemerang': 85,
    'bubble': 102,
    'bubblebeam': 1,
    'clamp': 40,
    'cometpunch': 11,
    'confuseray': 101,
    'confusion': 61,
    'constrict': 163,
    'conversion': 133,
    'counter': 156,
    'crabhammer': 139,
    'cut': 10,
    'defensecurl': 79,
    'dig': 34,
    'disable': 77,
    'dizzypunch': 104,
    'double-edge': 130,
    'doublekick': 37,
    'doubleslap': 24,
    'doubleteam': 3,
    'dragonrage': 78,
    'dreameater': 16,
    'drillpeck': 83,
    'earthquake': 67,
    'eggbomb': 25,
    'ember': 116,
    'explosion': 58,
    'fireblast': 29,
    'firepunch': 7,
    'firespin': 123,
    'fissure': 70,
    'flamethrower': 118,
    'flash': 12,
    'fly': 112,
    'focusenergy': 9,
    'furyattack': 64,
    'furyswipes': 18,
    'glare': 41,
    'growl': 146,
    'growth': 44,
    'guillotine': 45,
    'gust': 33,
    'harden': 117,
    'haze': 13,
    'headbutt': 74,
    'highjumpkick': 68,
    'hornattack': 63,
    'horndrill': 136,
    'hperbeam': 138,
    'hydropump': 28,
    'hyperfang': 153,
    'hypnosis': 76,
    'icebeam': 128,
    'icepunch': 22,
    'jumpkick': 88,
    'karatechop': 158,
    'kinesis': 19,
    'leechlife': 17,
    'leechseed': 20,
    'leer': 135,
    'lick': 86,
    'lightscreen': 65,
    'lovelykiss': 36,
    'lowkick': 15,
    'meditate': 160,
    'megadrain': 164,
    'megakick': 100,
    'megapunch': 95,
    'metronome': 113,
    'mimic': 159,
    'minimize': 154,
    'mirrormove': 109,
    'mist': 91,
    'nightshade': 87,
    'payday': 55,
    'peck': 5,
    'petaldance': 94,
    'pinmissile': 93,
    'poisongas': 125,
    'poisonpowder': 144,
    'poisonsting': 32,
    'pound': 122,
    'psybeam': 152,
    'psychic': 52,
    'psywave': 111,
    'quickattack': 103,
    'rage': 114,
    'razorleaf': 143,
    'razorwind': 165,
    'recover': 124,
    'reflect': 147,
    'rest': 26,
    'roar': 71,
    'rockslide': 106,
    'rockthrow': 42,
    'rollingkick': 49,
    'sandattack': 35,
    'scratch': 4,
    'screech': 73,
    'seismictoss': 110,
    'self-destruct': 14,
    'sing': 89,
    'skullbash': 38,
    'skyattack': 157,
    'slam': 126,
    'slash': 56,
    'sleeppowder': 39,
    'sludge': 8,
    'smog': 30,
    'smokescreen': 127,
    'soft-boiled': 53,
    'solarbeam': 23,
    'sonicboom': 69,
    'sparpen': 148,
    'spikecannon': 75,
    'splash': 98,
    'spore': 43,
    'stomp': 21,
    'strength': 134,
    'stringshot': 107,
    'struggle': 62,
    'submission': 31,
    'substitute': 48,
    'superfang': 57,
    'supersonic': 151,
    'surf': 141,
    'swift': 66,
    'swordsdance': 54,
    'tackle': 150,
    'tailwhip': 121,
    'takedown': 131,
    'teleport': 132,
    'thrash': 119,
    'thunder': 51,
    'thunderbolt': 142,
    'thunderpunch': 81,
    'thundershock': 162,
    'thunderwave': 60,
    'toxic': 140,
    'transform': 97,
    'triattack': 50,
    'twineedle': 47,
    'vicegrip': 129,
    'vinewhip': 115,
    'waterfall': 149,
    'watergun': 108,
    'whirlwind': 72,
    'wingattack': 80,
    'withdraw': 161,
    'wrap': 90}


#dictionary "offense" determines type bonus. The element on the left is what nature type the attack is and the nature type on the right would be the nature type of the defending pokemon
#NOTE: for example if a defending pokemon had a grass/ice dual nature type and it was attacked by a fire attack. since the damage would be doubled by the grass and the ice individually, It would be a x4 multiplier rather then just x2
offense={('', ''):1.0}
offense[('', 'normal')]=1.0
offense[('', 'fire')]=1.0
offense[('', 'water')]=1.0
offense[('', 'electric')]=1.0
offense[('', 'grass')]=1.0
offense[('', 'ice')]=1.0
offense[('', 'fighting')]=1.0
offense[('', 'poison')]=1.0
offense[('', 'ground')]=1.0
offense[('', 'flying')]=1.0
offense[('', 'psychic')]=1.0
offense[('', 'bug')]=1.0
offense[('', 'rock')]=1.0
offense[('', 'ghost')]=1.0
offense[('', 'dragon')]=1.0
offense[('normal', '')]=1.0
offense[('normal', 'normal')]=1.0
offense[('normal', 'fire')]=1.0
offense[('normal', 'water')]=1.0
offense[('normal', 'electric')]=1.0
offense[('normal', 'grass')]=1.0
offense[('normal', 'ice')]=1.0
offense[('normal', 'fighting')]=1.0
offense[('normal', 'poison')]=1.0
offense[('normal', 'ground')]=1.0
offense[('normal', 'flying')]=1.0
offense[('normal', 'psychic')]=1.0
offense[('normal', 'bug')]=1.0
offense[('normal', 'rock')]=0.5
offense[('normal', 'ghost')]=0.0
offense[('normal', 'dragon')]=1.0
offense[('fire', '')]=1.0
offense[('fire', 'normal')]=1.0
offense[('fire', 'fire')]=0.5
offense[('fire', 'water')]=0.5
offense[('fire', 'electric')]=1.0
offense[('fire', 'grass')]=2.0
offense[('fire', 'ice')]=2.0
offense[('fire', 'fighting')]=1.0
offense[('fire', 'poison')]=1.0
offense[('fire', 'ground')]=1.0
offense[('fire', 'flying')]=1.0
offense[('fire', 'psychic')]=1.0
offense[('fire', 'bug')]=2.0
offense[('fire', 'rock')]=0.5
offense[('fire', 'ghost')]=1.0
offense[('fire', 'dragon')]=0.5
offense[('water', '')]=1.0
offense[('water', 'normal')]=1.0
offense[('water', 'fire')]=2.0
offense[('water', 'water')]=0.5
offense[('water', 'electric')]=1.0
offense[('water', 'grass')]=0.5
offense[('water', 'ice')]=1.0
offense[('water', 'fighting')]=1.0
offense[('water', 'poison')]=1.0
offense[('water', 'ground')]=2.0
offense[('water', 'flying')]=1.0
offense[('water', 'psychic')]=1.0
offense[('water', 'bug')]=1.0
offense[('water', 'rock')]=2.0
offense[('water', 'ghost')]=1.0
offense[('water', 'dragon')]=0.5
offense[('electric', '')]=1.0
offense[('electric', 'normal')]=1.0
offense[('electric', 'fire')]=1.0
offense[('electric', 'water')]=2.0
offense[('electric', 'electric')]=0.5
offense[('electric', 'grass')]=0.5
offense[('electric', 'ice')]=1.0
offense[('electric', 'fighting')]=1.0
offense[('electric', 'poison')]=1.0
offense[('electric', 'ground')]=0.0
offense[('electric', 'flying')]=2.0
offense[('electric', 'psychic')]=1.0
offense[('electric', 'bug')]=1.0
offense[('electric', 'rock')]=1.0
offense[('electric', 'ghost')]=1.0
offense[('electric', 'dragon')]=0.5
offense[('grass', '')]=1.0
offense[('grass', 'normal')]=1.0
offense[('grass', 'fire')]=0.5
offense[('grass', 'water')]=2.0
offense[('grass', 'electric')]=1.0
offense[('grass', 'grass')]=0.5
offense[('grass', 'ice')]=1.0
offense[('grass', 'fighting')]=1.0
offense[('grass', 'poison')]=0.5
offense[('grass', 'ground')]=2.0
offense[('grass', 'flying')]=0.5
offense[('grass', 'psychic')]=1.0
offense[('grass', 'bug')]=2.0
offense[('grass', 'rock')]=2.0
offense[('grass', 'ghost')]=1.0
offense[('grass', 'dragon')]=0.5
offense[('ice', '')]=1.0
offense[('ice', 'normal')]=1.0
offense[('ice', 'fire')]=1.0
offense[('ice', 'water')]=0.5
offense[('ice', 'electric')]=1.0
offense[('ice', 'grass')]=2.0
offense[('ice', 'ice')]=0.5
offense[('ice', 'fighting')]=1.0
offense[('ice', 'poison')]=1.0
offense[('ice', 'ground')]=2.0
offense[('ice', 'flying')]=2.0
offense[('ice', 'psychic')]=1.0
offense[('ice', 'bug')]=1.0
offense[('ice', 'rock')]=1.0
offense[('ice', 'ghost')]=1.0
offense[('ice', 'dragon')]=2.0
offense[('fighting', '')]=1.0
offense[('fighting', 'normal')]=2.0
offense[('fighting', 'fire')]=1.0
offense[('fighting', 'water')]=1.0
offense[('fighting', 'electric')]=1.0
offense[('fighting', 'grass')]=1.0
offense[('fighting', 'ice')]=2.0
offense[('fighting', 'fighting')]=1.0
offense[('fighting', 'poison')]=0.5
offense[('fighting', 'ground')]=1.0
offense[('fighting', 'flying')]=0.5
offense[('fighting', 'psychic')]=0.5
offense[('fighting', 'bug')]=0.5
offense[('fighting', 'rock')]=2.0
offense[('fighting', 'ghost')]=0.0
offense[('fighting', 'dragon')]=1.0
offense[('poison', '')]=1.0
offense[('poison', 'normal')]=1.0
offense[('poison', 'fire')]=1.0
offense[('poison', 'water')]=1.0
offense[('poison', 'electric')]=1.0
offense[('poison', 'grass')]=2.0
offense[('poison', 'ice')]=1.0
offense[('poison', 'fighting')]=1.0
offense[('poison', 'poison')]=0.5
offense[('poison', 'ground')]=0.5
offense[('poison', 'flying')]=1.0
offense[('poison', 'psychic')]=1.0
offense[('poison', 'bug')]=2.0
offense[('poison', 'rock')]=0.5
offense[('poison', 'ghost')]=0.5
offense[('poison', 'dragon')]=1.0
offense[('ground', '')]=1.0
offense[('ground', 'normal')]=1.0
offense[('ground', 'fire')]=2.0
offense[('ground', 'water')]=1.0
offense[('ground', 'electric')]=2.0
offense[('ground', 'grass')]=0.5
offense[('ground', 'ice')]=1.0
offense[('ground', 'fighting')]=1.0
offense[('ground', 'poison')]=2.0
offense[('ground', 'ground')]=1.0
offense[('ground', 'flying')]=0.0
offense[('ground', 'psychic')]=1.0
offense[('ground', 'bug')]=0.5
offense[('ground', 'rock')]=1.0
offense[('ground', 'ghost')]=1.0
offense[('ground', 'dragon')]=1.0
offense[('flying', '')]=1.0
offense[('flying', 'normal')]=1.0
offense[('flying', 'fire')]=1.0
offense[('flying', 'water')]=1.0
offense[('flying', 'electric')]=0.5
offense[('flying', 'grass')]=2.0
offense[('flying', 'ice')]=1.0
offense[('flying', 'fighting')]=2.0
offense[('flying', 'poison')]=1.0
offense[('flying', 'ground')]=1.0
offense[('flying', 'flying')]=1.0
offense[('flying', 'psychic')]=1.0
offense[('flying', 'bug')]=2.0
offense[('flying', 'rock')]=0.5
offense[('flying', 'ghost')]=1.0
offense[('flying', 'dragon')]=1.0
offense[('psychic', '')]=1.0
offense[('psychic', 'normal')]=1.0
offense[('psychic', 'fire')]=1.0
offense[('psychic', 'water')]=1.0
offense[('psychic', 'electric')]=1.0
offense[('psychic', 'grass')]=1.0
offense[('psychic', 'ice')]=1.0
offense[('psychic', 'fighting')]=2.0
offense[('psychic', 'poison')]=2.0
offense[('psychic', 'ground')]=1.0
offense[('psychic', 'flying')]=1.0
offense[('psychic', 'psychic')]=0.5
offense[('psychic', 'bug')]=1.0
offense[('psychic', 'rock')]=1.0
offense[('psychic', 'ghost')]=1.0
offense[('psychic', 'dragon')]=1.0
offense[('bug', '')]=1.0
offense[('bug', 'normal')]=1.0
offense[('bug', 'fire')]=0.5
offense[('bug', 'water')]=1.0
offense[('bug', 'electric')]=1.0
offense[('bug', 'grass')]=2.0
offense[('bug', 'ice')]=1.0
offense[('bug', 'fighting')]=0.5
offense[('bug', 'poison')]=2.0
offense[('bug', 'ground')]=1.0
offense[('bug', 'flying')]=0.5
offense[('bug', 'psychic')]=2.0
offense[('bug', 'bug')]=1.0
offense[('bug', 'rock')]=1.0
offense[('bug', 'ghost')]=1.0
offense[('bug', 'dragon')]=1.0
offense[('rock', '')]=1.0
offense[('rock', 'normal')]=1.0
offense[('rock', 'fire')]=2.0
offense[('rock', 'water')]=1.0
offense[('rock', 'electric')]=1.0
offense[('rock', 'grass')]=1.0
offense[('rock', 'ice')]=2.0
offense[('rock', 'fighting')]=0.5
offense[('rock', 'poison')]=1.0
offense[('rock', 'ground')]=0.5
offense[('rock', 'flying')]=2.0
offense[('rock', 'psychic')]=1.0
offense[('rock', 'bug')]=2.0
offense[('rock', 'rock')]=1.0
offense[('rock', 'ghost')]=1.0
offense[('rock', 'dragon')]=1.0
offense[('ghost', '')]=1.0
offense[('ghost', 'normal')]=0.0
offense[('ghost', 'fire')]=1.0
offense[('ghost', 'water')]=1.0
offense[('ghost', 'electric')]=1.0
offense[('ghost', 'grass')]=1.0
offense[('ghost', 'ice')]=1.0
offense[('ghost', 'fighting')]=1.0
offense[('ghost', 'poison')]=1.0
offense[('ghost', 'ground')]=1.0
offense[('ghost', 'flying')]=1.0
offense[('ghost', 'psychic')]=0.0
offense[('ghost', 'bug')]=1.0
offense[('ghost', 'rock')]=1.0
offense[('ghost', 'ghost')]=2.0
offense[('ghost', 'dragon')]=1.0
offense[('dragon', '')]=1.0
offense[('dragon', 'normal')]=1.0
offense[('dragon', 'fire')]=1.0
offense[('dragon', 'water')]=1.0
offense[('dragon', 'electric')]=1.0
offense[('dragon', 'grass')]=1.0
offense[('dragon', 'ice')]=1.0
offense[('dragon', 'fighting')]=1.0
offense[('dragon', 'poison')]=1.0
offense[('dragon', 'ground')]=1.0
offense[('dragon', 'flying')]=1.0
offense[('dragon', 'psychic')]=1.0
offense[('dragon', 'bug')]=1.0
offense[('dragon', 'rock')]=1.0
offense[('dragon', 'ghost')]=1.0
offense[('dragon', 'dragon')]=2.0
def numberfy(L):
    total=0
    for i in range(len(L)):
        total=total +L[-(i+1)]*(10**i)
    return total
# dictionary "attacks" says how the attack is distributed attack/special/status and what nature type the attack has
attacks={'barrage':['physical','normal']}
attacks['bide']=['','']
attacks['bind']=['physical','normal']
attacks['bite']=['physical','normal']
attacks['bodyslam']=['physical','normal']
attacks['boneclub']=['physical','ground']
attacks['bonemerang']=['physical','ground']
attacks['clamp']=['physical','water']
attacks['cometpunch']=['physical','normal']
attacks['constrict']=['physical','normal']
attacks['counter']=['physical','fighting']
attacks['crabhammer']=['physical','water']
attacks['cut']=['physical','normal']
attacks['dig']=['physical','ground']
attacks['dizzypunch']=['physical','normal']
attacks['doublekick']=['physical','fighting']
attacks['doubleslap']=['physical','normal']
attacks['double-edge']=['physical','normal']
attacks['drillpeck']=['physical','flying']
attacks['earthquake']=['physical','ground']
attacks['hyperbeam']=['special','normal']
attacks['eggbomb']=['physical','normal']
attacks['explosion']=['physical','normal']
attacks['firepunch']=['physical','fire']
attacks['fissure']=['physical','ground']
attacks['fly']=['physical','flying']
attacks['furyattack']=['physical','normal']
attacks['furyswipes']=['physical','normal']
attacks['guillotine']=['physical','normal']
attacks['headbutt']=['physical','normal']
attacks['highjumpkick']=['physical','fighting']
attacks['hornattack']=['physical','normal']
attacks['horndrill']=['physical','normal']
attacks['hyperfang']=['physical','normal']
attacks['icepunch']=['physical','ice']
attacks['jumpkick']=['physical','fighting']
attacks['karatechop']=['physical','fighting']
attacks['leechlife']=['physical','bug']
attacks['lick']=['physical','ghost']
attacks['lowkick']=['physical','fighting']
attacks['megakick']=['physical','normal']
attacks['megapunch']=['physical','normal']
attacks['payday']=['physical','normal']
attacks['peck']=['physical','flying']
attacks['pinmissile']=['physical','bug']
attacks['poisonsting']=['physical','poison']
attacks['pound']=['physical','normal']
attacks['quickattack']=['physical','normal']
attacks['rage']=['physical','normal']
attacks['razorleaf']=['physical','grass']
attacks['rockslide']=['physical','rock']
attacks['rockthrow']=['physical','rock']
attacks['rollingkick']=['physical','fighting']
attacks['scratch']=['physical','normal']
attacks['seismictoss']=['physical','fighting']
attacks['self-destruct']=['physical','normal']
attacks['skullbash']=['physical','normal']
attacks['skyattack']=['physical','flying']
attacks['slam']=['physical','normal']
attacks['slash']=['physical','normal']
attacks['spikecannon']=['physical','normal']
attacks['stomp']=['physical','normal']
attacks['strength']=['physical','normal']
attacks['struggle']=['physical','normal']
attacks['submission']=['physical','fighting']
attacks['superfang']=['physical','normal']
attacks['tackle']=['physical','normal']
attacks['takedown']=['physical','normal']
attacks['thrash']=['physical','normal']
attacks['thunderpunch']=['physical','electric']
attacks['twineedle']=['physical','bug']
attacks['vicegrip']=['physical','normal']
attacks['vinewhip']=['physical','grass']
attacks['waterfall']=['physical','water']
attacks['wingattack']=['physical','flying']
attacks['wrap']=['physical','normal']
attacks['acidarmor']=['status','']
attacks['agility']=['status','']
attacks['amnesia']=['status','']
attacks['barrier']=['status','']
attacks['confuseray']=['status','']
attacks['conversion']=['status','']
attacks['defensecurl']=['status','']
attacks['disable']=['status','']
attacks['doubleteam']=['status','']
attacks['flash']=['status','']
attacks['focusenergy']=['status','']
attacks['glare']=['status','']
attacks['growl']=['status','']
attacks['growth']=['status','']
attacks['harden']=['status','']
attacks['haze']=['status','']
attacks['hypnosis']=['status','']
attacks['kinesis']=['status','']
attacks['leechseed']=['status','']
attacks['leer']=['status','']
attacks['lightscreen']=['status','']
attacks['lovelykiss']=['status','']
attacks['meditate']=['status','']
attacks['metronome']=['status','']
attacks['mimic']=['status','']
attacks['minimize']=['status','']
attacks['mirrormove']=['status','']
attacks['mist']=['status','']
attacks['poisongas']=['status','']
attacks['poisonpowder']=['status','']
attacks['recover']=['status','']
attacks['reflect']=['status','']
attacks['rest']=['status','']
attacks['roar']=['status','']
attacks['sandattack']=['status','']
attacks['screech']=['status','']
attacks['sparpen']=['status','']
attacks['sing']=['status','']
attacks['sleeppowder']=['status','']
attacks['smokescreen']=['status','']
attacks['soft-boiled']=['status','']
attacks['splash']=['status','']
attacks['spore']=['status','']
attacks['stringshot']=['status','']
attacks['substitute']=['status','']
attacks['supersonic']=['status','']
attacks['swordsdance']=['status','']
attacks['tailwhip']=['status','']
attacks['teleport']=['status','']
attacks['thunderwave']=['status','']
attacks['toxic']=['status','']
attacks['transform']=['status','']
attacks['whirlwind']=['status','']
attacks['withdraw']=['status','']
attacks['-']=['physical','']
attacks['absorb']=['special','grass']
attacks['acid']=['special','poison']
attacks['aurorabeam']=['special','ice']
attacks['blizzard']=['special','ice']
attacks['bubble']=['special','water']
attacks['bubblebeam']=['special','water']
attacks['confusion']=['special','psychic']
attacks['dragonrage']=['special','dragon']
attacks['dreameater']=['special','psychic']
attacks['ember']=['special','fire']
attacks['fireblast']=['special','fire']
attacks['firespin']=['special','fire']
attacks['flamethrower']=['special','fire']
attacks['gust']=['special','flying']
attacks['hydropump']=['special','water']
attacks['hperbeam']=['special','normal']
attacks['icebeam']=['special','ice']
attacks['megadrain']=['special','grass']
attacks['nightshade']=['special','ghost']
attacks['petaldance']=['special','grass']
attacks['psybeam']=['special','psychic']
attacks['psychic']=['special','psychic']
attacks['psywave']=['special','psychic']
attacks['razorwind']=['special','normal']
attacks['sludge']=['special','poison']
attacks['smog']=['special','poison']
attacks['solarbeam']=['special','grass']
attacks['sonicboom']=['special','normal']
attacks['surf']=['special','water']
attacks['swift']=['special','normal']
attacks['thunder']=['special','electric']
attacks['thundershock']=['special','electric']
attacks['thunderbolt']=['special','electric']
attacks['triattack']=['special','normal']
attacks['watergun']=['special','water']
strange=["leer"]
goesLast=["counter"]
# make a def select random pokes and moves!

def pick(screen,pokeA,l1,Master1):
    # displays in game what options you have to pick a pokemon
    d1= 50
    options=[]
    for mon in Master1:
        if mon==pokeA:
            continue
        poke1(screen, 100, d1)
        options= options+[Option(mon, (150, d1))]
        health_bar1(screen,100,d1+40,Master1[mon][2],pokemon[mon][2])
        d1=d1+80
    return options
def HP(base):
    #formula for converting base health to real health based on level,IV,EV but these are treated as constants for this project
    level=50
    IV=12
    EV=22000
    return int((((IV + base + math.sqrt(EV)/8 +50)*level)/50) +10)
def Stat(base):
    #formula for converting the other stats to real stats based on level,IV,EV but these are treated as constants for this project
    level=50
    IV=12
    EV=22000
    return int((((IV + base + math.sqrt(EV)/8)*level)/50) +5)
# this for loop turns pokemon base stats to real stats for pokemon at level 50.In addition it adds new features to the list pointing to each pokemon in the dictionary
for i in pokemon.keys():
    pokemon[i][2]=HP(pokemon[i][2])
    pokemon[i][3]=Stat(pokemon[i][3])
    pokemon[i][4]=Stat(pokemon[i][4])
    pokemon[i][6]=Stat(pokemon[i][6])
    pokemon[i]=pokemon[i] +[0,0,[],[],[0,0],0,"good",0,[0,0,0,0,0,0],i,0]

#pokemon["poke"]=[type1,type2,health,offense,defense, speed,special,moves, moves done, index pointing to playable moves, bide list->[how much damage gathered, turns to unleash bide], turns till confused is over, status update('good' -> has no negitive condition...however there are
# 5 types of negitive conditions: poisoned(damage over time), parayled(chance it cant move for turn), burned(damage over time and decreases attack stat),sleep( cant move at all in a few turns but goes away once pokemon wakes up), and frozen(cant make a move and wont go away) ,
#these 4 primary stats and 2 secondary stats have "stages" that either increase or decrease stats-->[offense,defense,speed,special, accuracy, evasive]  ]
def god(A):
    # a big issue i had when i was trying to duplicate a list that was in a dictionary but the list changed whenever a indexed value was changed....the lists were connected rather then being their own independent(but equal at the start) list.
    #so to fix that tempararily def god() simply added an element and deleted that element which for some reason separated the list bond.
    OO=A+[57]
    del OO[-1]
    return OO

#adds random damage to attacks so the game has a more random element to it.
def rand():
    return random.randint(85,100)/100.0
def Is_STAB(pokemon,pokeA,attacks,attackA):
    #if a pokemon uses a nature type attack thats the same as its own nature type (ex: fire pokemon using a fire attack) then theres automaticly a 50% increase in damage output.
    if attackA=="-":
        return 1.0
    A=pokemon[pokeA][0]
    AA=pokemon[pokeA][1]
    if attacks[attackA][1] == A or attacks[attackA][1] == AA:
        return 1.5
    else:
        return 1.0
def Ran(percent):
    #Ran() takes a decemial number between 0 and 1 and outputs either a 0 or 1 based on chances. EX: Ran(0.85) says theres a 85% chance that the output will be a 1 and 15% its a zero.....mainly used to see if an attack hit or missed
    if int(percent*100)>=random.randint(1,100):
        return 1
    else:
        return 0
#CONDITIONS
def Paralyzed(S):
    if S =="paralyzed":
        return [0.75,0.25]
    else:
        return [1,0]
def Poisoned(S):
    if S=="poisoned":
        return 1.0/8.0
    else:
        return 0
def Burned(S):
    if S== "burned":
        return [1.0/16.0, 0.5]
    else:
        return [0.0,1.0]
def Sleep(S):
    if S == "sleep":
        return random.randint(1,4)
    else:
        return 0
def Frozen(S):
    if S=="frozen":
        return 0
    else:
        return 1


def pl(x):
    #alternates between player 1 and 2
    if x==1:
        return 2
    if x==2:
        return 1
def typebonus(strange,pokemon,pokeB,attacks,attackA,offense):
    #determines the type bonus of an attack... dictionaries offense and attacks are used here
    if attackA in strange:
        return 0.0
    B=pokemon[pokeB][0]
    BB=pokemon[pokeB][1]
    A=1.0*offense[(attacks[attackA][1],B)]
    AA=1.0*offense[(attacks[attackA][1],BB)]
    return A*AA

#START OF ALL THE POSSIBLE MOVES IN THE GAME ABOUT 100-200 moves...most of them work but still working on some of them, however depending on time some moves will not be completed and replaced with other moves
#=========================================================================================================================================================================================================

def confuseray(i,order,pokemonorder,damage):
    if not(pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1):
        dick=random.randint(1,4)
        pokemonorder[i-1][13]=dick
    return pokemonorder
def barrage(i,order,pokemonorder,damage):
    power=15
    acc=0.85
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    times=random.randint(2,5)
    while(times!=0):
        damage=damage + raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
        times=times-1
    """print "player",pl(walk),order[i-1][0],pokemonorder[i-1][2]"""
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def bide(i,order,pokemonorder,damage):
    pokemonorder[i][12][0]=3
    return pokemonorder
def bind(i,order,pokemonorder,damage):
    power=15
    acc=0.85
    raz=random.randint(85,100)/100.0
    times=random.randint(4,5)
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    while(times!=0):
        damage=damage + raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
        times=times-1
    """print "player",pl(walk),order[i-1][0],pokemonorder[i-1][2]"""
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def bite(i,order,pokemonorder,damage):
    #flinching number in pokemon list
    power=60
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    """print int(damage),"player",pl(walk),order[i-1][0],pokemonorder[i-1][2]"""
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def bodyslam(i,order,pokemonorder,damage):
    power=85
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def boneclub(i,order,pokemonorder,damage):
    power=65
    acc=0.85
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def bonemerang(i,order,pokemonorder,damage):
    power=100
    acc=0.9
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def clamp(i,order,pokemonorder,damage):
    power=35
    acc=0.85
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    times=random.randint(4,5)
    while(times!=0):
        damage=damage + raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
        times=times-1
    """print "player",pl(walk),order[i-1][0],pokemonorder[i-1][2]"""
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def cometpunch(i,order,pokemonorder,damage):
    power=18
    acc=0.85
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    times=random.randint(2,5)
    while(times!=0):
        damage=damage + raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
        times=times-1
    """print "player",pl(walk),order[i-1][0],pokemonorder[i-1][2]"""
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder

def constrict(i,order,pokemonorder,damage):
    power=10
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def crabhammer(i,order,pokemonorder,damage):
    power=100
    acc=0.9
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    """print int(damage),"player",pl(walk),order[i-1][0],pokemonorder[i-1][2]"""
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def cut(i,order,pokemonorder,damage):
    power=50
    acc=0.95
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    """print int(damage),"player",pl(walk),order[i-1][0],pokemonorder[i-1][2]"""
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def dig(i,order,pokemonorder,damage):
    pokemonorder[i][8]=2
    return pokemonorder
def dizzypunch(i,order,pokemonorder,damage):
    power=70
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def doublekick(i,order,pokemonorder,damage):
    power=60
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def doubleslap(i,order,pokemonorder,damage):
    power=15
    acc=0.85
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    times=random.randint(2,5)
    while(times!=0):
        damage=damage + raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
        times=times-1
    """print "player",pl(walk),order[i-1][0],pokemonorder[i-1][2]"""
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def doubleedge(i,order,pokemonorder,damage):
    power=120
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    pokemonorder[i][2]= pokemonorder[i][2] - int(pimp*0.25)
    return pokemonorder
def drillpeck(i,order,pokemonorder,damage):
    power=80
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def earthquake(i,order,pokemonorder,damage):
    power=100
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def eggbomb(i,order,pokemonorder,damage):
    power=100
    acc=0.75
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def explosion(i,order,pokemonorder,damage):
    power=260
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    pokemonorder[i][2]=0
    return pokemonorder
def firepunch(i,order,pokemonorder,damage):
    power=75
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    if Ran(0.1)==1:
        pokemonorder[i-1][14]="burned"
    return pokemonorder
def fissure(i,order,pokemonorder,damage):
    acc=0.7
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=1
    #should be zero?
    if pokemonorder[i-1][5]>pokemonorder[i][5] :
        acc=1
    pokemonorder[i-1][2]= Ran(acc)*pokemonorder[i-1][2]
    return pokemonorder
def fly(i,order,pokemonorder,damage):
    pokemonorder[i][9]=2
    return pokemonorder
def furyattack(i,order,pokemonorder,damage):
    power=15
    acc=0.85
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    times=random.randint(2,5)
    while(times!=0):
        damage=damage + raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
        times=times-1
    """print "player",pl(walk),order[i-1][0],pokemonorder[i-1][2]"""
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def furyswipes(i,order,pokemonorder,damage):
    power=18
    acc=0.8
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    times=random.randint(2,5)
    damage=0
    while(times!=0):
        damage=damage + raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
        times=times-1
    """print "player",pl(walk),order[i-1][0],pokemonorder[i-1][2]"""
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def guillotine(i,order,pokemonorder,damage):
    acc=0.7
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=1
    if pokemonorder[i-1][5]>pokemonorder[i][5]:
        acc=1
    pokemonorder[i-1][2]= Ran(acc)*pokemonorder[i-1][2]
    return pokemonorder
def headbutt(i,order,pokemonorder,damage):
    power=70
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def highjumpkick(i,order,pokemonorder,damage):
    power=130
    acc=0.9
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    play=Ran(acc)
    if play == 1:
        pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(play*damage))
        pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
        if pokemonorder[i-1][12][0]>0:
            pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    else:
        pokemonorder[i][2]= pokemonorder[i][2] - int(0.5*pokemon[order[i][0]][2])
    return pokemonorder
def hornattack(i,order,pokemonorder,damage):
    power=65
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def horndrill(i,order,pokemonorder,damage):
    acc=0.7
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=1
    if pokemonorder[i-1][5]>pokemonorder[i][5]:
        acc=1
    pokemonorder[i-1][2]= Ran(acc)*pokemonorder[i-1][2]
    return pokemonorder
def hyperfang(i,order,pokemonorder,damage):
    power=80
    acc=0.9
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def icepunch(i,order,pokemonorder,damage):
    power=75
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def jumpkick(i,order,pokemonorder,damage):
    power=100
    acc=0.95
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    if Ran(acc) == 1:
        pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
        pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
        if pokemonorder[i-1][12][0]>0:
            pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    else:
        pokemonorder[i][2]= pokemonorder[i][2] - int(0.5*pokemon[order[i][0]][2])
    return pokemonorder
def karatechop(i,order,pokemonorder,damage):
    power=50
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    """print int(damage),"player",pl(walk),order[i-1][0],pokemonorder[i-1][2]"""
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/256)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def leechlife(i,order,pokemonorder,damage):
    power=20
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    pokemonorder[i][2]= pokemonorder[i][2] +pimp/2
    return pokemonorder
def counter(i,order,pokemonorder,damage):
    acc=1
    damage=2*int(damage)
    """print int(damage),"player",pl(walk),order[i-1][0],pokemonorder[i-1][2]"""
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - int((Ran(acc)*damage))
    return pokemonorder
def psychic(i,order,pokemonorder,damage):
    power=90
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][6]/pokemonorder[i-1][6])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder

def lick(i,order,pokemonorder,damage):
    power=30
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    if Ran(0.1)==1:
        pokemonorder[i-1][14]="paralyzed"
    return pokemonorder
def lowkick(i,order,pokemonorder,damage):
    power=50
    acc=0.9
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def megakick(i,order,pokemonorder,damage):
    power=120
    acc=0.75
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def megapunch(i,order,pokemonorder,damage):
    power=80
    acc=0.85
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def payday(i,order,pokemonorder,damage):
    power=40
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def peck(i,order,pokemonorder,damage):
    power=35
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def pinmissile(i,order,pokemonorder,damage):
    power=25
    acc=0.95
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    times=random.randint(2,5)
    while(times!=0):
        damage=damage + raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
        times=times-1
    """print "player",pl(walk),order[i-1][0],pokemonorder[i-1][2]"""
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def poisonsting(i,order,pokemonorder,damage):
    power=15
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    if Ran(0.3)==1:
        pokemonorder[i-1][14]="poisoned"
    return pokemonorder
def pound(i,order,pokemonorder,damage):
    power=40
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def quickattack(i,order,pokemonorder,damage):
    power=40
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def rage(i,order,pokemonorder,damage):
    power=20
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    pokemonorder[i][16][0]=pokemonorder[i][16][0]+1
    pokemonorder[i][3]=int(stages(pokemonorder[i][16][1])*Stat(pokemon[pokemonorder[i][17]][3]))
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    """print int(damage),"player",pl(walk),order[i-1][0],pokemonorder[i-1][2]"""
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def razorleaf(i,order,pokemonorder,damage):
    power=55
    acc=0.95
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/256)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def rockslide(i,order,pokemonorder,damage):
    #flinching number in pokemon list
    power=75
    acc=0.9
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    """print int(damage),"player",pl(walk),order[i-1][0],pokemonorder[i-1][2]"""
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def rockthrow(i,order,pokemonorder,damage):
    power=50
    acc=0.9
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def rollingkick(i,order,pokemonorder,damage):
    #flinching number in pokemon list
    power=60
    acc=0.85
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    """print int(damage),"player",pl(walk),order[i-1][0],pokemonorder[i-1][2]"""
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def scratch(i,order,pokemonorder,damage):
    power=40
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def seismictoss(i,order,pokemonorder,damage):
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - 50
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + 50
    return pokemonorder
def selfdestruct(i,order,pokemonorder,damage):
    power=200
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    pokemonorder[i][2]=0
    return pokemonorder
def skullbash(i,order,pokemonorder,damage):
    #charge move, wait first turn
    power=130
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    pokemonorder[i][16][1]=pokemonorder[i][16][1]+1
    pokemonorder[i][4]=int(stages(pokemonorder[i][16][1])*Stat(pokemon[pokemonorder[i][17]][4]))
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    """print int(damage),"player",pl(walk),order[i-1][0],pokemonorder[i-1][2]"""
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def skyattack(i,order,pokemonorder,damage):
    #charge move, wait first turn
    power=140
    acc=0.9
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def slam(i,order,pokemonorder,damage):
    power=80
    acc=0.75
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def slash(i,order,pokemonorder,damage):
    power=70
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/256)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def spikecannon(i,order,pokemonorder,damage):
    power=20
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    times=random.randint(2,5)
    while(times!=0):
        damage=damage + raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
        times=times-1
    """print "player",pl(walk),order[i-1][0],pokemonorder[i-1][2]"""
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def stomp(i,order,pokemonorder,damage):
    power=65
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/256)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def strength(i,order,pokemonorder,damage):
    power=80
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/256)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def struggle(i,order,pokemonorder,damage):
    power=50
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/256)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def submission(i,order,pokemonorder,damage):
    power=80
    acc=0.8
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    pokemonorder[i][2]= pokemonorder[i][2] - int(pimp*0.25)
    return pokemonorder
def superfang(i,order,pokemonorder,damage):
    acc=0.9
    pimp=0
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    if Ran(acc)==1:
        pokemonorder[i-1][2]= int(0.5*pokemonorder[i-1][2])
        pimp=pokemonorder[i-1][2]
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def tackle(i,order,pokemonorder,damage):
    power=50
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/256)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def takedown(i,order,pokemonorder,damage):
    power=90
    acc=0.85
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    pokemonorder[i][2]= pokemonorder[i][2] - int(pimp*0.25)
    return pokemonorder
def thrash(i,order,pokemonorder,damage):
    #make confused
    power=120
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    pokemonorder[i][2]= pokemonorder[i][2] - int(pimp*0.25)
    return pokemonorder
def thunderpunch(i,order,pokemonorder,damage):
    power=75
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    if Ran(0.1)==1:
        pokemonorder[i-1][14]="paralyzed"
    return pokemonorder
def twineedle(i,order,pokemonorder,damage):
    power=25
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    times=2
    while(times!=0):
        damage=damage + raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
        times=times-1
    """print "player",pl(walk),order[i-1][0],pokemonorder[i-1][2]"""
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def vicegrip(i,order,pokemonorder,damage):
    power=55
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    pokemonorder[i][2]= pokemonorder[i][2] - int(pimp*0.25)
    return pokemonorder
def vinewhip(i,order,pokemonorder,damage):
    power=45
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    pokemonorder[i][2]= pokemonorder[i][2] - int(pimp*0.25)
    return pokemonorder
def waterfall(i,order,pokemonorder,damage):
    power=80
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    pokemonorder[i][2]= pokemonorder[i][2] - int(pimp*0.25)
    return pokemonorder
def wingattack(i,order,pokemonorder,damage):
    power=65
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    pokemonorder[i][2]= pokemonorder[i][2] - int(pimp*0.25)
    return pokemonorder
def wrap(i,order,pokemonorder,damage):
    power=15
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    times=random.randint(2,5)
    while(times!=0):
        damage=damage + raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
        times=times-1
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def absorb(i,order,pokemonorder,damage):
    power=20
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
        return pokemonorder
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][6]/pokemonorder[i-1][6])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    pokemonorder[i][2]= pokemonorder[i][2] +pimp/2
    return pokemonorder
def acid(i,order,pokemonorder,damage):
    power=40
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
        return pokemonorder
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][6]/pokemonorder[i-1][6])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    if Ran(0.1)==1:
        pokemonorder[i-1][16][1]=pokemonorder[i-1][16][1]-1
        pokemonorder[i-1][4]=int(stages(pokemonorder[i-1][16][1])*Stat(pokemon[pokemonorder[i-1][17]][4]))
    return pokemonorder
def aurorabeam(i,order,pokemonorder,damage):
    power=65
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
        return pokemonorder
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][6]/pokemonorder[i-1][6])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    pokemonorder[i][2]= pokemonorder[i][2] - int(pimp*0.25)
    if Ran(0.1)==1:
        pokemonorder[i-1][16][0]=pokemonorder[i-1][16][0]-1
        pokemonorder[i-1][4]=int(stages(pokemonorder[i-1][16][0])*Stat(pokemon[pokemonorder[i-1][17]][4]))
    return pokemonorder
def blizzard(i,order,pokemonorder,damage):
    power=120
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
        return pokemonorder
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    if Ran(0.1)==1:
        pokemonorder[i-1][14]="frozen"
    return pokemonorder
def bubble(i,order,pokemonorder,damage):
    power=20
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
        return pokemonorder
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][6]/pokemonorder[i-1][6])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    pokemonorder[i][2]= pokemonorder[i][2] - int(pimp*0.25)
    if Ran(0.1)==1:
        pokemonorder[i-1][16][3]=pokemonorder[i-1][16][3]-1
        pokemonorder[i-1][4]=int(stages(pokemonorder[i-1][16][3])*Stat(pokemon[pokemonorder[i-1][17]][4]))
    return pokemonorder
def bubblebeam(i,order,pokemonorder,damage):
    power=65
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
        return pokemonorder
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][6]/pokemonorder[i-1][6])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    pokemonorder[i][2]= pokemonorder[i][2] - int(pimp*0.25)
    if Ran(0.1)==1:
        pokemonorder[i-1][16][3]=pokemonorder[i-1][16][3]-1
        pokemonorder[i-1][4]=int(stages(pokemonorder[i-1][16][3])*Stat(pokemon[pokemonorder[i-1][17]][4]))
    return pokemonorder
def confusion(i,order,pokemonorder,damage):
    power=65
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
        return pokemonorder
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][6]/pokemonorder[i-1][6])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    pokemonorder[i][2]= pokemonorder[i][2] - int(pimp*0.25)
    if Ran(0.1)==1:
        dick=random.randint(1,4)
        pokemonorder[i-1][13]=dick
    return pokemonorder
def dragonrage(i,order,pokemonorder,damage):
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0
        return pokemonorder
    pimp=40*acc
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    pokemonorder[i][2]= pokemonorder[i][2] - int(pimp*0.25)
    return pokemonorder
def dreameater(i,order,pokemonorder,damage):
    power=100
    acc=0.0
    if pokemonorder[i-1][14] == "sleep":
        acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
        return pokemonorder
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][6]/pokemonorder[i-1][6])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    pokemonorder[i][2]= pokemonorder[i][2] +pimp/2
    return pokemonorder
def ember(i,order,pokemonorder,damage):
    power=40
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
        return pokemonorder
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][6]/pokemonorder[i-1][6])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    if Ran(0.1)==1:
        pokemonorder[i-1][14]="burned"
    return pokemonorder
def fireblast(i,order,pokemonorder,damage):
    power=120
    acc=0.85
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
        return pokemonorder
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][6]/pokemonorder[i-1][6])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    if Ran(0.1)==1:
        pokemonorder[i-1][14]="burned"
    return pokemonorder
def firespin(i,order,pokemonorder,damage):
    power=15
    acc=0.7
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    times=random.randint(2,5)
    while(times!=0):
        damage=damage + raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
        times=times-1
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def flamethrower(i,order,pokemonorder,damage):
    power=90
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
        return pokemonorder
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][6]/pokemonorder[i-1][6])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    if Ran(0.1)==1:
        pokemonorder[i-1][14]="burned"
    return pokemonorder
def gust(i,order,pokemonorder,damage):
    power=90
    acc=1
    if pokemonorder[i-1][8]>=1:
        acc=0.0
        return pokemonorder
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][6]/pokemonorder[i-1][6])*power)+2)
    if pokemonorder[i-1][9]>=1:
        damage=2*damage
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    if Ran(0.1)==1:
        pokemonorder[i-1][14]="burned"
    return pokemonorder
def hydropump(i,order,pokemonorder,damage):
    power=120
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
        return pokemonorder
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][6]/pokemonorder[i-1][6])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def hyperbeam(i,order,pokemonorder,damage):
    power=150
    acc=0.9
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
        return pokemonorder
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][6]/pokemonorder[i-1][6])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def icebeam(i,order,pokemonorder,damage):
    power=95
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
        return pokemonorder
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][6]/pokemonorder[i-1][6])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    if Ran(0.1)==1:
        pokemonorder[i-1][14]="frozen"
    return pokemonorder
def megadrain(i,order,pokemonorder,damage):
    power=40
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
        return pokemonorder
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][6]/pokemonorder[i-1][6])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    pokemonorder[i][2]= pokemonorder[i][2] +pimp/2
    return pokemonorder
def nightshade(i,order,pokemonorder,damage):
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0
        return pokemonorder
    pimp=50*acc
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    pokemonorder[i][2]= pokemonorder[i][2] - int(pimp*0.25)
    return pokemonorder
def petaldance(i,order,pokemonorder,damage):
    power=120
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
        return pokemonorder
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][6]/pokemonorder[i-1][6])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
        pokemonorder[i][2]= pokemonorder[i][2] - int(pimp*0.25)
    if Ran(0.35)==1:
        dick=random.randint(1,4)
        pokemonorder[i][13]=dick
    return pokemonorder
def psybeam(i,order,pokemonorder,damage):
    power=65
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
        return pokemonorder
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][6]/pokemonorder[i-1][6])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    pokemonorder[i][2]= pokemonorder[i][2] - int(pimp*0.25)
    if Ran(0.1)==1:
        dick=random.randint(1,4)
        pokemonorder[i-1][13]=dick
    return pokemonorder
def psywave(i,order,pokemonorder,damage):
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0
        return pokemonorder
    pimp=50*acc*random.randint(1,2)
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    pokemonorder[i][2]= pokemonorder[i][2] - int(pimp*0.25)
    return pokemonorder
def razorwind(i,order,pokemonorder,damage):
    #charge
    power=80
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/256)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def sludge(i,order,pokemonorder,damage):
    power=65
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    if Ran(0.3)==1:
        pokemonorder[i-1][14]="poisoned"
    return pokemonorder
def smog(i,order,pokemonorder,damage):
    power=30
    acc=70
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    if Ran(0.4)==1:
        pokemonorder[i-1][14]="poisoned"
    return pokemonorder
def solarbeam(i,order,pokemonorder,damage):
    power=120
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
    #make it wait first turn ^^^
def sonicboom(i,order,pokemonorder,damage):
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0
        return pokemonorder
    pimp=20*acc
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    pokemonorder[i][2]= pokemonorder[i][2] - int(pimp*0.25)
    return pokemonorder
def surf(i,order,pokemonorder,damage):
    power=90
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def swift(i,order,pokemonorder,damage):
    power=60
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def thunder(i,order,pokemonorder,damage):
    power=110
    acc=0.7
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    P=Ran(acc)
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(P*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    if P==1:
        if Ran(0.3)==1:
            pokemonorder[i-1][14]="paralyzed"
    return pokemonorder
def thundershock(i,order,pokemonorder,damage):
    power=40
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    if Ran(0.1)==1:
        pokemonorder[i-1][14]="paralyzed"
    return pokemonorder
def thunderbolt(i,order,pokemonorder,damage):
    power=90
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    if Ran(0.1)==1:
        pokemonorder[i-1][14]="paralyzed"
    return pokemonorder
def triattack(i,order,pokemonorder,damage):
    power=110
    acc=0.7
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    if Ran(0.2)==1:
        choose=random.randint(1,3)
        if choose ==1:
            pokemonorder[i-1][14]="paralyzed"
        if choose ==2:
            pokemonorder[i-1][14]="burned"
        if choose ==3:
            pokemonorder[i-1][14]="frozen"
    return pokemonorder
def watergun(i,order,pokemonorder,damage):
    power=40
    acc=0.7
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    return pokemonorder
def acidarmor(i,order,pokemonorder,damage):
    pokemonorder[i][16][1]=pokemonorder[i][16][1]+2
    pokemonorder[i][4]=int(stages(pokemonorder[i][16][1])*Stat(pokemon[pokemonorder[i][17]][4]))
    return pokemonorder
def agility(i,order,pokemonorder,damage):
    pokemonorder[i][16][2]=pokemonorder[i][16][2]+2
    pokemonorder[i][5]=int(stages(pokemonorder[i][16][2])*Stat(pokemon[pokemonorder[i][17]][5]))
    return pokemonorder
def amnesia(i,order,pokemonorder,damage):
    pokemonorder[i][16][3]=pokemonorder[i][16][3]+2
    pokemonorder[i][6]=int(stages(pokemonorder[i][16][2])*Stat(pokemon[pokemonorder[i][17]][6]))
    return pokemonorder
def barrier(i,order,pokemonorder,damage):
    pokemonorder[i][16][1]=pokemonorder[i][16][1]+2
    pokemonorder[i][4]=int(stages(pokemonorder[i][16][1])*Stat(pokemon[pokemonorder[i][17]][4]))
    return pokemonorder
def conversion(i,order,pokemonorder,damage):
    return pokemonorder
def defensecurl(i,order,pokemonorder,damage):
    pokemonorder[i][16][1]=pokemonorder[i][16][1]+1
    pokemonorder[i][4]=int(stages(pokemonorder[i][16][1])*Stat(pokemon[pokemonorder[i][17]][4]))
    return pokemonorder
def disable(i,order,pokemonorder,damage):
    pokemonorder[i-1][7]=["splash" if x==order[i-1][1] else x for x in pokemonorder[i-1][7]]
    return pokemonorder
def doubleteam(i,order,pokemonorder,damage):
    pokemonorder[i][16][5]=pokemonorder[i][16][5]+1
    return pokemonorder
def flash(i,order,pokemonorder,damage):
    pokemonorder[i-1][16][4]=pokemonorder[i-1][16][4]-1
    return pokemonorder
def focusenergy(i,order,pokemonorder,damage):
    return pokemonorder
def glare(i,order,pokemonorder,damage):
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    if Ran(acc)==1:
        pokemonorder[i-1][14]="paralyzed"
    return pokemonorder
def growl(i,order,pokemonorder,damage):
    pokemonorder[i-1][16][0]=pokemonorder[i-1][16][0]-1
    pokemonorder[i-1][3]=int(stages(pokemonorder[i-1][16][1])*Stat(pokemon[pokemonorder[i-1][17]][3]))
    return pokemonorder
def growth(i,order,pokemonorder,damage):
    pokemonorder[i][16][3]=pokemonorder[i][16][3]+2
    pokemonorder[i][6]=int(stages(pokemonorder[i][16][2])*Stat(pokemon[pokemonorder[i][17]][6]))
    return pokemonorder
def harden(i,order,pokemonorder,damage):
    pokemonorder[i][16][1]=pokemonorder[i][16][1]+1
    pokemonorder[i][4]=int(stages(pokemonorder[i][16][1])*Stat(pokemon[pokemonorder[i][17]][4]))
    return pokemonorder
def haze(i,order,pokemonorder,damage):
    pokemonorder[i][16]= [0,0,0,0,0,0]
    pokemonorder[i-1][16]= [0,0,0,0,0,0]
    return pokemonorder
def hypnosis(i,order,pokemonorder,damage):
    if Ran(0.6)==1:
        pokemonorder[i-1][14]="sleep"
    return pokemonorder
def kinesis(i,order,pokemonorder,damage):
    if Ran(0.8):
        pokemonorder[i-1][16][4]=pokemonorder[i-1][16][4]-1
    return pokemonorder
def leechseed(i,order,pokemonorder,damage):
    damage=pokemon[pokemonorder[i-1][17]][2]/5
    if 'grass' not in pokemonorder[i-1][0] or 'grass' not in pokemonorder[i-1][1]:
        pokemonorder[i-1][2]=pokemonorder[i-1][2] - damage
        pokemonorder[i][2]=pokemonorder[i][2] + damage
    return pokemonorder
def leer(i,order,pokemonorder,damage):
    pokemonorder[i-1][16][1]=pokemonorder[i-1][16][1]-1
    pokemonorder[i-1][4]=int(stages(pokemonorder[i-1][16][1])*Stat(pokemon[pokemonorder[i-1][17]][4]))
    return pokemonorder
def lightscreen(i,order,pokemonorder,damage):
    return pokemonorder
def lovelykiss(i,order,pokemonorder,damage):
    if Ran(0.75)==1:
        pokemonorder[i-1][14]="sleep"
    return pokemonorder
def meditate(i,order,pokemonorder,damage):
    pokemonorder[i][16][0]=pokemonorder[i][16][0]+1
    pokemonorder[i][3]=int(stages(pokemonorder[i][16][0])*Stat(pokemon[pokemonorder[i][17]][3]))
    return pokemonorder
def mimic(i,order,pokemonorder,damage):
    return pokemonorder
def minimize(i,order,pokemonorder,damage):
    pokemonorder[i][16][5]=pokemonorder[i][16][5]+2
    return pokemonorder
def mirrormove(i,order,pokemonorder,damage):
    return pokemonorder
def mist(i,order,pokemonorder,damage):
    return pokemonorder
def poisongas(i,order,pokemonorder,damage):
    acc=0.9
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    if Ran(acc)==1:
        pokemonorder[i-1][14]="poisoned"
    return pokemonorder
def poisonpowder(i,order,pokemonorder,damage):
    acc=0.75
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    if Ran(acc)==1:
        pokemonorder[i-1][14]="poisoned"
    return pokemonorder
def recover(i,order,pokemonorder,damage):
    rec= int(((random.randint(1,5))/10.0)*HP(pokemon[pokemonorder[i][17]][2]))
    if pokemonorder[i][2] + rec >= 2*rec:
        pokemonorder[i][2]= 2*rec
    elif pokemonorder[i][2] + rec < 2*rec:
        pokemonorder[i][2]= pokemonorder[i][2] + rec
    return pokemonorder
def reflect(i,order,pokemonorder,damage):
    return pokemonorder
def rest(i,order,pokemonorder,damage):
    # 2 turns
    pokemonorder[i][14]="sleep"
    pokemonorder[i][2]=pokemon[pokemonorder[i][17]][2]
    return pokemonorder
def roar(i,order,pokemonorder,damage):
    #switches poke
    return pokemonorder
def sandattack(i,order,pokemonorder,damage):
    pokemonorder[i-1][16][4]=pokemonorder[i-1][16][4]-1
    return pokemonorder
def screech(i,order,pokemonorder,damage):
    pokemonorder[i-1][16][1]=pokemonorder[i-1][16][1]-2
    pokemonorder[i-1][4]=int(stages(pokemonorder[i-1][16][1])*Stat(pokemon[pokemonorder[i-1][17]][4]))
    return pokemonorder
def sharpen(i,order,pokemonorder,damage):
    pokemonorder[i][16][0]=pokemonorder[i][16][0]+1
    pokemonorder[i][3]=int(stages(pokemonorder[i][16][0])*Stat(pokemon[pokemonorder[i][17]][3]))
    return pokemonorder
def sing(i,order,pokemonorder,damage):
    if Ran(0.55)==1:
        pokemonorder[i-1][14]="sleep"
    return pokemonorder
def sleeppowder(i,order,pokemonorder,damage):
    if Ran(0.75)==1:
        pokemonorder[i-1][14]="sleep"
    return pokemonorder
def smokescreen(i,order,pokemonorder,damage):
    pokemonorder[i-1][16][4]=pokemonorder[i-1][16][4]-1
    return pokemonorder
def softboiled(i,order,pokemonorder,damage):
    rec= int((0.5*HP(pokemon[pokemonorder[i][17]][2])))
    if pokemonorder[i][2] + rec >= 2*rec:
        pokemonorder[i][2]= 2*rec
    elif pokemonorder[i][2] + rec < 2*rec:
        pokemonorder[i][2]= pokemonorder[i][2] + rec
    return pokemonorder
def splash(i,order,pokemonorder,damage):
    return pokemonorder
def spore(i,order,pokemonorder,damage):
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    if Ran(acc)==1:
        pokemonorder[i-1][14]="sleep"
    return pokemonorder
def stringshot(i,order,pokemonorder,damage):
    pokemonorder[i][16][2]=pokemonorder[i][16][2]-2
    pokemonorder[i][5]=int(stages(pokemonorder[i][16][2])*Stat(pokemon[pokemonorder[i][17]][5]))
    return pokemonorder
def stunspore(i,order,pokemonorder,damage):
    acc=0.75
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    if Ran(acc)==1:
        pokemonorder[i-1][14]="paralyzed"
    return pokemonorder
def substitute(i,order,pokemonorder,damage):
    power=160
    acc=0.8
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    raz=random.randint(85,100)/100.0
    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
    if pokemonorder[i-1][12][0]>0:
        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
    dick=random.randint(1,4)
    pokemonorder[i][13]=dick
    return pokemonorder
def supersonic(i,order,pokemonorder,damage):
    if Ran(0.55)==1:
        if not(pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1):
            dick=random.randint(1,4)
            pokemonorder[i-1][13]=dick
    return pokemonorder
def swordsdance(i,order,pokemonorder,damage):
    pokemonorder[i][16][0]=pokemonorder[i][16][0]+2
    pokemonorder[i][3]=int(stages(pokemonorder[i][16][0])*Stat(pokemon[pokemonorder[i][17]][3]))
    return pokemonorder
def tailwhip(i,order,pokemonorder,damage):
    pokemonorder[i-1][16][1]=pokemonorder[i-1][16][1]-1
    pokemonorder[i-1][4]=int(stages(pokemonorder[i-1][16][1])*Stat(pokemon[pokemonorder[i-1][17]][4]))
    return pokemonorder
def teleport(i,order,pokemonorder,damage):
    return pokemonorder
def thunderwave(i,order,pokemonorder,damage):
    acc=1
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    if Ran(acc)==1:
        pokemonorder[i-1][14]="paralyzed"
    return pokemonorder
def toxic(i,order,pokemonorder,damage):
    acc=0.9
    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
        acc=0.0
    if Ran(acc)==1:
        pokemonorder[i-1][14]="poisoned"
    return pokemonorder
def transform(i,order,pokemonorder,damage):
    for z in [0,1,7]:
        pokemonorder[i][z]=pokemon[pokemonorder[i-1][17]][z]
    return pokemonorder
def whirlwind(i,order,pokemonorder,damage):
    return pokemonorder
def withdraw(i,order,pokemonorder,damage):
    pokemonorder[i][16][1]=pokemonorder[i][16][1]+1
    pokemonorder[i][4]=int(stages(pokemonorder[i][16][1])*Stat(pokemon[pokemonorder[i][17]][4]))
    return pokemonorder
def metronome(i,order,pokemonorder,damage):
    R=random.choice(hashy.keys())
    pokemonorder=hashy[R](i,order,pokemonorder,damage)
    return pokemonorder
def blank(i,order,pokemonorder,damage):
    return pokemonorder


#rather than doing 200 "if statments" each move....dictionary hashy uses a hash map to just point to the move going to be used
hashy={'confuseray':confuseray}
hashy['barrage']= barrage
hashy['bide']= bide
hashy['bind']= bind
hashy['bite']= bite
hashy['bodyslam']= bodyslam
hashy['boneclub']= boneclub
hashy['bonemerang']= bonemerang
hashy['clamp']= clamp
hashy['cometpunch']= cometpunch
hashy['constrict']= constrict
hashy['crabhammer']= crabhammer
hashy['cut']= cut
hashy['dig']= dig
hashy['dizzypunch']= dizzypunch
hashy['doublekick']= doublekick
hashy['doubleslap']= doubleslap
hashy['double-edge']= doubleedge
hashy['drillpeck']= drillpeck
hashy['earthquake']= earthquake
hashy['eggbomb']= eggbomb
hashy['explosion']= explosion
hashy['firepunch']= firepunch
hashy['fissure']= fissure
hashy['fly']= fly
hashy['furyattack']= furyattack
hashy['furyswipes']= furyswipes
hashy['guillotine']= guillotine
hashy['headbutt']= headbutt
hashy['highjumpkick']= highjumpkick
hashy['hornattack']= hornattack
hashy['horndrill']= horndrill
hashy['hyperfang']= hyperfang
hashy['icepunch']= icepunch
hashy['jumpkick']= jumpkick
hashy['karatechop']= karatechop
hashy['leechlife']= leechlife
hashy['psychic']=psychic
hashy['lick']=lick
hashy['lowkick']=lowkick
hashy['megakick']=megakick
hashy['payday']=payday
hashy['peck']=peck
hashy['pinmissile']=pinmissile
hashy['poisonsting']=poisonsting
hashy['pound']=pound
hashy['quickattack']=quickattack
hashy['rage']=rage
hashy['razorleaf']=razorleaf
hashy['rockslide']=rockslide
hashy['rockthrow']=rockthrow
hashy['rollingkick']=rollingkick
hashy['scratch']=scratch
hashy['seismictoss']=seismictoss
hashy['self-destruct']=selfdestruct
hashy['skullbash']=skullbash
hashy['skyattack']=skyattack
hashy['slam']=slam
hashy['slash']=slash
hashy['spikecannon']=spikecannon
hashy['stomp']=stomp
hashy['strength']=strength
hashy['struggle']=struggle
hashy['submission']=submission
hashy['superfang']=superfang
hashy['tackle']=tackle
hashy['takedown']=takedown
hashy['thrash']=thrash
hashy['thunderpunch']=thunderpunch
hashy['twineedle']=twineedle
hashy['vicegrip']=vicegrip
hashy['vinewhip']=vinewhip
hashy['waterfall']=waterfall
hashy['wingattack']=wingattack
hashy['megapunch']=megapunch
hashy['wrap']=wrap
hashy['absorb']=absorb
hashy['acid']=acid
hashy['aurorabeam']=aurorabeam
hashy['blizzard']=blizzard
hashy['bubble']=bubble
hashy['bubblebeam']=bubblebeam
hashy['confusion']=confusion
hashy['dragonrage']=dragonrage
hashy['dreameater']=dreameater
hashy['ember']=ember
hashy['fireblast']=fireblast
hashy['firespin']=firespin
hashy['flamethrower']=flamethrower
hashy['gust']=gust
hashy['counter']=counter
hashy['hydropump']=hydropump
hashy['hyperbeam']=hyperbeam
hashy['icebeam']=icebeam
hashy['megadrain']=megadrain
hashy['nightshade']=nightshade
hashy['petaldance']=petaldance
hashy['psybeam']=psybeam
hashy['psywave']=psywave
hashy['razorwind']=razorwind
hashy['sludge']=sludge
hashy['smog']=smog
hashy['solarbeam']=solarbeam
hashy['sonicboom']=sonicboom
hashy['surf']=surf
hashy['swift']=swift
hashy['thunder']=thunder
hashy['thundershock']=thundershock
hashy['thunderbolt']=thunderbolt
hashy['triattack']=triattack
hashy['watergun']=watergun
hashy['acidarmor']=acidarmor
hashy['agility']=agility
hashy['amnesia']=amnesia
hashy['barrier']=barrier
hashy['confuseray']=confuseray
hashy['conversion']=conversion
hashy['defensecurl']=defensecurl
hashy['disable']=disable
hashy['doubleteam']=doubleteam
hashy['flash']=flash
hashy['focusenergy']=focusenergy
hashy['glare']=glare
hashy['growl']=growl
hashy['growth']=growth
hashy['harden']=harden
hashy['haze']=haze
hashy['hypnosis']=hypnosis
hashy['kinesis']=kinesis
hashy['leechseed']=leechseed
hashy['leer']=leer
hashy['lightscreen']=lightscreen
hashy['lovelykiss']=lovelykiss
hashy['meditate']=meditate
hashy['mimic']=mimic
hashy['minimize']=minimize
hashy['mirrormove']=mirrormove
hashy['mist']=mist
hashy['poisongas']=poisongas
hashy['poisonpowder']=poisonpowder
hashy['recover']=recover
hashy['reflect']=reflect
hashy['rest']=rest
hashy['roar']=roar
hashy['sandattack']=sandattack
hashy['screech']=screech
hashy['sharpen']=sharpen
hashy['sing']=sing
hashy['sleeppowder']=sleeppowder
hashy['smokescreen']=smokescreen
hashy['softboiled']=softboiled
hashy['splash']=splash
hashy['spore']=spore
hashy['stringshot']=stringshot
hashy['stunspore']=stunspore
hashy['substitute']=substitute
hashy['supersonic']=supersonic
hashy['swordsdance']=swordsdance
hashy['tailwhip']=tailwhip
hashy['teleport']=teleport
hashy['thunderwave']=thunderwave
hashy['toxic']=toxic
hashy['transform']=transform
hashy['whirlwind']=whirlwind
hashy['withdraw']=withdraw
hashy['metronome']=metronome
hashy['-']=blank
hashy['']=blank
hashy[' ']=blank
hashy['switch']=blank
hashy['sw']=blank
#condition=['good',"frozen","burned","poisoned","sleeping","paralyzed"]
cons={"sleep":1}
cons["frozen"]=5
cons["burned"]=4
cons["poisoned"]=3
cons["paralyzed"]=2
cons["good"]=0
# def P1vP1 simulates a 1 v 1 pokemon battle indexA,B are the history of what moves were made represented with numbers. a,b is the list of what moves will be played next. Normally it will be 2,3 moves it will play out.
def tracker(n):
    if n%2==1:
        return -1000
    else:
        return 1000
def find_depth(total):
    rat=0
    if total<4:
        return 0
    while(True):
        if (total)%4==0:
            rat=rat+1
            total=total/4
        else:
            return rat
def randompoke(A,B,goesLast,strange,pokemon,attacks,offense,condition,themove,picked,Master1,Master2,Player1,Player2):
    #theta = np.poly1d(np.polyfit(X, y, 15))
    global GLOBAL
    STATSA=[]
    STATSB=[]
    """P1vP1(goesLast,strange,pokemon,"wigglytuff",["counter","bite","double-edge"],"paras",["explosion","bite","counter"],attacks,offense,condition)"""
    """pokemon[ 'graveler']= [ 'rock','ground',55,95,115,35,45,"""
    #NOTE: think perspective of user
    pokeA=picked
    movesA=pokemon[pokeA][7]
    pokeB=themove
    movesB=pokemon[pokeB][7]
    t1=Master1[pokeA]
    t1=t1 +[57]
    t2=Master2[pokeB]
    TAT=[]
    freqz=[0,0,0,0,0]
    # TODO: do it for bide also, but know if those lists could be used then make if statement for it so it doesnt slow down program
    del t1[-1]
    t2=t2 +[57]
    del t2[-1]
    t1[16]=t1[16]+[57]
    del t1[16][-1]
    t2[16]=t2[16]+[57]
    del t2[16][-1]
    t1[12]=t1[12]+[57]
    del t1[12][-1]
    t2[12]=t2[12]+[57]
    del t2[12][-1]
    memoryA=[pokeA,pokeA,pokeA]
    memoryB=[pokeB,pokeB,pokeB]
    indexA=[pokeA,pokeA,pokeA]
    indexB=[pokeB,pokeB,pokeB]
    level=50
    sage=[0,0]
    power=0
    dat=0
    iters=-1
    a=[]
    b=[]
    adabt=3
    while(t1[2]>0 and t2[2]>0):
        while(True):
            iters=iters+1
            pepA=t1[2]
            pepB=t2[2]
            dat=dat+1
            string1=-1
            string2=-1
            sage=[0,0]
            #a=a+[hard(0,2,15,indexB,indexA[0:len(indexA)-1],memoryB,memoryA[0:len(memoryA) -1],string2,goesLast,strange,pokemon,pokeB,movesB,pokeA,movesA,attacks,offense,condition,t2,t1,t2,t1,2,2)[0]]
            #b=b+[hard(0,2,15,indexA[0:len(indexA)-1],indexB,memoryA[0:len(memoryA) -1],memoryB,string1,goesLast,strange,pokemon,pokeA,movesA,pokeB,movesB,attacks,offense,condition,t1,t2,t1,t2,2,2)[0]]
            a=a+[A[iters]]
            b=b+[B[iters]]
            
            while((string1<1 or string1>len(movesA))):
                if (memoryA[-1]=='dig')  or (memoryA[-1]=='fly') or (memoryA[-1]=='bide') or (memoryA[-2]=='bide'and memoryA[-1]==""):
                    string1=indexA[-1]
                    a[-1]=string1
                    if (memoryA[-2]=='bide'and memoryA[-1]==""):
                        string1=indexA[-2]
                        a[-1]=string1
                    memoryA=memoryA+ [""]
                    indexA=indexA+[string1]
                    break
                else:
                    string1=a[-1]
                    string1=int(string1)
                    memoryA=memoryA+[movesA[string1-1]]
                    indexA=indexA+[string1]
            
            
            while((string2<1 or string2>len(movesB))):
                if (memoryB[-1]=='dig') or (memoryB[-1]=='fly') or (memoryB[-1]=='bide') or (memoryB[-2]=='bide'and memoryB[-1]=="") :
                    string2=indexB[-1]
                    b[-1]=string2
                    if (memoryB[-2]=='bide'and memoryB[-1]==""):
                        string2=indexB[-2]
                        b[-1]=string2
                    memoryB=memoryB + [""]
                    indexB=indexB+[string2]
                    break
                else:
                    string2=b[-1]
                    string2=int(string2)
                    indexB=indexB+[string2]
                    memoryB=memoryB+[movesB[string2-1]]
            battleA=[pokeA,movesA[string1-1]]
            battleB=[pokeB,movesB[string2-1]]
            t1[11]=indexA
            t2[11]=indexB
            acc=0
            damage=0
            walk=0
            if battleA[1] in goesLast:
                first=battleB
                last=battleA
                pokemonFirst=t2
                pokemonLast=t1
                walk=2
            #W=2
            elif battleB[1] in goesLast:
                first=battleA
                last=battleB
                pokemonFirst=t1
                pokemonLast=t2
                walk=1
            #W=1
            elif t1[5]>t2[5] :
                first=battleA
                last=battleB
                pokemonFirst=t1
                pokemonLast=t2
                walk=1
            #W=1
            elif t1[5]==t2[5]:
                decide=random.randint(0,1)
                if decide==0:
                    first=battleA
                    last=battleB
                    pokemonFirst=t1
                    pokemonLast=t2
                    walk=1
                    #W=1
                    t1[5]=t1[5] +1
                else:
                    first=battleB
                    last=battleA
                    pokemonFirst=t2
                    pokemonLast=t1
                    walk=2
                    #W=2
                    t2[5]=t2[5] +1
                    """pokemonorder[i][3]"""
            else:
                first=battleB
                last=battleA
                pokemonFirst=t2
                pokemonLast=t1
                walk=2
            #W=2
            order=[first,last]
            pokemonorder=[pokemonFirst,pokemonLast]
            if string1==5  or string2==5:
                print "PASSED1"
                if battleB[1]=="switch" and walk==1:
                    pokemonorder[1][13]=0
                    #Master2[connect2[which2]]=pokemonorder[1]
                    pokemonorder[1]=Master2[themove]
                    order[1][1]="sw"
                    t2=pokemonorder[1]
                    pokeB=themove
                    order[1][0]=pokeB
                    movesB=Player2[pokeB]
                    memoryB=[pokeB,pokeB,pokeB]
                elif battleB[1]=="switch" and walk==2 :
                    pokemonorder[0][13]=0
                    #Master2[connect2[which2]]=pokemonorder[0]
                    pokemonorder[0]=Master2[themove]
                    order[0][1]="sw"
                    t2=pokemonorder[0]
                    pokeB=themove
                    order[0][0]=themove
                    movesB=Player2[pokeB]
                    memoryB=[pokeB,pokeB,pokeB]
                if battleA[1]=="switch" and walk==1:
                    pokemonorder[0][13]=0
                    #Master1[connect1[which1]]=pokemonorder[0]
                    pokemonorder[0]=Master1[picked]
                    order[0][1]="sw"
                    t1=pokemonorder[0]
                    pokeA=picked
                    order[0][0]=pokeA
                    movesA=Player1[pokeA]
                    memoryA=[pokeA,pokeA,pokeA]
                elif battleA[1]=="switch" and walk==2:
                    pokemonorder[1][13]=0
                    #Master1[connect1[which1]]=pokemonorder[1]
                    pokemonorder[1]=Master1[picked]
                    order[1][1]="sw"
                    t1=pokemonorder[1]
                    pokeA=picked
                    order[1][0]=pokeA
                    movesA=Player1[pokeA]
                    memoryA=[pokeA,pokeA,pokeA]
            for i in range(len(order)):
                if pokemonorder[i][14] =="paralyzed":
                    pokemonorder[i][5]= 3*pokemon[pokemonorder[i][17]][5]/4
                    if Ran(0.25)==1:
                        order[i][1]="-"
            
                if pokemonorder[i][14]=="poisoned":
                    pokemonorder[i][2]=pokemonorder[i][2] - pokemon[pokemonorder[i][17]][2]/8
                
                if pokemonorder[i][14]== "burned":
                    pokemonorder[i][2]=pokemonorder[i][2] - pokemon[pokemonorder[i][17]][2]/16
                    pokemonorder[i][3]=pokemon[pokemonorder[i][17]][3]/2
                
                if  pokemonorder[i][14]== "sleep":
                    if pokemonorder[i][18]==1:
                        pokemonorder[i][18]=pokemonorder[i][18]-1
                        pokemonorder[i][14]= "good"
                    elif pokemonorder[i][18]==0 and pokemonorder[i][14]== "sleep":
                        pokemonorder[i][18]=random.randint(1,4)
                        order[i][1]="-"
                        pokemonorder[i][18]=pokemonorder[i][18]-1
                    else:
                        pokemonorder[i][18]=pokemonorder[i][18]-1
                        order[i][1]="-"
                    
                if pokemonorder[i][14]=="frozen":
                    order[i][1]="-"
                pokemonorder[i][12][0]=pokemonorder[i][12][0]-1
                pokemonorder[i][8]=pokemonorder[i][8]-1
                pokemonorder[i][9]=pokemonorder[i][9]-1
                #order[i][2]
                if pokemonorder[i][2]>0:
                    if pokemonorder[i][13]>0 and order[i][1]!="switch":
                        acc=Ran(0.5)
                        power=40
                        damage=int(acc*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i][4])*power)+2))
                        if acc==1:
                            pokemonorder[i][2]=pokemonorder[i][2]-damage
                            pokemonorder[i][13]=pokemonorder[i][13]-1
                            if pokemonorder[i-1][12][0]>0:
                                pokemonorder[i][12][1]=pokemonorder[i][12][1] +damage
                            order[i][1]="-"
                        else:
                            pokemonorder[i][13]=pokemonorder[i][13]-1
                    if pokemonorder[i][12][0]==1:
                        damage=int(2*pokemonorder[i][12][1])
                        acc=1
                        """print int(damage),"player",pl(walk),order[i-1][0],pokemonorder[i-1][2]"""
                        pokemonorder[i-1][2]= pokemonorder[i-1][2] - int(damage*Ran(acc))
                        pokemonorder[i][12][1]=0
                        pokemonorder[i][12][0]=0
                        order[i][1]="-"
                    elif pokemonorder[i][8]==1:
                        power=80
                        acc=1
                        if pokemonorder[i-1][9]>=1 or pokemonorder[i-1][8]>=1:
                            acc=0
                        raz=random.randint(85,100)/100.0
                        damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
                        """print int(damage),"player",pl(walk),order[i-1][0],pokemonorder[i-1][2]"""
                        pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
                        pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
                        pokemonorder[i][8]=0
                        if pokemonorder[i-1][12][0]>0:
                            pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
                        order[i][1]="-"
                    elif pokemonorder[i][9]==1:
                        power=80
                        acc=1
                        if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
                            acc=0
                        raz=random.randint(85,100)/100.0
                        damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
                        """print int(damage),"player",pl(walk),order[i-1][0],pokemonorder[i-1][2]"""
                        pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
                        pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
                        pokemonorder[i][9]=0
                        if pokemonorder[i-1][12][0]>0:
                            pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
                        order[i][1]="-"
                else:
                    order[i][1]="switch"
                    if walk==1:
                        memoryA[-1]="switch"
                    if walk==2:
                        memoryB[-1]="switch"
                
                pokemonorder=hashy[order[i][1]](i,order,pokemonorder,damage)
                if walk ==1:
                    t1=pokemonorder[i]
                    t2=pokemonorder[i-1]
                    walk=2
                else:
                    t1=pokemonorder[i-1]
                    t2=pokemonorder[i]
                    walk=1
                
                sage[1]=round(100*(pepB - t2[2])/(pokemon[pokeB][2]) + adabt*(1 + (pepB - t2[2])/ (pepB)),1)
                sage[0]=round(100*(pepA - t1[2])/(pokemon[pokeA][2])+ adabt*(1 + (pepA - t1[2])/ (pepA)),1)
                
                if t1[2]<=0 and t2[2]<=0:
                    t1[2]=0
                    t2[2]=0
                    sage[1]=round(100*(pepB - t2[2])/(pokemon[pokeB][2]) + adabt*(1 + (pepB - t2[2])/ (pepB)),1)
                    sage[0]=round(100*(pepA - t1[2])/(pokemon[pokeA][2])+ adabt*(1 + (pepA - t1[2])/ (pepA)),1)
                    STATSA=STATSA+[sage[0]]
                    STATSB=STATSB+[sage[1]]
                    GLOBAL=GLOBAL+[[[1],STATSA,STATSB]]
                    return 1
                if t1[2]<=0:
                    t1[2]=0
                    sage[1]=round(100*(pepB - t2[2])/(pokemon[pokeB][2]) + adabt*(1 + (pepB - t2[2])/ (pepB)) ,1)
                    sage[0]=round(100*(pepA - t1[2])/(pokemon[pokeA][2])+ adabt*(1 + (pepA - t1[2])/ (pepA)),1)
                    STATSA=STATSA+[sage[0]]
                    STATSB=STATSB+[sage[1]]
                    GLOBAL=GLOBAL+[[[0],STATSA,STATSB]]
                    return 0
                if t2[2]<=0:
                    t2[2]=0
                    sage[1]=round(100*(pepB - t2[2])/(pokemon[pokeB][2])+ adabt*(1 + (pepB - t2[2])/ (pepB)),1)
                    sage[0]=round(100*(pepA - t1[2])/(pokemon[pokeA][2])+ adabt*(1 + (pepA - t1[2])/ (pepA)),1)
                    STATSA=STATSA+[sage[0]]
                    STATSB=STATSB+[sage[1]]
                    GLOBAL=GLOBAL+[[[2],STATSA,STATSB]]
                    return 2
                t1[10]=memoryA
                t2[10]=memoryB
            if len(a)>=len(A):
                sage[1]=round(100*(pepB - t2[2])/(pokemon[pokeB][2])+ adabt*(1 + (pepB - t2[2])/ (pepB)),1)
                sage[0]=round(100*(pepA - t1[2])/(pokemon[pokeA][2])+ adabt*(1 + (pepA - t1[2])/ (pepA)),1)
                STATSA=STATSA+[sage[0]]
                STATSB=STATSB+[sage[1]]
                GLOBAL=GLOBAL+[[[1],STATSA,STATSB]]
                return 1
            
            
            STATSA=STATSA+[sage[0]]
            STATSB=STATSB+[sage[1]]
        STATSA=STATSA+[sage[0]]
        STATSB=STATSB+[sage[1]]
        GLOBAL=GLOBAL+[[[1],STATSA,STATSB]]
        return 1
def order1(n,order11):
    n=str(n)
    total=1
    for ci in range(len(n)):
        CI=-(ci+1)
        total=total + (int(n[CI])-1)*(4**ci)
    return total
def inverse_order1(n,length):
    string=""
    n=n-1
    while length>0:
        if (4**(length-1))<=n or n==1:
            sims=int(n/(4**(length-1)))
            string=string+str(sims+1)
            n=n-((int(sims))*(4**(length-1)))
        else:
            string=string+"1"
        length=length-1
    return string
def insert_turns(pol,scaler,order11,i_max,t_turns,themove,picked,Master2,Master1,Player2,Player1):
    ser=" "
    global GLOBAL
    GLOBAL=[]
    for i in range(1,(4**t_turns)+1):
        ser=str(inverse_order1(i,t_turns))
        L1=[]
        L2=[]
        c=0
        linger=[]
        for char in ser:
            c=c+1
            if c%2==0:
                L1=L1+[int(char)]
                linger=linger+[int(char)]
            else:
                L2=L2+[int(char)]
                linger=linger+[int(char)]
        randompoke(L2,L1,goesLast,strange,pokemon,attacks,offense,condition,themove,picked,Master1,Master2,Player2,Player1)
        GLOBAL[-1]=GLOBAL[-1]+[linger]
    data=np.array(GLOBAL)
    X1=data[:,1]
    X2=data[:,2]
    X3=data[:,3]
    Key={}
    for z in range(len(X1)):
        Key[order1(numberfy(X3[z]),order11)]=round(np.mean(X2[z]) - np.mean(X1[z]),1)
    y=np.array(Key.values())
    X=np.array(Key.keys())
    y=y.reshape((len(y),1))
    X=X.reshape((len(X),1))
    #if t_turns==6:
    #plt.close("all")
    #plt.plot(X,y,"ro")
    #plt.plot(X,np.poly1d(np.polyfit(X, y, 15))(X),"b")
    #plt.pause(0.0001)
    #plt.show()
    #=======set degree of poly=======
    
    
    #pol= 5
    
    
    #===============
    X=1.0*X
    X=feature_normalize(X)
    X= superpower(X,pol)
    #X = mat(X)
    y = c_[y]
    m = X.shape[0]
    
    theta=np.zeros(pol+1)
    
    theta=theta.reshape((1+pol,1))
    i=0
    #i_max=1000
    r=-computeCostMulti_df(theta,X,y)
    d=r
    delta=np.dot(r.transpose(),r)
    delta_0=delta
    curr=computeCostMulti(theta,X,y)
    prev=0
    N=np.polyfit(X[:,1], y, pol)
    N=N.transpose()[0][::-1]
    N=N.reshape(len(N),1)
    sigma=0.01
    alphastore=[sigma]
    while i<i_max:
        if i%1==0:
            prev=curr
            curr=computeCostMulti(theta,X,y)
        #print "cost at iter",i," is :", curr
        
        alpha=-sigma*(np.divide(np.dot(-r.transpose(),d),np.dot(computeCostMulti_df(theta+sigma*d,X,y).transpose(),d) - np.dot(-r.transpose(),d) +0.001)[0][0])
        #alpha=-np.divide(np.dot(-r.transpose(),d),np.dot(np.dot(d.transpose(),hessian(X)),d+0.00000001))
        alphastore=alphastore+[alpha]
        #print "alpha",alpha
        #print "sigma",sigma
        sigma=alpha
        #TT=TT.reshape(len(TT),1)
        theta=theta + alpha*d
        Dr=r
        r=-computeCostMulti_df(theta,X,y)
        beta=(np.divide(np.dot(r.transpose(),r),np.dot(Dr.transpose(),Dr)+.001)[0][0])
        #beta=max(np.divide(np.dot(r.transpose(),r-Dr),np.dot(Dr.transpose(),Dr)),0)
        d=r+beta*d
        i=i+1
    #print "cost at poly fit is : ",computeCostMulti(N,X,y)
    
    func=np.poly1d(theta.transpose()[0][::-1])
    if t_turns==9:
        plt.close("all")
        plt.plot(X[:,1],y,"ro")
        plt.plot(X[:,1],func(X[:,1]),"b")
        plt.pause(0.0001)
        plt.show()
    return [func,X[:,1]]

def hard(scale,ahead,turns_lookingahead,maxs,indexB,indexA,memoryB,memoryA,goesLast,strange,pokemon,pokeB,movesB,pokeA,movesA,attacks,offense,condition,pokemonB,pokemonA,T2,T1,life2,life1,theta):
    """game(goesLast,strange,pokemon,"wigglytuff",["double-edge","confuseray","bide","dig"],"slowbro",["double-edge","confuseray","bide","dig"],attacks,offense,condition)"""
    turns= int(turns_lookingahead*2)
    vertical= LETTERS[:(turns+1)]
    strict=vertical[-1]
    #masterhash=cookie(vertical)
    valuetracker={}
    #print "show",graph
    GL=basic(vertical)
    check=0
    total=0
    trace={}
    bomb={}
    LLL=[0]*(len(vertical)-1)
    for p in range(len(LLL)):
        LLL[p]=tracker(p)
    wine=1
    pink=0
    if turns%2==0:
        pink=1
    screen.fill(TEAL)
    pygame.display.update()
    done=False
    xy_position = (20, 20)
    dangz=-1
    bestie=0
    while int(GL[-1][1:])<=(4**(len(vertical)-1)+1):
        dangz=dangz+1
        if done==False and dangz%90==0 and ahead==0:
            event = pygame.event.poll()
            keyinput = pygame.key.get_pressed()
            # exit on corner 'x' click or escape key press
            if keyinput[pygame.K_ESCAPE]:
                raise SystemExit
            elif event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #print(event.pos)  # test
                xy_position = event.pos
            # this erases the old sreen
            # put the image on the screen at given position
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
            
            
            # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
            
            # Call draw stick figure function
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
            
            # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
            
            # First, clear the screen to white. Don't put other drawing commands
            # above this, or they will be erased with this command.
            screen.fill(TEAL)
            menu_font = pygame.font.Font(None, 40)
            P11= pokeB+" "+str(T2[2])+" / "+str(pokemon[pokeB][2])
            P12= pokeA+" "+str(T1[2])+" / "+str(pokemon[pokeA][2])
            Option(P11, (50, 90)).draw()
            Option(P12, (350, 90)).draw()
            
            Option(T2[14], (100, 260)).draw()
            Option(T1[14], (400, 260)).draw()
            
            Option(T2[10][-1], (50, 130)).draw()
            Option(memoryA[-1], (350, 130)).draw()
            options = [Option(movesB[0], (50, 400)), Option(movesB[1], (50, 450)), Option(movesB[2], (300, 400)),Option(movesB[3], (300, 450)),Option("switch", (50, 350))]
            poke_master(life2-1,life1-1)
            health_bar1(screen,170,170,T2[2],pokemon[pokeB][2])
            health_bar1(screen,400,170,T1[2],pokemon[pokeA][2])
            picachu(screen, x-5, y-3)
            screen.blit(red_square, xy_position)
            z=0
            for option in options:
                z=z+1
                if option.rect.collidepoint(xy_position):
                    option.hovered = True
                    done=True
                    Option("LOADING MOVE", (50, 50))
                    bestie=z
                    ahead=1
                else:
                    option.hovered = False
                option.draw()
            pygame.display.update()
            pygame.display.flip()
            clock.tick(60)
        check=check+1
        total=total+1
        v=GL[-1]
        prev=GL[-2]
        DD=find_depth(total-1)
        for p in range(1,DD):
            if tracker(-p+1+pink)== 1000 and LLL[-p]>LLL[-p-1]:
                LLL[-p-1]=LLL[-p]
            if tracker(-p+1+pink)== -1000 and LLL[-p]<LLL[-p-1]:
                LLL[-p-1]=LLL[-p]
            LLL[-p]=tracker(-p+1+pink)
        if int(GL[-1][1:])==(4**(len(vertical)-1)+1):
            break
        if strict==v[0]:
            value=round(theta[0](theta[1][total-1]),1)
            """health %"""
            """win %"""
            valuetracker[v]=value
            trace[valuetracker[v]]=valuetracker[v]
        
        if (( tracker(vertical.index(v[0]))==1000)):
            if LLL[-1] >= valuetracker[v]:
                check=0
                total=round4(total,4)
                trace={}
                GL[-2]=prev[0] + str(int(prev[1:])+1)
                GL[-1]=v[0] +str(round4(int(v[1:]),4)+1)
                continue
        elif ((tracker(vertical.index(v[0]))==-1000)):
            if LLL[-1] <= valuetracker[v]:
                check=0
                total=round4(total,4)
                trace={}
                GL[-2]=prev[0] + str(int(prev[1:])+1)
                GL[-1]=v[0] +str(round4(int(v[1:]),4)+1)
                continue
        if check>=4:
            if len(vertical)>2:
                check=0
                if tracker(vertical.index(v[0]))==1000:
                    valuetracker[prev]=min(trace)
                    trace={}
                    LLL[-1]=valuetracker[prev]
                    bomb[prev]=valuetracker[prev]
                    DD=find_depth(total)
                    for i in range(2,len(LLL)+1):
                        if ((tracker(-i)==-1000) and LLL[-i]>=LLL[-wine]) or ((tracker(-i)==1000) and LLL[-i]<=LLL[-wine]):
                            total=round4(total,4**(wine+1))
                            GL[-2]=prev[0] + str(round4(int(prev[1:]),4**(wine)))
                            GL[-1]=v[0] +str(round4(int(v[1:]),4**(wine+1)))
                            wine=wine+1
                        else:
                            wine=1
                            break
                
                else:
                    valuetracker[prev]=max(trace)
                    trace={}
                    LLL[-1]=valuetracker[prev]
                    bomb[prev]=valuetracker[prev]
                    DD=find_depth(total)
                    for i in range(2,len(LLL)+1):
                        if ((tracker(-i)==1000) and LLL[-i]>=LLL[-wine]) or ((tracker(-i)==-1000) and LLL[-i]<=LLL[-wine]):
                            total=round4(total,4**(wine+1))
                            GL[-2]=prev[0] + str(round4(int(prev[1:]),4**(wine)))
                            GL[-1]=v[0] +str(round4(int(v[1:]),4**(wine+1)))
                            wine=wine+1
                        else:
                            wine=1
                            break
                wine=1
        
        GL=genius(GL)
    vertical=vertical[:-1]
    check=0
    total=0
    GL=basic(vertical)
    newvaluetracker={}
    newbomb={}
    while(len(vertical))!=2:
        trace={}
        for v in sorted(bomb):
            prev=vertical[vertical.index(v[0])-1] + str(1+(int(v[1:])-1)/4)
            if newvaluetracker.get(prev)==None:
                newvaluetracker[prev]=tracker(len(vertical)+1)
            if valuetracker[v]>newvaluetracker[prev] and tracker(vertical.index(v[0]))==-1000 :
                newvaluetracker[prev]=valuetracker[v]
                newbomb[prev]=valuetracker[v]
            if valuetracker[v]<newvaluetracker[prev] and tracker(vertical.index(v[0]))==1000 :
                newvaluetracker[prev]=valuetracker[v]
                newbomb[prev]=valuetracker[v]
        vertical=vertical[:-1]
        bomb=newbomb
        valuetracker=newvaluetracker
        
        newbomb={}
        newvaluetracker={}
        if len(vertical)<=2:
            wake=-100
            themove=1
            print valuetracker
            if valuetracker.get("A1")>=wake:
                wake=valuetracker.get("A1")
                themove=1
            if valuetracker.get("A2")>=wake:
                wake=valuetracker.get("A2")
                themove=2
            if valuetracker.get("A3")>=wake:
                wake=valuetracker.get("A3")
                themove=3
            if valuetracker.get("A4")>=wake:
                wake=valuetracker.get("A4")
                themove=4
                newbomb={}
                newvaluetracker={}
            return [themove,wake,bestie]
    wake=-100
    themove=1
    print valuetracker
    if valuetracker.get("A1")>=wake:
        wake=valuetracker.get("A1")
        themove=1
    if valuetracker.get("A2")>=wake:
        wake=valuetracker.get("A2")
        themove=2
    if valuetracker.get("A3")>=wake:
        wake=valuetracker.get("A3")
        themove=3
    if valuetracker.get("A4")>=wake:
        wake=valuetracker.get("A4")
        themove=4
        newbomb={}
        newvaluetracker={}
    return [themove,wake,bestie]
def game(goesLast,strange,pokemon,attacks,offense,condition):
    #IMPORTANT FIX: fly wierd with turns game not working right fix mewtwo/snorlax game
    """game(goesLast,strange,pokemon,attacks,offense,condition)"""
    CROSS={}
    scale=0.1**4
    #TIP: for the "acc" value apply changes to evasion and accuracy of attacks for example"
    #acc=0.85*Stage(accuracy of u)*Stage(evasion of them)
    Player1={}
    Player2={}
    Master1={}
    Master2={}
    pokeB=pokemon[pokenumber[random.randint(1,26)]][17]
    pokeA=pokemon[pokenumber[random.randint(1,26)]][17]
    Player1[pokeA]=pokemon[pokeA][7]
    Player2[pokeB]=pokemon[pokeB][7]
    back=27
    for z in range(5):
        print back
        Qa=pokemon[pokenumber[random.randint(back,back+24)]][17]
        Qb=pokemon[pokenumber[random.randint(back,back+24)]][17]
        Player1[Qa]=pokemon[Qa][7]
        Player2[Qb]=pokemon[Qb][7]
        back=back+25
    
    #print Player2[pokeB]
    movesA=Player1[pokeA]
    movesB=Player2[pokeB]
    memoryA=[pokeA,pokeA,pokeA]
    memoryB=[pokeB,pokeB,pokeB]
    indexA=[pokeA,pokeA,pokeA]
    indexB=[pokeB,pokeB,pokeB]
    hurt1=""
    hurt2=""
    if len(movesA)>4 or len(movesB)>4:
        return "to many moves must be 4 or less per pokemon"
    """pokemon[ 'graveler']= [ 'rock','ground',55,95,115,35,45,"""
    for oo in Player1:
        pokemonAA=[]
        for i in range(len(pokemon[oo])):
            pokemonAA=pokemonAA +[pokemon[oo][i]]
        pokemonAA=god(pokemonAA)
        pokemonAA[10]=[oo,oo,oo]
        pokemonAA[11]=[oo,oo,oo]
        pokemonAA[12]=god([0,0])
        pokemonAA[16]=god([0,0,0,0,0,0])
        Master1[oo]=god(pokemonAA)
    for cc in Player2:
        pokemonBB=[]
        for i in range(len(pokemon[cc])):
            pokemonBB=pokemonBB +[pokemon[cc][i]]
        pokemonBB=god(pokemonBB)
        pokemonBB[10]=[cc,cc,cc]
        pokemonBB[11]=[cc,cc,cc]
        pokemonBB[12]=god([0,0])
        pokemonBB[16]=god([0,0,0,0,0,0])
        Master2[cc]=god(pokemonBB)
    turn=0
    level=50
    power=0
    T1=[]
    T2=[]
    life1=len(Player1)
    life2=len(Player2)
    T1=Master1[pokeA]
    T2=Master2[pokeB]
    screen.fill(TEAL)
    pygame.display.update()
    """for pa in Master1.keys():
        for pb in Master2.keys():
        theta=insert_turns(4,pa,pb,Master1,Master2,Player1,Player2)
        sheen=hard(1,2,10,indexA[0:len(indexA)-1],indexB,memoryA[0:len(memoryA) -1],memoryB,goesLast,strange,pokemon,pa,Player1[pa],pb,Player2[pb],attacks,offense,condition,pokemonAA,pokemonBB,Master1[pa],Master2[pb],life1,life2,theta)
        CROSS[pa+pb]=sheen[1]"""
    #TODO: figure out pre"switch" situations AND make it work with hard and game
    while(T1[2]>0 and T2[2]>0):
        T1[10]=memoryA
        T2[10]=memoryB
        screen.fill(TEAL)
        xy_position = (20,20)
        if life1==0 and life2>0:
            return "Player 2!!"
        if life2==0 and life1>0:
            return "Player 1!!"
        if life1==0 and life2==0:
            return "good tie"
        for i in range(len(movesA)):
            if (memoryA[-1]=='dig') or (memoryA[-1]=='fly') or (memoryA[-1]=='bide')or (memoryA[-2]=='bide'and memoryA[-1]==""):
                break
            print str(i+1),":",movesA[i]
        string1=-1
        string2=-1
        done=False
        eeps=False
        while((string2<1 or string2>len(movesB)+1)):
            if (memoryB[-1]=='dig' ) or (memoryB[-1]=='fly') or (memoryB[-1]=='bide') or (memoryB[-2]=='bide'and memoryB[-1]=="") :
                string2=indexB[-1]
                if (memoryB[-2]=='bide'and memoryB[-1]==""):
                    string2=indexB[-2]
                indexB=indexB+[string2]
                memoryB=memoryB + [""]
                break
            else:
                start = timeit.default_timer()
                scale=0.1**6
                theta=insert_turns(12,scale,5,1750,6,pokeA,pokeB,Master1,Master2,Player1,Player2)
                carlo=hard(scale,0,3,10,indexA[0:len(indexA)-1],indexB,memoryA[0:len(memoryA) -1],memoryB,goesLast,strange,pokemon,pokeA,movesA,pokeB,movesB,attacks,offense,condition,pokemonAA,pokemonBB,T1,T2,life1,life2,theta)
                string2=carlo[0]
                wake=carlo[1]
                SWITCH="no"
                scale=0.1**4
                for pb in Master2.keys():
                    if pb != pokeB:
                        theta=insert_turns(10,scale,4,300,4,pokeA,pb,Master1,Master2,Player1,Player2)
                        sheen=hard(scale,1,2,10,indexA[0:len(indexA)-1],indexB,memoryA[0:len(memoryA) -1],memoryB,goesLast,strange,pokemon,pokeA,Player1[pokeA],pb,Player2[pb],attacks,offense,condition,pokemonAA,pokemonBB,Master1[pokeA],Master2[pb],life1,life2,theta)
                        #CROSS[poke+pb]=sheen[1]
                        if sheen[1]>wake +20:
                            wake=sheen[1]-20
                            themove= pb
                            SWITCH="yes"
                if SWITCH=="yes" and life2>1:
                    string2=5
                #eeps=True
                if life2<2:
                    string2=carlo[0]
                stop = timeit.default_timer()
                print stop - start
                string2=int(string2)
                indexB=indexB+[string2]
                if string2<5:
                    memoryB=memoryB+[movesB[string2-1]]
                    battleB=[pokeB,movesB[string2-1],memoryB]
                else:
                    memoryB=memoryB+["switch"]
                    battleB=[pokeB,"switch",memoryB]
                    print "switch"
        while (done==False) and ((string1<1 or string1>len(movesA)+1)):
            z=0
            if carlo[2]!=0:
                bestie=carlo[2]
                print "bam",bestie
            else:
                bestie=0
            if (memoryA[-1]=='dig')  or (memoryA[-1]=='fly') or (memoryA[-1]=='bide')or (memoryA[-2]=='bide'and memoryA[-1]==""):
                string1=indexA[-1]
                if (memoryA[-2]=='bide'and memoryA[-1]==""):
                    string1=indexA[-2]
                indexA=indexA+[string1]
                memoryA=memoryA+ [""]
                break
            else:
                while not done:
                    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
                    event = pygame.event.poll()
                    keyinput = pygame.key.get_pressed()
                    # exit on corner 'x' click or escape key press
                    if keyinput[pygame.K_ESCAPE]:
                        raise SystemExit
                    elif event.type == pygame.QUIT:
                        done = True
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        #print(event.pos)  # test
                        xy_position = event.pos
                    # this erases the old sreen
                    # put the image on the screen at given position
                    
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            done = True
                    pos = pygame.mouse.get_pos()
                    x = pos[0]
                    y = pos[1]
                    screen.fill(TEAL)
                    menu_font = pygame.font.Font(None, 40)
                    P11= pokeA+" "+str(T1[2])+" / "+str(pokemon[pokeA][2])
                    P12= pokeB+" "+str(T2[2])+" / "+str(pokemon[pokeB][2])
                    Option(P11, (50, 90)).draw()
                    Option(P12, (350, 90)).draw()
                    
                    Option(T1[14], (100, 260)).draw()
                    Option(T2[14], (400, 260)).draw()
                    
                    Option(memoryA[-1], (50, 130)).draw()
                    Option(memoryB[-2], (350, 130)).draw()
                    options = [Option(movesA[0], (50, 400)), Option(movesA[1], (50, 450)), Option(movesA[2], (300, 400)),Option(movesA[3], (300, 450)),Option("switch", (50, 350))]
                    poke_master(life1-1,life2-1)
                    health_bar1(screen,170,170,T1[2],pokemon[pokeA][2])
                    health_bar1(screen,400,170,T2[2],pokemon[pokeB][2])
                    picachu(screen, x-5, y-3)
                    screen.blit(red_square, xy_position)
                    z=0
                    for option in options:
                        z=z+1
                        if option.rect.collidepoint(xy_position):
                            option.hovered = True
                            Option("LOADING MOVE", (50, 50))
                            bestie=z
                        else:
                            option.hovered = False
                        option.draw()
                    Option(hurt1, (50, 50)).draw()
                    Option(hurt2, (250, 50)).draw()
                    pygame.display.update()
                    pygame.display.flip()
                    clock.tick(60)
                    if bestie==0:
                        continue
                    if string1==5 and life1==1:
                        print "at your last poke cant switch"
                        string1=-1
                        continue
                    if string1<=5:
                        print bestie," SUPER!"
                        string1=bestie
                        
                        if string1==5:
                            Done=False
                            while not Done:
                                event = pygame.event.poll()
                                keyinput = pygame.key.get_pressed()
                                
                                if keyinput[pygame.K_ESCAPE]:
                                    raise SystemExit
                                elif event.type == pygame.QUIT:
                                    Done = True
                                elif event.type == pygame.MOUSEBUTTONDOWN:
                                    
                                    xy_position = event.pos
                                
                                
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        Done = True
                                
                                pos = pygame.mouse.get_pos()
                                x = pos[0]
                                y = pos[1]
                                screen.fill(TEAL)
                                menu_font = pygame.font.Font(None, 40)
                                options = pick(screen,pokeA,life1,Master1)
                                options= options+[Option("cancel", (500, 400))]
                                #pygame.event.pump()
                                picachu(screen, x-5, y-3)
                                screen.blit(red_square, xy_position)
                                picked=" "
                                for option in options:
                                    if option.rect.collidepoint(xy_position):
                                        option.hovered = True
                                        Done=True
                                        done=True
                                        picked=option.text
                                        if picked=="cancel":
                                            done=False
                                            string1=-1
                                            bestie=0
                                            continue
                                    else:
                                        option.hovered = False
                                    option.draw()
                                pygame.display.update()
                                pygame.display.flip()
                                clock.tick(60)
                            indexA=indexA+[string1]
                            memoryA=memoryA+["switch"]
                            battleA=[pokeA,"switch",memoryA]
                            print "switch"
                            continue
                        indexA=indexA+[string1]
                        done=True
                        memoryA=memoryA+[movesA[string1-1]]
                        battleA=[pokeA,movesA[string1-1],memoryA]
            
            if ((string1<1 or string1>len(movesA)+1)):
                print "index out of bounds try again"
        
        
        T1[11]=indexA
        T2[11]=indexB
        acc=0
        damage=0
        walk=0
        if battleA[1] in goesLast:
            first=battleB
            last=battleA
            pokemonFirst=T2
            pokemonLast=T1
            walk=2
            W=2
        elif battleB[1] in goesLast:
            first=battleA
            last=battleB
            pokemonFirst=T1
            pokemonLast=T2
            walk=1
            W=1
        elif T1[5]>T2[5] :
            first=battleA
            last=battleB
            pokemonFirst=T1
            pokemonLast=T2
            walk=1
            W=1
        elif T1[5]==T2[5]:
            decide=random.randint(0,1)
            print"tie"
            if decide==0:
                first=battleA
                last=battleB
                pokemonFirst=T1
                pokemonLast=T2
                walk=1
                W=1
                T1[5]=T1[5] +1
            else:
                first=battleB
                last=battleA
                pokemonFirst=T2
                pokemonLast=T1
                walk=2
                W=2
                T2[5]=T2[5] +1
                """pokemonorder[i][3]"""
        else:
            first=battleB
            last=battleA
            pokemonFirst=T2
            pokemonLast=T1
            walk=2
            W=2
        print first[0:2]
        print last[0:2]
        print W
        print T1[5],T1[17]
        print T2[5],T2[17]
        print "change?"
        
        
        hurt1=""
        hurt2=""
        order=[first,last]
        pokemonorder=[pokemonFirst,pokemonLast]
        turn=turn +1
        #Fix switch switch
        if string1==5  or string2==5:
            print "PASSED1"
            if battleB[1]=="switch" and walk==1:
                pokemonorder[1][13]=0
                #Master2[connect2[which2]]=pokemonorder[1]
                pokemonorder[1]=Master2[themove]
                order[1][1]="sw"
                T2=pokemonorder[1]
                pokeB=themove
                order[1][0]=pokeB
                movesB=Player2[pokeB]
                memoryB=[pokeB,pokeB,pokeB]
            elif battleB[1]=="switch" and walk==2 :
                pokemonorder[0][13]=0
                #Master2[connect2[which2]]=pokemonorder[0]
                pokemonorder[0]=Master2[themove]
                order[0][1]="sw"
                T2=pokemonorder[0]
                pokeB=themove
                order[0][0]=themove
                movesB=Player2[pokeB]
                memoryB=[pokeB,pokeB,pokeB]
            if battleA[1]=="switch" and walk==1:
                pokemonorder[0][13]=0
                #Master1[connect1[which1]]=pokemonorder[0]
                pokemonorder[0]=Master1[picked]
                order[0][1]="sw"
                T1=pokemonorder[0]
                pokeA=picked
                order[0][0]=pokeA
                movesA=Player1[pokeA]
                memoryA=[pokeA,pokeA,pokeA]
            elif battleA[1]=="switch" and walk==2:
                pokemonorder[1][13]=0
                #Master1[connect1[which1]]=pokemonorder[1]
                pokemonorder[1]=Master1[picked]
                order[1][1]="sw"
                T1=pokemonorder[1]
                pokeA=picked
                order[1][0]=pokeA
                movesA=Player1[pokeA]
                memoryA=[pokeA,pokeA,pokeA]
        superman=0
        damage=0
        for i in range(len(order)):
            
            if pokemonorder[i][14] =="paralyzed":
                pokemonorder[i][5]=3*pokemon[pokemonorder[i][17]][5]/4
                if Ran(0.25)==1:
                    order[i][1]="-"

            if pokemonorder[i][14]=="poisoned":
                pokemonorder[i][2]=pokemonorder[i][2] - pokemon[pokemonorder[i][17]][2]/8

            if pokemonorder[i][14]== "burned":
                pokemonorder[i][2]=pokemonorder[i][2] - pokemon[pokemonorder[i][17]][2]/16
                pokemonorder[i][3]=pokemon[pokemonorder[i][17]][3]/2

            if  pokemonorder[i][14]== "sleep":
                if pokemonorder[i][18]==1:
                    pokemonorder[i][18]=pokemonorder[i][18]-1
                    pokemonorder[i][14]= "good"
                elif pokemonorder[i][18]==0 and pokemonorder[i][14]== "sleep":
                    pokemonorder[i][18]=random.randint(1,4)
                    pokemonorder[i][18]=pokemonorder[i][18]-1
                    order[i][1]="-"
                else:
                    pokemonorder[i][18]=pokemonorder[i][18]-1
                    order[i][1]="-"

            if pokemonorder[i][14]=="frozen":
                order[i][1]="-"

            if superman==1:
                break
            pokemonorder[i][12][0]=pokemonorder[i][12][0]-1
            pokemonorder[i][8]=pokemonorder[i][8]-1
            pokemonorder[i][9]=pokemonorder[i][9]-1
            if pokemonorder[i][2]>0:
                if pokemonorder[i][13]>0 and order[i][1]!="sw":
                    acc=Ran(0.5)
                    power=40
                    damage=int(acc*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i][4])*power)+2))
                    if acc==1:
                        print "player ",walk," hurt itself"
                        if walk==1:
                            hurt1="player 1 hurt self"
                        if walk==2:
                            hurt2="player 2 hurt self"
                        pokemonorder[i][2]=pokemonorder[i][2]-damage
                        pokemonorder[i][13]=pokemonorder[i][13]-1
                        if pokemonorder[i-1][12][0]>0:
                            pokemonorder[i][12][1]=pokemonorder[i][12][1] +damage
                        order[i][1]="-"
                    else:
                        pokemonorder[i][13]=pokemonorder[i][13]-1
                if pokemonorder[i][12][0]==1:
                    damage=int(2*pokemonorder[i][12][1])
                    acc=1
                    """print int(damage),"player",pl(walk),order[i-1][0],pokemonorder[i-1][2]"""
                    pokemonorder[i-1][2]= pokemonorder[i-1][2] - int(damage*Ran(acc))
                    pokemonorder[i][12][1]=0
                    pokemonorder[i][12][0]=0
                    order[i][1]="-"
                elif pokemonorder[i][8]==1:
                    power=80
                    acc=1
                    if pokemonorder[i-1][9]>=1 or pokemonorder[i-1][8]>=1:
                        acc=0
                    raz=random.randint(85,100)/100.0
                    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
                    """print int(damage),"player",pl(walk),order[i-1][0],pokemonorder[i-1][2]"""
                    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
                    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
                    pokemonorder[i][8]=0
                    if pokemonorder[i-1][12][0]>0:
                        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
                    order[i][1]="-"
                elif pokemonorder[i][9]==1:
                    power=80
                    acc=1
                    if pokemonorder[i-1][8]>=1 or pokemonorder[i-1][9]>=1:
                        acc=0
                    raz=random.randint(85,100)/100.0
                    damage=raz*Is_STAB(pokemon,order[i][0],attacks,order[i][1])*typebonus(strange,pokemon,order[i-1][0],attacks,order[i][1],offense)*(((((2.0*level)+10)/250.0)*(1.0*pokemonorder[i][3]/pokemonorder[i-1][4])*power)+2)
                    """print int(damage),"player",pl(walk),order[i-1][0],pokemonorder[i-1][2]"""
                    pimp=int((1 +0.9*Ran((1.0*pokemonorder[i][5]/512)))*(Ran(acc)*damage))
                    pokemonorder[i-1][2]= pokemonorder[i-1][2] - pimp
                    pokemonorder[i][9]=0
                    if pokemonorder[i-1][12][0]>0:
                        pokemonorder[i-1][12][1]=pokemonorder[i-1][12][1] + pimp
                    order[i][1]="-"
            else:
                order[i][1]="sw"
                if walk==1:
                    memoryA[-1]="sw"
                if walk==2:
                    memoryB[-1]="sw"
            
            pokemonorder=hashy[order[i][1]](i,order,pokemonorder,damage)
            if walk ==1:
                walk=2
            else:
                walk=1
            if T1[2]<=0 and T2[2]<=0:
                print "      "
                print order[0][0],pokemonorder[0][2],"/",pokemon[order[0][0]][2]
                print order[1][0],pokemonorder[1][2],"/",pokemon[order[1][0]][2]
                superman=1
            
            
            
            
            if T1[2]<=0:
                print "      "
                print order[0][0],pokemonorder[0][2],"/",pokemon[order[0][0]][2]
                print order[1][0],pokemonorder[1][2],"/",pokemon[order[1][0]][2]
                superman=1
            
            
            if T2[2]<=0:
                print "      "
                print order[0][0],pokemonorder[0][2],"/",pokemon[order[0][0]][2]
                print order[1][0],pokemonorder[1][2],"/",pokemon[order[1][0]][2]
                superman=1
            
            
            if W==1:
                print "player 1",order[0][0],pokemonorder[0][2],"/",pokemon[order[0][0]][2]
                print "player 2",order[1][0],pokemonorder[1][2],"/",pokemon[order[1][0]][2]
            else:
                print "player 2",order[0][0],pokemonorder[0][2],"/",pokemon[order[0][0]][2]
                print "player 1",order[1][0],pokemonorder[1][2],"/",pokemon[order[1][0]][2]
            xy_position = (20,20)
            if W==1:
                T1=pokemonorder[0]
                T2=pokemonorder[1]
                Player1[pokeA]=T1[7]
                Player2[pokeB]=T2[7]
                Master1[pokeA]=T1
                Master2[pokeB]=T2
                movesA=Player1[pokeA]
                movesB=Player2[pokeB]
                if T1[2]<=0 or T2[2]<=0:
                    if T1[2]<=0 and T2[2]<=0:
                        life1=life1-1
                        life2=life2-1
                        if life2==0 and life1==0:
                            screen.fill(TEAL)
                            Option("tie", (200, 300)).draw()
                            pygame.display.update()
                            pygame.display.flip()
                            return "tie"
                        if life2==0:
                            screen.fill(TEAL)
                            Option("Player 1 wins", (200, 300)).draw()
                            pygame.display.update()
                            pygame.display.flip()
                            return "Player 1 wins"
                        if life1==0:
                            screen.fill(TEAL)
                            Option("Player 2 wins", (200, 300)).draw()
                            pygame.display.update()
                            pygame.display.flip()
                            return "Player 2 wins"
                        del Player1[order[0][0]]
                        del Master1[order[0][0]]
                        Done=False
                        while not Done:
                            event = pygame.event.poll()
                            keyinput = pygame.key.get_pressed()
                            
                            if keyinput[pygame.K_ESCAPE]:
                                raise SystemExit
                            elif event.type == pygame.QUIT:
                                Done = True
                            elif event.type == pygame.MOUSEBUTTONDOWN:
                                
                                xy_position = event.pos
                            
                            
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    Done = True
                            
                            pos = pygame.mouse.get_pos()
                            x = pos[0]
                            y = pos[1]
                            screen.fill(TEAL)
                            menu_font = pygame.font.Font(None, 40)
                            
                            
                            
                            options = pick(screen,pokeA,life1,Master1)
                            #pygame.event.pump()
                            picachu(screen, x-5, y-3)
                            screen.blit(red_square, xy_position)
                            picked=" "
                            for option in options:
                                if option.rect.collidepoint(xy_position):
                                    option.hovered = True
                                    Done=True
                                    done=True
                                    picked=option.text
                                else:
                                    option.hovered = False
                                option.draw()
                            pygame.display.update()
                            pygame.display.flip()
                            clock.tick(60)
                        pokeA=picked
                        movesA=Player1[picked]
                        T1= Master1[picked]
                        memoryA=[pokeA,pokeA,pokeA]
                        del Player2[order[1][0]]
                        del Master2[order[1][0]]
                        themove=" "
                        wake=-100
                        for mon in Player2:
                            theta=insert_turns(10,scale,4,300,4,pokeA,mon,Master1,Master2,Player1,Player2)
                            sheen=hard(scale,1,2,10,indexA[0:len(indexA)-1],indexB,memoryA[0:len(memoryA) -1],memoryB,goesLast,strange,pokemon,pokeA,Player1[pokeA],mon,Player2[mon],attacks,offense,condition,pokemonAA,pokemonBB,Master1[pokeA],Master2[mon],life1,life2,theta)
                            if sheen[1]>wake:
                                wake=sheen[1]
                                themove= mon
                        pokeB=themove
                        movesB=Player2[pokeB]
                        T2= Master2[themove]
                        memoryB=[pokeB,pokeB,pokeB]
                        print "dead tie1"
                    if T2[2]<=0:
                        life2=life2-1
                        if life2==0:
                            screen.fill(TEAL)
                            Option("Player 1 wins", (200, 300)).draw()
                            pygame.display.update()
                            pygame.display.flip()
                            return "Player 1 wins"
                        del Player2[order[1][0]]
                        del Master2[order[1][0]]
                        themove=" "
                        wake=-100
                        for mon in Player2:
                            theta=insert_turns(10,scale,4,300,4,pokeA,mon,Master1,Master2,Player1,Player2)
                            sheen=hard(scale,1,2,10,indexA[0:len(indexA)-1],indexB,memoryA[0:len(memoryA) -1],memoryB,goesLast,strange,pokemon,pokeA,Player1[pokeA],mon,Player2[mon],attacks,offense,condition,pokemonAA,pokemonBB,Master1[pokeA],Master2[mon],life1,life2,theta)
                            if sheen[1]>wake:
                                wake=sheen[1]
                                themove= mon
                        pokeB=themove
                        movesB=Player2[pokeB]
                        T2= Master2[themove]
                        memoryB=[pokeB,pokeB,pokeB]
                        print "player 2 dead"
                    if T1[2]<=0:
                        life1=life1-1
                        if life1==0:
                            screen.fill(TEAL)
                            Option("Player 2 wins", (200, 300)).draw()
                            pygame.display.update()
                            pygame.display.flip()
                            return "Player 2 wins"
                        del Player1[order[0][0]]
                        del Master1[order[0][0]]
                        Done=False
                        while not Done:
                            event = pygame.event.poll()
                            keyinput = pygame.key.get_pressed()
                            
                            if keyinput[pygame.K_ESCAPE]:
                                raise SystemExit
                            elif event.type == pygame.QUIT:
                                Done = True
                            elif event.type == pygame.MOUSEBUTTONDOWN:
                                
                                xy_position = event.pos
                            
                            
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    Done = True
                            
                            pos = pygame.mouse.get_pos()
                            x = pos[0]
                            y = pos[1]
                            screen.fill(TEAL)
                            menu_font = pygame.font.Font(None, 40)
                            
                            
                            
                            options = pick(screen,pokeA,life1,Master1)
                            #pygame.event.pump()
                            picachu(screen, x-5, y-3)
                            screen.blit(red_square, xy_position)
                            picked=" "
                            for option in options:
                                if option.rect.collidepoint(xy_position):
                                    option.hovered = True
                                    Done=True
                                    done=True
                                    picked=option.text
                                else:
                                    option.hovered = False
                                option.draw()
                            pygame.display.update()
                            pygame.display.flip()
                            clock.tick(60)
                        pokeA=picked
                        movesA=Player1[picked]
                        T1= Master1[picked]
                        memoryA=[pokeA,pokeA,pokeA]
                        print "player 1 dead"
                else:
                    pokemonorder[0][10]=memoryA
                    pokemonorder[1][10]=memoryB
                    pokemonorder[0][11]=indexA
                    pokemonorder[1][11]=indexB
                    T1=pokemonorder[0]
                    T2=pokemonorder[1]
            else:
                T1=pokemonorder[1]
                T2=pokemonorder[0]
                Player1[pokeA]=T1[7]
                Player2[pokeB]=T2[7]
                Master1[pokeA]=T1
                Master2[pokeB]=T2
                movesA=Player1[pokeA]
                movesB=Player2[pokeB]
                if T1[2]<=0 or T2[2]<=0:
                    if T1[2]<=0 and T2[2]<=0:
                        life1=life1-1
                        life2=life2-1
                        if life2==0 and life1==0:
                            screen.fill(TEAL)
                            Option("tie", (200, 300)).draw()
                            pygame.display.update()
                            pygame.display.flip()
                            return "tie"
                        if life2==0:
                            screen.fill(TEAL)
                            Option("Player 1 wins", (200, 300)).draw()
                            pygame.display.update()
                            pygame.display.flip()
                            return "Player 1 wins"
                        if life1==0:
                            screen.fill(TEAL)
                            Option("Player 2 wins", (200, 300)).draw()
                            pygame.display.update()
                            pygame.display.flip()
                            return "Player 2 wins"
                        del Player1[order[1][0]]
                        del Master1[order[1][0]]
                        Done=False
                        while not Done:
                            event = pygame.event.poll()
                            keyinput = pygame.key.get_pressed()
                            
                            if keyinput[pygame.K_ESCAPE]:
                                raise SystemExit
                            elif event.type == pygame.MOUSEBUTTONDOWN:
                                
                                xy_position = event.pos
                            
                            
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    Done = True
                            
                            pos = pygame.mouse.get_pos()
                            x = pos[0]
                            y = pos[1]
                            screen.fill(TEAL)
                            menu_font = pygame.font.Font(None, 40)
                            
                            
                            
                            options = pick(screen,pokeA,life1,Master1)
                            #pygame.event.pump()
                            picachu(screen, x-5, y-3)
                            screen.blit(red_square, xy_position)
                            picked=" "
                            for option in options:
                                if option.rect.collidepoint(xy_position):
                                    option.hovered = True
                                    Done=True
                                    done=True
                                    picked=option.text
                                else:
                                    option.hovered = False
                                option.draw()
                            pygame.display.update()
                            pygame.display.flip()
                            clock.tick(60)
                        pokeA=picked
                        movesA=Player1[picked]
                        T1= Master1[picked]
                        memoryA=[pokeA,pokeA,pokeA]
                        del Player2[order[0][0]]
                        del Master2[order[0][0]]
                        themove=" "
                        wake=-100
                        for mon in Player2:
                            theta=insert_turns(10,scale,4,300,4,pokeA,mon,Master1,Master2,Player1,Player2)
                            sheen=hard(scale,1,2,10,indexA[0:len(indexA)-1],indexB,memoryA[0:len(memoryA) -1],memoryB,goesLast,strange,pokemon,pokeA,Player1[pokeA],mon,Player2[mon],attacks,offense,condition,pokemonAA,pokemonBB,Master1[pokeA],Master2[mon],life1,life2,theta)
                            if sheen[1]>wake:
                                wake=sheen[1]
                                themove= mon
                        pokeB=themove
                        movesB=Player2[pokeB]
                        T2= Master2[themove]
                        memoryB=[pokeB,pokeB,pokeB]
                        print "dead tie2"
                    if T2[2]<=0:
                        life2=life2-1
                        if life2==0:
                            screen.fill(TEAL)
                            Option("Player 1 wins", (200, 300)).draw()
                            pygame.display.update()
                            pygame.display.flip()
                            return "Player 1 wins"
                        del Player2[order[0][0]]
                        del Master2[order[0][0]]
                        themove=" "
                        wake=-100
                        for mon in Player2:
                            theta=insert_turns(10,scale,4,300,4,pokeA,mon,Master1,Master2,Player1,Player2)
                            sheen=hard(scale,1,2,10,indexA[0:len(indexA)-1],indexB,memoryA[0:len(memoryA) -1],memoryB,goesLast,strange,pokemon,pokeA,Player1[pokeA],mon,Player2[mon],attacks,offense,condition,pokemonAA,pokemonBB,Master1[pokeA],Master2[mon],life1,life2,theta)
                            if sheen[1]>wake:
                                wake=sheen[1]
                                themove= mon
                        pokeB=themove
                        movesB=Player2[pokeB]
                        T2= Master2[themove]
                        memoryB=[pokeB,pokeB,pokeB]
                        print "player 2 dead"
                    if T1[2]<=0:
                        life1=life1-1
                        if life1==0:
                            screen.fill(TEAL)
                            Option("Player 2 wins", (200, 300)).draw()
                            pygame.display.update()
                            pygame.display.flip()
                            return "Player 2 wins"
                        del Player1[order[1][0]]
                        del Master1[order[1][0]]
                        Done=False
                        while not Done:
                            event = pygame.event.poll()
                            keyinput = pygame.key.get_pressed()
                            
                            if keyinput[pygame.K_ESCAPE]:
                                raise SystemExit
                            elif event.type == pygame.QUIT:
                                Done = True
                            elif event.type == pygame.MOUSEBUTTONDOWN:
                                
                                xy_position = event.pos
                            
                            
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    Done = True
                            
                            pos = pygame.mouse.get_pos()
                            x = pos[0]
                            y = pos[1]
                            screen.fill(TEAL)
                            menu_font = pygame.font.Font(None, 40)
                            
                            
                            
                            options = pick(screen,pokeA,life1,Master1)
                            #pygame.event.pump()
                            picachu(screen, x-5, y-3)
                            screen.blit(red_square, xy_position)
                            picked=" "
                            for option in options:
                                if option.rect.collidepoint(xy_position):
                                    option.hovered = True
                                    Done=True
                                    done=True
                                    picked=option.text
                                else:
                                    option.hovered = False
                                option.draw()
                            pygame.display.update()
                            pygame.display.flip()
                            clock.tick(60)
                        pokeA=picked
                        movesA=Player1[picked]
                        T1= Master1[picked]
                        memoryA=[pokeA,pokeA,pokeA]
                        print "player 1 dead"
                else:
                    pokemonorder[0][10]=memoryB
                    pokemonorder[1][10]=memoryA
                    pokemonorder[0][11]=indexB
                    pokemonorder[1][11]=indexA
                    T1=pokemonorder[1]
                    T2=pokemonorder[0]
for i in range(1):
    game(goesLast,strange,pokemon,attacks,offense,condition)
    time.sleep(1.5)