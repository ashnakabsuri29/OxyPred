from tensorflow.keras.models import load_model
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from flask import Response
from pickle import load
class RegressorRNN:
    dataset_train = pd.read_excel('IOEL_NEXTDAY_DATASET.xlsx')
    training_set = dataset_train.iloc[:,1:2].values
    sc = load(open('scaler.pkl', 'rb'))
    regressor = load_model('IOE_RNN')
    # dataset_test = pd.read_csv('IOE_RNN_TEST4.csv')
    
    def predictor(self,dataset_test):
        original_cases = dataset_test.iloc[:,0].values
        dataset_total = pd.concat((self.dataset_train['newCases'],dataset_test['newCases']),axis = 0)
        inputs = dataset_total[len(dataset_total)-len(dataset_test)-20:].values
        inputs = inputs.reshape(-1,1)
        inputs = self.sc.transform(inputs)
        x_test = []
        for i in range(20,50):
            x_test.append(inputs[i-20:i,0])
        x_test = np.array(x_test)
        x_test = np.reshape(x_test,(x_test.shape[0],x_test.shape[1],1))
        predicted_cases = self.regressor.predict(x_test)
        predicted_cases = self.sc.inverse_transform(predicted_cases)
        return original_cases,predicted_cases
    
    def plotter(self,original_cases,predicted_cases):
        plt.rcParams["figure.figsize"] = [7.50, 3.50]
        fig = plt.figure()
        plt.plot(original_cases, color = 'red', label = 'Original Cases')
        plt.plot(predicted_cases, color = 'blue', label = 'Predicted Cases')
        plt.title('Hypoxia Patients Prediction')
        plt.xlabel('Days')
        plt.ylabel('Cases')
        plt.legend()
        
        
        output = io.BytesIO()
        FigureCanvas(fig).print_png(output)
        return Response(output.getvalue(), mimetype='image/png')


