l = [[1, 2], [2, 3], [3, 4]]

print(' '.join([str(i) for i in l]))

print('\n'.join([str(i) for i in l]))

#改行区切りで縦並びの出力
print('\n'.join([str(i) for i in l]))

#上の二つの組み合わせ
print('\n'.join(' '.join([str(j) for j in i]) for i in l))

print("-"*30)

k = [i for i in range(10)]
print(k)

x3 = '\n'.join(' '.join([str((i + 1) + (j * 3)) for i in range(3)]) for j in range(3))
print(x3)

x4 = '\n'.join(' '.join([str((i + 1) + (j * 4)) for i in range(4)]) for j in range(4))
print(x4)

init = 10
x = '\n'.join(' '.join([str((i + 1) + (j * init)) for i in range(init)]) for j in range(init))
print(x)

print("-"*30)

def sq_matrix(n):
  matrix = '\n'.join(' '.join([str((i + 1) + (j * n)) for i in range(n)]) for j in range(n))
  return print(matrix)
sq_matrix(20)
