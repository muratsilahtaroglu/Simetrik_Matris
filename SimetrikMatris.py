import numpy as np

n=int(input("Matris Boyutu:"))
random_matris=np.zeros(n**2).reshape(n,n)
np_matris=random_matris
for i in range(n):
    for j in range(i, n):
        random_matris[i][j] = np.random.randint(1,100)
        random_matris[j][i] =  random_matris[i][j]
# np_matris=np.array([3,1,1,1,0,2,1,2,0]).reshape(3,3)
print("matris:",np_matris)

def matris_mulp(matris1, matris2):
    result_matris = np.zeros(len(matris1) ** 2).reshape((len(matris1), len(matris1)))
    for i in range(len(matris1)):
        for j in range(i, len(matris1)):
            toplam = 0
            for k in range(len(matris1)):
                toplam += matris1[i, k] * matris2[k, j]
            result_matris[i,j] = toplam
            result_matris[j,i] = toplam
    return result_matris

def binarydecoder(n):
    z= n
    l = []
    if z < 1:
        return l
    while z >= 1:
        l.append(z % 2)
        z //= 2
    return l


def matris_pow(matris, pow):
    #1.Adım
    stack = [matris]
    bin = binarydecoder(pow)
    # print(f"bin: {bin}")
    for i in range(len(bin)-1):
        stack.append(matris_mulp(stack[-1], stack[-1]))
    #2.Adım
    maxpow2_matris = np.copy(stack[-1])
    result=maxpow2_matris
    for i in range(len(bin) - 1):
        if bin[i] == 1:
            # print(f"i: {i}")
            result = matris_mulp(maxpow2_matris, stack[i])
            stack.append(result)
    #3.Adım
    for k in range(100):
        if pow<=(2**k):
            matris_sayisi=k+1
            break
    for i in range(matris_sayisi-1):
            if i!=matris_sayisi-1:
                n_matris=2**i
            print(f"matris**{n_matris}:",stack[i])
    return result

print(binarydecoder(3))
matris_power=int(input("matris_power:"))
print("***********************************")
print(f"matris**{matris_power}",matris_pow(np_matris, matris_power))
