import list_sum


'''
Esta maneira de testar tambem funciona:
 - BOM:  O teste é repetivel com pouco esforço
 - BOM:  O resultado esperado é checado automaticamente
 - OK:   A falha é visível, mas o output sai bagunçado
 - RUIM: Porém se um dos testes falhar, o restante dos testes nao serao executados.
'''
# É impresso no console a lista que foi testada, o resultado esperado, e a chamada da função que retornará o valor computado.
print("Soma da lista [1, 3, 5] = %s, deveria ser 9" % list_sum.soma_lista(list_sum.numbers))

# A função assert é chamada na função testada, testando se o resultado da função é o esperado.
assert list_sum.soma_lista(list_sum.numbers) == 9
