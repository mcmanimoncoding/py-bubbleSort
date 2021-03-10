import random

# create an array of random integers between (x, y) for an array length of 20
random_items = [random.randint(-50, 100) for c in range(20)]


# create the bubble sort algorithm assigning 'random_items' to 'items' 
# for i variable in length of range 'items'
# compare to j variable set by length of range -1-i
# if items[j]>[j+1] change [j] to [j+1] and [j+1] to [j]
def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
                
                
              

print('Before: ', random_items)
# call bubble sort function with random_items as the variable
bubble_sort(random_items)
print('After: ', random_items)


# this code is based on Herman Martinus' SkillShare coursework helping me understand althorithms in Python