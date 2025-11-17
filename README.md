# Análise de Acidentes Aéreos (1908-2009)

Este projeto analisa o dataset "**airplane.csv**" para identificar tendências históricas na segurança da aviação.

---

## O que este script faz:
* Carrega os dados usando `pandas`.
* Limpa e transforma a coluna de datas (`Date`).
* Agrega os dados para contar o número de acidentes por ano.
* Gera um gráfico de linha com `matplotlib` mostrando a tendência ao longo do tempo.
* Exporta o resultado agregado para `acidentes_por_ano.csv` (que está ignorado pelo .gitignore).

---

## Conclusão da Análise 📊
A análise mostra que o **número absoluto de acidentes** aéreos atingiu o pico por volta dos anos 1970/1990 e, desde então, tem **diminuído drasticamente**.

Considerando o **crescimento massivo** no número total de voos ✈️, esta tendência comprova que a aviação se tornou **muito mais segura** ao longo das décadas (a taxa de acidentes por voo caiu).
<img width="640" height="480" alt="grafico_acidentes_aereos" src="https://github.com/user-attachments/assets/e545e6ea-d10a-447a-8e49-74786084db20" />



---

## Como executar:
1.  Certifique-se de ter o Python e o Git instalados.
2.  Clone este repositório.
3.  Instale as bibliotecas necessárias:
    ```bash
    pip install pandas matplotlib
    ```
4.  Execute o script:
    ```bash
    python main.py
    ```