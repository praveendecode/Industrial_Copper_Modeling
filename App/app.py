import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import *
from streamlit_extras.colored_header import colored_header
from streamlit_extras.keyboard_url import keyboard_to_url
import json as js
import numpy as np
from datetime import date
import pickle
import pymongo as pm
import time 
class App:

    def model(self):

        st.set_page_config(page_title='ICM Project By Praveen', layout="wide")

        
        with st.sidebar:  # Navbar
            selected = option_menu(
                menu_title="ICM Workflow",
                options=['Intro', "Classification Model", "Regression Model",'Feedback'],
                icons=['mic-fill', '', '', '', ''],
                menu_icon='alexa',
                default_index=0,
            )

        def lottie(filepath):
            with open(filepath, 'r') as file:
              return js.load(file)
            
        if selected == 'Intro':
            st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)



            # Start Intro
            col1, col2 = st.columns([11, 7])
            with col1:
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")

                st.markdown(
                    "<h1 style='font-size: 79px;'><span style='color:white;'>Howdy ,</span> <span style='color: white;'>I'm </span><span style='color: cyan;'> Praveen</span> </h1>",
                    unsafe_allow_html=True)


            with col2:
                file = lottie("intro1.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=500,
                    width=700,
                    key=None
                )

            st.write("")
            st.write('')
            st.write("")
            st.write('')
            st.write("")
            st.write("")
            st.write('')
            st.write("")
            with col1:
                file = lottie("sound.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=240,
                    width=600,
                    key=None
                )

            col1,col2,col3 = st.columns([3.4,10,2])
            with col2:
                st.markdown(
                    "<h1 style='font-size: 100px;'><span style='color:white;'>Data</span> <span style='color: cyan;'> Scientist </span> <span style='color:white;'></span> <span style='color: white ;'> From </span> <span style='color: cyan;'> India </span></h1>",
                    unsafe_allow_html=True)
                
            col1,col2,col3 = st.columns([8,10,2])
            col2.markdown(
                    "<h1 style='font-size: 27px;'>  <span style='color: cyan;'>To Know About Me  </span> <span style='color: cyan;'>Press 'P'  </span></h1>",
                    unsafe_allow_html=True)
            keyboard_to_url(key="P", url="https://www.linkedin.com/in/praveen-n-2b4004223/")


            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col1,col2,col3 = st.columns([10,10,2])
            with col1:
                st.markdown(
                    "<h1 style='font-size: 100px;'><span style='color:white;'>About </span><span style='color:Cyan;'>ICM Project </span> </h1>",
                    unsafe_allow_html=True)
            col1,col2,col3 = st.columns([2,10,2])
            with col2:
                file = lottie("cyan_boy_lap2.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=800,
                    width=1200,
                    key=None
                )
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
                
            col1,col2,col3 = st.columns([16,10,2])
            with col1:
                st.markdown(
                    "<h1 style='font-size: 100px;'><span style='color:white;'>What has </span><span style='color:Cyan;'>Praveen </span><span style='color:white;'> Done ? </span> </h1>",
                    unsafe_allow_html=True)
            col1,col2,col3 = st.columns([5,10,2])
            col2.write("")
            col2.write("")
            col2.write("")
            with col2:
                file = lottie("boydoubtface.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=800,
                    width=800,
                    key=None
                )
            with col2:
                file = lottie("lets_start.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=900,
                    width=900,
                    key=None
                )
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
        


            col1,col2,col3 = st.columns([16,10,2])
            with col1:
                st.markdown(
                    "<h1 style='font-size: 100px;'><span style='color:white;'> </span><span style='color:Cyan;'>Problem </span><span style='color:white;'> Statement </span> </h1>",
                    unsafe_allow_html=True)
            col1,col2,col3 = st.columns([1,10,1])
            
            with col2:
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.markdown(
                    "<h1 style='font-size: 60px;'><span style='color:white;'> Build </span><span style='color:cyan;'> Regression Model  </span><span style='color:white;'>TO Predict Selling Price </span> </h1>",
                    unsafe_allow_html=True)
                st.markdown(
                    "<h1 style='font-size: 60px;'><span style='color:white;'> Build </span><span style='color:cyan;'> Classification Model  </span><span style='color:white;'>TO Predict Status </span> </h1>",
                    unsafe_allow_html=True)
            # Data collection and understanding
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col1,col2,col3 = st.columns([19,10,1])
            col2.write("")
            col2.write("")
            col2.write("")
            with col1:
                st.markdown(
                    "<h1 style='font-size: 90px;'><span style='color:cyan;'> Data Collection </span><span style='color:white;'> and  </span><span style='color:cyan;'>  Understand </span> </h1>",
                    unsafe_allow_html=True)
            col1,col2,col3 = st.columns([5,10,2])
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            with col2:
                file = lottie("database.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=800,
                    width=900,
                    key=None
                )
            col2.write("")
            col2.write("")
            col2.write("")
            col1,col2,col3 = st.columns([19,10,1])
            col2.write("")
            col2.write("")
            col2.write("")
            with col1:
                st.markdown(
                    "<h1 style='font-size: 90px;'><span style='color:cyan;'> Data </span><span style='color:white;'> Preprocessing </span><span style='color:cyan;'>  </span> </h1>",
                    unsafe_allow_html=True)
            col1,col2,col3 = st.columns([5,10,2])
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            with col2:
                file = lottie("vacuum Cleaner.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=700,
                    width=1000,
                    key=None
                )
            col2.write("")
            col2.write("")
            col2.write("")
            col1,col2,col3 = st.columns([19,10,1])
            col2.write("")
            col2.write("")
            col2.write("")
            with col1:
                st.markdown(
                    "<h1 style='font-size: 90px;'><span style='color:cyan;'> Exploratory </span><span style='color:white;'> Data  </span><span style='color:cyan;'> Analysis </span> </h1>",
                    unsafe_allow_html=True)
            col1,col2,col3 = st.columns([5,10,2])
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            with col2:
                file = lottie("data_exploaration.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=900,
                    width=1000,
                    key=None
                )



            col2.write("")
            col2.write("")
            col2.write("")
            col1,col2,col3 = st.columns([19,10,1])
            col2.write("")
            col2.write("")
            col2.write("")
            with col1:
                st.markdown(
                    "<h1 style='font-size: 100px;'><span style='color:cyan;'> Model </span><span style='color:white;'>  </span><span style='color:white;'> Process </span> </h1>",
                    unsafe_allow_html=True)
            col1,col2,col3 = st.columns([5,10,2])
            col2.write("")
           
            with col2:
                file = lottie("model_training.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=1000,
                    width=1000,
                    key=None
                )
            col2.write("")
            col2.write("")
            col2.write("")
            col1,col2,col3,col4 = st.columns([2,10,10,2])
            with col2:
                file = lottie("sellprice.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=700,
                    width=700,
                    key=None
                )
                
            
            # col1,col2,col3 = st.columns([10,3,10])

            with col3:
                file = lottie("classification.json")
                st_lottie(
                    file,
                    speed=1,
                    reverse=False,
                    loop=True,
                    quality='low',
                    # renderer='svg',
                    height=900,
                    width=900,
                    key=None
                )
            col1,col2,col3,col4 = st.columns([3.6,15,10,2])
            with col2:
                st.markdown(
                    "<h1 style='font-size: 50px;'><span style='color:cyan;'>      Regression </span><span style='color:white;'> Model </span><span style='color:white;'>  </span> </h1>",
                    unsafe_allow_html=True)
            with col3:
                st.markdown(
                    "<h1 style='font-size: 50px;'><span style='color:cyan;'> Classification </span><span style='color:white;'> Model </span><span style='color:white;'> </span> </h1>",
                    unsafe_allow_html=True)
            colored_header(
                    label="",
                    description="",
                    color_name="blue-green-70"
                )
                
                
        elif selected == 'Classification Model':

            st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)
            col1,col2,col3 = st.columns([4,10,2])
            with col2:
                st.markdown(
                    "<h1 style='font-size: 100px;'><span style='color: cyan;'>Classification </span><span style='color: white;'> Model</span> </h1>",
                    unsafe_allow_html=True)
            col1,col2,col3 = st.columns([4,10,5])
            with col2:
                colored_header(
                    label="",
                    description="",
                    color_name="blue-green-70"
                )
            col1,col2,col3 = st.columns([2,10,2])
            # Start from options
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")  

            with col2 :
                st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>Quantity  </span><span style='color: white;'> Ton </span> </h1>",
                    unsafe_allow_html=True)
                qt =  st.number_input('',min_value=0.1, max_value=1000000000.0, value=1.0)
                quantity_log = np.log(qt)

                #___________________________________________________________________________________________
                st.write("")
                st.write("")
                st.markdown(
                "<h1 style='font-size: 40px;'><span style='color: cyan;'>Customer  </span><span style='color: white;'> Value </span> </h1>",
                unsafe_allow_html=True)
                customer =  st.number_input('',min_value=12458.0, max_value=2147483647.0, value=12458.0,)
                #________________________________________________________________________
                st.write("")
                st.write("")
                st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>Country  </span><span style='color: white;'> Code </span> </h1>",
                    unsafe_allow_html=True)
                country =  st.selectbox(' ',[ 28,  38,  78,  27,  30,  32,  77,  25, 113,  26,  39,  40,  84, 80,  79,  89, 107])
                #________________________________________________________________________
                st.write("")
                st.write("")
                st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>Item  </span><span style='color: white;'> Type </span> </h1>",
                    unsafe_allow_html=True)
                cc = {'W':5, 'WI':6, 'S':3, 'Others':1, 'PL':2, 'IPL':0, 'SLAWR':4}
                item_type =  st.selectbox('          ',cc)

                #________________________________________________________________________
                st.write("")
                st.write("")
                st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>Application </span><span style='color: white;'> Code </span> </h1>",
                    unsafe_allow_html=True)
                av =  st.selectbox('          ',[2.0, 3.0, 4.0, 5.0, 10.0, 15.0, 19.0, 20.0, 22.0, 25.0, 26.0, 
                        27.0, 28.0, 29.0, 38.0, 39.0, 40.0, 41.0, 42.0, 56.0, 58.0, 
                        59.0, 65.0, 66.0, 67.0, 68.0, 69.0, 70.0, 79.0, 99.0])
                
                application_log = np.log(av)
                #________________________________________________________________________
                
                st.write("")
                st.write("")
                st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>Product </span><span style='color: white;'> Referal Code</span> </h1>",
                    unsafe_allow_html=True)
                
                pr = [1670798778,     611993, 1668701376,  164141591,     628377,
                                1671863738,     640665, 1332077137, 1668701718,     640405,
                                1693867550, 1665572374, 1282007633, 1668701698,     628117,
                                1690738206,     640400, 1671876026,     628112,  164336407,
                                    164337175, 1668701725, 1665572032,     611728, 1721130331,
                                1693867563,     611733, 1690738219, 1722207579, 1665584662,
                                1665584642,  929423819, 1665584320]
                product_ref = st.selectbox("",pr)

                #________________________________________________________________________
                with col2:
                    st.write("")
                    st.write("")
                    st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>Thickness  </span><span style='color: white;'> Value </span> </h1>",
                    unsafe_allow_html=True)
                    thickness =  st.number_input('',min_value=0.1, max_value=2500.000000, value=1.0)
                    thickness_log = np.log(thickness)
                #________________________________________________________________________
                    st.write("")
                    st.write("")
                    st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>Width  </span><span style='color: white;'> Value </span> </h1>",
                    unsafe_allow_html=True)
                    wv =  st.number_input('',min_value=1.0, max_value=2990.000000, value=1.0)
                    width_log = np.log(wv)

                #________________________________________________________________________
                    st.write("")
                    st.write("")
                    st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>Item  </span><span style='color: white;'> Date </span> </h1>",
                    unsafe_allow_html=True)
                    item_date = st.date_input(label='', min_value=date(1995,1,1), 
                                            max_value=date(2021,12,31), value=date(2021,8,1))
                #__________________________________________________________________________________________________________
                    st.write("")
                    st.write("")
                    st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>Delivery </span><span style='color: white;'> Date </span> </h1>",
                    unsafe_allow_html=True)
                    delivery_date = st.date_input(label='    ', min_value=date(2020,1,1), 
                                            max_value=date(2023,12,31), value=date(2021,8,1))
                #___________________________________________________________________________________________________________
                    st.write("")
                    st.write("")
                    st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>Selling </span><span style='color: white;'> Price </span> </h1>",
                    unsafe_allow_html=True)
                    sp =  st.number_input('',min_value=1.0, max_value=100001015.0, value=1.0)
                    selling_price  = np.log(sp)

                    predict_data = [quantity_log,customer,country,cc[item_type],application_log,thickness_log,width_log,product_ref,item_date.day,
                                    item_date.month,item_date.year,delivery_date.day,delivery_date.month,delivery_date.year,
                                    selling_price]
                    
                    with open('classification_model_icm.pkl', 'rb') as f:
                        model = pickle.load(f)
                col1,col2,col3 = st.columns([10,2,10])
                
                with col1 :
                    st.write("")
                    if st.button('Process'):
                        x = model.predict([predict_data])
                        if x[0] == 1.0:
                            st.markdown(
                                "<h1 style='font-size: 40px;'><span style='color: cyan;'>Predicted Status : </span><span style='color: white;'> Won </span> </h1>",
                                unsafe_allow_html=True)
                            
                        elif x[0] == 0.0:
                            st.markdown(
                            "<h1 style='font-size: 40px;'><span style='color: cyan;'>Predicted Status : </span><span style='color: white;'> Lost </span> </h1>",
                            unsafe_allow_html=True)
                                     
        elif selected == 'Regression Model':
            st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)
            col1,col2,col3 = st.columns([4,10,2])
            with col2:
                st.markdown(
                    "<h1 style='font-size: 100px;'><span style='color: cyan;'>Regression </span><span style='color: white;'> Model</span> </h1>",
                    unsafe_allow_html=True)
            col1,col2,col3 = st.columns([4,10,7])
            with col2:
                colored_header(
                    label="",
                    description="",
                    color_name="blue-green-70"
                )
            col1,col2,col3 = st.columns([2,10,2])
            # Start from options
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")  

            with col2 :
                st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>Quantity  </span><span style='color: white;'> Ton </span> </h1>",
                    unsafe_allow_html=True)
                qt =  st.number_input('',min_value=0.1, max_value=1000000000.0, value=1.0)
                quantity_log = np.log(qt)

                #___________________________________________________________________________________________
                st.write("")
                st.write("")
                st.markdown(
                "<h1 style='font-size: 40px;'><span style='color: cyan;'>Customer  </span><span style='color: white;'> Value </span> </h1>",
                unsafe_allow_html=True)
                customer =  st.number_input('',min_value=12458.0, max_value=2147483647.0, value=12458.0,)
                #________________________________________________________________________
                st.write("")
                st.write("")
                st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>Country  </span><span style='color: white;'> Code </span> </h1>",
                    unsafe_allow_html=True)
                country =  st.selectbox(' ',[ 28,  38,  78,  27,  30,  32,  77,  25, 113,  26,  39,  40,  84, 80,  79,  89, 107])
                #________________________________________________________________________
                st.write("")
                st.write("")
                st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>Item  </span><span style='color: white;'> Type </span> </h1>",
                    unsafe_allow_html=True)
                cc = {'W':5, 'WI':6, 'S':3, 'Others':1, 'PL':2, 'IPL':0, 'SLAWR':4}
                item_type =  st.selectbox('          ',cc)

                #________________________________________________________________________
                st.write("")
                st.write("")
                st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>Application </span><span style='color: white;'> Code </span> </h1>",
                    unsafe_allow_html=True)
                av =  st.selectbox('          ',[2.0, 3.0, 4.0, 5.0, 10.0, 15.0, 19.0, 20.0, 22.0, 25.0, 26.0, 
                        27.0, 28.0, 29.0, 38.0, 39.0, 40.0, 41.0, 42.0, 56.0, 58.0, 
                        59.0, 65.0, 66.0, 67.0, 68.0, 69.0, 70.0, 79.0, 99.0])
                
                application_log = np.log(av)
                #________________________________________________________________________
                
                st.write("")
                st.write("")
                st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>Product </span><span style='color: white;'> Referal Code</span> </h1>",
                    unsafe_allow_html=True)
                
                pr = [1670798778,     611993, 1668701376,  164141591,     628377,
                                1671863738,     640665, 1332077137, 1668701718,     640405,
                                1693867550, 1665572374, 1282007633, 1668701698,     628117,
                                1690738206,     640400, 1671876026,     628112,  164336407,
                                    164337175, 1668701725, 1665572032,     611728, 1721130331,
                                1693867563,     611733, 1690738219, 1722207579, 1665584662,
                                1665584642,  929423819, 1665584320]
                product_ref = st.selectbox("",pr)

                #________________________________________________________________________
                with col2:
                    st.write("")
                    st.write("")
                    st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>Thickness  </span><span style='color: white;'> Value </span> </h1>",
                    unsafe_allow_html=True)
                    thickness =  st.number_input('',min_value=0.1, max_value=2500.000000, value=1.0)
                    thickness_log = np.log(thickness)
                #________________________________________________________________________
                    st.write("")
                    st.write("")
                    st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>Width  </span><span style='color: white;'> Value </span> </h1>",
                    unsafe_allow_html=True)
                    wv =  st.number_input('',min_value=1.0, max_value=2990.000000, value=1.0)
                    width_log = np.log(wv)

                #________________________________________________________________________
                    st.write("")
                    st.write("")
                    st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>Item  </span><span style='color: white;'> Date </span> </h1>",
                    unsafe_allow_html=True)
                    item_date = st.date_input(label='', min_value=date(1995,1,1), 
                                            max_value=date(2021,12,31), value=date(2021,8,1))
                #__________________________________________________________________________________________________________
                    st.write("")
                    st.write("")
                    st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>Delivery </span><span style='color: white;'> Date </span> </h1>",
                    unsafe_allow_html=True)
                    delivery_date = st.date_input(label='    ', min_value=date(2020,1,1), 
                                            max_value=date(2023,12,31), value=date(2021,8,1))
                #___________________________________________________________________________________________________________
                    st.write("")
                    st.write("")
                    st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>Status </span><span style='color: white;'> Code </span> </h1>",
                    unsafe_allow_html=True)
                    status_code = {'Won':1, 'Draft':2, 'To be approved':3, 'Lost':0, 'Not lost for AM':5, 'Wonderful':6, 'Revised':7, 'Offered':8, 'Offerable':4}
                    Status =  st.selectbox('             ',status_code) 
               
                #_____________________________________________________________________________________________________________
                    
                    predict_data = [quantity_log,customer,country,cc[item_type],application_log,thickness_log,width_log,product_ref,item_date.day,
                                    item_date.month,item_date.year,delivery_date.day,delivery_date.month,delivery_date.year,
                                    status_code[Status]]
                    
                    with open('regression_model.pkl', 'rb') as f:
                        model = pickle.load(f)
                col1,col2,col3 = st.columns([10,1,10])
                
                with col1 :
                    st.write("")
                    if st.button('Process'):
                        x = model.predict([predict_data])
                        st.markdown(
                                f"<h1 style='font-size: 40px;'><span style='color: cyan;'>Predicted Selling Price : </span><span style='color: white;'> {np.exp(x[0])}</span> </h1>",
                                unsafe_allow_html=True)
                            
        elif selected == 'Feedback':
            praveen_1 = pm.MongoClient(
                'mongodb://praveen:praveenroot@ac-cd7ptzz-shard-00-00.lsdge0t.mongodb.net:27017,ac-cd7ptzz-shard-00-01.lsdge0t.mongodb.net:27017,ac-cd7ptzz-shard-00-02.lsdge0t.mongodb.net:27017/?ssl=true&replicaSet=atlas-ac7cyd-shard-0&authSource=admin&retryWrites=true&w=majority')
            db = praveen_1['Feedback_icm']
            collection = db['comment']

            st.markdown("<style>div.block-container{padding-top:2rem;}</style>", unsafe_allow_html=True)

            col1, col2, col3, = st.columns([3, 8, 3])

            with col2:
                selected_1 = option_menu(
                    menu_title="OPINION BOX",
                    options=['CHOOSE OPTION', 'Your Feedback', "Explore User Thoughts"],
                    icons=['arrow-down-circle-fill', 'envelope-plus-fill', 'people-fill'],
                    default_index=0)
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")

            if selected_1 == 'CHOOSE OPTION':
                # animation

                def lottie(filepath):
                    with open(filepath, 'r') as file:
                        return js.load(file)

                col1, col2, col3, col4 = st.columns([15, 15, 15, 15])
                with col2:
                    file = lottie("angry_emoji.json")
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=300,
                        width=300,
                        key=None
                    )
                with col1:
                    file = lottie("smile_emoji.json")
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=300,
                        width=300,
                        key=None
                    )
                with col3:
                    file = lottie("calm_emoji.json")
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=300,
                        width=300,
                        key=None
                    )
                with col4:
                    file = lottie("love_emoji.json")
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=300,
                        width=300,
                        key=None
                    )


            elif selected_1 == 'Your Feedback':

                def lottie(filepath):
                    with open(filepath, 'r') as file:
                        return js.load(file)

                col1, col2, col3 = st.columns([10, 30, 5])
                col2.markdown(
                    "<h1 style='font-size: 90px;'><span style='color:white;'>Your</span> <span style='color:cyan;'>Feedback</span> <span style='color: white;'>Here </span> </h1>",
                    unsafe_allow_html=True)
                # animation

                st.write("")

                st.write("")

                st.write("")
                col1, col2, col3 = st.columns([15, 30, 5])
                with col2:
                    file = lottie("star_before_fb.json")
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=500,
                        width=600,
                        key=None
                    )

                col1, col2, col3, = st.columns([3, 8, 3])

                with col2:
                    col2.markdown(
                        "<h1 style='font-size: 30px;'><span style='color:white;'>Enter</span> <span style='color:cyan;'>Comment</span> <span style='color: white;'>Here ⬇️</span> </h1>",
                        unsafe_allow_html=True)
                    Comment = st.text_input('   ')
                    st.write(Comment)
                    if st.button('Save Comment'):
                        collection.insert_one({'comment of user': Comment})
                        st.write("")
                        st.write("")
                        col1, col2, col3, = st.columns([5, 8, 5])
                        st.success('Your Valuable Comment Saved Thankyou!', icon="✅")
                        col1, col2, col3 = st.columns([10, 30, 10])
                        with col2:
                            file = lottie("star.json")
                            st_lottie(
                                file,
                                speed=1,
                                reverse=False,
                                loop=True,
                                quality='low',
                                # renderer='svg',
                                height=100,
                                width=500,
                                key=None
                            )

                col1, col2, col3, = st.columns([3, 8, 3])
                with col2:
                    colored_header(
                        label="",
                        description="",
                        color_name="blue-green-70", )


            elif selected_1 == 'Explore User Thoughts':

                def lottie(filepath):
                    with open(filepath, 'r') as file:
                        return js.load(file)

                col1, col2, col3 = st.columns([10, 30, 5])

                with col2:

                    file = lottie("down_arrow.json")
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=300,
                        width=800,
                        key=None
                    )
                col2.markdown(
                    "<h1 style='font-size: 70px;'><span style='color:white;'>Explore</span> <span style='color:cyan;'>User Thoughts </span> <span style='color: white;'>Here </span> </h1>",
                    unsafe_allow_html=True)
                col2.write("")
                col2.write("")

                with col2:

                    file = lottie("thoughts.json")
                    st_lottie(
                        file,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality='low',
                        # renderer='svg',
                        height=500,
                        width=800,
                        key=None
                    )
                st.write("")
                st.write("")
                st.write("")
                col1, col2, col3, = st.columns([3.6, 10, 3])
                with col2:
                    # if st.button("Click Me!"):
                    res = [i['comment of user'] for i in collection.find()]
                    st.write("")
                    with st.spinner('Wait for it...'):
                        time.sleep(5)

                    colored_header(
                        label="Comments By Users ⬇",
                        description="",
                        color_name="blue-green-70", )
                    for i in res:
                        print(st.code(i))

                    col1, col2, col3 = st.columns([1, 10, 1])
                    col2.write("")
                    col2.write('')
                    col2.markdown(
                        "<h1 style='font-size: 35px;'><span style='color:cyan;'>Press</span> <span style='color:white;'>'G'</span> <span style='color:cyan;'>On Keyboard To Explore More Project</span> </h1>",
                        unsafe_allow_html=True)
                    with col2:
                        keyboard_to_url(key="G", url="https://github.com/praveendecode")

                    def lottie(filepath):
                        with open(filepath, 'r') as file:  # 'G' On Keyboard To Explore More Project
                            return js.load(file)

                    with col2:
                        file = lottie("click2.json")
                        st_lottie(
                            file,
                            speed=1,
                            reverse=False,
                            loop=True,
                            quality='low',
                            height=100,
                            width=700,
                            key=None
                        )

                    colored_header(
                        label="",
                        description="",
                        color_name="blue-green-70", )                      
                                    
            

# Object

Object = App()
Object.model()
