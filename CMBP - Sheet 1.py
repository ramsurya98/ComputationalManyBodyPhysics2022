
#importing packages
from subprocess import list2cmdline
from tkinter import N, OFF
from tkinter.messagebox import YES
import matplotlib.pyplot as plt
from matplotlib import colors, figure
import numpy as np



# _______________ RULE 30 CODE _______________________

def Newgeneration(numberofcells, generations):
    '''
    creates a list of lists, each represents a generation.
    '''
    # defining the conditions for rule 30:
    alivecell = [[1,0,0],[0,1,1],[0,1,0],[0,0,1]];
    deadcells = [[1,1,1],[1,1,0],[0,0,0],[1,0,1]];

    #initiating (all zero except the middle cell):
    oldgen = [0]*numberofcells
    cellinthemiddle = int(len(oldgen)/2)
    oldgen[cellinthemiddle] = 1
    endplot = [oldgen];

    # applying the rules to find out the outcome of the following generations
    for i in range(0,generations):
        newgen = []
        for i in range(0,len(oldgen)):
            if i+1<len(oldgen):
                effectivelist = [oldgen[i-1] , oldgen[i], oldgen[i+1]]
            elif i+1 == len(oldgen):
                effectivelist = [oldgen[i-1] , oldgen[i], 0]
            if effectivelist in alivecell:
                newgen.append(1)
            elif effectivelist in deadcells:
                newgen.append(0)
        oldgen = newgen
        endplot.append(newgen)
    #print(endplot)
    return endplot



def plotting(list, gridsize=[10,10]):
    '''
    takes the input the list of lists and transforms it into a grid
    '''  
    cmap = colors.ListedColormap(['white', 'blue'])
    bounds = [0,0.9]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    fig, ax = plt.subplots();
    fig.set_size_inches(gridsize);
    ax.imshow(list, cmap=cmap, norm=norm);

    # draw gridlines
    ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2);
    ax.set_xticks(np.arange(-.5, len(list[0]), 1));
    ax.set_yticks(np.arange(-.5, len(list), 1));

    plt.show()



def countcells(numberofcells, generations):
    '''
    counting the number of alive cells in each generation
    '''
    list = Newgeneration(numberofcells, generations)
    population = []
    for i in list:
        population.append(i.count(1))
    print("The number of alive celsl in each generations are as follows: ",population)



#_________________ Example Code __________________________

# example for getting the final result of rule 30 as a list:
Newgeneration(120,50)


# example for plotting the final rule 30 grid:
plotting(Newgeneration(120,50), [100,100])


# example for counting the alive cell in each generation:
countcells(120, 50)



# _______________ GAME OF LIFE CODE _______________________



# _______________ GAME OF LIFE CODE _______________________



# the rule:
def GoL_Rule(oldgenmat, index):
    '''
    Checking if the rule applies on the element index
    '''
    # getting the dimension of the matrix for the boundary condition
    Rows = len(oldgenmat)
    columns = len(oldgenmat[0])


    # getting the values of the nighbors
    # ______ getting the indices of our cell-in-question:
    rownum = index[0]
    columnum = index[1]
    # ______ Defining the step:
    left  = top = -1
    right = bottom = +1
    # ______ Getting the values of the neighboring cells:
    leftcell = (rownum , (columnum + left)%columns)
    rightcell = (rownum , (columnum + right)%columns)
    bottomcell = ((rownum + bottom)%Rows, columnum )
    topcell = ((rownum + top)%Rows, columnum )
    toprightcorner = ((rownum + top)%Rows, (columnum + right)%columns)
    topleftcorner = ((rownum + top)%Rows, (columnum + left)%columns)
    bottomrightcorner = ((rownum + bottom)%Rows, (columnum + right)%columns)
    bottomleftcorner = ((rownum + bottom)%Rows, (columnum + left)%columns)
    #_______ Creating the actual effective matrix:
    effectmat = np.array([[oldgenmat[topleftcorner],oldgenmat[topcell],oldgenmat[toprightcorner]]\
        ,[oldgenmat[leftcell], oldgenmat[index],oldgenmat[rightcell]]\
        ,[oldgenmat[bottomleftcorner],oldgenmat[bottomcell],oldgenmat[bottomrightcorner]]])

    # Getting the summation of the neighboring values
    sumneighbors = effectmat.sum() - oldgenmat[index]
    
    if oldgenmat[index] == 0:
        if sumneighbors == 3:
            state = True
        else:
            state = False
    elif oldgenmat[index] == 1:
        if sumneighbors == 3 or sumneighbors == 2:
            state = True
        else:
            state = False    
    return state




def GoL_application(configuration = [(1,3),(2,3)] ,size = (20,20),generations = 5):
    oldgenmat = np.zeros(size, dtype=int)
    
    # initilization:
    for index in configuration:
        oldgenmat[index] = 1
    
    Rows = len(oldgenmat)
    columns = len(oldgenmat[0])
    aliveindices = []
    deadindices = []
    plotting(oldgenmat, gridsize=size)
    for gen in range(1,generations):
        for i in range(0,Rows):
            for j in range(0,columns):
                if GoL_Rule(oldgenmat,(i,j)):
                    # creating a list of the affected indices
                    aliveindices.append((i,j))
                    
                else:
                    deadindices.append((i,j))
                    
        
        # changing the affected indices in the matrix
        for index in aliveindices:
            oldgenmat[index] = 1
    
            
        for index in deadindices:
            oldgenmat[index] = 0
  

        #whiping the list so it can be ready to accept the new list in the next generation.
        aliveindices.clear()
        deadindices.clear()
        plotting(oldgenmat, gridsize=size)
        




#_________________ Example Code __________________________

GoL_application(configuration=[(4,4),(4,5),(4,6),(3,5),(3,6),(3,7)],size=(10,10))

