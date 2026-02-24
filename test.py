# class Counter:
#     def __init__(self):
#         self.current = 0

#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.current < 5:
#             self.current += 1
#             return self.current
#         else:
#             raise StopIteration
        
# c = Counter()
        
# for number in c:
#     print(number)

class A:
    def __iter__(self):
        return self
    def __next__(self):
        return 1
for x in A():
    print(x)
