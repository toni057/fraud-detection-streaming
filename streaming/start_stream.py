from settings import *
import sys
sys.path.append(ROOT)

import socket
from time import sleep
import numpy as np


if __name__ == "__main__":

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind(('localhost', 12345))
  s.listen(1)

  while True:
      # accept connection
      conn, addr = s.accept()
      while (True):
          # read csv and send one line at a time
          with open(os.path.join(ROOT, 'data', 'data.csv')) as f:
              for i, line in enumerate(f):
                  # skip csv header
                  if (i == 0):
                      continue
                  out = line.encode('utf-8')
                  print('Sending ----> ', line[:-1])
                  conn.send(out)
                  # set message interarrival time to Exp(1)
                  sleep(np.random.exponential(1))
  conn.close()
