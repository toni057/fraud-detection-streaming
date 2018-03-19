# fraud-detection-streaming

A ML model for fraud detection, implemented in python.  

The dataset used is the paysim dataset and can be obtained from [kaggle](https://www.kaggle.com/ntnu-testimon/paysim1).

Dataset should be downloaded and put into `data/` folder.

### Dataset information

PaySim simulates mobile money transactions based on a sample of real transactions extracted from one month of financial logs from a mobile money service implemented in an African country. The original logs were provided by a multinational company, who is the provider of the mobile financial service which is currently running in more than 14 countries all around the world.

### Exploratory data analysis

Before training we perform the EDA to explore the dataset, which makes it easier to do feature engineering and selection.

### Sampling due to class imbalance

Given that frauds are a very rare occurrence, the percentage of fraudulent transactions is extremely low, which makes it hard to

### Model selection

Currently model selection is based on a randomised search. An improvement is to implement a search based on bayesian optimisation.

### Model evaluation

The model is evaluated using the ROC and precision-recall curves.

### Complete pipeline packaged in a single class

To make the streaming pipeline easier to implement, entire pipeline (ETL along with the ML model) is wrapped in a single portable class.

### Streaming prototype

A simple streaming prototype is implemented based on socket.


## Streaming instructions

To run the streaming example:
1. Clone the project.
* Run the notebook to create the pipeline.
* Run python start_streaming.py from terminal.
* Open new terminal and run streaming_app.py.
* The app prints classification results along with true classes.


## Project structure
```
├── README.md
├── __init__.py
├── aux
│   └── aux.py
├── data
│   └── data.csv
├── models
│   └── pipeline.pickle
├── notebooks
│   ├── ETL\ and\ model\ fitting.ipynb
│   ├── __init__.py
│   └── settings.py
├── settings.py
└── streaming
    ├── __init__.py
    ├── settings.py
    ├── start_stream.py
    └── streaming_app.py
```
