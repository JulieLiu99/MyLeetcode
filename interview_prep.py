def get_shortest_unique_substring(arr, str):
  
  def allIn(cur):
    for c in arr:
        if c not in cur:
            return False
    return True
  
  l = r = 0
  res = ""
  size = len(str)
  while l <= r < len(str):
    cur = str[l:r+1]
    if allIn(cur):
        if len(cur) <= size:  # has to have =, because we might need to return entire str
            res = cur
            size = len(cur)
        l += 1
    else:
        r += 1
  
  return res

  """
  arr = ['x','y','z'], str = "xyyzyzyx"
  
  xyyz allIn
  l = 0, r = 4
  size = 4
  
  yyz
  yyzy
  yyzyz
  yyzyzy
  yyzyzyx allIn
  yzyzyx
  zyzyx
  yzyx
  zyx
  
  """

print(get_shortest_unique_substring(["A"], "A"))