import time
import collections

ora ="oraoraoraroaroaroaroaroaroaroaroaroaroaoraoraoraoraoraoraoroaroaroaroaroaoraoraoraoroaroaroaroaroaoraoraoraoraoraoraoraoraoroaraoroaraora"

def conv (str):
   if str is not None:
       c = collections.Counter(str).most_common()
       return c

for i in range(250000, 25250000, 100000):
    a = [0] * 10
    for j in range(len(a)):
        tiempo_inicial = time.time()  # segundos
        conv(ora)
        duracion = time.time() - tiempo_inicial
        a[j] = duracion

    acc = 0
    promedio = sum(a) / len(a)
    for j in a:
        acc += (j - promedio) ** 2
    des_std = (acc / (len(a) - 1)) ** 0.5
    print(i, promedio, des_std)
