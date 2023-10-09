#Intuition
#We need to find 2 numbers that add up to a target value and return their indices.

#Approach
#Check all possible pairs of elements in the array using nested loops to find the ones that add up to the target sum.

#1. Iterate through the array
#Outer loop → iterate from the first element to the second-to-last element.
#2. Compare with other elements
#Inner loop → iterate from the second element to the last element.
#3. Check for the target sum
#If the sum of the numbers at two indices add up to the target sum, return the indices.
#4. Repeat
#Continue this process until it finds a valid pair of indices. If it doesn't find a pair within the nested loops, it means there is no valid solution, and it will return nothing.
#Complexity
#Time complexity: O(n²)
#In the worst case, both loops will run for almost all pairs of elements in the array, leading to a time complexity of approximately O(n²), where n is the number of elements in the array.

#Space complexity: O(1)
#The space required does not depend on the size of the input array, so only constant space is used.

#Code: