
The program contains code for running an animation of a agent based model. The source code for running an agent based model is set into 
two python files, agentframework and Final Model, in (.py) format. Within the folder is also the liscence file. Within the python files
are documentation and comments, which explain what each part of the code means. The codes were witten in an object-oriented programming
language- i.e, python. Spyder IDE was used for code editing and viewing. The code development was done in Windows 10. The details of the 
code files are as follows:

###agentframework.py: This file has to be open from Spyder. It contains code to build the agents and give characters to them. A class named
'Agent' is created here and __init__ function used to pass initialize the agents for the model. The parameters set for the objects are: 
environment, agents, x and y location of agents.
The methods passed to this object gave behaviour of the agents. the function 'move' set the conditions of the agents to move, 'eat' set
the condition of feeding of the agents, the 'share_with_neighbours' functions assigned the communication of the agents. The distance between agents
were calculated using the Pythagoras' theorem.
This file has to be run once, before the FinalModel.py is run. 

###FinalModel.py: This file imports modules and packages from internal and external libraries and contain the code to pass the behaviour to the 
agents, extract values from webpage and create an animation of the model.The module created 'agentframework' is imported here. 

The file contains the code to genrate number of agents, and to extract their y and x coordinate value from a web page. The text values are 
extracted from the html using BeautifulSoup package.

The enviornment data is imported from a webpage containg raster grid values, using csv read code. The webpage link to the environment data 
is provided with the code. The environment data is appended to anenvironment list created.

The image of the environment and plot of agents in them are displayed using matplotlib. So the matplotlib is imported in to this file. 

The 'gen-function' is used to generate frames, between animation function. And 'run' function is used to run the model.

The model output is displayed in a new window. The title, and layout of this new window by using TKinter, a GUI package. The new windows 
title is set as 'Model' with a sub-tab 'Model' chowing 'Run model' option

------------------------------------------------------------------------------------------------------------------------------------
### Running the model
To run the model the FinalModel python file has to be open in Spyder. along with the agentframework, which has been already loaded. By 
pressing the 'Run@ button in main window, the model can be begun in the IPython console. 






---------------------------------------------------------------------------------------------------------------------------------
##Licence
The model code has been licenced using : MIT License

Copyright (c) 2018 Nawfee. A text file, detailing the licence terms and conditions has been attached in the model folder. 

--------------------------------------------------------------------------------------------------------------------------------------

