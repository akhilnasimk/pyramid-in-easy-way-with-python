n=int(input("enter the number of rows"))

def pira(n,i,str,h):
    while(i<=n):
        d=n-i
        print(h*d,str*i,h*d)
        i=i+1
pira(n,i=1,str="*   ",h="  ")
