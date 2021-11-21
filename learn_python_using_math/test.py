import matplotlib.pyplot as plt

# draw the damn graph

def draw_graph(x, y):
    plt.title('Change of Gravitational force with distance')
    plt.xlabel('Distance in meters')
    plt.ylabel('Force in Newtons')
    plt.plot(x, y, marker='o')
    plt.show()
    
# do the math
def generate_F_r():
    # define the distance
    r = range(100, 1001, 50)
    # define the two attracting mass
    m1 = 25
    m2 = 79
    # The gravitational constant
    G = 6.674*(10**-11)
    # Make an empty list to store the desired value
    F = []
    
    for dist in r:
        force = (G*m1*m2) / (dist**2)
        F.append(force)
    draw_graph(r, F)
    
if __name__ == '__main__':
    generate_F_r()