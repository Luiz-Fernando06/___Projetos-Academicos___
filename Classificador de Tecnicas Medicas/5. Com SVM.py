#impotando as bibliotecas necessarias
import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn import svm #
from sklearn.metrics import accuracy_score 

#lendo o arquivo
df = pd.read_csv('/content/medico_db_TotalemnteTratado.csv')
df.head()

#separando as colunas em entradas e saidas
X = df[['IdMedico', 'tip_urgencia', 'tip_acomod', 'tipo_cirurgia']]
y = df['tecnica']

#Fazendo o treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

#Criando o classificador
clf = svm.SVC()

#treinando o clf com os dados de treino
clf.fit(X_train, y_train)

#fazendo previsão com os testes e calculando seu desempenho
y_pred = clf.predict(X_test)
acuracia = accuracy_score(y_test, y_pred)
print("Acurácia:", acuracia)

#entradas dos dados
entrada_dicionario = {'IdMedico': int(input('Id Medico(1 até 721): ')),
            'tip_urgencia': float(input('Tipo de Urgencia(0: não urgente ou 1: urgente): ')),
            'tipo_cirurgia': int(input('Tipo de Cirugia (0: cirurgia de alta complexidade, 1: Cirurgia complexa, 2: Cirurgia Média, 3: Procedimento simples, 4: Procedimento estético, 5: Procedimento emergencial): ')),
            'tip_acomod': int(input('Tipo de acomodação(1: Acomodação Comum ou 2: Acomodação de Emergencia): ')),
            }
entrada = pd.DataFrame([entrada_dicionario],  columns=['IdMedico', 'tip_urgencia', 'tip_acomod', 'tipo_cirurgia'])
pred = clf.predict(entrada)
print('Tecnica:', pred)

#criando condicional
if pred == 1:
  print('Tecnica usada: Ola mundo')
else:
  print('Tecnica usada: Eai mundo')
