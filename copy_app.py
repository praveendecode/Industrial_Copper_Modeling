from  streamlit import *
from streamlit_extras import *
from streamlit_lottie import *
from streamlit_option_menu import *
import pandas as pd 
from streamlit_extras.colored_header import colored_header
from streamlit_extras.metric_cards import style_metric_cards
import plotly.express as px



class airbnb:

    def dashboard(self):
                            
        st.set_page_config(page_title='airBnB Project By Praveen', layout="wide")

        
                                                                                         # PROGRAMS INITIATED
        with st.sidebar:     # Navbar
                        selected = option_menu(
                                                   menu_title="airbnb",
                                                   options=['Intro','Descriptive Statistics',"Insights",""],
                                                   icons = ['mic-fill','cash-stack','phone-flip','geo-alt-fill','clock-fill','globe-central-south-asia','envelope-paper-heart-fill'],
                                                   menu_icon='alexa',
                                                   default_index=0,
                                               )
                        
         # Pandas 
        df = pd.read_csv("Airbnbfinal_data.csv")
        df['id'] = df['id'].apply(lambda x : str(x))
        df['host_iD'] = df['host_iD'].apply(lambda x : str(x))
        continous_features = df.select_dtypes(include=['int64','float64']).columns
        cat_deatures = df.select_dtypes(include=['object']).columns

                        
        if selected =='Descriptive Statistics':
                st.markdown("<style>div.block-container{padding-top:3rem;}</style>", unsafe_allow_html=True)

                                
                explore = option_menu(
                            menu_title="",
                            options=['Click', 'Features','Summary'],
                            icons=['arrow-right-circle-fill', 'eye-fill'],
                            menu_icon='',
                            default_index=0,
                            orientation='horizontal')
                
               
 
                
                if explore == 'Features':
                        col1,col2,col3 = st.columns([13.5,10,10])
                        col2.write("")
                        col2.write("")
                        col2.write("")
                        col2.write("")

                        col2.markdown( "<h1 style='font-size: 50px;'><span style='color: cyan;'>Know </span> <span style='color: white;'>The</span> <span style='color: cyan;'>Features</span></h1>",unsafe_allow_html=True)
                        col2.write("")
                        col2.write("")
                        col1,col2,col3 = st.columns([18,10,10])

                        if col2.button('Know features'):
                                 
                            col1,col2,col3,col4 = st.columns([2,10,10,2])
                            
                            with col2 :
                                st.markdown( f"<h1 style='font-size: 50px;'><span style='color: cyan;'>Continous</span><span style='color: White;'> Features</span> </h1>",unsafe_allow_html=True)
                                colored_header(
                                label="",
                                description="",
                                color_name="blue-green-70", )

                                   
                                for i in continous_features:
                                        st.markdown( f"<h1 style='font-size: 20px;'><span style='color: white;'> {i} </span> </h1>",unsafe_allow_html=True)

                            with col3 :
                                st.markdown( f"<h1 style='font-size: 50px;'><span style='color: cyan;'>Categorical </span><span style='color: White;'> Features</span> </h1>",unsafe_allow_html=True)
                                colored_header(
                                label="",
                                description="",
                                color_name="blue-green-70", )

                                   
                                for i in cat_deatures:
                                        st.markdown( f"<h1 style='font-size: 20px;'><span style='color: white;'> {i} </span> </h1>",unsafe_allow_html=True)

                elif explore == "Summary":
                       
                    col1,col2,col3 = st.columns([9,10,5])
                    col2.markdown( f"<h1 style='font-size: 65px;'><span style='color: cyan;'> Summary </span><span style='color: white;'> Statistics </span> </h1>",unsafe_allow_html=True)
                    col2.write("")
                    col2.write("")
                    col2.write("")
                    col2.write("")
                    col2.write("")
                    col2.write("")
                    col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Select </span><span style='color: white;'> Feature Type </span> </h1>",unsafe_allow_html=True)

                    col1,col2,col3 = st.columns([9,10,5])
                    select = col2.selectbox('',['Continous Features','Categorical Features'])
                    # col2.write("")
                    # col2.write("")
                    col2.write("")
                    col2.write("")

                    if select == 'Continous Features':
                        col2.markdown( f"<h1 style='font-size: 50px;'><span style='color: cyan;'> Continous </span><span style='color: white;'> Features </span> </h1>",unsafe_allow_html=True)

                        col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Select </span><span style='color: white;'> Feature </span> </h1>",unsafe_allow_html=True)

                        option = col2.selectbox('',continous_features)
                        if col2.button('Show'):

                            x = df[option].describe()

                            col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Selected Feature : </span><span style='color: white;'> {option}</span> </h1>",unsafe_allow_html=True)
                            col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Count : </span><span style='color: white;'>{x[0]} </span> </h1>",unsafe_allow_html=True)
                            col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Mean : </span><span style='color: white;'> {x[1]} </span> </h1>",unsafe_allow_html=True)
                            col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Std :  </span><span style='color: white;'> {x[2]}</span> </h1>",unsafe_allow_html=True)
                            col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Min  : </span><span style='color: white;'>  {x[3]}</span> </h1>",unsafe_allow_html=True)
                            col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> 25 % : </span><span style='color: white;'> {x[4]}</span> </h1>",unsafe_allow_html=True)
                            col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> 50 % : </span><span style='color: white;'>  {x[5]}</span> </h1>",unsafe_allow_html=True)
                            col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> 75 % : </span><span style='color: white;'>  {x[6]}</span> </h1>",unsafe_allow_html=True)
                            col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Max  : </span><span style='color: white;'>  {x[7]}</span> </h1>",unsafe_allow_html=True)



                    elif select == 'Categorical Features':
                        col2.markdown( f"<h1 style='font-size: 50px;'><span style='color: cyan;'> Categorical  </span><span style='color: white;'> Features </span> </h1>",unsafe_allow_html=True)

                        col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Select </span><span style='color: white;'> Feature </span> </h1>",unsafe_allow_html=True)

                        option = col2.selectbox('',cat_deatures)

                        if col2.button('Show'):

                            x = df[option].describe()

                            col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Selected Feature : </span><span style='color: white;'> {option}</span> </h1>",unsafe_allow_html=True)
                            col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Count : </span><span style='color: white;'>{x[0]} </span> </h1>",unsafe_allow_html=True)
                            col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Unique : </span><span style='color: white;'> {x[1]} </span> </h1>",unsafe_allow_html=True)
                            col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Top :  </span><span style='color: white;'> {x[2]}</span> </h1>",unsafe_allow_html=True)
                            col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Feq  : </span><span style='color: white;'>  {x[3]}</span> </h1>",unsafe_allow_html=True)
            
        elif selected == 'Insights':
                st.markdown("<style>div.block-container{padding-top:3rem;}</style>", unsafe_allow_html=True)

                # Metrics 

                col1,col2,col3,col4,col5 = st.columns([10,10,10,10,10])

                col1.metric(label="Total Host Count", value=f'{len(df.host_name.unique())}',delta=int(len(df.host_name.unique())/100))
                col2.metric(label="Total Room Types", value=f'{len(df.room_type.unique())}',delta=int(len(df.room_type.unique())))
                col3.metric(label="Total Listings Available", value=f'{len(df.name.unique())}',delta=int(len(df.name.unique())/10))
                col4.metric(label="Total Amount Earned", value=f'{df.price.sum()}',delta=int(df.price.sum()/100))
                col5.metric(label="Total Host Neighbourhood", value=f'{len(df.host_neighbourhood.unique())}',delta=int(len(df.host_neighbourhood.unique())/10))

                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                # Filters :
                col1,col2,col3,col4 ,col5,col6,col7= st.columns([10,10,10,10,10,10,10])

                with col2.expander("FILTER"):

                    st.write("")
                    room_type = st.selectbox('CHOOSE ROOM TYPE',df.room_type.unique())

                with col4.expander("FILTER"):

                    st.write("")
                    place = st.selectbox('CHOOSE HOST NEIGHBOURHOOD',df.host_neighbourhood.unique())

                with col6.expander("FILTER"):

                    st.write("")
                    property_type = st.selectbox('CHOOSE Property Type',df.property_type.unique())

                
            

                # Availaibility
                col1,col2 = st.columns([10,10])
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.markdown( f"<h1 style='font-size: 70px;'><span style='color: cyan;'> Availability  </span><span style='color: white;'> Analysis </h1>",unsafe_allow_html=True)

                col1,col2,col3 = st.columns([10,20,5])
                col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Availability  days </span><span style='color: white;'>  based on</span> <span style='color: white;'> {room_type} and {property_type} and {place} </span></h1>",unsafe_allow_html=True)
                col1,col2 = st.columns([10,10])

                value = df.query(f"room_type=='{room_type}' and property_type == '{property_type}' and host_neighbourhood=='{place}'")[['availability_30', 'availability_60', 'availability_90', 'availability_365']].sum()
                name=['availability_30','availability_60','availability_90','availability_365']

                fig = px.bar( x=name, y=value)
                fig.update_layout(title_x=1)
                fig.update_layout(
                    plot_bgcolor='#0E1117',
                    paper_bgcolor='#0E1117',
                    xaxis_title_font=dict(color='#0DF0D4'),
                    yaxis_title_font=dict(color='#0DF0D4')
                )
                fig.update_traces(hoverlabel=dict(bgcolor="#0E1117"),
                                    hoverlabel_font_color="#0DF0D4")
                fig.update_xaxes(title_text="Availability Types")

                fig.update_yaxes(title_text="Days  Count")

                fig.update_traces(marker_color='#1BD4BD')
                
                st.plotly_chart(fig, theme=None, use_container_width=True)
                
               

                # Host Analysis

                col1,col2 = st.columns([10,10])
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
              
                col1.markdown( f"<h1 style='font-size: 70px;'><span style='color: cyan;'> Host  </span><span style='color: white;'> Analysis </h1>",unsafe_allow_html=True)
                 # Filters :
                col1,col2,col3= st.columns([10,10,10])
                
                
                
                # 1

                col1,col2,col3= st.columns([13,10,15])
                col2.write("")
                with col2.expander("FILTER"):

                    st.write("")
                    place = st.selectbox('HOST NEIGHBOURHOOD',df.host_neighbourhood.unique())
                col1,col2,col3 = st.columns([10,20,5])
                col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Top  10  Hosts </span><span style='color: white;'>  based on </span> <span style='color: white;'> Host Neighbourhood : {place} </span></h1>",unsafe_allow_html=True)
                
                col1,col2 = st.columns([10,10])

                filter = df.query(f"host_neighbourhood=='{place}'").groupby('host_name')['host_total_listings_count'].sum().nlargest(10)
                name = filter.index.tolist()
                value = filter.values.tolist()
                fig = px.bar( x=name, y=value)
                fig.update_layout(title_x=1)
                fig.update_layout(
                    plot_bgcolor='#0E1117',
                    paper_bgcolor='#0E1117',
                    xaxis_title_font=dict(color='#0DF0D4'),
                    yaxis_title_font=dict(color='#0DF0D4')
                )
                fig.update_traces(hoverlabel=dict(bgcolor="#0E1117"),
                                    hoverlabel_font_color="#0DF0D4")
                fig.update_xaxes(title_text="Host Name")

                fig.update_yaxes(title_text="Listings Count")

                fig.update_traces(marker_color='#1BD4BD')
                
                st.plotly_chart(fig, theme=None, use_container_width=True)
                col1.write("")
                col1.write("")
                col1.write("")
                 # 2
                col1,col2,col3= st.columns([13,10,15])
                with col2.expander("FILTER"):

                    st.write("")
                    room_type = st.selectbox('ROOM TYPE',df.room_type.unique())
                col1,col2,col3 = st.columns([10,20,5])
                col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Top  10  Hosts </span><span style='color: white;'>  based on </span> <span style='color: white;'> Room Type : {room_type} </span></h1>",unsafe_allow_html=True)
               
                col1,col2 = st.columns([10,10])

                filter = df.query(f"room_type=='{room_type}'").groupby('host_name')['host_total_listings_count'].sum().nlargest(10)
                name = filter.index.tolist()
                value = filter.values.tolist()
                fig = px.bar( x=name, y=value)
                fig.update_layout(title_x=1)
                fig.update_layout(
                    plot_bgcolor='#0E1117',
                    paper_bgcolor='#0E1117',
                    xaxis_title_font=dict(color='#0DF0D4'),
                    yaxis_title_font=dict(color='#0DF0D4')
                )
                fig.update_traces(hoverlabel=dict(bgcolor="#0E1117"),
                                    hoverlabel_font_color="#0DF0D4")
                fig.update_xaxes(title_text="Host Name")

                fig.update_yaxes(title_text="Listings Count")

                fig.update_traces(marker_color='#1BD4BD')
                
                st.plotly_chart(fig, theme=None, use_container_width=True)

                # Room_type Analysis
                col1,col2 = st.columns([10,10])
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.markdown( f"<h1 style='font-size: 70px;'><span style='color: cyan;'> Room Type  </span><span style='color: white;'> Analysis </h1>",unsafe_allow_html=True)
                col1.write("")
                col1.write("")
                col1,col2,col3= st.columns([13,10,15])
                with col2.expander("FILTER"):

                    st.write("")
                    room_type = st.selectbox('Room Type',df.room_type.unique())

                    option = st.selectbox('Choose Option',['Minimun','Maximum'])



                col1,col2,col3 = st.columns([7,20,5])

                if option == 'Minimun':

                    col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Top 10  </span><span style='color: white;'> minimun price host neighbourhoods based on Room Type :</span> <span style='color: cyan;'> {room_type}</span></h1>",unsafe_allow_html=True)
                    filter = df.query(f"room_type== '{room_type}'").groupby('host_neighbourhood')['price'].mean().nsmallest(10)

                    name = filter.index.tolist()

                    value = filter.values.tolist()
                    fig = px.bar( x=name, y=value)
                    fig.update_layout(title_x=1)
                    fig.update_layout(
                        plot_bgcolor='#0E1117',
                        paper_bgcolor='#0E1117',
                        xaxis_title_font=dict(color='#0DF0D4'),
                        yaxis_title_font=dict(color='#0DF0D4')
                    )
                    fig.update_traces(hoverlabel=dict(bgcolor="#0E1117"),
                                        hoverlabel_font_color="#0DF0D4")
                    fig.update_xaxes(title_text="Host Name")

                    fig.update_yaxes(title_text="Listings Count")

                    fig.update_traces(marker_color='#1BD4BD')
                    
                    st.plotly_chart(fig, theme=None, use_container_width=True)

                elif option == 'Maximum':
                    col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Top 10  </span><span style='color: white;'> Maximun price host neighbourhoods based on Room Type :</span> <span style='color: cyan;'> {room_type}</span></h1>",unsafe_allow_html=True)
                    filter = df.query(f"room_type== '{room_type}'").groupby('host_neighbourhood')['price'].mean().nlargest(10)

                    name = filter.index.tolist()

                    value = filter.values.tolist()
                    fig = px.bar( x=name, y=value)
                    fig.update_layout(title_x=1)
                    fig.update_layout(
                        plot_bgcolor='#0E1117',
                        paper_bgcolor='#0E1117',
                        xaxis_title_font=dict(color='#0DF0D4'),
                        yaxis_title_font=dict(color='#0DF0D4')
                    )
                    fig.update_traces(hoverlabel=dict(bgcolor="#0E1117"),
                                        hoverlabel_font_color="#0DF0D4")
                    fig.update_xaxes(title_text="Host Name")

                    fig.update_yaxes(title_text="Listings Count")

                    fig.update_traces(marker_color='#1BD4BD')
                    
                    st.plotly_chart(fig, theme=None, use_container_width=True)
                     
                col2.write("")
                col2.write("")
                col2.write("")
                col2.write("")
                col2.write("")
                col1,col2,col3= st.columns([13,10,15])
                with col2.expander("FILTER"):

                    st.write("")
                    room_type = st.selectbox('Choose Room Type',df.room_type.unique())




                col1,col2,col3 = st.columns([7,20,5])
                col2.markdown( f"<h1 style='font-size: 30px;'><span style='color: cyan;'> Top 10  </span><span style='color: white;'> maximun review host neighbourhoods based on Room Type :</span> <span style='color: cyan;'> {room_type}</span></h1>",unsafe_allow_html=True)
                filter = df.query(f"room_type== '{room_type}'").groupby('host_neighbourhood')['number_of_Reviews'].sum().nlargest(10)

                name = filter.index.tolist()

                value = filter.values.tolist()
                fig = px.bar( x=name, y=value)
                fig.update_layout(title_x=1)
                fig.update_layout(
                    plot_bgcolor='#0E1117',
                    paper_bgcolor='#0E1117',
                    xaxis_title_font=dict(color='#0DF0D4'),
                    yaxis_title_font=dict(color='#0DF0D4')
                )
                fig.update_traces(hoverlabel=dict(bgcolor="#0E1117"),
                                    hoverlabel_font_color="#0DF0D4")
                fig.update_xaxes(title_text="Host Name")

                fig.update_yaxes(title_text="Review Count")

                fig.update_traces(marker_color='#1BD4BD')
                
                st.plotly_chart(fig, theme=None, use_container_width=True)

                # Price  Analysis
                col1,col2 = st.columns([10,10])
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.markdown( f"<h1 style='font-size: 70px;'><span style='color: cyan;'> Price  </span><span style='color: white;'> Analysis </h1>",unsafe_allow_html=True)
                col1.write("")
                col1.write("")

                df_1 = df.copy()
                df_1.columns = ['id', 'name', 'description', 'Property Type', 'Room Type',
                            'minimum_nights', 'maximum_nights', 'number_of_Reviews', 'amenities',
                            'price', 'host_iD', 'Host', 'Host Neighbourhood',
                            'host_total_listings_count', 'longitide', 'latitude', 'availability_30',
                            'availability_60', 'availability_90', 'availability_365', 'rating'] 
                col1,col2,col3,col4,col5 = st.columns([10,10,10,10,10])
                with col2.expander("FILTER"):

                    st.write("")
                    choose_10 = st.selectbox('CHOOSE OPTION',['Top 10', "Bottom 10"])

                with col4.expander("FILTER"):

                    st.write("")
                    field = st.selectbox('CHOOSE FIELD',['Host',"Host Neighbourhood","  Property Type","Room Type"])

                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1.write("")
                col1,col2,col3 = st.columns([15,20,5])
                col2.markdown( f"<h1 style='font-size: 35px;'><span style='color: cyan;'> {choose_10} </span><span style='color: white;'> {field}  based on </span> <span style='color: cyan;'> Price </span></h1>",unsafe_allow_html=True)
                
                if choose_10 == 'Top 10':
                    host_filter = df_1.groupby(f'{field}')['price'].sum().nlargest(10)

                    name = host_filter.index.tolist()

                    value = host_filter.values.tolist()
                    fig = px.bar( x=name, y=value)
                    fig.update_layout(title_x=1)
                    fig.update_layout(
                        plot_bgcolor='#0E1117',
                        paper_bgcolor='#0E1117',
                        xaxis_title_font=dict(color='#0DF0D4'),
                        yaxis_title_font=dict(color='#0DF0D4')
                    )
                    fig.update_traces(hoverlabel=dict(bgcolor="#0E1117"),
                                        hoverlabel_font_color="#0DF0D4")
                    fig.update_xaxes(title_text="Host Name")

                    fig.update_yaxes(title_text="Review Count")

                    fig.update_traces(marker_color='#1BD4BD')
                    
                    st.plotly_chart(fig, theme=None, use_container_width=True)

                elif choose_10 == "Bottom 10":
                    host_filter = df_1.groupby(f'{field}')['price'].sum().nsmallest(10)

                    name = host_filter.index.tolist()

                    value = host_filter.values.tolist()
                    fig = px.bar( x=name, y=value)
                    fig.update_layout(title_x=1)
                    fig.update_layout(
                        plot_bgcolor='#0E1117',
                        paper_bgcolor='#0E1117',
                        xaxis_title_font=dict(color='#0DF0D4'),
                        yaxis_title_font=dict(color='#0DF0D4')
                    )
                    fig.update_traces(hoverlabel=dict(bgcolor="#0E1117"),
                                        hoverlabel_font_color="#0DF0D4")
                    fig.update_xaxes(title_text="Host Name")

                    fig.update_yaxes(title_text="Review Count")

                    fig.update_traces(marker_color='#1BD4BD')
                    
                    st.plotly_chart(fig, theme=None, use_container_width=True)


                style_metric_cards(
                                    border_left_color='#08EED2',
                                    background_color='#0E1117', border_color="#0E1117")
                    
                colored_header(
                                label="",
                                description="",
                                color_name="blue-green-70", )



# Object 

Object = airbnb()
Object.dashboard()
