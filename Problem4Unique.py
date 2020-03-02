#----------------------------------------
#David Gibbs
#February 27, 2020
#
#This program contains the use of the append function to create
#a new unique list of elements from the first list
#of numbers after checking the first list of values 
#----------------------------------------

def unique_elements(list):
#sets definition for unique list of values

  result = []
  for value in list:
    if value not in result:
        result.append(value)
#appends each item to the end each value in the new list
  return result
#checks to see if the value is located in the list as a unique value
#if it's not there then it appends the value to the new list

print(unique_elements([1,3,3,3,6,2,3,5])) 






