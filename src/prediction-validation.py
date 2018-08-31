# Python2.7
# -*- coding: UTF-8 -*-

import sys

# Sort stocks, time component should be sorted in ascending order 
# When time component is same, then stock ID should be sorted in order of lexicography 
def comp(x, y):
	if long(x[0]) < long(y[0]):
		return -1
	elif long(x[0]) > long(y[0]):
		return 1
	elif x[1] < y [1]:
		return -1
	elif x[1] > y [1]:
		return 1
	else:
		return 0

# get data from actual.txt
def get_actual(intput_path):	
	actf = open(intput_path)
	actline = actf.readline()[:-1]
	actdata_list = []
	while actline:
		data = actline.split("|")
		actdata_list.append(data)
		actline = actf.readline()[:-1]	
	actf.close()
	
	return actdata_list

# get data from predicted.txt
def get_predicted(intput_path):
	pref = open(intput_path)
	preline = pref.readline()[:-1]
	predata_list = []
	while preline:
		predata = preline.split("|")
		predata_list.append(predata)
		preline = pref.readline()[:-1]
	pref.close()
	
	return predata_list

# get data from window.txt
def get_window(intput_path):
	winf = open(intput_path)
	k = winf.read()
	
	return k

# computer number of matches and total error, then save as counts list & errors list 
def compute_error():
	errors = [] 					# each element in list is total error at particular time
	counts = [] 					# each element in list is number of matches at particular time 
	error = 0.00					# initial error
	count = 0						# initial count
	key = long(predata_list[0][0])	# judge whether a particular predicted time changes to next time period
	l = 0 							# a pointer points to current actdata_list location
	time = 1            			# time indicator, starts from 1
	errors.append(0.0)
	counts.append(0)

	for num in predata_list :
		#judge whether current time is a new time period
		while time < key:
			errors.append(0.0)
			counts.append(0)
			time = time + 1

		if long(num[0]) != long(key) :
			errors.append(error)
			error = 0.00
			counts.append(count)
			count = 0
			key = long(num[0])
			time = time + 1
		
		# visit all actual data but still left predicted data, error cases!
		if l == len(actdata_list) :
			print("*Error! predicted stock info: " + num[0] + "|" + num[1] + "|" + num[2])
			break
			
		while l < len(actdata_list) :
			if long(num[0]) == long(actdata_list[l][0]) :
				if num[1] == actdata_list[l][1] :
					error += abs(float(actdata_list[l][2]) - float(num[2]))
					count = count + 1
					l = l + 1
					break
			# visit all actual data at particular time but cannot find predicted data at that time
			elif long(num[0]) < long(actdata_list[l][0]):
				print("Error! predicted stock info: " + num[0] + "|" + num[1] + "|" + num[2])
				break
			l = l + 1
					
	counts.append(count)
	errors.append(error)

	while time < long(actdata_list[len(actdata_list)-1][0]):
		errors.append(0.0)
		counts.append(0)
		time = time + 1

	return errors, counts 

# calculate average error for certain window size
def compute_window_error():
	res = 0.0
	cnt = 0
	output = []

	start = long(actdata_list[0][0])
	end = long(actdata_list[len(actdata_list)-1][0])
	for i in range (start, end - int(k) + 2) :
		if(i == start):
			for j in range (i, i + int(k)) :
				res += errors[j]
				cnt += counts[j]
		else :
			res -= errors[i - 1]
			res += errors[i + int(k) - 1]
			cnt -= counts[i - 1]
			cnt += counts[i + int(k) - 1]
			
		if cnt != 0 :
			output.append("%d|%d|%.2f" %(i, i+int(k)-1, res/cnt))
		else :
			output.append("%d|%d|NA" %(i, i+int(k)-1))

	return output


if __name__ == '__main__':
	if len(sys.argv) != 5:
		print("Please input the command correctly: ")
		print("python src/prediction-validation.py input/actual.txt input/predicted.txt input/window.txt output/output.txt")
		exit(1)

	input_actual_path = sys.argv[1]
	input_predicted_path = sys.argv[2]
	input_window_path = sys.argv[3]
	output_path = sys.argv[4]

	# read data from actual.txt and sort it
	actdata_list = get_actual(input_actual_path)
	actdata_list.sort(comp)
	
	# read data from predicted.txt and sort it
	predata_list = get_predicted(input_predicted_path)
	predata_list.sort(comp)
	
	# read data from window.txt
	k = get_window(input_window_path)
		
	# computer total error and number of matches for any particular time, then save as errors list & counts list 
	errors, counts = compute_error()
	
	# calculate average error for certain window size
	output = compute_window_error()						
	
	# write output to file
	output_file = open(output_path, 'w')
	for i in output:
		output_file.write(i + "\n")


			
		  