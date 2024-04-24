import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('https://raw.githubusercontent.com/YBI-Foundation/Dataset/main/Bank%20Churn%20Modelling.csv')
df.head()
df.info()
df.duplicated('CustomerId').sum()
df=df.set_index('CustomerId')
df.info()
df.['Geography'].value_counts()
df.replace({'Geography':{'France':2, 'Germany':1, 'Spain':0}}, inplace=True)
df['Gender'].value_counts()
df.replace({'Gender':{'Male':0, 'Female':1}}, inplace=True)
df{'Num of Products'}.value_counts()
df.replace({'Num of Products':{1:0, 2:1, 3:1,4:1}}, inplace=True)
df['Has Credit Card'].value_counts()
df['Is Active Member'].value_counts()
df.loc[(df['Balance']==0), 'Churn'].value_counts()
df['Zero Balance']=np.where(df['Balance']>0, 1, 0)
df['Zero Balance'].hist()
df.groupby(['Churn', 'Geogrephy']).count()
df.columns
x=df.drop(['Surname','Churn'], axis = 1)
y=df['Churn']
x.shape, y.shape
df['Churn'].value_counts()
sns.countplot(x='Churn', data=df) 
x.shape, y.shape
from imblearn.under_sampling import RandomUnderSampler
rus=RandomUnderSampler(random_state=2529)
x_rus, y_rus= rus.fit_resample(x,y)
x_rus.shape, y_rus.shape, x.shape, y.shape
y.value_counts()
y_rus.value_counts()
y-rus.plot(kind='hist')
from imblearn.over_sampling import RandomOverSampler
ros=RandomOverSampler(random_state=2529)
x_ros, y_ros= ros.fit_resample(x,y)
x_ros.shape, y_ros.shape, x.shape, y.shape
y.value_counts()
y_ros.value_counts()
y-ros.plot(kind='hist')
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3, random_state=2529)
x_train_rus, x_test_rus, y_train_rus, y_test_rus = train_test_split(x_rus,y_rus,test_size=0.3, random_state=2529)
x_train_ros, x_test_ros, y_train_ros, y_test_ros = train_test_split(x_ros,y_ros,test_size=0.3, random_state=2529)
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train[['CreditScore','Age','Tenure','Balance','Estimated Salary']]=sc.fit_transform(X_train[['Creditscore','Age','Tenure','Balance','Estimated salary']])
x_test[['CreditScore','Age','Tenure','Balance','Estimated Salary']]=sc.fit_transform(X_test[['Creditscore','Age','Tenure','Balance','Estimated salary']])
x_train_rus[['CreditScore','Age','Tenure','Balance','Estimated Salary']]=sc.fit_transform(X_train_rus[['Creditscore','Age','Tenure','Balance','Estimated salary']])
x_test_rus[['CreditScore','Age','Tenure','Balance','Estimated Salary']]=sc.fit_transform(X_test_rus[['Creditscore','Age','Tenure','Balance','Estimated salary']])
x_train_ros[['CreditScore','Age','Tenure','Balance','Estimated Salary']]=sc.fit_transform(X_train_ros[['Creditscore','Age','Tenure','Balance','Estimated salary']])
x_test_ros[['CreditScore','Age','Tenure','Balance','Estimated Salary']]=sc.fit_transform(X_test_ros[['Creditscore','Age','Tenure','Balance','Estimated salary']])
from sklearn.svm import SVC
svc=SVC()
svc.fit(x_train,y_train)
y_pred=svc.predict(x_test)
from sklearn.metrics import confusion_matrix, classification_report
confusion_matrix(y_test, y_pred)
print(classification_report(y_test,y_pred))
from sklearn.model_selection import GridSearchCV
param_grid={'C':[0.1,1,10], 'gamma':[1,0.1,0.01], 'kernel':['rbf'], 'class_weight':['balanced']}
grid=GridSearchCV(SVC(),param_grid,refit=True,verbose=2,cv=2)
grid.fit(x-train,y_train)
print(grid.best_estimator_)
grid_prediction=grid.predict(x_test)
confusion_matrix(y_test,grid_prediction)
print(classification_report(y_test,grid_predictions))
svc_rus=SVC()
svc_rus.fit(x_train_rus, y_train_rus)
y_pred_rus=svc_rus.predict(x_test_rus)
confusion_matrix(y_test_rus, y_pred_rus)
print(classification_report(y_test_rus, y_pred_rus))
param_grid={'C':[0.1,1,10], 'gamma':[1,0.1,0.01], 'kernel':['rbf'], 'class_weight':['balanced']}
grid_rus=GridSearchCV(SVC(),param_grid,refit=True,verbose=2, cv=2)
grid_rus.fit(x_train_rus, y_train_rus)
print(grid_rus.best_estimator_)
grid_prediction_rus=grid_rus.predict(x_test_rus)
confusion_matrix(y_test_rus, grid_prediction_rus)
print(classification_report(y_test_rus,grid_prediction_rus))
svc_ros=SVC()
svc_ros.fit(x_train_ros,y_train_ros)
y_pred_ros=svc_ros.predict(x_test_ros)
confusion_matrix(y_test_ros, y_pred_ros)
print(classification_report(y_test_ros, y_pred_ros))
param_grid={'C':[0.1,1,10], 'gamma':[1,0.1,0.01], 'kernel':['rbf'], 'class_weight':['balanced']}
grid_ros=GridSearchCV(SVC(),param_grid,refit=True,verbose=2, cv=2)
grid_ros.fit(x_train_ros, y_train_ros)
print(grid_ros.best_estimator_)
grid_prediction_ros=grid_ros.predict(x_test_ros)
confusion_matrix(y_test_ros, grid_prediction_ros)
print(classification_report(y_test_ros,grid_prediction_ros))
print(classification_report(y_test, y_pred))
confusion_matrix(y_test, grid_prediction)
print(classification_report(y_test_rus, y_pred_rus))
print(classification_report(y_test_rus,grid_prediction_rus))
print(classification_report(y_test_ros, y_pred_ros))
print(classification_report(y_test_ros,grid_prediction_ros))