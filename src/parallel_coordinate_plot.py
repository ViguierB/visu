import numpy as np
import matplotlib.pyplot as plt
import csv_reader

data = csv_reader.readcsv('datasets/cars.csv')

npdata = np.array(data["data"])

fig = plt.figure(figsize=[12.8, 90.6])

def plot_data_point(datapoint, fig):
    plt.plot(range(len(datapoint)), datapoint)

# d = npdata[:200]
d = npdata

for point_index in range(d.shape[0]):
    datapoint = d[point_index, :]
    plot_data_point(datapoint, fig)


labels = []
for col in data['columns']:
  labels.append(col['name'])

plt.title("parallel coordinate plot")
plt.xticks(range(len(labels)), labels=labels)
plt.savefig("parallel_coordinates.pdf")
plt.close()