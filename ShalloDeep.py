original=[[10,20],[30,40]]
original[0][0]=90
print(original)
original=[[10,20],[30,40]]
shallow=original.copy()
print(id(original))
print(id(shallow))
print(original)
shallow[0][0]=100
print(shallow)
print(original)

