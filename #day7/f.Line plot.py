# importing the required module
import matplotlib . pyplot as plt
x = [1 ,2 ,3 ,4 ,6 ,7 , 8] # x axis values
y = [2 ,7 ,9 ,1 ,5 , 10 , 3] # corresponding y axis values
plt . plot (x , y , 'r+--') # plotting the points
plt . xlabel ('x - axis ') # naming the x axis
plt . ylabel ('y - axis ') # naming the y axis
plt . title ('My first graph !') # giving a title to my graph
plt . show () # function to show the plot