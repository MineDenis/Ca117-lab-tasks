def l2d(file):
   s = file.readlines()
   s[0] = s[0].strip().split()
   s[1] = s[1].strip().split()
   d = {}
   for i in range(0, len(s[0])):
      d[s[0][i]] = s[1][i]
   return d
