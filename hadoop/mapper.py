#!/usr/bin/env python
import sys
for line in sys.stdin:
	line=line.strip()
	#words=line.split(",")
	stadium,capacity,expanded,location,surface,turf,team,opened,weather,roof,elevation=line.split(",")
	surf=str(surface)
	#res_surf=[surf,"1"]
	tur=str(turf)
	#res_tur=[tur,"1"]
	if tur=="TRUE":
		res_sur_tur=[surf,tur,"1"]
	else:
		res_sur_tur=[surf,tur,"1"]
	print "\t".join(res_sur_tur)
		
