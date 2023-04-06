import random
if 230>300:
    N = 20
    masiv = []
    for i in range(N):  
        if i%2 == 1:
            masiv.append(i)
    print(masiv)
    print(len(masiv))
    print(max(masiv))
    print(sum(masiv))
#2
N = 14
masiv = []
for i in range(N):
    if i>0:
        a = pow(2, i)
        masiv.append(a)
print(masiv)




