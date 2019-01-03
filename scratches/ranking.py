class Order():

  def __init__(self):
    self.l = []
    self.d = {}

  def add(self, data):
    if type(data) != list:
      print('your data is not a list!')
    elif len(data) < 2:
      print('your list is missing some elements!')
    elif len(data) > 2:
      print('your have too much elements in your list!')
      self = str(data[0])
    elif type(data[1]) != int:
      print('second argument should be an integer!')
    else:
      self.name = str(data[0])
      self.value = data[1]
      self.l.append([self.name, self.value])
      
  def aggregate(self):
    for data in self.l:
      self.name = data[0]
      self.value = data[1]
      if self.name not in self.d:
        self.d[self.name] = 0
      self.d[self.name] += self.value
    print(self.d)
    
  def sort(self):
    print("-" * 30)
    print("Top Ranking" + " | " + "Name" + " | " + "Value")
    tr = sorted(order.d.items(), key = lambda x: x[1], reverse=True)
    for i in range(len(tr)):
      #scoreが同じときのランキングNo.の処理
      if i >= 1 and tr[i][1] == tr[i -1][1]:
        print("No." + str(i) + " | " + tr[i][0] + " | " + str(tr[i][1]))
      else:
        print("No." + str(i + 1) + " | " + tr[i][0] + " | " + str(tr[i][1]))

  def sort_r(self):
    print("-" * 30)
    print("Worst Ranking" + " | " + "Name" + " | " + "Value")
    wr = sorted(order.d.items(), key = lambda x: x[1], reverse=False)
    for i in range(len(wr)):
      if i >= 1 and wr[i][1] == wr[i -1][1]:
        print("Worst" + str(i) + " | " + wr[i][0] + " | " + str(wr[i][1]))
      else:
        print("Worst" + str(i + 1) + " | " + wr[i][0] + " | " + str(wr[i][1]))

    print("-" * 30)


order = Order()
order.add(1)

order = Order()
order.add([1])

order = Order()
order.add([1, 2, 3])

order = Order()
order.add([1, '2'])

print(order.l)

order = Order()

#adding data to the list
import random
for i in range(10):
  order.add([random.randint(1, 11), random.randint(1, 11)])

print(order.l)

print(order.d)

#aggregate the data by its key
order.aggregate()

#sorted by the value
order.sort()

#sorted by the value reversed
order.sort_r()
