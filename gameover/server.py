# server

import socket
from uuid import NAMESPACE_X500
import pygame
# импортирую файл клиент
#import client
import random
import sys
import time
from threading import Thread
import database
FPS = 60
work_on_server = False
server_ip = '192.168.1.39'
#server_ip = 'localhost'
colours={'0':(255,255,0),'1':(255,0,0),'2':(0,255,0),'3':(0,255,255),'4':(128,0,128)}
main_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
main_socket.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY, 1)
main_socket.bind((server_ip,10000))
main_socket.setblocking(0)
main_socket.listen(5)      
clock = pygame.time.Clock()
path='stats.db'
table='statistics'
tick=-1
server_work=True
looking_for_pair=True
clients = 0
x_1=10
y_1=10
x_2=12
y_2=12
win_1="0"
win_2="0"
win = '0'
x_1max = 10
y_1max = 10
x_2max = 10
y_2max = 10
flag_mes_2 = False
flag_mes_1 = False
next_level = 5
first_game = 1
second_game = 0
gamerunning = '1'
new_color_1 = str(random.Random().randint(0,2))
new_color_2 = str(random.Random().randint(3,4))
flag_1 = False
flag_2 = False
IPshnik_rowid_1 = 0
IPshnik_rowid_2 = 0
while server_work:
    key_1 = '0'
    key_2 = '0'
    if looking_for_pair:
        
        tick+=1
        clock.tick(FPS)
        if tick>=200 and clients<2:
            #print('looking')
            tick=0
            #проверим, есть ли желающие войти в игру
            if clients==0:
                try:
                    new_socket_1,addr_1=main_socket.accept()
                    new_socket_1.setblocking(0)
                    clients+=1
                    #print('client 1 connected')
                    #data = new_socket_1.recv(8).decode()
                    #if data == "*":
                        #new_socket_1.send(str.encode(new_color_1 + ";" + new_color_2))
                        #print('client 1 is ready')
                    # отправляем клиенту его цвет
                    #new_socket_1.send(str(new_color).encode())
                except:
                    pass
            elif clients==1:
                try:
                    new_socket_2,addr_2=main_socket.accept()
                    #print('client 2 connected')
                    new_socket_2.setblocking(0)
                    clients += 1
                    #data = new_socket_1.recv(8).decode()
                    #if data == "*":
                        #new_socket_2.send(str.encode(new_color_2 + ";" + new_color_1))
                    # отправляем клиенту его цвет
                    #new_socket_2.send(str(new_color).encode())
                except:
                    pass
    '''try: 
        IPshnik_rowid_1=database.search_by_IP(path,table,"IP",addr_1[0])
    except:
        pass
    if not IPshnik_rowid_1 and clients >0:
            database.add_one_statsdb(path,table,addr_1[0],'1','1','0')
            IPshnik_rowid_1= addr_1[0]
    try: 
        IPshnik_rowid_2=database.search_by_IP(path,table,"IP",addr_2[0])
    except:
        pass
    if not IPshnik_rowid_2 and clients>1:
            database.add_one_statsdb(path,table,addr_2[0],'1','1','0')
            IPshnik_rowid_2= addr_2[0]'''

        
   
    if clients>=2 :
        looking_for_pair=False
    # цикл перебора клиентов
    #for i in range(clients):
    if first_game== 1:
        if ( int(y_1) >= 550) and (int(x_1) >=750):
            gamerunning='0'
            win='1'
            print('win')
            #winner_ID = IPshnik_rowid_1
            #loser_ID = IPshnik_rowid_2
            #database.update_victories(path,winner_ID)
            #database.update_losses(path,loser_ID)
            #next_level = 1
        if ( (int(y_2) >= 550) and (int(x_2) >=750)):
            gamerunning='0'
            win='2'
            #next_level = 1
            print('win')
            #winner_ID = IPshnik_rowid_2
            #loser_ID = IPshnik_rowid_1
            #database.update_victories(path,winner_ID)
            #database.update_losses(path,loser_ID)
        #print(x_1,y_1)
        # цикл по четырем клиентам
        for i in range(3):
            try:
                data = new_socket_1.recv(64).decode()
                #print(data)
                if ";" in data:
                
                    # получаем координыты первого клиента x_1 и y_1
                    x_1, y_1 = data.split(";")
                    #print('client 1 send coordinate')
                    # отсылаем 1 клиенту координаты второго 
                    new_socket_1.send(str.encode(str(x_2) + ";" + str(y_2)))
                if '#' in data:
                    deaths_1 = int(data.split('#')[0])
                if  '?' in data:
                    new_socket_1.send(str.encode(str(gamerunning)+";"+str(next_level)))
                    print('client 1 ', gamerunning, next_level)
                    if next_level==1 or  next_level==0:
                        flag_1 = True
                
           
                
            except:
                pass
            try:
                data = new_socket_2.recv(512).decode()
                if ";" in data:
                
       
                    # получаем координыты первого клиента x_2 и y_2
                    x_2, y_2 = data.split(";")
                    #print('client 2 send coordinate')
                    # отсылаем 2 клиенту координаты первого
                    new_socket_2.send(str.encode(str(x_1) + ";" + str(y_1)))
                if '?' in data:
                    new_socket_2.send(str.encode(str(gamerunning)+";"+str(next_level)))
                    print('client 2', gamerunning, next_level)
                    if next_level==1 or  next_level==0:
                        flag_2 = True
                if '#' in data:
                    deaths_2 = int(data.split('#')[0])
                
            except:
                pass
        
        x_win = 770
        y_win = 10
        if ((x_win-int(x_1))**2 + (y_win - int(y_1))**2)**(0.5) < ((x_win-x_1max)**2 + (y_win - y_1max)**2)**(0.5):
            x_1max = int(x_1)
            y_1max = int(y_1)
        if ((x_win-int(x_2))**2 + (y_win - int(y_2))**2)**(0.5) < ((x_win-x_2max)**2 + (y_win - y_2max)**2)**(0.5):
            x_2max = int(x_2)
            y_2max = int(y_2)
        if (next_level == 1 or next_level == 0) and flag_1 and flag_2:
            first_game = 0   
        if (next_level == 1) and gamerunning == '0':
            second_game = 1
            gamerunning = '1'
        if gamerunning == '0':
            #print('game over')
            print('deaths_1', deaths_1)
            print('deaths_2', deaths_2)
            rating_1 = (1/(deaths_1+1)+(1000/((x_win-x_1max)**2 + (y_win - y_1max)**2)**(0.5))) 
            print(rating_1)
            rating_2 =1/(deaths_2+1)+(1000/(((x_win-x_2max)**2 + (y_win - y_2max)**2)**(0.5)))
            print(rating_2)
            '''final_rating_1 = 0
            final_rating_2 = 0
            final_rating_1 = database.take_rating(path,table,'rowid',str(IPshnik_rowid_1))
            final_rating_2 = database.take_rating(path,table,'rowid',str(IPshnik_rowid_2))
            final_rating_1 = (final_rating_1 + rating_1) / 2
            final_rating_2 = (final_rating_2 + rating_2) / 2
            database.update_rating(path,final_rating_1,IPshnik_rowid_1)
            database.update_rating(path,final_rating_2,IPshnik_rowid_2)'''
            if win == '1' and rating_1>rating_2:
                next_level = 0 
            elif win == '2' and rating_2>rating_1:
                next_level = 0
            else:
                next_level = 1
        
            
                
    if second_game == 1:
        try:
            data = new_socket_1.recv(512).decode()
            #print(data)
            if ";" in data:
                
                # получаем координыты первого клиента x_1 и y_1
                x_1, y_1 = data.split(";")
                #print('client 1 send coordinate')
                # отсылаем 1 клиенту координаты второго 
                new_socket_1.send(str.encode(str(x_2) + ";" + str(y_2)))
            if  '?' in data:
                new_socket_1.send(str.encode(str(gamerunning)))
                
        except:
            pass
        try:
            data = new_socket_2.recv(512).decode()
            if ";" in data:
                
       
                # получаем координыты первого клиента x_2 и y_2
                x_2, y_2 = data.split(";")
                #print('client 2 send coordinate')
                # отсылаем 2 клиенту координаты первого
                new_socket_2.send(str.encode(str(x_1) + ";" + str(y_1)))
            if '?' in data:
                new_socket_2.send(str.encode(str(gamerunning)))
                
        except:
            pass
        # 
        x_win = 770
        y_win = 10
        if ((x_win-int(x_1))**2 + (y_win - int(y_1))**2)**(0.5) < ((x_win-x_1max)**2 + (y_win - y_1max)**2)**(0.5):
            x_1max = int(x_1)
            y_1max = int(y_1)
        if ((x_win-int(x_2))**2 + (y_win - int(y_2))**2)**(0.5) < ((x_win-x_2max)**2 + (y_win - y_2max)**2)**(0.5):
            x_2max = int(x_2)
            y_2max = int(y_2)
        
        if ( int(y_1) >= 550) and (int(x_1) >=750):
            gamerunning='0'
            win_1='1'
            win_2='0'

        if ( (int(y_2) <= 555) and (int(x_2) >=750)):
            gamerunning='0'
            win_2='1'
            win_1='0'

        
    
        
    
          
      

             
             
            
            