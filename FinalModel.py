# -*- coding: utf-8 -*-
"""
Final Model (Agent based model)
Author: Shahreen Muntaha Nawfee
Created on Tue Dec  15 14:24:25 2018

"""
#modules/packages imported 

import matplotlib #to create plot of agents  
matplotlib.use('TkAgg')
import tkinter #GUI package
import random
import matplotlib.pyplot
import agentframework #the module containg agent class, that we created
import csv  #to read environment data
import matplotlib.animation 
import matplotlib.backends.backend_tkagg #for GUI output formats
import requests
import bs4



'''Extract y and x values of agent from  html 
   
website link for y and x values are set and a package- BeautifulSoup- is used
to extract content from the html as text
'''

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text #to derive text from html
soup = bs4.BeautifulSoup(content, 'html.parser') #package to extract values
td_ys = soup.find_all(attrs={"class" : "y"}) #to get the y values from the html
td_xs = soup.find_all(attrs={"class" : "x"}) #to extract the x values from the html
print(td_ys) #shows y values of agents
print(td_xs) #shows x values of agents



'''Create agent list, set iteration number and neighbourhood ''' 
num_of_agents = 10 
num_of_iterations = 100 #iteration no. 100
neighbourhood=20 #neigbourhood radius set to 20
agents = [] #make an empty agent list 



'''Extract environment data 

in.txt file contain evironment data which is extracted to the environment list
'''
#use the CSV reading code to get environment data from in.txt and shift the data
#to a 2D list, make an environment list
with open('in.txt', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)#convert number to floats
    environment = []  #environment list
    for row in reader:#create loop to fetch data from reader, i.e, the csv file
        rowlist = []   #list of rows
        for value in row: #list of values in row
           rowlist.append(value) #add values to row list
        environment.append(rowlist) # add rowlist to the environment 



'''make a plot of the environment'''       
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()
            


'''Selecting the size of the window we get'''
fig = matplotlib.pyplot.figure(figsize=(7,7)) #the grid axis will be 7 by 7
ax = fig.add_axes([0, 0, 1, 1]) #ax.set_autoscale_on(False) 
                                #left, right, bottom and top values



'''Give environment to the agents and list of agents to each agent'''
for i in range(num_of_agents):
    y = int(td_ys[i].text)#initialise with data from web that have been extraxted
    x = int(td_xs[i].text)# initialise with data from web that have been extracted
    agents.append(agentframework.Agent(environment, agents, y, x))
    


'''creating stopping condition for the animation to reach stopping stage

The animation will carry on and update each frame as the agents move and eat 
and interact with other agents in the environment. The animation will stop 
running when the random state of 0.1 is reached. And we have print the stopping
condition which is an image showing the condition of environment and also the 
agents after reaching the stopping condition
'''
carry_on = True

def update(frame_number):#change the frames as animation runs
    
    fig.clear()
    global carry_on #the global variable set before is passed here    
#if it gets a random number mentioned it stops
    if random.random() < 0.1: #the random() function within the random module, 
                              #that generates float number betweer 0 and 1. 
            carry_on = False
            print("stopping condition") #prints the final condition of the environment
            
            
    '''Agents behaviour, movement eating and sharing condtion set  '''
    for j in range(num_of_iterations):#Move the agent number of iteration time
     for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        


    '''Create plot of agents in environment '''       
    matplotlib.pyplot.xlim(0, 99) #set the x-axis, i.e, it will go from 0 to 99
    matplotlib.pyplot.ylim(0, 99) #set the y-axis, from 0 to 99
    matplotlib.pyplot.imshow(environment) #display the image of environment
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y) #create a scatterplot of agents in the environment
    


def gen_function(b = [0]):
    '''setting condition of generating frames during animation 

    The animation keeps running until a<10        
    '''
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on == True) :
        yield a	# Returns control and waits next call.
        a = a + 1
      
 
    
def run():
    '''defined run function to generate the animation'''
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)  
    canvas.show()
    run(animation)
    
  
    
root = tkinter.Tk()      #builds the main window
'''Construct a blank window

The window gets a tkinter symbol, minimize,maximize and close button
then the window is given name, a sub window and the anmation set to run 
inside it. 
'''
root.wm_title("Model")   #setting title of the main window
#createing a matplotlib canvas within our window
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)    
#sets layout of the matplotlip canvas
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) 
#creating a menu bar in the new window
menu_bar = tkinter.Menu(root)  
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)#add menu bar in the model window
model_menu.add_command(label="Run Model", command=run)#add run model option in 

tkinter.mainloop() #to keep the window until close button is pressed