import turtle #adds turtle library

joanna = turtle.Turtle() #create the object turtle





def loop(numberofrepeats): #create function
    counter= 0
    countercolor= 0
    colorslist = ["red","blue","yellow","green"] #lists of colors for turtle
    while counter != numberofrepeats:
        joanna.forward(200)
        joanna.right(100)
        counter= counter + 1
        joanna.color(colorslist[countercolor]) #change color of turtle line 
        
        if countercolor == 3: # if the colors exceed the colors on the list, start over
            countercolor = 0
        else:
            countercolor = countercolor + 1
        
     
      

    

loop(10) #call function
