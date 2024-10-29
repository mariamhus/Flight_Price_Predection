
import streamlit as st
import pandas as pd
import sklearn
import xgboost
import joblib

model = joblib.load("Final_Model.pkl")
inputs = joblib.load("Inputs.pkl")


def Prediction(Airline,Source,Destination,Total_Stops,Journey_day,Dep_hour,Arrival_hour,Dep_Period):
    df = pd.DataFrame(columns=inputs)
    df.at[0,'Airline'] = Airline
    df.at[0,'Source'] = Source
    df.at[0,'Destination'] = Destination
    df.at[0,'Total_Stops'] = Total_Stops
    df.at[0,'Journey_day'] = Journey_day
    # df.at[0,'Journey_month'] = Journey_month
    df.at[0,'Dep_hour'] = Dep_hour
    df.at[0,'Arrival_hour'] = Arrival_hour
    # df.at[0,'Arrival_min'] = Arrival_min
    df.at[0,'Dep_Period'] = Dep_Period
#     df.at[0,'Duration_mins'] = Duration_mins
#     df.at[0,'Duration_hours'] = Duration_hours
    result = model.predict(df)
    return result[0]
    
def get_period_per_day(r):
    if int(r) in range(5,13) : 
        return "Morning"
    elif int(r) in range(13,18):
        return "Afternoon"
    elif int(r) in range(18,23):
        return "Evening"
    else:
        return "Night" 
    
def main():
    st.title("Flights Price Prediction")
    Airline = st.selectbox("Airline" , ['Air India', 'Jet Airways', 'IndiGo', 'SpiceJet','Multiple carriers', 'GoAir', 'Vistara', 'Air Asia'])
    Source = st.selectbox("Source" , ['Kolkata', 'Delhi', 'Banglore', 'Chennai', 'Mumbai'])
    Destination = st.selectbox("Destination" , ['Banglore', 'Cochin', 'New Delhi', 'Kolkata', 'Delhi', 'Hyderabad'])
    Total_Stops = st.selectbox("Stops" , [0,1,2, 3, 4])
    Journey_day = st.selectbox("Day of Journey" , range(1,32))
    # Journey_month = st.selectbox("Month of Journey" ,['May', 'June', 'March', 'April'] )
    Dep_hour = st.selectbox("Departure Hour" , range(0,24))
    Arrival_hour = st.selectbox("Arrival Hour" , range(0,24))
    Dep_Period = get_period_per_day(Dep_hour)
    Arrival_Period = get_period_per_day(Arrival_hour)
    
    if st.button("Predict"):
        result = Prediction(Airline,Source,Destination,Total_Stops,Journey_day,Dep_hour,Arrival_hour,Dep_Period)
        st.text(f"{result} $")
        st.write(result, " $")
main()
    
