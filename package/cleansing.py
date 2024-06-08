from package.linkedList import LL
from package.functions import *

def load_main():
  # make converter file
  with open('data/converter.csv', 'w') as file:
    file.write('')
    file.close
  with open('data/unique.csv', 'w') as file:
    file.write('')
    file.close

  # count line
  with open(r"data\heart_2020_cleaned.csv", 'r') as file:
    file_len = count_line(file)

  # allocate array of string
  lines = ["" for line in range(file_len)]

  # fill the array
  lines = filling_array(lines)

  # get array
  lines = [split(lines[i]) for i in range(len(lines))]

  # change to float if possible
  lines = [toFloat(lines[i]) for i in range(len(lines))]

  datas = [[] for i in range(18)]

  # get unique
  for i in range(18):

    with open('data/unique.csv', 'a') as file:
      if i in [0, 2, 3, 4, 7, 8, 10, 11, 12, 13, 15, 16, 17]:
        unik = ll_to_arr(uniquePColumn(lines, i))
        print(i, unik)
        file.write(f'{i}, {unik}\n')
      file.close

    with open('data/converter.csv', 'a') as file:
      if i in [0, 2, 3, 4, 7, 8, 10, 11, 12, 15, 16, 17]:
        for j in range(len(unik)):
          file.write(f'{i}, "{unik[j]}", {j/(len(unik)-1)}\n')

    if i == 13:
      with open("data/converter.csv", 'a') as file:
        file.write('13, "Poor", 0.0\n')
        file.write('13, "Fair", 0.25\n')
        file.write('13, "Good", 0.5\n')
        file.write('13, "Very good", 0.75\n')
        file.write('13, "Excellent", 1.0\n')
        file.close

    # 1, 5, 6, 14
    if i in [1, 5, 6, 14]:
      Min, Max = min_max(ll_to_arr(uniquePColumn(lines, i)))
      print(i, Min, Max)
      with open('data/converter.csv', 'a') as file:
        file.write(f'{i}, {Min}, {Max}\n')
        file.close

    # for str
    if isinstance(lines[1][i], str):
      # line 13 are special
      if i != 13:
        unique = ll_to_arr(uniquePColumn(lines, i))
        # print(i, unique)
        if i == 9: 
          a = unique
          unique = [float(unique[i][:2]) for i in range(len(unique))]
          b = bubble_sort(unique)
        if isinstance(unique[0], float): unique = bubble_sort(unique)
      else:
        unique = ["Poor", "Fair", "Good", "Very good", "Excellent"]
    
      # convert str
      if isinstance(unique[0], str):
        column, unique = convertUnique(lines, i, unique)
        column = convertSorted(column, unique)
      
      #convert float
      else: 
        column = [float(lines[j][i][:2]) for j in range(1, len(lines))]
        column = convertSorted(column, column)
        if i == 9: 
          c = bubble_sort(ll_to_arr(getUnique(column)))
          with open('data/converter.csv', 'a') as file:
            for LINE in range(18, 101):
              jjj = -1
              for j in range(len(b)-1):
                if b[j] <= LINE < b[j+1]:
                  jjj = j
                  break
              if jjj == -1:
                jjj = len(b)-1
              file.write(f'9, "{LINE}", {c[jjj]}\n')
            file.close

    # for float
    else: 
      column = [lines[j][i] for j in range(1, len(lines))]
      column = convertSorted(column, column)

    # if i == 0: print(bubble_sort(ll_to_arr(getUnique(column))))
    datas[i] = column

  datas = transpose(datas)
  return datas

def count_line(file) -> int:
  num = 0
  for line in file: num += 1
  return num

def filling_array(lines:list[str]) -> list[str]:
  with open(r"data\heart_2020_cleaned.csv", 'r') as file:
    line_num = 0
    for line in file:
      lines[line_num] = str(line)[:-1]
      line_num += 1
  return lines

def split(line:str):
  datas = ["" for data in range(18)]
  if not isIn(line):
    word = ""
    data_idx = 0
    for i in range(len(line)):
      if line[i] != ',':
        word += line[i]
      else:
        datas[data_idx] = word
        data_idx += 1
        word = ""
    datas[data_idx] = word

  else:
    idxs = findQuote(line)
    word = ""
    data_idx = 0
    for i in range(idxs[0]):
      if line[i] != ',':
        word += line[i]
      else:
        datas[data_idx] = word
        data_idx += 1
        word = ""
    datas[data_idx] = line[idxs[0]+1:idxs[1]]
    data_idx += 1
    for i in range(idxs[1]+2, len(line)):
      if line[i] != ',':
        word += line[i]
      else:
        datas[data_idx] = word
        data_idx += 1
        word = ""
    datas[data_idx] = word

  return datas

def isIn(line:str) -> bool:
  for i in range(len(line)):
    if line[i] == '"': return True
  return False

def findQuote(line:str) -> int:
  idxs = [0, 0]
  idx = 0
  for i in range(len(line)):
    if line[i] == '"':
      idxs[idx] = i
      idx += 1
  return idxs

def toFloat(line:list[str]) -> list:
  for i in range(18):
    try: line[i] = float(line[i])
    except ValueError: pass
  return line

def uniquePColumn(lines:list[list], idx:int) -> LL:
  # exception for the head of the column
  column = [lines[i][idx] for i in range(1, len(lines))]
  unique = getUnique(column)
  return unique

def convertUnique(lines:list[list], idx:int, unique) -> list[float]:
  column = [lines[i][idx] for i in range(1, len(lines))]
  for i in range(len(column)):
    for j in range(len(unique)):
      if column[i] == unique[j]: column[i] = j
  unique = [i for i in range(len(unique))]
  return column, unique

def convertSorted(column, unique) -> list[float]:
  min, max = min_max(unique)
  for i in range(len(column)):
    column[i] = (column[i]-min)/(max-min)
  return column

def min_max(arr:list[float]) -> list:
  min = float('inf')
  max = -1
  for i in range(len(arr)):
    if arr[i] > max: max = arr[i]
    if arr[i] < min: min = arr[i]
  return [min, max]

def transpose(matrix: list[list]) -> list[list]:
  return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

