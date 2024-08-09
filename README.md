# 🏡 House-Price-Prediction

Welcome to the study on Pune House Price Prediction! With the help of this web tool, users can figure out the cost of a property in Pune depending on several parameters, including location, total area, and the number of bedrooms and bathrooms. It is a useful tool for anyone wishing to purchase or sell real estate in Pune because it makes use of a machine learning algorithm to generate precise predictions.

## 🚀 Features
1. User-Friendly Interface: The web application is built using Flask and has a clean, simple form for inputting house details.

2. Dynamic Location Search: Users can quickly search for and choose destinations inside Pune using a clever dropdown list.

3. Accurate Predictions: To forecast prices, the application makes use of a machine learning model that has been trained on actual housing data.

4. Responsive Design: The program appears fantastic on mobile and desktop platforms.

## 📊 Model of Machine Learning
An open-source housing dataset specific to Pune was used to train the model. A simple linear regression approach was used to create it; however, you are welcome to experiment with different algorithms or fine-tune the current model to improve accuracy.

## 🧠 How It Works
1. Features of the Input House
The user is shown a form to fill out with information regarding the house they are interested in, including:

      •	Count of Bedrooms
 
      •	Total Area in Square Feet
 
      •	Count of the Bathrooms
 
      •	Count of Balconies
 
      •	Location within Pune

2. Estimate Home Prices
After the form is submitted, the program analyzes the data and predicts the house's price using a machine learning model that has already been developed. Next, the prediction appears on the screen.

3. Effective Place Finding
Users may quickly locate and choose the preferred place inside Pune via to the dynamic search option included in the location field.


## 📷 Screenshots
Here’s a sneak peek at the application:

Home Page:
![Screenshot (870)](https://github.com/user-attachments/assets/465ceff1-429a-4534-a63c-9b44bb6cb179)


Prediction Result:

![Screenshot (871)](https://github.com/user-attachments/assets/994fc522-c6af-4bdf-b96c-719e8c937eaf)




## 📝 Documentation
### Code Overview
1. The primary Flask application file that manages user interactions and routes is app.py.

2. The script used to train the machine learning model and save it as model.pkl is contained in train_model.py.

3. run.py: A short script that launches the Flask program.

4. The HTML files needed to render the web pages are located in the templates/folder.

5. The CSS and JavaScript files for styling and extra functionality are located in the static/ directory.

6. requirements.txt: Enumerates every dependency needed to execute the project.

