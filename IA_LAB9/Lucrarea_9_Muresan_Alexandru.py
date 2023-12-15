import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor,MLPClassifier

n_samples=1000
blob_centers=([1,0.5],[3.5,4],[1,3.3],[5,1.2],[6,6],[2,8])
data,labels=make_blobs(n_samples=n_samples,
                       centers=blob_centers,
                       cluster_std=0.5,
                       random_state=0)

X_train,X_test,y_train,y_test=train_test_split(data,labels,test_size=0.2,train_size=0.8)

mlp=MLPClassifier(hidden_layer_sizes=50,max_iter=100,alpha=1e-4,
                  solver="sgd",verbose=10,tol=1e-4,random_state=1,
                  learning_rate_init=0.1)

mlp.fit(X_train,y_train)
print("Training set score",mlp.score(X_train,y_train))
print("Testing set score",mlp.score(X_test,y_test))

