#impotando as bibliotecas necessarias
import pandas as pd 
from sklearn import tree
from sklearn.model_selection import train_test_split #biblioteca para dividir os dados em treino e teste
from sklearn.tree import DecisionTreeClassifier #Arvore de decisão
from sklearn.metrics import accuracy_score #acuracia
import matplotlib.pyplot as plt

#lendo o arquivo
df = pd.read_csv('/content/medico_db_TotalemnteTratado.csv')
df.head()

#separando as colunas em entradas e saidas
X = df[['IdMedico', 'tip_urgencia', 'tip_acomod', 'tipo_cirurgia']]
y = df['tecnica']

#Fazendo o treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

#Criando o classificador
clf = DecisionTreeClassifier(random_state=1)

#treinando o clf com os dados de treino
clf.fit(X_train, y_train)

#fazendo previsão com os testes e calculando seu desempenho
y_pred = clf.predict(X_test)
acuracia = accuracy_score(y_test, y_pred)
print("Acurácia:", acuracia)

data_colunas_uteis = ['IdMedico', 'tip_urgencia', 'tip_acomod', 'tipo_cirurgia']
data_class_names = ['0','1']
tree.plot_tree(clf, feature_names = data_colunas_uteis,class_names= data_class_names, filled = True)
plt.show()
