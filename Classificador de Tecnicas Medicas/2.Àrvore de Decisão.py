#impotando as bibliotecas necessarias
import pandas as pd 
from sklearn.model_selection import train_test_split #biblioteca para dividir os dados em treino e teste
from sklearn.tree import DecisionTreeClassifier #Arvore de decisão
from sklearn.metrics import accuracy_score #acuracia

#lendo o arquivo
df = pd.read_csv('/content/medico_db_TotalemnteTratado.csv')
df.head()
df.tail()
df.info()

#separando as colunas em entradas e saidas
X = df.drop('tecnica', axis=1)
y = df['tecnica']

#Fazendo o treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

#Criando o classificador
clf = DecisionTreeClassifier()

#treinando o clf com os dados de treino
clf.fit(X_train, y_train)

#fazendo previsão com os testes e calculando seu desempenho
y_pred = clf.predict(X_test)
acuracia = accuracy_score(y_test, y_pred)
print("Acurácia:", acuracia)
