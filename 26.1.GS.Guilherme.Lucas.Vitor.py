#===============================================
#CORES E FORMAÇÃO DO TÍTULO
#===============================================

titulo = "\033[92m" # Verde
reset = "\033[0m"
vermelho = "\033[31m"

print(40 * "=")
print(f"{titulo}SISTEMA DE MONITORAMENTO ESPACIAL{reset}")
print(40 * "=")



#===============================================
#PARTE 1 E 2 (ENTRADA DE DADOS E FORMAÇÃO DAS LISTAS)
#===============================================

tipos_eventos = []
pais = []
regiao = []
cidade = []
area_afetada = []
intensidades = []
numeros_ocorrencias = []


eventos_registrados = int(input("Insira a quantidade de eventos registrados: "))

for i in range(eventos_registrados):
    print(f"\n --- Evento {i + 1} ---")

    tipos_eventos.append(input("Tipo de evento: "))
    pais.append(input("País: "))
    regiao.append(input("Região: "))
    cidade.append(input("Cidade: "))

#Colocar nada da erro
    while True:
        try:
            area = float(input("Área Afetada em km²: "))
            if area < 0:
                print("ERRO: A ÁREA DEVE SER MAIOR QUE O KM²")
            else:
                break  # saiu do loop, valor válido
        except ValueError:
            print("ERRO: COLOQUE ALGUM NÚMERO VÁLIDO!")

    area_afetada.append(area)

    while True:
        try:
            intensidade = int(input("Intensidade de 1 a 10: "))
            if intensidade < 1 or intensidade > 10:
                print("ERRO: A INTENSIDADE DEVE ESTAR ENTRE 1 A 10")
            else:
                break  # saiu do loop, valor válido
        except ValueError:
            print("ERRO: COLOQUE ALGUM NÚMERO VÁLIDO!")

    intensidades.append(intensidade)

    while True:
        try:
            ocorrencia = int(input("Número de ocorrências: "))

            if ocorrencia < 0:
                print("ERRO: O NÚMERO DE OCORRÊNCIAS NÃO PODE SER NEGATIVO!")
            else:
                break

        except ValueError:
            print("ERRO: COLOQUE UM NÚMERO INTEIRO VÁLIDO!")

    numeros_ocorrencias.append(ocorrencia)

#===================================================================
#PARTE 3 (ANÁLISE DE DADOS)
#===================================================================

#Total de eventos registrados
total_eventos = len(tipos_eventos)


#Soma total das áreas afetadas
soma_area = sum(area_afetada)


#Média das intensidades
media_intensidade = sum(intensidades) / total_eventos

#Evento com a maior área afetada
indice_maior_area = area_afetada.index(max(area_afetada))


#Região com o maior número de ocorrencias
indice_maior_ocorrencia = numeros_ocorrencias.index(max(numeros_ocorrencias))
regiao_maior_ocorrencia = regiao[indice_maior_ocorrencia]


#Densidade Média
soma_densidade = 0

for i  in range(total_eventos):

    if area_afetada[i] > 0:

        densidade = numeros_ocorrencias[i] / area_afetada[i]

        soma_densidade += densidade

densidade_media = soma_densidade / total_eventos

#Evento mais Crítico

lista_criticidade = []

for i in range(total_eventos):

    criticidade = intensidades[i] * area_afetada[i]

    lista_criticidade.append(criticidade)

maior_criticidade = max(lista_criticidade)
indice_evento_critico = lista_criticidade.index(maior_criticidade)

#Eventos com intensidade acima da média
eventos_acima_media = 0

for intensidade in intensidades:
    if intensidade > media_intensidade:
        eventos_acima_media += 1

#===================================================================
#PARTE 4 (RELATÓRIO DE ANÁLISE)
#===================================================================
print("\n" + "=" * 40)
print(f"{titulo} RELATÓRIO DE ANÁLISE{reset}")
print("=" * 40)

print(f"\nTotal de eventos registrados: {total_eventos}")

print("\n" + "-" * 40)

print("\nResumo Geral")

print("-" * 40)

print(f"\nÁrea total afetada: {soma_area:.2f} km²")
print(f"\nMédia de intensidade: {media_intensidade:.2f}")

print("\n" + "-" * 40)

print("\nAnálises")

print("-" * 40)

print(f"\nEvento com maior área afetada: {tipos_eventos[indice_maior_area]}")

print(f"\nRegião com maior número de ocorrências: {regiao_maior_ocorrencia}")

print(f"\nQuantidade de eventos acima da média de intensidade: {eventos_acima_media}")

print(f"\nDensidade média de ocorrências: {densidade_media:.2f} ocorrências/km²")

print("\n" + "-" * 40)

print("\nEvento Mais Crítico")

print("-" * 40)

print(f"\nTipo: {tipos_eventos[indice_evento_critico]}")

print(f"\nLocal: {cidade[indice_evento_critico]}, "
      f"{regiao[indice_evento_critico]}, "
      f"{pais[indice_evento_critico]}")

print(f"\nIntensidade: {intensidades[indice_evento_critico]}")

print(f"\nÁrea afetada: {area_afetada[indice_evento_critico]:.2f} km²")

print("\n" + "=" * 40)







