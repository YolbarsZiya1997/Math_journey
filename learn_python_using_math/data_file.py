def sum_data(filename):
    s = 0
    
    with open(filename) as f:
        for line in f:
            s = s + float(line)
    print('Sum of the numbers: {0}'.format(s))
    
if __name__ == '__main__':
    sum_data('D:\Math_journey\learn_python_using_math\mydata.txt')