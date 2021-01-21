comb_1 = int(input("Digite o número total de elementos: "))
comb_2 = int(input("Digite o número de elementos de cada grupo: "))
l = comb_1
k = comb_2

x = comb_1 - comb_2
if x == 0:
    x = 1


element_1 = 1

while comb_1 > 0:
    element_1 = comb_1 * element_1
    comb_1 -= 1

element_2 = 1
while comb_2 > 0:
    element_2 = element_2 * comb_2
    comb_2 -= 1



element_3 = 1
while x > 0:
    element_3 = x * element_3
    x -= 1


y = round(element_1/(element_2*element_3))
print(f"A combinação simples entre {l} e {k}; C:{l},{k} ; é igual a {y}")