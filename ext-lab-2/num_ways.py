def num_ways_with_1_2_to_get(n):
    if n < 2:
        return 1
    return num_ways_with_1_2_to_get(n - 1) + num_ways_with_1_2_to_get(n - 2)


def num_ways_with_1_2_to_get_result(num1, num2):
    if num1 == 1:
        print(f"{num2} + 1")
    elif num1 == 2:
        print(f"{num2} + 1 + 1")
        print(f"{num2} + 2")
    else:
        if(num2 == ""):
            num_ways_with_1_2_to_get_result(num1 - 1, num2 + "1")
            num_ways_with_1_2_to_get_result(num1 - 2, num2 + "2")
            print(num_ways_with_1_2_to_get(num1))
        else:
            num_ways_with_1_2_to_get_result(num1 - 1, num2 + " + 1")
            num_ways_with_1_2_to_get_result(num1 - 2, num2 + " + 2")

def num_ways_with_1_2_to_get_result2(num):
    num_ways_with_1_2_to_get(num)
    num_ways_with_1_2_to_get_result(num, "")
    
def num_ways_with_1_2_3_to_get(n):
    if n < 2:
        return 1
    return num_ways_with_1_2_to_get(n - 1) + num_ways_with_1_2_to_get(n - 2) + num_ways_with_1_2_to_get(n - 3)

# def num_ways_with_1_2_3_to_get_result(num1, num2):
#     if num1 == 1:
#         print(f"{num2} + 1")
#     elif num1 == 2:
#         print(f"{num2} + 1 + 1")
#         print(f"{num2} + 2")
#     else:
#         if(num2 == ""):
#             num_ways_with_1_2_to_get_result(num1 - 1, num2 + "1")
#             num_ways_with_1_2_to_get_result(num1 - 2, num2 + "2")
#             print(num_ways_with_1_2_to_get(num1))
#         else:
#             num_ways_with_1_2_to_get_result(num1 - 1, num2 + " + 1")
#             num_ways_with_1_2_to_get_result(num1 - 2, num2 + " + 2")
    
    
# num_ways_with_1_2_to_get_result2(3)
print(num_ways_with_1_2_3_to_get(3))