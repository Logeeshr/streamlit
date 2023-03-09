import pickle
import streamlit as st
import pandas as pd
import numpy as np
import requests
from streamlit_lottie import st_lottie

loaded_model = pickle.load(open("D:/Cuistomer_Conversion/Xgb_model", "rb"))


st.set_page_config(page_title='Customer_Conversion', page_icon=':moneybag:', layout='wide')

#Animations 
def load_lottieur(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()  
lottie_coding = load_lottieur("https://assets8.lottiefiles.com/packages/lf20_v3jtadhg.json")  


#title 
left_column,right_column = st.columns(2)
with left_column:
    st.title(":blue[_ABC LIFE INSURANCE_]")
    st.subheader(":red[_Customer Conversion Predictor_]")

with right_column:
    st_lottie(lottie_coding,height=150, key='codings')
    
    
    
#background image
def add_bg_from_url():
  st.markdown(
     f"""
     <style>
     .stApp {{
         background-image: url("https://assets.kpmg.com/is/image/kpmg/Insurance-insights-banner:cq5dam.web.1400.350");
         background-attachment: auto;
         background-size: cover
     }}
     </style>
     """,
     unsafe_allow_html=True
 )
  
add_bg_from_url()

job_encoded = {'student':10,
              'retired': 9,
              'unemployed': 8,
              'management': 7,
              'admin': 6, 
              'self-employed': 5, 
              'technician': 4,
              'services': 3,
              'housemaid': 2,
              'entrepreneur': 1, 
              'blue-collar': 0}

marital_encoded = {'single':2,
                   'divorced':1,
                   'married':0}

education_qual_encoded = {'tertiary':3,
                          'unknown':2,
                          'secondary':1,
                          'primary':0}

month_encoded = {'mar': 11, 
                 'dec': 10,
                 'sep': 9,
                 'oct': 8,
                 'apr': 7,
                 'feb': 6,
                 'aug': 5,
                 'jun': 4,
                 'nov': 3,
                 'jan': 2,                                                       
                 'jul': 1,                             
                 'may':0}

y = {'yes':1, 'no':0}

call_type_encoded = {'cellular':2,
                     'telephone':1,
                     'unknown':0}


prev_outcome_encoded = {'success':3,
                        'other':2,
                        'failure':1,
                        'unknown':0}

Y = {1 : "Purchase Insurance", 0 : "not Purchase Insurance "}



def main():
    
    Age = st.slider("Select the Age of person",0,100,25)
   
    Marital_status = st.selectbox("Select Marital Status of person",["Married","Single","Divorced"])
    Marital_status = Marital_status.lower()
    
    Job =  st.selectbox("Select Occupation of the person",['Management', 'Technician', 'Entrepreneur', 'Blue-collar', 'Retired', 
                                             'Admin', 'Services', 'Self-employed', 'Unemployed', 'Housemaid', 'Student'])
    Job = Job.lower()
    
    Education = st.selectbox("Select Educational Qualification", ["Tertiary", "Secondary", "Primary", "Unknown"])
    Education = Education.lower()
    
    Month = st.selectbox("Last Contacted Month", ["January", "February", "March", "April" , "May", "June", 
                                                  "July", "August" , "September" , "October", 'November', 'December'])
    Month = Month[:3].lower()
    
    Day = st.slider("Select the date of the month",0,30,15)
    
    
    call_types = st.selectbox("Select last call type", ["Cellular", "Telephone",'Unknown'])
    call_types = call_types.lower()
    
    
    
    Duration = st.slider("Select the Duration of the call",0,1000,100)
    
    Total_calls = st.slider("Select the Number of times you called",0,20,3)
    
    previous_outcome = st.selectbox("Select Previous response",['Unknown', 'Failure', 'Other', 'Success'])
    previous_outcome = previous_outcome.lower()
    
    if st.button("Predict"):
        
        age = Age
        
        job = job_encoded[Job]
        
        marital = marital_encoded[Marital_status]
        
        education_qual = education_qual_encoded[Education]
        
        call_type = call_type_encoded[call_types]
        
        day = Day
        
        mon = month_encoded[Month]
        
        dur = Duration
        
        num_calls = Total_calls
        
        prev_outcome = prev_outcome_encoded[previous_outcome]
        
        input_values = [age,job,marital,education_qual,call_type,day,mon,dur,num_calls,prev_outcome]
        input_array = np.array([input_values])
        result = loaded_model.predict(input_array)
        result_1 = Y[int(result[0])]
        st.write("Based on the given inputs above mentioned person will ",result_1)
        
    
        
        
        
        
    
    
    


if __name__ == "__main__":
  main()




















