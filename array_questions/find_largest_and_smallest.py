# How do you find the largest and smallest number in an unsorted integer array? (solution)

def find_largest_and_smallest(arr):
	min = arr[0]
	max = arr[0]
	for x in arr:
		if x < min:
			min = x
		elif x > max:
			max = x
	return {'largest': min, 'smallest': max}