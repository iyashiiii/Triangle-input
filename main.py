x = [[input().split(' ')] for i in range(4)]

def last():
	yield x[0]
	yield y = max(x[1])
	
	if x.index(y) == 0:     
		yield yy = max(x[2][:2])    #x[2]
		
		if x.index(yy) == 0:    #x[3]
			yield max(x[3][:2])
			
		if x.index(yy) == 1:
			yield max(x[3][1:3])  
	
    else:                  
        yield yy = max(x[2][1:])    #x[2]
        
        if x.index(yy) == 1:    #x[3]
			yield max(x[3][1:3])
			
		if x.index(yy) == 2:
			yield max(x[3][2:]) 
			
last = list(last())
print(last)