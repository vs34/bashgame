import os
from pytimedinput import timedInput as Input
import random
output_stream = os.popen('tput cols')
writh=int(str(output_stream.read())[:-1])
output_stream = os.popen('tput lines')
hight=int(str(output_stream.read())[:-1])-2
os.system('tput civis      -- invisible')
space_ship=[
[' ','A',' '],
['=','+','='],
[' ','A',' ']]
space_ship_pos=[[-1 for a in range(len(space_ship[0]))] for a in range(len(space_ship))]
space=[[' ' for a in range(writh)] for a in range(hight)]
space_ship_pos=[[(int(hight/2),int(writh/2)),(int(hight/2),int(writh/2)+1),(int(hight/2),int(writh/2)+2)],[(int(hight/2)+1,int(writh/2)),(int(hight/2)+1,int(writh/2)+1),(int(hight/2)+1,int(writh/2)+2)],[(int(hight/2)+2,int(writh/2)),(int(hight/2)+2,int(writh/2)+1),(int(hight/2)+2,int(writh/2)+2)]]
i=hight
score=0

def end():
    input('boom boom')
    return
def dimintion4():
    os.system('clear')
    for a in space:
        l=''
        for b in a:
            l=l+b
        os.system('echo '+'"'+l+'"')

def metoride():
    global i,metor,metor_pos,score,safe
    if i == hight:
        metor,metor_pos,safe=[],[],[]
        lr=random.randint(3,writh-len(space_ship[0])-3)
        rl=random.randint(lr,writh)
        for a in range(writh):
            if a<=lr or a>rl:
                metor.append('8')
                metor_pos.append((0,a))
            else:
                metor.append(' ')
                metor_pos.append((0,a))
                safe.append((0,a))
            
        i,score=0,score+1
        return metor,metor_pos
    else:
        i=i+1
        for a in range(len(metor_pos)):metor_pos[a]=(metor_pos[a][0]+1,metor_pos[a][-1])
        for a in range(len(safe)):safe[a]=(safe[a][0]+1,safe[a][-1])
        return metor,metor_pos


def space_time():
    for a in range(hight):
        for b in range(writh):
           # print(space_ship_pos[0][1][0],metor_pos[0][0])
            if (a,b)==(hight-1,writh-1):space[a][b]=str(score)
            if (a,b) in metor_pos:space[a][b]=metor[b]
            if space_ship_pos[0][0][0] == metor_pos[0][0]:
                if space_ship_pos[0][1] not in safe:end()
            for c in range(len(space_ship_pos)):
                if (a,b) in space_ship_pos[c]:
                    space[a][b]=space_ship[c][space_ship_pos[c].index((a,b))]

                else:pass

# space_time()



while 1==1:
    d=Input('',timeout=0.1)[0]

    if d=='w':
        if space_ship_pos[0][0][0]-1 >= 0:
            for a in range(len(space_ship)):
                for b in range(len(space_ship[0])):
                    space_ship_pos[a][b]=(space_ship_pos[a][b][0]-1,space_ship_pos[a][b][1])

    elif d=='a':
        if space_ship_pos[0][0][-1]-3 >= 0:
            for a in range(len(space_ship)):
                for b in range(len(space_ship[0])):
                    space_ship_pos[a][b]=(space_ship_pos[a][b][0],space_ship_pos[a][b][1]-3)

    elif d=='s':
        if space_ship_pos[0][-1][0]+1 <= hight:
            for a in range(len(space_ship)):
                for b in range(len(space_ship[0])):
                    space_ship_pos[a][b]=(space_ship_pos[a][b][0]+1,space_ship_pos[a][b][1])

    elif d=='d':
        if space_ship_pos[0][-1][-1]+3 <= writh:
            for a in range(len(space_ship)):
                for b in range(len(space_ship[0])):
                    space_ship_pos[a][b]=(space_ship_pos[a][b][0],space_ship_pos[a][b][1]+3)

    
    else:pass
   # print(space_ship_pos)
    metor,metor_pos=metoride()
    dimintion4()
    space=[[' ' for a in range(writh)] for a in range(hight)]
    space_time()
   # input()


os.system('tput cnorm   -- normal')