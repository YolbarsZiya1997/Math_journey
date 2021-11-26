import matplotlib.pyplot as plt
import math 

g = 9.8

# draw your graph 
def draw_graph(x,y):
    plt.plot(x, y)
    plt.xlabel("x-coordinate")
    plt.ylabel("y-coordinate")
    plt.title('Projectile Motion of A ball')
    
# set the floating range
def frange(start, final, increment):
    numbers = []
    while start < final:
        numbers.append(start)
        start = start + increment
        
    return numbers

def draw_trajectory(u, theta, t_flight):
    # define interval
    interval = frange(0, t_flight, 0.001)
    x = []
    y = []
    
    for t in interval:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t - 0.5*g*t**2)
    
    # draw the graph    
    draw_graph(x, y)
    
if __name__ == '__main__':
    num_trajectories = int(input("How many trajectories: "))
    
    velocities = []
    angles = []
    for i in range(1, num_trajectories + 1):
        v = input('Enter the initial velocity for trajectory {0} (m/s): '.format(i))
        theta = input('Enter the angle of projection for trajectory {0} (degrees): '.format(i))
        velocities.append(float(v))
        angles.append(math.radians(float(theta)))
        
    for i in range(num_trajectories):
        # Calculate the time of flight, maximum horizontal distance and 
        # maximum vertical distance
        t_flight = 2*velocities[i]*math.sin(angles[i]) / g
        S_x = velocities[i]*math.cos(angles[i])*t_flight
        S_y = velocities[i]*math.sin(angles[i])*(t_flight/2) - 0.5*g*(t_flight/2)**2
        print('Initial velocity : {0} Angle of projection: {1}'. format(velocities[i], angles[i]))
        print('T : {0}, S_x: {1}, S_y: {2}'.format(t_flight, S_x, S_y))
        print()
        draw_trajectory(velocities[i], angles[i], t_flight)
        
    # Add a legend and show the graph 
    legends = []
    for i in range(0, num_trajectories):
        legends.append('{0} - {1}'.format(velocities[i], math.degrees(angles[i])))
    plt.legend(legends)
    plt.show()       