import time

def QSort(array:list) -> list:
	"""Function of quick sorting. 
	Returns sorted array """

	N = len(array)
	left = []
	right = []
	equal = []

	if N > 1:
		pivot = array[-1]
		for item in array:
			if item > pivot:
				right.append(item)
			if item < pivot:
				left.append(item)
			if item == pivot:
				equal.append(item)
		return QSort(left) + equal + QSort(right)
	else:
		return array

def BubbleSort(arr:list) ->list:
	"""Bubble sorting. Returns array"""
	N = len(arr)
	for i in range(1, N):
		for j in range(N-i):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
	return arr

def tester():
	t = time.time()
	print("Tester function starts")
	arr1 = [3, 2, 5, 2 ,3, 4, 5, 7, 6]
	print("Quick sorting of array [3, 2, 5, 2 ,3, 4, 5, 7, 6]:")
	print(QSort(arr1))
	print(time.time() - t)

	t2 = time.time()
	print("Bubble sorting of array [3, 2, 5, 2 ,3, 4, 5, 7, 6] ")
	print(BubbleSort(arr1))
	print(time.time() - t2)
if __name__ =="__main__":
	tester()
	