comb_1 = int(input("Quantas incógnitas possui a combinação? "))
comb_2 = int(input("Qual o valor total que a equação assume? "))

condicao = input("O zero entra como uma possível solução para as incógnitas? [tecle s/n]  ")

if condicao == "s":
    z = comb_1 - 1

    total_comb = z + comb_2


    valor_1 = 1
    while total_comb > 0:
        valor_1 = total_comb * valor_1
        total_comb -= 1
    valor_2 = 1
    while z > 0:
        valor_2 = valor_2 * z
        z -= 1

    valor_3 = 1
    while comb_2 > 0:
        valor_3 = valor_3 *comb_2
        comb_2 -= 1


    comb_comp = valor_1/(valor_2*valor_3)

    print(comb_comp)
elif condicao == "n":
    cond_1 = int(input("Qual o valor mínimo que cada incógnita pode receber? "))

    igualdade_menor = comb_1 * cond_1

    total_menor = comb_2 - igualdade_menor

    k = comb_1 - 1
    total_fat_menor = total_menor + k

    total = 1
    while total_fat_menor > 0:
        total = total * total_fat_menor
        total_fat_menor -= 1

    total_inc = 1
    while k > 0:
        total_inc = total_inc * k
        k -= 1
    total_inc2 = 1
    while total_menor > 0:
        total_inc2 = total_inc2 * total_menor
        total_menor -= 1
    
    total_x = total/(total_inc*total_inc2)

    print(f"O total de combinações completas possíveis é igual a {total_x}")

else:
    print("Erro. referido à terceira opção inválido.")


