# How do you find all pairs of an integer array whose sum is equal to a given number?
import math

# First, sort the array (O(nlog(n))). Then, for each element, compare it to the middle element of the array. 
# If the sum is less than n, create a subarray from the original middle element to the first, and repeat 
# def sum_pairs_equals_n_recursive(pairs, n):



# First, sort the array (O(nlog(n))). Then, for each element, compare it to the middle element of the array. 
# If the sum is less than n, create a subarray from the original middle element to the first, and repeat 
def sum_pairs_equals_n_iterative(numbers, n):
	numbers.sort()
	pairs = []
	l = len(numbers)
	for i in range(l):
		start_index = i
		end_index = l - 1
		middle_index = math.floor((start_index + end_index) / 2)
		# divide and conquer - choose the middle value in the array
		while start_index != end_index:
			if numbers[i] + numbers[middle_index] == n:
				pairs.append((numbers[i], numbers[middle_index]))
				break
			elif numbers[i] + numbers[middle_index] > n:
				# look at left hand side of array
				end_index = middle_index
				middle_index = math.floor((start_index + end_index) / 2)
			elif numbers[i] + numbers[middle_index] < n:
				# look at right hand side of array
				start_index = middle_index
				middle_index = math.ceil((start_index + end_index) / 2)
			
	
	return pairs


if __name__ == '__main__':
    print(sum_pairs_equals_n_iterative([1,4,2,3, 6, 7], 10))
