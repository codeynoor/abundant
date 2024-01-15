def isAbundant(num: int):
  factors = []
  for i in range(1, num+1):
    if num % i == 0:
      factors.append(i)
  factors.remove(num)
  return sum(factors) > num

def getAbundant(start: int, stop: int):
    abundant = []
    for i in range(start, stop+1):
        if isAbundant(i) is True:
            abundant.append(i)
        else:
            continue
    return abundant

print(getAbundant(1, 100))  # Change the start and stop values here
