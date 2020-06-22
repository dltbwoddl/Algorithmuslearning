#https://www.acmicpc.net/problem/5622
a=[i for i in input()]
b={3:['A','B','C'],4:['D','E','F'],5:['G','H','I'],6:['J','K','L'],7:['M','N','O']
   ,8:['P','Q','R','S'],9:['T','U','V'],10:['W','X','Y','Z']}
result=0
for i in a:
    for key, value in b.items():
        if i in value:
            result+=key
print(result)

