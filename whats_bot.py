from pyautogui import *
import pyautogui
import time
import random
#import keyboard


def take_shot(x,y,w,h):
    #left top width and height

    ret_dic ={
            "width": 0,
            "height": 0
    }

    #DEBUGGING#screenshot = pyautogui.screenshot('region_shot.png', region=(x,y,w,h))

    screenshot = pyautogui.screenshot(region=(x,y,w,h))
    
    width, height = screenshot.size

    ret_dic["width"] = width
    ret_dic["height"] = height

    return(ret_dic)

def send_msg(msg_x, msg_y):Hi, this is Whats_Bot

    
    pyautogui.click(msg_x, msg_y)

    pyautogui.write('Hi, this is Whats_Bot')

    pyautogui.press('enter')

    #print("\nclicked, wrote, and pressed enter in function\n")
    

#send_msg ends here

def main():
    #it is necessary to change these variables to take the appropriate screenshot and click in the correct place
    #since a different screen size can mess the bot up. 
    #(Reminder: Make a bot that resizes to standard computer screen sizes)
    region_x = 0
    region_y = 0
    region_w = 0
    region_h = 0
    inputbox_x = 0
    inputbox_y = 0
    chat_shot_x = 0
    chat_shot_y = 0
    chat_shot_w = 0
    chat_shot_h = 0

    temp_dic = {
            "w": 0,
            "h": 0
    }

    #a try and catch statement was used cause the program is closed using ctrl-c
    #originally it's supposed to use the keyboard module but there were issues getting it to work
 
    try:
        while True:
            
            time.sleep(30) #sleep for 30 sec to not overtax the program
            
            screenshot = pyautogui.screenshot(region=(region_x, region_y, region_w, region_h))

            width, height = screenshot.size

            '''
            Loop where the program iterates by every 5 pixels searching for a recieved message.
            It does it by every 5 pixels to speed up the process a little.
            Note: This can be sped up more if the size of the screen shot is reduced. (Do later)
            '''

            for iter_x in range(0,width,5):

                for iter_y in range(0,height,5):

                    r,g,b = screenshot.getpixel((iter_x,iter_y))
            
                    if((g == 215) and (b == 85)):
                        #pyautogui.moveTo(((iter_x + region_x) - 50),(iter_y + region_y))
                        
                        pyautogui.click(((iter_x + region_x) - 50),(iter_y + region_y))

                        #print("\nClicked in the loop\n")#DEBUGGING
                        
                        send_msg(inputbox_x, inputbox_y)

                        #print("msg sent at X: " + str(iter_x + region_x) + ", Y: " + str(iter_y + region_y))#DEBUGGING

                        height = 0 # used to break out of the innermost loop.

                        width = 0 # used to break out of the outermost loop

                        break # this is just a redundancy that also breaks out of the innermost loop.

            #ends the first double for loop
    
            #the following lines are used to reply to a message where whats_bot is already in. It's also a failsafe in case the loop from above messes up.
            screenshot = pyautogui.screenshot('reply_chat.png', region=(chat_shot_x, chat_shot_y, chat_shot_w, chat_shot_h))
            
            r,g,b = screenshot.getpixel((2,1))

            #print("\nred: "+ str(r) + ", blue: " + str(b) + "\n")

            if((r == 255)  and (b == 255) ):

                send_msg(inputbox_x, inputbox_y)
            
    except KeyboardInterrupt:
        print("\nWhats_bot is done working.\n")


#main ends here

main()
