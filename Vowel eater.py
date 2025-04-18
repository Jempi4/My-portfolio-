my_list = [17, 3, 11, 5, 1, 9, 7, 23, 13]



#               FINDING THE LARGEST NUMBER


#temporarily assume that the first number in the list is the largest

largest = my_list[0]

#now compare with the rest

for i in range (1, len(my_list)):
    if my_list[i] > largest:

#That means that the largest is in that particular index
        largest = my_list[i]


print("largest number: ", largest)




#               FINDING THE SMALLEST NUMBER


#temporarily assume that the first number in the list is the smallest

smallest = my_list[0]

#now compare with the rest

for i in range (1, len(my_list)):
    if my_list[i] < smallest:

#That means that the smallest is in that particular index
        smallest = my_list[i]


print("smallest number: ", smallest)





#               OR BETTER STILL

largest = my_list[0]

for i in my_list:
    if i > largest:
        largest = i

print ("largest number: ", largest)

repeated = False
number = my_list[0]

for i in my_list:
    
    repeated = my_list[i + 1] == my_list[i]

    if repeated:
        del my_list[i + 1]
        
        
        
        

print (my_list)
