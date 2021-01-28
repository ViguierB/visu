import numpy as np

def parse_string(in_str):
  return in_str

def parse_double(in_str):
  return float(in_str)

def parse_int(in_str):
  return int(in_str)

def get_parse_function(t):
  t = t.upper()
  switcher = {
    "STRING": parse_string,
    'DOUBLE': parse_double,
    'INT': parse_int,
  }
  return switcher.get(t, parse_string)

def readcsv(filename):
  result = { }
  reader = open(filename)
  try:
    cols = reader.readline()[:-1].split(';')
    cols_type = reader.readline()[:-1].split(';')
    lines = reader.readlines()

    result["columns"] = []
    convertors = []
    for i in range(len(cols)):
      convertors.append(get_parse_function(cols_type[i]))
      result["columns"].append({ "name": cols[i], "type": cols_type[i] })

    result["data"] = []
    for line in lines:
      values = line[:-1].split(';')
      for i in range(len(values)):
        values[i] = convertors[i](values[i])
      result["data"].append(values)
    return result
  finally:
    reader.close()

