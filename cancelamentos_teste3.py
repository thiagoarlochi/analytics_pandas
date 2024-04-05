import pandas as pd
import plotly.express as px

tabela = pd.read_csv("cancelamentos_sample.csv")

#Limpando colunas inúteis
tabela = tabela.drop(columns="CustomerID")

#Limpar linhas vazias
tabela = tabela.dropna()
print(tabela.info())

#Saber a porcentagem de clientes que cancelaram
print(tabela["cancelou"].value_counts(normalize=True).map("{:.0%}".format))



#Criando o loop para criar os gráficos automaticamente
for coluna in tabela.columns:

    grafico = px.histogram(tabela, x=coluna, color="cancelou")

#Exibir o gráfico 

    grafico.show()

    # Se o problema for resolvido, como vai impactar nos cancelamentos?
tabela = tabela[tabela["duracao_contrato"]!= "Monthly"]
tabela = tabela[tabela["ligacoes_callcenter"]<= 4]
tabela = tabela[tabela["dias_atraso"]<= 20]

print(tabela["cancelou"].value_counts(normalize=True).map("{:.0%}".format))
print('teste')




