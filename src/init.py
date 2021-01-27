import matplotlib.pyplot as plt
import pandas as pd

def choose_elements(columns):
    size = len(columns)
    for i, element in enumerate(columns):
        print(i, element)
    line = ""
    val1 = -1
    val2 = -1
    print("Choose 2 parameter:")
    while (line != "exit"):
        line = input()
        if (int(line) < size and int(line) > -1):
            if (val1 == -1):
                val1 = int(line)
            else:
                val2 = int(line)
                break
        else:
            print("Choose a correct number")
    return columns[val1], columns[val2]


def scatter_plot(df, parameter1, parameter2):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(x = df[parameter1], y = df[parameter2])
    plt.xlabel(parameter1)
    plt.ylabel(parameter2)
    plt.show()

df = pd.read_csv('../datasets/cars.csv', sep=r'\s*;\s*',
                        header=0, encoding='ascii', engine='python')
columns = df.columns
val1 , val2 = choose_elements(columns)
print(val1, val2)
scatter_plot(df, val1, val2)
