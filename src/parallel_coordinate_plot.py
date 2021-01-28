import numpy as np
import matplotlib.pyplot as plt
import csv_reader

data = csv_reader.readcsv('datasets/cars.csv')

npdata = np.array(data["data"])

def plot_data_point(datapoint, fig):
    plt.plot(range(len(datapoint)), datapoint)

# d = npdata[:20]
d = npdata

fig = plt.figure(figsize=[12.8, len(d) * 0.9])

for point_index in range(d.shape[0]):
    datapoint = d[point_index, :]
    plot_data_point(datapoint, fig)

labels = list(map(lambda c: c['name'], data['columns']))

plt.title("parallel coordinate plot")
plt.xticks(range(len(labels)), labels=labels)
plt.savefig("parallel_coordinates.pdf")
plt.close()