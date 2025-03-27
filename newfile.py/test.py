def find_max_number(numbers:list):
    maximum = 0
    if len(numbers) == 0:
        return "Invalid List"

    for i in numbers:
        print(i)
        if i >= maximum:
            maximum = i 
        else:
            return f"Max is {maximum}"
            break
    


print(find_max_number([1,2,3,4,5,6,7,8,9,10]))