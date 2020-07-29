import numpy as np

def calculate(list):
    ''' This function transforms a list into an 3x3 np array and then returns a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix.'''
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    else: 
        a = np.array(list).reshape(3,3)
        calculations = {
            'mean': [np.mean(a,axis = 0).tolist(),a.mean(axis = 1).tolist(),np.mean(a.flatten()).tolist()],
            'variance': [a.var(axis = 0).tolist(),a.var(axis = 1).tolist(),np.var(a.flatten())],
            'standard deviation': [a.std(axis = 0).tolist(),a.std(axis = 1).tolist(),np.std(a.flatten())],
            'max': [a.max(axis = 0).tolist(),a.max(axis = 1).tolist(),np.max(a.flatten())],
            'min': [a.min(axis = 0).tolist(),a.min(axis = 1).tolist(),np.min(a.flatten())],
            'sum': [a.sum(axis = 0).tolist(),a.sum(axis = 1).tolist(),np.sum(a.flatten())]
        }
        return calculations
