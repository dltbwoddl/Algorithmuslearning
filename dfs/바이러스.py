#https://www.acmicpc.net/problem/2606
#입력받은 값들을 서로 연관되는 모든 것과 연관 지어 표현해야 한다.
#1 단순한 딕셔너리로 나타내려고 했다., key값이 같을 수 없다.
#2 연결된 모든 것을 추가한 형태로 자료를 바꾼다.
com={}
global result_1
result_1=set()
global result_2
result_2=set()
a=int(input(""))
b=int(input(""))
for i in range(0, b):
    c=[int(i) for i in input("").split()]
    if c[0] in com.keys():
        com[c[0]].append(c[1])
    else:
        com.update({c[0]:[c[1]]})
    if c[1] in com.keys():
        com[c[1]].append(c[0])
    else:
        com.update({c[1]:[c[0]]})
#{1: [2, 5], 2: [1, 3, 5], 3: [2], 5: [1, 2, 6], 6: [5], 4: [7], 7: [4]}
#이런 결과 나오는 과정 살피기.
def abs(n,com):
    result_1.update(com[n])
    if result_1==result_2:
        return
    result_2.update(com[n])
    for i in com[n]:
        for j in com[i]:
            abs(j,com)
abs(1,com)
print(len(result_1)-1)
