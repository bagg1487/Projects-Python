from numpy import *
from matplotlib.pyplot import *
def q(t):
    return 63 * 10**-6 * cos(1428.58 * t)
t = linspace(0, 88*10**-4, 1000)

figure(figsize=(10, 6))
plot(t, q(t), label=r'$q(t) = 63 \times 10^{-6} \cos(1428.58 t)$')
title('График зависимости заряда от времени (2 периода)')
xlabel('Время, t (с)')
ylabel('Заряд, q (Кл)')
grid(True)
legend()
show()
