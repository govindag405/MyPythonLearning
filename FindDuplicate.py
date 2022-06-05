def duplicate_num(lis):
    duplicate_lis = []
    """Takes a list input and checks
    if there are any duplicates in the list"""
    if type(lis) != list:
        print("The input for the function can only be type list")
    else:
        for num in lis:
            lis.remove(num)
            if num in lis:
                duplicate_lis.append(num)
    return duplicate_lis

dupl_lis = duplicate_num([1,2,3,4,4,5,5,6,6])
print(dupl_lis)

