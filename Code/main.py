import random as rn
import pygame as py
import time
import math
py.init()

window_size = (800, 800)
#Create the window
screen = py.display.set_mode(window_size)
#Set the title of the window
py.display.set_caption("Jump test")

# basic font for user typed 
base_font = py.font.Font(None, 32) 
user_text = '' 
  
# create rectangle 
input_rect = py.Rect(200, 200, 400, 32) 
  
# color_active stores color(lightskyblue3) which 
# gets active when input box is clicked by user 
color_active = py.Color((47, 200, 255)) 
  
# color_passive store color(chartreuse4) which is 
# color of input box. 
color_passive = py.Color((200, 255, 47)) 
color = color_passive 
  
active = False
running = True
while running == True:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
            exit() 
        if event.type == py.MOUSEBUTTONDOWN: 
            if input_rect.collidepoint(event.pos): 
                active = True
            else: 
                active = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                running = False
                exit()
            if event.key == py.K_TAB:
                pass
            # Check for backspace 
            if event.key == py.K_BACKSPACE: 
  
                # get text input from 0 to -1 i.e. end. 
                user_text = user_text[:-1] 
  
            # Unicode standard is used for string 
            # formation 
            else:
                if(len(user_text)<=100):
                    user_text += event.unicode
    #filling the background
    screen.fill((90,50,100)) 
    try:
        myimage = py.image.load("Languages\\" + user_text + ".png").convert_alpha()
        py.draw.rect(screen, (100, 200, 100), (10, 10, 20,20))  
        image_width = myimage.get_width()
        image_height= myimage.get_height()
        while((image_width>600)|(image_height>536)):
            
            if(image_width>600):
                image_width = image_width /1.25

                image_height = image_height /1.25
            if(image_height>536):
                image_width = image_width /1.25

                image_height = image_height /1.25
            
        myimage = py.transform.smoothscale(py.image.load("Languages\\" + user_text + ".png").convert_alpha(),(image_width,image_height))    
        print(str(image_height))    
        #myimage = py.transform.smoothscale(py.image.load("Languages\\" + user_text + ".png").convert_alpha(),(600,536))
        screen.blit(myimage, (100,input_rect.y+2*input_rect.height))  
    except:
        pass
    
    if active: 
        color = color_active 
    else: 
        color = color_passive 
    py.draw.rect(screen, (255, 200, 47), (input_rect.x-5, input_rect.y-5, input_rect.width+10,input_rect.height+10))            
    # draw rectangle and argument passed which should 
    # be on screen 
    py.draw.rect(screen, color, input_rect)
    
    
    text_surface = base_font.render(user_text, True, (255, 255, 255)) 
      
    # render at position stated in arguments 
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5)) 
      
    # set width of textfield so that text cannot get 
    # outside of user's text input 
    input_rect.w = max(100, text_surface.get_width()+10) 
     
    # display.flip() will update only a portion of the 
    # screen to updated, not full area 
    py.display.flip() 

    #py.display.update()

#Initialize py
py.init()