import matplotlib.pyplot as plt
import scatter_plot as sp
import prompt
import parallel_coordinate_plot as pcp

def entrypoint(filename):
    r = prompt.choose("Visu method ?", ['scatter plot', 'parallel coordinate plot'], 1)[0]

    if r == 0:
        sp.scatter_plot(filename)
    else:
        pcp.parallel_coordinate_plot(filename)


if __name__ == '__main__':
    entrypoint('./datasets/cars.csv')