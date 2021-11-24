import matplotlib.pyplot as plt
import math

# draw your graph

def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Projectile Motion')
    # put extra care here if you put the plt.show() here the code would not combine the inputs
    
def frange(start, final, increment):
    numbers = []
    
    while start < final:
        numbers.append(start)
        start = start + increment
        
    return numbers

def trajectory(u, theta):
    # define constants
    g = 9.8 
    theta = math.radians(theta)
    t_flight = (2*u*math.sin(theta)) / g
    # set the time interval
    interval = frange(0, t_flight, 0.001)
    # now for the coordinates
    x = []
    y = []
    
    for t in interval:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t - 0.5*g*t**2)
        
    draw_graph(x, y)
    
if __name__ == '__main__':
    # List of three different initial velocities
    u_list = [20, 40, 60]
    theta = 45
    for u in u_list:
        trajectory(u, theta)
    # Add a legend an show the graph
    plt.legend(['20', '40', '60'])
    plt.show()