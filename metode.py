import pandas as pd
from sklearn.model_selection import train_test_split


data = pd.read_excel("datalatihbaru.xlsx")
data.shape
data.head(10)
data.tail(10)
data.describe()
data.columns
data['SENTIMEN'].value_counts()
x = data.Komentar
y = data.SENTIMEN

x_train, x_test, y_train, y_test = train_test_split (x,y, test_size = 0.22, random_state=90)
print('Banyak data x_train :',len(x_train))
print('Banyak data x_test  :',len(x_test))
print('Banyak data y_train :',len(y_train))
print('Banyak data y_test  :',len(y_test))

from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer, HashingVectorizer
cvec=CountVectorizer()
tvec=TfidfVectorizer()
hvec=HashingVectorizer()

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import BernoulliNB
from sklearn.svm import SVC

clf1 = BernoulliNB()
clf2 = LogisticRegression()
clf3 = RandomForestClassifier()
clf4 = SVC()

from sklearn.pipeline import Pipeline
model= Pipeline([('vectorizer',tvec)
                 ,('classifier',clf1)])
model.fit(x_train,y_train)
y_pred=model.predict(x_test)

from sklearn import metrics
print("Accuracy", metrics.accuracy_score(y_test, y_pred))
print("Confussion Metrics", metrics.confusion_matrix(y_test, y_pred))