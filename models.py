import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from sklearn.pipeline import Pipeline


from sklearn.model_selection import GridSearchCV


from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LogisticRegressionCV

from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, NuSVC, LinearSVC 

from sklearn import tree

from sklearn.neural_network import MLPClassifier


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler


#Obtaining data

data  = pd.read_pickle('./imputed_data.pkl')
#data.to_csv("imputed_data.csv")

y = data["Food_InsecurityLevel"]

all_columns = list(data.columns)
columns_of_interest = ['HHsizemembers', 'HHsizeMAE', 'LandOwned']
col_indeces = []

for col in columns_of_interest:
	col_indeces.append(all_columns.index(col))


X_reduced = data.iloc[:, col_indeces]
#print(data_reduced)

#print(data_reduced_array)


# Support functions

def scale_data(X):
	scaler = MinMaxScaler()
	for col in X.columns:
		X[col] = scaler.fit_transform(X[col].to_numpy().reshape(-1,1))[:,0]
	return X


def split_data(X,y):
	X_array = X.to_numpy()
	y_array = y.to_numpy()
	X_train, X_test, y_train, y_test = train_test_split(X_array, y_array, test_size=0.3) 
	return X_train, X_test, y_train, y_test



X_reduced = scale_data(X_reduced)
X_train, X_test, y_train, y_test = split_data(X_reduced, y)


#Metrics





"""
# Models
# Logistic regression
def ridge(X_train, X_test, y_train, y_test):
	reg = LogisticRegression(penalty='l1', solver='saga') 
	reg.fit(X_train, y_train)
	accuracy = reg.score(X_test, y_test)
	print(accuracy)

def ridgecv(X_train, X_test, y_train, y_test):
	reg = LogisticRegressionCV(cv=5, random_state=0, penalty='l1', solver='saga')
	reg.fit(X_train, y_train)
	accuracy = reg.score(X_test, y_test)
	print(accuracy)

def lasso(X_train, X_test, y_train, y_test):
	reg = LogisticRegression(penalty='l2')
	reg.fit(X_train, y_train)
	accuracy = reg.score(X_test, y_test)
	print(accuracy)

def lassocv(X_train, X_test, y_train, y_test):
	reg = LogisticRegressionCV(cv=5)
	reg.fit(X_train, y_train)
	accuracy = reg.score(X_test, y_test)
	print(accuracy)



# SVMs
def svc(X_train, X_test, y_train, y_test):
	clf = SVC()
	clf.fit(X_train, y_train)
	accuracy = clf.score(X_test, y_test)
	print(accuracy)



def linear_svc(X_train, X_test, y_train, y_test):
	clf = LinearSVC()
	clf.fit(X_train, y_train)
	accuracy = clf.score(X_test, y_test)
	print(accuracy)




def nu_svc(X_train, X_test, y_train, y_test):
	clf = NuSVC()
	clf.fit(X_train, y_train)
	accuracy = clf.score(X_test, y_test)
	print(accuracy)







# KNN
def knn(X_train, X_test, y_train, y_test):
	clf = KNeighborsClassifier(n_neighbors=4)
	clf.fit(X_train, y_train)
	accuracy = clf.score(X_test, y_test)
	print(accuracy)




# Trees
# Decision Tree 
def dct(X_train, X_test, y_train, y_test):
	clf = tree.DecisionTreeClassifier()
	clf.fit(X_train, y_train)
	clf.predict(X_test, y_test)
	#tree.plot_tree(clf) 


# Random Forest




# Neural Network
def nn(X_train, X_test, y_train, y_test):
	clf = MLPClassifier(hidden_layer_sizes=(100,), random_state=1)
	clf.fit(X_train, y_train)
	accuracy =  clf.score(X_test, y_test)
	print(accuracy)

"""


# Visualizations

#NN

def nn_vis(time_valid, x_valid, results, history, epochs, cases_scaler):

	time = np.arange(len(dataset_full), dtype="float32") #Time is represented as day x since first covid case

	#Plot x_valid and predicted results on same graph to see how similar they are
	plt.figure(figsize=(10, 6))
	plt.plot(time_valid, x_valid_unscaled, 'r-')
	plt.plot(time_valid, results_unscaled, 'b-')
	plt.title("Validation and Results for confirmed cases")
	plt.xlabel("Time")
	plt.ylabel("Confirmed Cases")
	plt.legend(["True value", "Predicted"])
	plt.show()

	#-----------------------------------------------------------
	# Retrieve a list of list results on training and test data
	# sets for each training epoch
	#-----------------------------------------------------------
	mae=history.history['mae']
	loss=history.history['loss']

	epochs=range(len(loss)) # Get number of epochs

	#------------------------------------------------
	# Plot MAE and Loss
	#------------------------------------------------
	plt.figure(figsize=(10, 6))
	plt.plot(epochs, mae, 'r')
	plt.plot(epochs, loss, 'b')
	plt.title('MAE and Loss')
	plt.xlabel("Epochs")
	plt.ylabel("Accuracy")
	plt.legend(["MAE", "Loss"])
	plt.show()


# Model calling

"""
ridge(X_train, X_test, y_train, y_test)
ridgecv(X_train, X_test, y_train, y_test)
lasso(X_train, X_test, y_train, y_test)
lassocv(X_train, X_test, y_train, y_test)

knn(X_train, X_test, y_train, y_test)

svc(X_train, X_test, y_train, y_test)
linear_svc(X_train, X_test, y_train, y_test)
nu_svc(X_train, X_test, y_train, y_test)

dct(X_train, X_test, y_train, y_test)

nn(X_train, X_test, y_train, y_test)
"""


pipelines = []
pipelines.append(('ridge' , (Pipeline([('scaled' , MinMaxScaler()), ('ridge', LogisticRegression(penalty='l1', solver='saga'))]))))
pipelines.append(('lasso' , (Pipeline([('scaled' , MinMaxScaler()), ('lasso', LogisticRegression(penalty='l2'))]))))
pipelines.append(('knn' , (Pipeline([('scaled' , MinMaxScaler()), ('knn', KNeighborsClassifier(n_neighbors=4))]))))

"""
pipelines.append(('svc' , (Pipeline([('scaled' , MinMaxScaler()), ('svc', SVC())]))))
pipelines.append(('linear_svc' , (Pipeline([('scaled' , MinMaxScaler()), ('linear_svc', LinearSVC())]))))
pipelines.append(('nu_svc' , (Pipeline([('scaled' , MinMaxScaler()), ('nu_svc', NuSVC())]))))
#pipelines.append(('dct' , (Pipeline([('scaled' , MinMaxScaler()), ('dct', tree.DecisionTreeClassifier())]))))
pipelines.append(('nn' , (Pipeline([('scaled' , MinMaxScaler()), ('nn', MLPClassifier(hidden_layer_sizes=(100,)))]))))
"""



ridge_params = {}

lasso_params = {}

knn_params = {}

svc_params = {}

lsvc_params = {}

nusvc_params = {}

dct_params = {}

nn_params = {}



parameters = [ridge_params, lasso_params, knn_params, svc_params, lsvc_params, nusvc_params, dct_params, nn_params]

for (pipe_name, model), p in zip(pipelines, parameters):
	#clf = GridSearchCV(model, p)
	model.fit(X_train ,y_train)
	accuracy = model.score(X_test, y_test)
	print(pipe_name, accuracy)

