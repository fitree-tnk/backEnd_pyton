def loop(a,b):
  result = []
  for i in range(a,b+1):
      if i % 3 != 0:
          result.append(i)
  return result

def sum(nums,sum1,sum2):
  while True:
    if nums > 0:
        sum1 += nums
    elif nums < 0:
        sum2 += nums
    else:
        break
    return sum1, sum2
