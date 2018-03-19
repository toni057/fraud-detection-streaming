from settings import *
import sys
sys.path.append(ROOT)

import pickle
import socket
import os

from io import StringIO
from aux.aux import *


if __name__ == "__main__":

    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(('localhost', 12345))

    # read in the model pipeline
    with open(os.path.join(ROOT, 'models', 'pipeline.pickle'), 'rb') as handle:
        predClass = pickle.load(handle)

    # loop and receive data
    while (True):
        try:
            # receive message (incoming transactions to score)
            message = sock.recv(8192).decode('ascii')
            # parse incoming messages, set data frame schema
            d = pd.read_csv(StringIO(message),
                            header=None, names=['step', 'type', 'amount', 'nameOrig', 'oldbalanceOrg', 'newbalanceOrig',
                                                'nameDest', 'oldbalanceDest', 'newbalanceDest', 'isFraud', 'isFlaggedFraud'],
                            dtype = {'step': np.int64,
                                     'type': str,
                                     'amount': np.float64,
                                     'nameOrig': str,
                                     'oldbalanceOrg': np.float64,
                                     'newbalanceOrig': np.float64,
                                     'nameDest': str,
                                     'oldbalanceDest': np.float64,
                                     'newbalanceDest': np.float64,
                                     'isFraud': np.float64,
                                     'isFlaggedFraud': np.float64})

            # Since messages are coming in streams,
            # scoring incoming transactions row by row using a for loop
            for row in d.itertuples():
                print("Prediction: %9s   Actual: %9s " % (predClass.predict(row), ["NON_FRAUD", "FRAUD"][int(row.isFraud)]))

        except:
            pass