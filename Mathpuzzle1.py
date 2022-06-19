# What two square numbers add up to 36482
# a^2 + b^2 = 2ab (36482)
# dict = {'set1': [139, 131]}
dict = {}
for i in range(1,1000):
    for j in range(1,i):
        counter = 0
        if i**2 + j**2 == 36482:
            counter += 1
            dict.update({counter:[i,j]})
            
            
print(dict)