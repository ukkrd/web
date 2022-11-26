#Learn and Build LR Model Test Example
import pickle

mdl = pickle.load(open('Trained_Model.pkl','rb'))
print('Expected Salary is: ',mdl.predict([[5, 7, 9]]))
