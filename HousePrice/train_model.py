import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle


data = pd.read_csv('Pune house data.csv')

data['size'] = data['size'].str.extract('(\d+)').astype(float)
data = data.dropna(subset=['size', 'total_sqft', 'bath', 'balcony', 'price', 'site_location'])

def convert_sqft_to_num(x):
    try:
        return float(x)
    except:
        tokens = x.split('-')
        if len(tokens) == 2:
            return (float(tokens[0]) + float(tokens[1])) / 2
        return None

data['total_sqft'] = data['total_sqft'].apply(convert_sqft_to_num)
data = data.dropna(subset=['total_sqft'])

X = data[['size', 'total_sqft', 'bath', 'balcony', 'site_location']]
y = data['price']
X = pd.get_dummies(X, columns=['site_location'])


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)

pickle.dump(model, open('model.pkl', 'wb'))
