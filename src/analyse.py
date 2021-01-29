import matplotlib.pyplot as plt
from numpy import arange
from scipy.optimize import curve_fit
import csv_reader

def get_col_data(data, row):
  res = list()
  for i in range(len(data['data'])):
    res.append(data['data'][i][row])
  return res

def objective(x, a, b, c):
	return a * x + b * x**2 + c

def entrypoint(filename):
  data = csv_reader.readcsv(filename)
  mpg = get_col_data(data, 1)
  hp = get_col_data(data, 4)

  # remove uncomplete data
  remove_list = list()
  for i in range(len(mpg)):
    if mpg[i] == 0:
      remove_list.append(i)
  for i in range(len(hp)):
    if hp[i] == 0:
      remove_list.append(i)
  remove_list.sort()
  remove_list.reverse()
  for i in remove_list:
    del mpg[i]
    del hp[i]

  popt, _ = curve_fit(objective, mpg, hp)

  a, b, c = popt
  plt.scatter(mpg, hp)
  x_line = arange(min(mpg), max(mpg), 1)
  y_line = objective(x_line, a, b, c)
  plt.xlim([10,40])

  plt.plot(x_line, y_line, '--', color='red')
  plt.show()


if __name__ == '__main__':
    entrypoint('./datasets/cars.csv')