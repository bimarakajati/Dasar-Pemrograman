for i in range(1,4): # Outer Loop
	print ("Outer Loop ke - ",i)
	for j in range(1,3): # Inner Loop
		print (" - Inner Loop ke - ",j)
print("selesai")

a = 1
while (a < 4) :
    print ("Outer Loop ke - ",a)
    b = 1
    while (b < 3) :
        print ("* Inner Loop ke - ",b)
        b+=1
    a+=1
    print ("")
print("selesai")
