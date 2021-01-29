import matplotlib.pyplot as plt
import csv_reader

def get_col_data(data, row):
  res = list()
  for i in range(len(data['data'])):
    res.append(data['data'][i][row])
  return res

def entrypoint(filename):
  data = csv_reader.readcsv(filename)
  mpg = get_col_data(data, 1)
  hp = get_col_data(data, 4)

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

  


  plt.plot(mpg, hp)
  plt.title("Hannnnn")
  plt.xlabel("mpg")
  plt.ylabel("Horsepower")
  plt.show()
  plt.close()

  plt.plot(mpg, hp, "o")
  plt.title("Hannnnn")
  plt.xlabel("mpg")
  plt.ylabel("Horsepower")
  plt.show()
  plt.close()

  plt.plot(mpg, hp, "x")
  plt.title("Hannnnn")
  plt.xlabel("mpg")
  plt.ylabel("Horsepower")
  plt.show()
  plt.close()


if __name__ == '__main__':
    entrypoint('./datasets/cars.csv')