import numpy as np
import pickle
import streamlit as st
model=pickle.load(open('weather_models.sav','rb'))
def weather_prediction(input_data):
    inputasarray=np.asarray(input_data)
    input_data_reshape=inputasarray.reshape(1,-1)
    prediction=model.predict(input_data_reshape)
    print(prediction)
    if(prediction==1):
      return "Rainy 🌧️"
    elif(prediction==0):
      return "Cloudy ☁️"
    elif(prediction==3):
      return "Sunny ☀️"
    else:
      return "Snowy ❄️"
def main():
    st.title('🌤️ Weather Prediction App using Machine Learning')
    Temperature=st.text_input('Enter temparutre in celcius')
    Humidity=st.text_input('Enter humididty(1-100)')
    WindSpeed=st.text_input('enter wind Speed')
    Precipitation=st.text_input('Enter precipation level(1-100)')
    CloudCover=st.text_input('Enter cloudCover(party Cloudy:3,Overcast:2,Clear:0,cloudy:1)')
    AtmosphericPressure=st.text_input('Enter Atmospheric Pressure(900-2000)')
    UVIndex=st.text_input('Enter UVIndex(1-10)')
    Season=st.text_input('Enter Season(Autumn:0,Summer:2,Spring:1,Winter:3)')
    Visibility=st.text_input('Enter visiblity in km(1-10)')
    Location=st.text_input('Enter Location(coastal:0,inland:1,mountain:2)')
   
    weather_type=''
    if st.button('Predict Weather'):
        weather_type=weather_prediction([Temperature,Humidity,WindSpeed,Precipitation,CloudCover,AtmosphericPressure,UVIndex,Season,Visibility,Location])
    st.success(weather_type)
main()
