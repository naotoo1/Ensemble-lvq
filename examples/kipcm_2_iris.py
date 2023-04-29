"""Kernel Improved Possibilistic C-Means II clustering example using Iris Data."""

# import prosemble package
import prosemble as ps
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# load some data
X, y = load_iris(return_X_y=True)

# Get data split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Setup the model
ipcm = ps.models.KIPCM2(
    data=X_train,
    c=3,
    num_iter=100,
    epsilon=0.0001,
    ord='fro',
    m=2,
    k=2,
    sigma=10,
    set_centroids='fcm',
    set_U_matrix='fcm',
    plot_steps=True
)

# fit the model
ipcm.fit()

# summary of the objective function
print(ipcm.get_objective_function())

# Get the clustering results of the input vector
print(ipcm.predict())

# Make new prediction
print(ipcm.predict_new(x=X_test))

# Get the learned centroids
print(ipcm.final_centroids())
