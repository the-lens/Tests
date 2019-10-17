# Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1),
# while the other is "far", differing from both other values by 2 or more.


def close_far(a, b, c):
  if abs(a - b) < 2:
    if abs(b - c) >= 2 and abs(a - c) >= 2:
      return True
    else:
      return False
  elif abs(a - c) < 2:
    if abs(a - b) >= 2 and abs(c - b) >= 2:
      return True
    else:
      return False
  else:
    return False



print(close_far(1, 2, 10), # → True
      close_far(1, 2, 3),# → False
      close_far(4, 1, 3))# → True


