import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import plotly.express as px


DF=pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")
print (DF.head()) #5 primeiras linhas
print (DF.tail()) #5 ultimas linhas
print (DF.describe()) #resumo estatisticos
print (DF.columns) #colunas
print (DF.dtypes) #tipo de dados
print (DF.shape) #numero de linhas e colunas

print (DF['experience_level'].value_counts())
print (DF['employment_type'].value_counts())
print (DF['remote_ratio'].value_counts())
print (DF['company_size'].value_counts())

novos_nomes = { #Usando dicionario para mudar os nomes da coluna da tabela para um melhor entendimento.
'work_year' : 'ano',
'experience_level' : 'senioridade', 
'employment_type' : 'contrato',
'job_title' : 'cargo', 
'salary' : 'salario',
'salary_currency' : 'moeda',
'salary_in_usd' : 'usd',
'employee_residence' : 'residencia',
'remote_ratio' : 'remoto',
'company_location' : 'empresa',
'company_size' : 'tamanho_empresa'
}

DF.rename( columns=novos_nomes, inplace=True) #verificando resultados
print (DF.head())

senioridade={
    'SE' : 'senior',
    'MI' : 'pleno',
    'EN' : 'junior',
    'EX' : 'executivo'
}
DF['senioridade'] = DF['senioridade'].replace(senioridade) #resultado e quantidade de valores
print (DF['senioridade'].value_counts())

contrato={
    'FT' : 'integral',
    'CT' : 'contrato',
    'PT' : 'parcial',
    'FL' : 'Freelancer',
}
DF ['contrato'] = DF['contrato'].replace(contrato)
print (DF['contrato'].value_counts())

remoto ={
    0 : 'presencial',
    100 : 'remoto',
    50 : 'híbrido',
}
DF ['remoto'] =DF['remoto'].replace(remoto)
print(DF['remoto'].value_counts())

tamanho_empresa ={
    'M' : 'media',
    'L' : 'grande',
    'S' : 'pequena',
}
DF['tamanho_empresa'] = DF['tamanho_empresa'].replace(tamanho_empresa)
print(DF['tamanho_empresa'].value_counts())

print(DF.isnull())
print(DF.isnull().sum())

print(DF['ano'].unique())
print(DF[DF.isnull().any(axis=1)])

DF_limpo =DF.dropna()
print(DF_limpo.isnull().sum())
print(DF_limpo.head())
DF_limpo =DF_limpo.assign(ano = DF_limpo['ano'].astype('int64'))
print(DF_limpo.head())

#parte dos graficos
ordem = DF_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=True).index

plt.figure(figsize=(8,5)) #tamanho do grafico 8(largura) 5(altura)
sns.barplot(data=DF_limpo, x='senioridade', y='usd', order=ordem) #grafico de barras
plt.title('Salário médio por senioridade') #titulo
plt.xlabel('Senioridade') #eixo x
plt.ylabel('Salário médio anual (USD)') #eixo y
plt.show() #exibe o grafico criado

plt.figure(figsize=(10,5))
sns.histplot(DF_limpo['usd'], bins = 50, kde=True) 
plt.title("Distribuição dos salários anuais") 
plt.xlabel("Salário em USD")
plt.ylabel ("Frequência")
plt.show( )

plt.figure(figsize=(8,5))
sns.boxplot (x=DF_limpo[ 'usd' ])
plt.title ("Boxplot salário") 
plt.xlabel("salário em USD")
plt.show( )