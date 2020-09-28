from point import point
p1=point(3,(1,2,3))
p2=point(3,(6,7,8))
print(p2.dist(p1.data))
p2.mirror()
print(p2.__repr__())
