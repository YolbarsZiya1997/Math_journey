import matplotlib.pyplot as plt
import math

# draw your graph 

def draw_graph(x, y):
    plt.plot(x, y)
    plt.title('Projectile Motion')
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.show()
 
# for the floating time interval   
def frange(start, final, increment):
    
    numbers = []
    while start < final:
        numbers.append(start)
        start = start + increment
    
    return numbers

# now applie math

def draw_trajectory(u, theta):
    theta = math.radians(theta)
    g = 9.8
    
    #airborne duration
    t_flight = 2*u*math.sin(theta)/g
    # define the interval 
    intervals = frange(0, t_flight, 0.001)
    #make empty list for the coordinates
    x = []
    y = []
    
    for t in intervals:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t - 0.5*g*t**2)
        
    draw_graph(x, y)
    
#if __name__ == '__main__':
    #u = float(input('Enter the initial velocity: '))
    #theta = float(input('The initial angle: '))
    #draw_trajectory(u, theta)
if __name__ == '__main__':
    u_list = [40, 60, 80]
    theta = 45
    for u in u_list:
        draw_trajectory(u, theta)
    plt.legend(['40', '60', '80'])
    plt.show()