def minimum(m):
    if len(m) == 1:
       return m[0]
    else:
       minN = minimum(m[1:])
       min = m[0]
       if minN < min:
            min = minN
       return min
