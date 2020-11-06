def print_floor(floor, i, j):
    for l in range(len(floor)):
        for m in range(len(floor[l])):
            if i == l and j == m:
                print('_ ', end="")
            else:
                print(str(floor[l][m]) + " ", end="")
        print()
    print()

def clean(floor):
    
    for i in range(len(floor)):
        if i % 2 == 0:
            for j in range(len(floor[i])):
                if floor[i][j] == 1:
                    floor[i][j]=0
                print_floor(floor, i, j)
               
        else:
            for j in range(len(floor[i])-1, -1, -1):
                if floor[i][j] == 1:
                    floor[i][j]=0
                print_floor(floor, i, j)
                
R = int(input("Enter the number of rows:")) 
floor = [] 

for i in range(0,R):          
    a = list(map(int,input().split(" ")))
    floor.append(a)
print("\n")
print_floor(floor, -1, -1)
clean(floor)
