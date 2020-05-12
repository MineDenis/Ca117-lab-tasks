def maximum(m):
    if len(m) == 1:
       return m[0]
    else:
       maxN = maximum(m[1:])
       max = m[0]
       if maxN > max:
            max = maxN
       return max
