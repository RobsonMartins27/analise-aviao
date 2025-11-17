# --- Análise para saber se os acidentes por ano aumentou ou diminuiu durante os anos. ---
# autor: Robson Martins
# Versão: 1.0

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("airplane.csv")
print("--- As 5 primeiras linhas ---")
print(df.head())

print("""
      --- Informações técnicas ---
      """)
# Aqui estou olhando as informações como data type de cada coluna/cabeçalho
# Aqui eu transformei a coluna Date para o tipo de Data, antes estava como objeto
df['Date'] = pd.to_datetime(df['Date'])
print(df.info())

# aqui estou criando uma nova coluna chamada Year, e o dt.year reconhece na coluna Date um número que seja semelhante a um ano, em diversos formatos.
df['Year'] = df['Date'].dt.year

# imprimir as 5 primeiras linhas para verificar a nova coluna
print(df.head())

# Atribuí a uma nova varíavel, utilizei o values_count para fazer a contagem e o sort_index para mostrar a quantidades de acidentes na ordem do index.
acidentes_por_ano = df['Year'].value_counts().sort_index()

# aqui estou salvando o novo arquivo para consultar em outras ferramentas como Power Bi, Looker ou Tableau
acidentes_por_ano.to_csv("acidentes_por_ano.csv")

# utilizei o plot para desenhar uma linha do tempo com a varíavel e o show para mostrar em uma janela para o usuário.
plt.plot(acidentes_por_ano)
plt.show()