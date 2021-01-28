
def choose(message, titles, limit = -1, min = -1):
  print(message)
  if limit <= 0: limit = len(titles)

  for i, title in enumerate(titles):
    print(f"{i+1}: {title}")
  
  input_line = input(f"Select using numbers - ex: 1,5,8 (all if empty) - limit={limit}:\n")

  if not input_line:
    return range(len(titles))

  selection = list(map(lambda n: int(n) - 1, input_line.split(',')))

  for s in selection:
    if s >= len(titles) or s < 0:
      raise Exception(f"{s+1}: Out of bound")

  if len(selection) > limit:
    raise Exception("Limit exceeded")

  if min > 0 and len(selection) < min:
    raise Exception("Min limit not reached")

  return selection