from matplotlib import pyplot as plt
import math

def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x-coordinates')
    plt.ylabel('y-coordinates')
    plt.title('Projectile motion of a ball')
    
def frange(start, final, increment):
    
    numbers = []
    while start < final:
        numbers.append(start)
        start = start + increment
        
    return numbers

def draw_trajectory(u, theta):
    theta = math.radians(theta)
    g = 9.8
    
    # Time of flight 
    t_fight = 2*u*math.sin(theta)/g
    # Find the time intervals
    intervals = frange(0, t_fight, 0.001)
    # List of x and y coordinates
    x = []
    y = []
    for t in intervals:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t - 0.5*g*t*t)
        
    draw_graph(x, y)
    

        
if __name__ == '__main__':
    # List of three different initial velocities
    u_list = [20, 40, 60]
    theta = 45
    for u in u_list:
        draw_trajectory(u, theta)
    # Add a legend an show the graph
    plt.legend(['20', '40', '60'])
    plt.show()