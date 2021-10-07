class number():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def findPrimenumber(self):
        for num in range(self.x, self.y):
            if num > 1:
                for i in range(2, num):
                    if num % i == 0:
                        break
                else:
                    print(num, end=' ')
# c = number(1,100)
# print(c.findPrimenumber())

file = open("/Users/abhimanyu_yadav/Desktop/Practice/Python/text.txt")
count = 0
for i in file:
    count +=1
    if count == 5:
        print(i)
        break