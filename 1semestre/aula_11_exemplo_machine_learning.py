#Site com o conteúdo: https://code.tutsplus.com/pt/tutorials/introduction-to-machine-learning-in-python--cms-30623
#Código alterado por Fábio Henrique Cabrini
#Maio de 2020
from sklearn import tree #importa o módulo "tree" do Sklearn Árvore de Decisão
features = [[7, 0.6, 40], [7, 0.6, 41], [37, 600, 37], [37, 600, 38]]
#labels = [galinha, galinha, cavalo, cavalo]
#Uma galinha será representada por 0, enquanto um cavalo será representado por 1
labels = [0, 0, 1, 1]
classif = tree.DecisionTreeClassifier() #Classificador
classif.fit(features, labels)
altura = float(input("Digite a altura do animal:"))
peso = float(input("Digite a o peso do animal:"))
temperatura = float(input("Digite a temperatura do animal:"))
x = classif.predict([[altura, peso, temperatura]])
if x == 0:
    print("O animal é uma Galinha!")
else:
        print("O animal é um Cavalo!") 
#output
# [0]  or a Chicken