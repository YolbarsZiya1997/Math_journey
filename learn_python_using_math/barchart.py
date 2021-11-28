import matplotlib.pyplot as plt

# draw your graph first
def create_bar_chart(data, labels):
    # number of bar charts
    num_bars = len(data)
    # This list s the point on the y-axis where each
    # bar is centered. Here it will be [1, 2, 3...]
    positions = range(1, num_bars + 1)
    plt.barh(positions, data, align='center')
    # Set the label of each bar
    plt.yticks(positions, labels)
    plt.xlabel('Amount ($)')
    plt.ylabel('Category')
    plt.title('Weekly expenditures')
    plt.grid()
    plt.show()
    
if __name__ == '__main__':
    n = int(input('Enter the number of categories. '))
    
    categories = []
    expenditures = []
    
    for i in range(n):
        category = input('Enter the category: ')
        expenditure = float(input('Enter the amount: '))
        
        categories.append(category)
        expenditures.append(expenditure)
        
    create_bar_chart(expenditures, categories)