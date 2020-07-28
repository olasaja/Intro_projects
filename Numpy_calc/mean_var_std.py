import numpy as np

def calculate(list):
    ''' This function transforms a list into an 3x3 np array and then returns a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix.'''
    a = np.array(list).reshape(3,3)
    #mean_a = [np.mean(a,axis = 0),a.mean(axis = 1),np.mean(a.flatten())]
    #var_a = [a.var(axis = 0),a.var(axis = 1),np.var(a.flatten())]
    #sd_a = [a.std(axis = 0),a.std(axis = 1),np.std(a.flatten())]
    #max_a = [a.max(axis = 0),a.max(axis = 1),np.max(a.flatten())]
    #min_a = [a.min(axis = 0),a.min(axis = 1),np.min(a.flatten())]
    #sum_a = [a.sum(axis = 0),a.sum(axis = 1),np.sum(a.flatten())]
    calculations = {
        'mean': [np.mean(a,axis = 0).tolist(),a.mean(axis = 1).tolist(),np.mean(a.flatten()).tolist()],
        'var': [a.var(axis = 0).tolist(),a.var(axis = 1).tolist(),np.var(a.flatten())],
        'sd': [a.std(axis = 0).tolist(),a.std(axis = 1).tolist(),np.std(a.flatten())],
        'max': [a.max(axis = 0).tolist(),a.max(axis = 1).tolist(),np.max(a.flatten())],
        'min': [a.min(axis = 0).tolist(),a.min(axis = 1).tolist(),np.min(a.flatten())],
        'sum': [a.sum(axis = 0).tolist(),a.sum(axis = 1).tolist(),np.sum(a.flatten())]
    }
    return calculations

l1 = [0,1,2,3,4,5,6,7,8]
print(calculate(l1))