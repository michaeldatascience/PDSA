"""
def DishPrepareOrder(Order_List):
    dish_count = {}
    for item in Order_List:
        if item not in dish_count:
            dish_count[item]=0
        dish_count[item] +=1

    print (dish_count.keys())
    for dish_id in dish_count.keys():
        print((-dish_count[dish_id],dish_id))

    sorted_dishes = sorted(dish_count.keys(), key=lambda dish_id: (-dish_count[dish_id], dish_id))
    print(sorted_dishes)

"""





def DishPrepareOrder(L):
    dish_count = {}
    
    # Count the occurrences of each dish_id
    for item in L:
        if item not in dish_count:
            dish_count[item] = 0
        dish_count[item] += 1
    
    # Sort by count in descending order and by dish_id in ascending order
    DishSorted = sorted(dish_count.items(), key=lambda item: (-item[1], item[0]))
    
    # Extract the dish_id from the tuples
    result = [dish_id for dish_id, count in DishSorted]
    
    return result


L = [1006, 1008, 1009, 1008, 1007, 1005, 1008, 1001, 1003, 1009, 1006, 1003, 1004, 1002, 1008, 1005, 1004, 1007, 1006, 1002, 1002, 1001, 1004, 1001, 1003, 1007, 1007, 1005, 1004, 1002]
print (DishPrepareOrder(L))