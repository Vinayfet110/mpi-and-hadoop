#!/usr/bin/env python
import sys
current_word=None
current_count=0
fal_counter=0
turff=None
for line in sys.stdin:
	line=line.strip()
	surf,turff,count=line.split('\t',3)
	
	try:
		count=int(count)
	except ValueError:
		continue
	if turff=="TRUE":
		current_count+=count
	else:
		fal_counter+=count	

print "Numer of natural surfaces =%s"%(fal_counter)
print "Number of artifitial surfaces =%s"%(current_count)

		 
