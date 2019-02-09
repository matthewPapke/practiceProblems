# Q: How do you check if two strings are anagrams of each other? 
import sys

# check the counts of each character in each string. if the strings are the same length, and the counts for each character
# are the same, then they're anagrams, else they're not
def is_anagram_v1(str_a, str_b):
	# create dict of letter and count
	# also compare size
	if len(str_a) != len(str_b):
		return False
	
	dict_a = {}
	dict_b = {}

	for i in range(len(str_a)):
  		char_a = str_a[i]
  		char_b = str_b[i]

  		count_a = dict_a.get(char_a, None)
  		count_b = dict_b.get(char_b, None)

  		if count_a is None:
  			dict_a[char_a] = 1
  		else:
  			dict_a[char_a] = count_a + 1

  		if count_b is None:
  			dict_b[char_b] = 1
  		else:
  			dict_b[char_b] = count_b + 1

  	for k in dict_a.keys():
  		if dict_a.get(k) != dict_b.get(k):
  			return False
	return True


# for each char in str_a, check if it is in str_b. if it is, then remove it from both strings. if it's not, then return false.
# once str_a is empty, if str_b is also empty then return true. else false
def is_anagram_v2(str_a, str_b):
	while(len(str_a) > 0):
		c = str_a[0]
		ind = str_b.find(c)
		if ind == -1:
			return False
		else:
			str_a = str_a[1:]
			str_b = str_b[:ind] + str_b[ind+1:]

	return len(str_b) == 0




if __name__ == '__main__':
    print(is_anagram_v2(*sys.argv[1:]))



