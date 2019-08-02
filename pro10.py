# pro10.py
viji=int(input())
bin=[int(i) for i in input().split()]
zen=0
for k in range(viji):
   for j in range(k):
      if bin[j]<bin[k]:
         zen+=bin[j]
print(zen) 
