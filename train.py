import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np


data_dict = pickle.load(open(r'C:\Users\Lin Can\Desktop\Handsign project\Handsign_detection\data.pickle', 'rb'))
#214

length_counts = {len(item): data_dict['data'].count(item) for item in data_dict['data']}

print(length_counts)

data = np.array(data_dict['data'], dtype=float)

labels = np.array(data_dict['labels'])

x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)

print(type(x_train))
print(type(y_train))
print("CIAOOO")

model = RandomForestClassifier()

model.fit(x_train, y_train)

y_predict = model.predict(x_test)

score = accuracy_score(y_predict, y_test)

print('{}% of samples were classified correctly !'.format(score * 100))

f = open('model.p', 'wb')
pickle.dump({'model': model}, f)
f.close()