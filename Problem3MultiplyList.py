#----------------------------------------
#David Gibbs
#February 27, 2020
#
#This program contains a function which multiplies all
#numbers in the list specified from [5, 2, 7, and -1] and will return the
#"product" to the screen
#----------------------------------------

def Multiply(num1, num2, num3, num4):
    answer = num1 * num2 * num3 * num4
    return answer
#sets definition and returns what is assigned to "answer"
print(Multiply(5, 2, 7, -1))
#displays the results to the screen
#See code below to accommodate a flexible range 
#def multiplyList(numbers) : 
      
    # Multiply elements one by one 
 #   result = 1
 #   for x in numbers: 
 #        result = result * x  
 #   return result  
      
# Driver code 
#numbers = [5, 2, 7, -1]  
#print(multiplyList(numbers))
