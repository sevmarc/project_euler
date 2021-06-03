import time

#time at the start of the program execution
start = time.time()

#counter for couting number of possibilities
counter = 0

# number of 100p coins
for a in range(3):
	# number of 50p coins
	for b in range(int(1+(200-100*a)/50)):
		# number of 20p coins
		for c in range(int(1+(200-100*a-50*b)/20)):
			# number of 10p coins
			for d in range(int(1+(200-100*a-50*b-20*c)/10)):
			    # number of 5p coins
				for e in range(int(1+(200-100*a-50*b-20*c-10*d)/5)):
					# number of 2p coins
					for f in range(int(1+(200-100*a-50*b-20*c-10*d-5*e)/2)):
						counter += 1

# Total number of ways we can form the 200p
# Added 1 for 200p case
print(counter + 1)

#time at the end of program execution
end = time.time()

#Total time taken for the program execution
print(end - start)
