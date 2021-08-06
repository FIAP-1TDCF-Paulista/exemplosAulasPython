alist = [54,26,93,17,77,31,44,55,20,1,10,2,5,100,100,200,7,8,900,500,300,100,100,200,50,1,20]
for passnum in range(len(alist)-1,0,-1):
	        for i in range(passnum):
	            if alist[i]>alist[i+1]:
	                temp = alist[i]
	                alist[i] = alist[i+1]
	                alist[i+1] = temp
print("O tamanho da lista é =",len(alist))
print(alist)