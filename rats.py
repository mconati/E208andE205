import numpy as np
import argparse
import math

def nCr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

def maxBottlesHelper(r,t,visited):
    if visited[r-1,t-1] != -1:
        return visited[r-1,t-1]
    else:
        temp = 1
        for x in range(1, r+1):
            temp += nCr(r, r-x) * maxBottlesHelper(x, t-1, visited)
        visited[r-1, t-1] = temp
        return visited[r-1, t-1]

def maxBottles(parser, r=0, t=0):
    if parser!=None:
        args = parser.parse_args()
        r, t = int(args.r), int(args.t)
    visited = np.ones((r,t)) * -1
    visited[:, 0] = np.power(np.ones(r)*2, (np.arange(r)+1))
    visited[0,:] = np.arange(t)+2
    visited[r-1,t-1] = maxBottlesHelper(r,t,visited)
    return visited[r-1,t-1]


#Maybe next time
def maxBottlesWithMultiPoison(parser):
    args = parser.parse_args()
    r, t, p = int(args.r), int(args.t), int(args.p)
    return


def plotContour():
    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib.pyplot as plt
    import numpy as np
    r, t = 4, 6
    visited = np.ones((r,t)) * -1
    for x in range(1, r+1):
        for y in range(1, t+1):
            visited[x-1, y-1] = maxBottles(None, x, y)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
 
    x_data, y_data = np.meshgrid( np.arange(visited.shape[1]),
                                np.arange(visited.shape[0]) )

    x_data = x_data.flatten()
    y_data = y_data.flatten()
    z_data = visited.flatten()
    ax.bar3d( x_data,
            y_data,
            np.zeros(len(z_data)),
            1, 1, z_data )

    ax.set_ylabel('Rats')
    ax.set_xlabel('Timesteps')
    ax.set_zlabel('Max Bottles Checked')
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "-rats", dest='r', default = 2, help = "number of rats")
    parser.add_argument("-b", "-bottles", dest='b', default = False, help = "number of bottles")
    parser.add_argument("-p", "-poisoned", dest='p', default = 1, help = "number of poisoned bottles")
    parser.add_argument("-t", "-time periods", dest='t', default = 3, help = 'number of feedings')
    parser.add_argument("-plot", dest="plot", default=False, help = 'set this true to plot a bunch of things instead')
   
    if parser.parse_args().plot != False:
        plotContour()
    elif parser.parse_args().b==False and parser.parse_args().p==1:
        print("There can be {} max bottles!".format(maxBottles(parser)))
    else:
        #Todo maybe
        print(maxBottlesWithMultiPoison(parser))