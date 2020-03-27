#a welcome mat function
def drawMat(n, m):
  #top triangle
  for i in range(1, n, 2):
    print((('.|.')*i).center(m, '-'))
  #center
  print(('WELCOME').center(m, '-'))

  #bottom triangle
  for i in range(n-2, 0, -2):
    print((('.|.')*i).center(m, '-'))
