
#Напишите функцию для транспонирования матрицы


matrix=[(1,2,3),(4,5,6),(7,8,9),(10,11,12)]
for i in matrix:
	print(i)
print("\n")
t_matrix = zip(*matrix)
for i in t_matrix:
	print(i)



