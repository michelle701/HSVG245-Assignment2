import matplotlib.pyplot as plt
#To define the function
def plot_data():
#To open the txt file
    the_file = open('C:/Users/TAYZ/Downloads/x_y_coordinates.txt', 'r')

    x_coords = []
    y_coords = []
    the_file.readline()


    for line in the_file.readlines():
        x_coords.append(float(line.split(',')[0]))
        y_coords.append(float(line.split(',')[1]))

#To plot the coordinates
    plt.scatter(x_coords, y_coords)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

plot_data()