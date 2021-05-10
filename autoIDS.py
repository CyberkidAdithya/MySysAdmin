import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import sys
print("DONE IMPORTING MODULES")

df_train = pd.read_csv("KDD_optimized.csv")
df_train = df_train.iloc[:,:-1] #remove result column
col_names = ["duration","protocol_type","service","flag","src_bytes",
    "dst_bytes","land","wrong_fragment","urgent","hot","num_failed_logins",
    "logged_in","num_compromised","root_shell","su_attempted","num_root",
    "num_file_creations","num_shells","num_access_files","num_outbound_cmds",
    "is_host_login","is_guest_login","count","srv_count","serror_rate",
    "srv_serror_rate","rerror_rate","srv_rerror_rate","same_srv_rate",
    "diff_srv_rate","srv_diff_host_rate","dst_host_count","dst_host_srv_count",
    "dst_host_same_srv_rate","dst_host_diff_srv_rate","dst_host_same_src_port_rate",
    "dst_host_srv_diff_host_rate","dst_host_serror_rate","dst_host_srv_serror_rate",
    "dst_host_rerror_rate","dst_host_srv_rerror_rate","labels"]
df_train.columns = col_names
print("DONE LOADING INTO DATA FRAMES")

del df_train['num_root']
del df_train['rerror_rate']
del df_train['srv_rerror_rate']
del df_train['srv_serror_rate']
del df_train['dst_host_serror_rate']
del df_train['dst_host_srv_rerror_rate']
del df_train['dst_host_srv_serror_rate']
print("REMOVED DUPLICATE COLUMNS FOR SPEED")

df_train['labels'] = df_train['labels'].apply(lambda x : 0 if x=='normal' else 1)   # normal is SAFE
df_train['protocol_type'] = df_train['protocol_type'].apply(lambda x : 0 if x=='tcp' else 1 if x=='udp' else 2)   #tcp is SAFE
df_train['service'] = df_train['service'].apply(lambda x : 0)
df_train['flag'] = df_train['flag'].apply(lambda x : 0 if x=='SF' else 1 if x=='S0' else 2 if x=='RSTR' else 3)   #SF is SAFE
print("\n After conversion: \n", df_train.tail(), sep="")
print("DONE CONVERSION OF VALUES TO NUMBERS")

def create_one_hot_encoding(classes, shape):  #convert categorical data to numbers
    one_hot_encoding = np.zeros(shape)
    for i in range(0, len(one_hot_encoding)):
        one_hot_encoding[i][int(classes[i])] = 1
    return one_hot_encoding
def train(weights, x, y):   #linear regression !
    h = x.dot(weights)
    h = np.maximum(h, 0, h)
    return np.linalg.pinv(h).dot(y)
def soft_max(layer):    # turns a vector of K real values into a vector of K real values that sum to 1
    soft_max_output_layer = np.zeros(len(layer))
    for i in range(0, len(layer)):
        numitor = 0
        for j in range(0, len(layer)):
            numitor += np.exp(layer[j] - np.max(layer))
        soft_max_output_layer[i] = np.exp(layer[i] - np.max(layer)) / numitor
    return soft_max_output_layer
def matrix_soft_max(matrix_):
    soft_max_matrix = []
    for i in range(0, len(matrix_)):
        soft_max_matrix.append(soft_max(matrix_[i]))
    return soft_max_matrix
def check_network_power(o, o_real):
    count = 0
    for i in range(0, len(o)):
        count += 1 if np.argmax(o[i]) == np.argmax(o_real[i]) else 0
    return count
def test(weights, beta, x, y):
    h = x.dot(weights)
    h = np.maximum(h, 0, h)  # ReLU
    o = matrix_soft_max(h.dot(beta))
    return check_network_power(o, y) / len(y)

def runIDS():
    class_column = df_train.shape[1]-1
    print(class_column)

    test_size = 0.1
    db = df_train.iloc[:, :].values.astype(np.float)
    np.random.shuffle(db)
    y = db[:, class_column]
    y -= np.min(y)
    output_layer_perceptron_count = len(np.unique(y))
    y = create_one_hot_encoding(y, (len(y), len(np.unique(y))))
    x = np.delete(db, [class_column], axis=1)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size)
    hidden_layer_perceptron_count = len(y_test)
    x = preprocessing.normalize(x)
    weights = np.random.random((len(x[0]), hidden_layer_perceptron_count))
    beta = train(weights, x_train, y_train)
    accuracy_val = test(weights, beta, x_test, y_test)
    print("Accuracy = %s." % accuracy_val)
runIDS()