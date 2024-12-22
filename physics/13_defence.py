from numpy import *
from matplotlib.pyplot import *
def q(t):
    return 4 * exp(-100 * t) * cos(10**4 * pi * t)
#T = 4 * 10**4
t = linspace(0, 4*10**-3, 1000)

figure(figsize=(20, 6))
plot(t, q(t), label=r'$q(t) = 4e^{-100t} \cdot \cos(10^4 \pi t)$')
title('График зависимости заряда от времени (2 периода)')
xlabel('Время, t (с)')
ylabel('Заряд, q (мкКл)')
grid(True)
legend()
show()
