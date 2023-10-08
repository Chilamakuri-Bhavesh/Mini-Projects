{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bbd9cda3",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "from sklearn.tree import DecisionTreeRegressor\n",
    "from sklearn.preprocessing import LabelEncoder\n",
    "from sklearn.metrics import mean_squared_error, r2_score\n",
    "\n",
    "import streamlit as st\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "asia= pd.read_excel(\"ASIA.xlsx\")\n",
    "asia.dropna(inplace=True)\n",
    "europe=pd.read_excel(\"EUROPE.xlsx\")\n",
    "\n",
    "label_encoder = LabelEncoder()\n",
    "asia[\"Country\"]=label_encoder.fit_transform(asia['Country'])\n",
    "europe[\"Country\"]=label_encoder.fit_transform(europe['Country'])\n",
    "\n",
    "\n",
    "x_train= asia.iloc[:,:-1]\n",
    "y_train= asia.iloc[:,-1:]\n",
    "#x_test= europe.iloc[:,:-1]\n",
    "y_test= europe.iloc[:,-1:]\n",
    "\n",
    "dt_regressor = DecisionTreeRegressor()\n",
    "dt_regressor.fit(x_train, y_train)\n",
    "\n",
    "\n",
    "st.title(\"DENGUE CASES PER 100,000 PEOPLE PREDICTION ALGORITHM\")\n",
    "\n",
    "st.subheader(\"ENTER THE VALUES : \")\n",
    "\n",
    "\n",
    "\n",
    "Country_Name = st.number_input(\"Enter the Country Name \")\n",
    "\n",
    "Year =  st.number_input(\"Enter the Year\")\n",
    "\n",
    "Temperature = st.number_input(\"Enter the Average Temperature (Celsius (°C))\")\n",
    "\n",
    "Wind_Speed = st.number_input(\"Enter the Average Wind Speed (m/s) \")\n",
    "\n",
    "Average_Relative_Humidity  = st.number_input(\"Enter the Average Relative Humidity (%)\")\n",
    "\n",
    "Geographic_Average_Precipitation = st.number_input(\"Enter the Geographic_Average Precipitation (mm/day)\")\n",
    "\n",
    "\n",
    "di={\"Country\":Country_Name,\"Year\":Year,\"Geographic_Average Temperature at 2 Meters (Celsius (°C))\":Temperature,\n",
    "        \"Geographic_Average Wind Speed at 10M Range (m/s)\":Wind_Speed,\n",
    "            \"Geographic_Average Relative Humidity at 2 Meters (%) \":Average_Relative_Humidity,\n",
    "    \"Geographic_Average Precipitation (mm/day)\":Geographic_Average_Precipitation}\n",
    "\n",
    "x_test=pd.DataFrame([di])\n",
    "y_pred = dt_regressor.predict(x_test)\n",
    "\n",
    "result = y_pred\n",
    "\n",
    "st.subheader(\"PREDICTED DENGUE CASES PER 100,000 PEOPLE : \")\n",
    "st.write(result)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}