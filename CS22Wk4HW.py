import time
import random
import timeit

####################################################
# CS 22, Prof. Muldrow
# Name: Soliday Ek  
# Assignment: Week 4 Homework
# Due Date: 10/22/2023
####################################################

def set_list1D(list):
    for i in range(len(list)):  
        list[i] = random.randint(0,500)

def show_list1D(list):
    for i in list:
        print(i, end = " ")
    print()
    
def set_list2D(list):
    # Populates a 2D list with random values between 0 and 500.
    rows = len(list)
    columns = len(list[0])
    for i in range(rows):
        for j in range(columns):
            list[i][j] = random.randint(0,500)

def show_list2D(list):
    rows = len(list)
    columns = len(list[0])
    for i in range(rows): # two nested for loop for 2 dimesional list
        for j in range(columns):
            print(list[i][j], end = " ")
        print()


def main():
    list1 = [0] * 10 # there are 10 elements in tbis list and all consists of zeroes
    # we will define the number of rows and columns
    rows = 10
    columns = 10

    # create a two-dimensional array named LIST2
    list2 = [[0]* columns for i in range(rows)]

    # 1D set_list
    start_time = time.perf_counter()
    set_list1D(list1)
    total_time = time.perf_counter() - start_time
    print("set_list1D took " + str(total_time) + " seconds to execute.")
    
    # 1D show_list1D
    start_time = time.perf_counter()
    show_list1D(list1)
    total_time = time.perf_counter() - start_time
    print("show_list1D took " + str(total_time) + " seconds to execute.")

    # 2D set_list
    start_time = timeit.default_timer()
    set_list2D(list2)
    total_time = timeit.default_timer() - start_time
    print('set_list2D took' + str(total_time) + ' seconds to execute.')

    # 2D show_list1D
    start_time = timeit.default_timer()
    show_list2D(list2)
    total_time = timeit.default_timer() - start_time
    print("show_list2D took " + str(total_time) + " seconds to execute.")

if __name__ == "__main__":
    main()
    
  # run using python3 CS22Wk4HW.py

