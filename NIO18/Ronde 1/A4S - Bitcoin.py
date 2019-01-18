b=[int(input())for _ in range(int(input()))]
print(sum([(0,b[i+1]-b[i])[b[i+1]>b[i]]for i in range(len(b)-1)]))