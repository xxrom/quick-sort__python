def quickSort(array, left, right):
  if left >= right:
    return ;

  pivot = checkArray(array, left, right)
  print(' end pivot %s ' % pivot)
  quickSort(array, left, pivot - 1)
  quickSort(array, pivot + 1, right)

def swap(array, i, j):
  temp = array[i]
  array[i] = array[j]
  array[j] = temp

def checkArray(array, low, high):
  middle = (low + high) // 2 # get middle index

  # выбираем значение для сравнения из середины массива
  # это значение ставим в самый конец массива и начинаем сравнивать
  # и двигать стенку, значений меньших pivot и больших pivot
  swap(array, middle, high) # set the pivot at the end of array

  wall = low # слева от стены значения меньше, справа - больше

  for i in range(low, high): # проходимся по всему массиву
    print('w - %s | i - %s | middle - %s ' % (wall, i, array[high]))
    if array[i] <= array[high]:
      swap(array, i, wall) # если значение меньше pivot [high]
      # то меняем местами wall и I и сдвигаем wall(стену) + 1
      wall += 1 # слева добавили значение меньше чем pivot [high]

  swap(array, wall, high) # ставим pivot обратно, сразу после стены

  return wall # возвращаем индекс pivot (стены нашей)


# TEST
if __name__ == '__main__':
  unsortedArray = [22, -2, 33, 32, 0, -2, 11, 3, 500, 100]
  quickSort(unsortedArray, 0, len(unsortedArray) - 1)
  print(unsortedArray)

