#With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number 
# between 1 and n (both included). and then the program should print the dictionary.
def sample_dict(number):
    dict_result = {}
    for num in range(1,number+1):
        dict_result.update({num:num**2})

    print(dict_result)

sample_dict(9)