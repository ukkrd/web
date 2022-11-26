#Learn and Build LR Model Development Example
import sys
sys.path.append("C:/Users/UJJWAL KUMAR/AppData/Local/Programs/Python/Python311/Lib/site-packages")
import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression 
Lreg = LinearRegression()
dataset = pd.read_csv(r"C:\Users\UJJWAL KUMAR\Desktop\python project\recruitment.csv")

f = dataset.iloc[:, :3]
print(f)
l = dataset.iloc[:, -1]
Lreg.fit(f, l) 
#print('Expected Salary is INR > ',Lreg.predict([[5,8,9]]))

pickle.dump(Lreg, open('Trained_Model.pkl','wb'))


