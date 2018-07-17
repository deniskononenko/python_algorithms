def qsort(arr:list)->list:
	""" Realization of Quick sort algorithm
	with help of list comprehentions. 
	Gets an array. Returns an array"""

	if len(arr)>1:
		return (qsort([ell for ell in arr if ell<arr[-1]]) + 
		[ell for ell in arr if ell == arr[-1]] + 
		qsort([ell for ell in arr if ell>arr[-1]]))
	else:
		return arr


def tester():
	"""Sorting testing function"""

	arr1 = [2, 3 , 4, 3, 2, 7, 6, 5, 1, 4]

	print("Tester starts: qsort([2, 3 , 4, 3, 2, 7, 6, 5, 1, 4])")
	print(qsort(arr1))

if __name__ == "__main__":
	tester()