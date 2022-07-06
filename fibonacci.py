my_dict = {}


def fib(n):
    if n < 2:
        return 1
    else:

        # print(fib(n - 1) + fib(n - 2))
        # x = fib(n - 1) + fib(n - 2)
        # print(x)
        return fib(n - 1) + fib(n - 2)


# print(fib(100))
def dynamicFib(n, my_dict):
    if n < 2:
        return 1
    else:
        if n in my_dict:
            return my_dict[n]
        my_dict[n] = dynamicFib(n - 1, my_dict) + dynamicFib(n - 2, my_dict)
        return my_dict[n]


# print(dynamicFib(100,my_dict))


def gridTraveller(n, m):
    if n == 0 or m == 0:
        return 0
    if n == 1 and m == 1:
        return 1
    return gridTraveller(n - 1, m) + gridTraveller(n, m - 1)


# print(gridTraveller(3,3))
# print(gridTraveller(18,18))


def dynamic_grid_traveller(n: int, m: int, my_dict: dict):
    # key = str(n) + ',' + str(m)
    # print(key)
    if n == 1 and m == 1:
        return 1
    if n == 0 or m == 0:
        return 0
    if (n,m) in my_dict:
        return my_dict[(n,m)]
    my_dict[(n,m)] = dynamic_grid_traveller(n - 1, m, my_dict) + dynamic_grid_traveller(n, m - 1, my_dict)
    return my_dict[(n,m)]


print(dynamic_grid_traveller(3,3,my_dict))
# print(dynamic_grid_traveller(18, 18, my_dict))
# numbers = [2,3]
def can_sum(targetsum, numbers):
    if(targetsum == 0): return True
    if(targetsum < 0): return False


    for num in numbers:
        remainder = targetsum - num
        if(can_sum(remainder, numbers)==True):
            return True

    return False

# print(can_sum(300,[7,14]))

def dynamic_can_sum(targetsum: int, numbers: list, my_dict:dict):
    if (targetsum == 0): return True
    if (targetsum < 0): return False
    if targetsum in my_dict:
        return True

    for num in numbers:
        remainder = targetsum- num
        if dynamic_can_sum(remainder, numbers, my_dict)==True:
            my_dict[targetsum] = True
            return True
    my_dict[targetsum] = False
    return False

# print(dynamic_can_sum(300,[7,14],my_dict))
""" needs practice"""
def how_sum(targetsum:int,numbers:list):
    if (targetsum == 0): return []
    if targetsum <0 : return None
    for num in numbers:
        remainder = targetsum - num
        # print(remainder)
        # number_list = num

        number_list = how_sum(remainder,numbers)
        if(number_list is not None):
            # print(num)
            number_list.append(num)

            return number_list
    return None

""" needs practice"""
memo = {}
def how_many_ways(coins, length, sum):
    if  (length,sum) in memo:
        return memo[(length,sum)]
    if sum < 0:
        return 0
    if sum == 0:
        return 1
    if length < 0:
        return 0
    if length < 0 and sum > 0:
        return 0
    memo[(length,sum)] = how_many_ways(coins,length-1,sum) + how_many_ways(coins, length, sum - coins[length-1])
    return memo[(length,sum)]
# print(how_sum(9,[10,2,3]))
# print(how_many_ways([1,2,3],3,100))

""" needs practice"""
ans = []
temp = []
def combination_sum(input_list,temp_list,sum,index):
    if(sum == 0 ):
        ans.append(list(temp_list))
        return
    for i in range(index, len(input_list)):
        if(sum - input_list[i]) >= 0:
            temp_list.append(input_list[i])
            combination_sum(input_list,temp_list,sum-input_list[i],i)
            temp_list.remove(input_list[i])

combination_sum([2,4,6,8,1],temp,8,0)
print(ans)

def hello_world():
    print("Hello World")



def logged(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        with open('log.txt', 'a+') as ff:
            fname = func.__name__
            print(f"{fname} returned value {value}")
            ff.write(f"{fname} returned value {value}")
        return value
    return wrapper

@logged
def add(x,y):
    return x + y

print(add(3,4))

import time

def time_count(func):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = func(*args, **kwargs)
        after = time.time()
        with open('log.txt', 'a+') as ff:
            fname = func.__name__
            print(f"function:{fname} runtime {after - before} second")
            ff.write(f"\nfunction:{fname} runtime {after - before} second")
        return value
    return wrapper

@time_count
def multiple(num):
    ans =1
    for i in range(0,num):
        ans *= i
    return ans

multiple(10000)

memo = {}
ans = []
def dynamic_howsum(targetsum:int,numbers:list,memo:dict):
    if targetsum == 0:
        return []
    if targetsum < 0:
        return None
    if targetsum in memo:
        return memo[targetsum]
    for num in numbers:
        remainder = targetsum - num
        ans = dynamic_howsum(remainder,numbers,memo)
        if ans is not None:
            ans.append(num)
            memo[targetsum] = ans
            return ans
    return None

print(dynamic_howsum(300,[7,15],memo))
print(how_sum(8,[1,2,3,4]))
