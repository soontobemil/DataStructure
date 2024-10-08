import time

nemo = ['nemo']
everyone = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'nemo', 'Hannah', 'Ivy', 'Jack']
large = ["nemo"] * 1000000 # Creates 100 arrays

def find_nemo (array):
    t0 = time.perf_counter()
    for i in range(len(array)):
        print("running")
        if array[i] == "nemo":
            print("Found nemo!!")
            break
    t1 = time.perf_counter()
    print(f"Time taken {t1 - t0} milliseconds") # This measures the time it has taken to run the function

find_nemo(everyone)

# How do we measure efficency and scalability?
# Big O(n) --> Linear Time (# of Inputs == # of Operations)
