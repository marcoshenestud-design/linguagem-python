# Calcule:
# a) seno de 30°
# b) cosseno de 60°
# c) tangente de 45°
# Lembre-se de converter para radianos primeiro!

import math as m

senoantes = m.radians(30)
cossenoantes = m.radians(60)
tangenteantes = m.radians(45)

senodepois = m.sin(senoantes)
cossendepois = m.cos(cossenoantes)
tangentedepois = m.tan(tangenteantes)

print(f'Os resuldados foram: \nSeno de 30° é {senodepois}; \nCosseno de 60° é {cossendepois}; \nTangente de 45° é {tangentedepois}.')