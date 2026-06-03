import streamlit as st
from sklearn import linear_model
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from streamlit_option_menu import option_menu
#label encoder catagorical data ko numerical data me convert krta hai
import plotly.express as px 
st.set_page_config(layout="wide")
select = option_menu(
    menu_title=None,
    options=["Home", "Predict Price", "About Tesla Y Model"],
    orientation="horizontal",
    icons=["house", "calculator", "car-front"]
    )
df=pd.read_csv("teslay.csv")
if select == "Home":

    st.title("Tesla Y Model Price Prediction")

   
    

    
    col5, col6, col7, col8 = st.columns(4)
    with col5:
        st.metric("total colors of cars ", df["color"].nunique())
    with col6:
        st.metric("Average price of tesla Y Model", round(df["price"].mean(), 2))
    with col7:
        st.metric("Maximum price of tesla Y Model", round(df["price"].max(), 2))
    with col8:
        st.metric("Minimum price of tesla Y Model", round(df["price"].min(), 2))
    #st.metric("Total cars", len(df))
    col3, col4 = st.columns(2)
    with col3:
        st.title("Color wise car count!")
        df2=df["color"].value_counts().reset_index()
        st.dataframe(df2)
    with col4:
        st.title("Year wise model price!")
        date_year =  df.groupby("year")["price"].mean().reset_index()

        fig=px.line(
            date_year, 
            x="year", 
            y="price",
            title="Price trend" 
            )
        st.plotly_chart(fig)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Row Data set")
        st.dataframe(df)
    with col2:
        st.subheader("Color Wise Data")
        #st.metric("Unique colors", df["color"].nunique())

        fig_price = px.bar(
        df,
        x="color",
        y="price",
        color="color",
        text="color"
    )
        

        st.plotly_chart(fig_price)
        
        fig_year = px.bar(
        df,
        x="year",
        y="price",
        color="year",
        text="year"
    )
        st.plotly_chart(fig_year)
if select == "Predict Price":  
    st.title("Predict Price of Tesla Y Model")
    le = LabelEncoder()

    df["color"] = le.fit_transform(df["color"])
    X = df[["year", "color", "km"]] #independent variable hai year, color aur km
    y = df.price #dependent variable hai price
    model = linear_model.LinearRegression() #multiple linear regression model banaya hai
    model.fit(X, y) #model ko fit kiya hai X aur y data ke sath
    col9, col10 = st.columns(2)
    with col9:
        st.info("By Selecting the year, color and km's")

        year = st.selectbox("Enter the year of the car",[2020,2021,2022,2023,2024,2025,2026,2027,2028,2029])
        color = st.selectbox("Select the color of the car",le.classes_)
        km = st.number_input("Enter the kilometers of the car", min_value=6000)
        pred=st.button("Predict Price")
    with col10:
        col_ch = le.transform([color])[0] #color ko numerical data me convert kiya hai
        predicted_price = model.predict([[year, col_ch, km]]) #model se price predict kiya hai
        score = model.score(X, y)
        accuracy = int(score * 100)
        st.metric("Current Model Accuracy as per recent data!",accuracy, "%")
        if pred:    
            if color:
                col_ch = le.transform([color])[0] #color ko numerical data me convert kiya hai
                predicted_price = model.predict([[year, col_ch, km]]) #model se price predict kiya hai
                st.balloons()
                score = model.score(X, y)
                accuracy = int(score * 100)

                st.subheader("How accurate the predicted price is!")
                st.info(f"{accuracy}%") 
                st.subheader("Here is your Predicted Price for tesla Y Model! ")


                predic=int(predicted_price[0])
                st.info(predic)
            existing_data=pd.read_csv("teslay.csv")
            new_data = pd.DataFrame({"year": [year], "color": [color], "km": [km], "price": [predic]})
            updated_data = pd.concat([existing_data, new_data])
            updated_data.to_csv("teslay.csv", index=False)

if select == "About Tesla Y Model":



    st.title("🚘About Tesla Model Y")
    st.caption("The Future of Electric Mobility")


    st.markdown("""
    Tesla Model Y is a revolutionary all-electric SUV designed to deliver
    exceptional performance, advanced technology, and sustainable transportation.

    Combining sleek design, intelligent software, and cutting-edge battery
    technology, Model Y provides a premium driving experience while supporting
    a cleaner and greener future.
    """)
    st.divider()

    # layout split (image + text)
    col1, col2 = st.columns([2, 2])

    with col1:
       
        st.image("black-2025.webp", use_container_width=True)     
       
    with col2:
        st.markdown("""
    ### 🚘 Tesla Model Y (2024 - Black Edition)

    - ⚫ Premium black finish
    - 🔋 Long range electric performance
    - 🚀 0–60 mph in ~3.5 sec
    - 🛡️ Advanced safety system
    - 🌍 Zero emissions SUV
    """)

    st.divider()

    

    st.subheader("⚡ Key Highlights")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        - 🔋 Long-range electric battery technology
        - 🚀 Rapid acceleration and smooth performance
        - 🛡️ Industry-leading safety features
        """)

    with col2:
        st.markdown("""
        - 📱 Intelligent touchscreen control system
        - 🌍 Zero-emission sustainable mobility
        - ⚡ Tesla Supercharger network access
        """)

    st.divider()

  

    st.subheader("📊 Performance Snapshot")

    col3, col4, col5 = st.columns(3)

    with col3:
        st.metric("Range", "330 mi")

    with col4:
        st.metric("0-60 mph", "3.5 sec")

    with col5:
        st.metric("Top Speed", "155 mph")

    st.info(
        "Driving the future with innovation, performance, and sustainability."
    )

    st.divider()


    st.subheader("✨ Premium Features")

    col6, col7, col8 = st.columns(3)

    with col6:
        st.success("🔋 Long Range Battery")
        st.write("Extended driving range with advanced battery efficiency.")

    with col7:
        st.success("⚡ Fast Charging")
        st.write("Quick charging support through Tesla's charging ecosystem.")

    with col8:
        st.success("🛡️ Advanced Safety")
        st.write("Designed with intelligent safety and driver-assistance systems.")

    st.divider()

    
st.markdown(
    """
    <div style="display:flex; justify-content:center; background-color:black; padding:20px;">
        <div>
            <h3 style="color:white;">🚘 Tesla Model Y Dashboard</h3>
            <p style="text-align:center; color:white;">
                Explore electric mobility through analytics and innovation.
            </p>
            <p style="text-align:center; color:white;">© 2026 Tesla Model Y Dashboard</p>
            <p style="text-align:center; color:white;"><b>Developed by Syeda Anusha</b></p>
            <p style="text-align:center; color:white;">Built with ❤️ using Python & Streamlit</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
