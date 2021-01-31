import numpy as np
import matplotlib.pyplot as plt
import csv_reader
import prompt



def parallel_coordinate_plot(filename):
  data = csv_reader.readcsv(filename)
  npdata = np.array(data["data"])

  def plot_data_point(datapoint):
      plt.plot(range(len(datapoint)), datapoint)

  print(f"data len: {npdata.shape[0]}")
  section_str = input("Choose a section 'start:stop:step' ex: 10:100:10 (empty -> entire data)\n")
  if not section_str:
    d = npdata
  else:
    section = list(map(lambda n: int(n), section_str.split(':')))
    d = npdata[slice(section[0], section[1], section[2])]

  labels = list(map(lambda c: c['name'], data['columns']))
  selection = prompt.choose("Choose parametes", labels)

  labels = list(map(lambda idx: labels[idx], selection))
  print(labels)

  for point_index in range(d.shape[0]):
      datapoint = list(map(lambda idx: d[point_index, :][idx], selection))
      plot_data_point(datapoint)

  plt.title("parallel coordinate plot")
  plt.xticks(range(len(labels)), labels=labels)
  plt.show()

if __name__ == '__main__':
  data = csv_reader.readcsv('datasets/cars.csv')
  parallel_coordinate_plot(data)