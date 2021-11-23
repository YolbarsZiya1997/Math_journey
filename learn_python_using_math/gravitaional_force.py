import matplotlib.pyplot as plt

# draw your graph 

def draw_graph(x, y):
    plt.plot(x, y, marker='o')
    plt.title('Change of gravitational force by distance')
    plt.xlabel('Distance in meters')
    plt.ylabel('Force in Newton')
    plt.show()
    
# applie the math 

def generator_F_r():
    # define the range of action
    r = range(100, 1001, 50)
    # define the constants
    m1 = 0.5
    m2 = 1.5
    G = 6.674*(10**-11)
    # make an empty list to store the value of F
    F = []
    
    for dist in r:
        force = (G*m1*m2) / (dist**2)
        F.append(force)
        
    draw_graph(r, F)
    
if __name__ == '__main__':
    generator_F_r()