# # # basic 
# for i in range(0, 150):
#     print(i)

# # #multiples of 5

# for i in range(5, 1000000):
#     if (i % 5 == 0):
#         print(i)

# #Counting the Dojo Way

# for i in range(1, 100):
#     print(i)
#     if(i % 5 == 0):
#         print("Coding")
#     if(i % 10 == 0):
#         print("Dojo")

# # Whoa that suckers big
# def bigSucker():
#     sum = 0
#     for i in range(0, 500000):
#         if (i % 2 == 1):
#             sum+= i
#     return sum
# print(bigSucker())

# #countdown by fours
# for i in range(2018, 0, -4):
#     print(i)

# #flexible countdown
# def flexible(lowNum, highNum, mult):
#     for i in range(lowNum, highNum+1):
#         if (i % mult == 0):
#             print(i)
# print(flexible(2,9,3))

b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)