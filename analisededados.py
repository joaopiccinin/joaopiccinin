#!/usr/bin/env python
# coding: utf-8

# # Análise de Dados com Python


# In[13]:


import pandas as pd
import plotly.express as px
#importando base de dados
tabela = pd.read_csv(r"Clientes.csv", encoding = 'latin', sep =";")
tabela = tabela.drop("Unnamed: 8", axis = 1)
display(tabela)
print(tabela.info())


# In[11]:


tabela["Salário Anual (R$)"] = pd.to_numeric(tabela["Salário Anual (R$)"], errors = "coerce")
tabela = tabela.dropna()
print(tabela.info())


# In[12]:


display(tabela.describe())


# In[10]:


import plotly.express as px
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x = coluna, y = "Nota (1-100)", text_auto = True, histfunc = "avg", nbins = 10)
    grafico.show()


# In[7]:


#considerações finais
#A origem do cliente não influencia tanto
#Clientes acima de 15 anos são melhores
#Profissão de entretenimento e artistas são melhores
#Profissão e advocacia são piores
#clientes com familias de até 7 pessoas são melhores
#clientes com 10-15 anos de experiencia de trabalho são melhores






