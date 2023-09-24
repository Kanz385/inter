
filename = "requirements.txt"
pd.read_csv("https://raw.githubusercontent.com/Kanz385/inter/main/streamlit_app.py")

import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')


import streamlit as st
import pandas as pd
import plotly.express as px

# Load your data
df = pd.read_csv('/Users/kanzmroue/Desktop/MSBA 325 fz/PCOS_data.csv')

# Streamlit app function
def main():
    st.title("Interactive BMI vs. Weight Visualization")

    # Sidebar for filtering data
    st.sidebar.header("Data Filters")

    # Create a filter for BMI range
    bmi_min = st.sidebar.slider("Minimum BMI", min_value=df['BMI'].min(), max_value=df['BMI'].max(), value=df['BMI'].min())
    bmi_max = st.sidebar.slider("Maximum BMI", min_value=df['BMI'].min(), max_value=df['BMI'].max(), value=df['BMI'].max())

    # Filter the data based on BMI range
    filtered_data = df[(df['BMI'] >= bmi_min) & (df['BMI'] <= bmi_max)]

    # Display the filtered data
    st.write("Filtered Data:")
    st.write(filtered_data)

    # Create an interactive scatter plot with Plotly
    st.header("BMI vs. Weight Scatter Plot")
    fig = px.scatter(
        filtered_data,
        x='Weight (Kg)',
        y='BMI',
        color='BMI',
        opacity=0.7,
        title='BMI vs. Weight',
    )
    
    # Customize the layout (optional)
    fig.update_xaxes(title_text='Weight (Kg)')
    fig.update_yaxes(title_text='BMI')
    fig.update_traces(marker=dict(size=5))
    
    # Display the Plotly figure using Streamlit
    st.plotly_chart(fig)

if __name__ == '__main__':
    main()

######

# Load your data


##### Features for the second visual

#######
import streamlit as st
import pandas as pd
import plotly.express as px

# Load your data
df = pd.read_csv('/Users/kanzmroue/Desktop/MSBA 325 fz/PCOS_data.csv')

# Streamlit app function
def main():
    st.title("Interactive Bar Chart")

    # Sidebar for user input
    st.sidebar.header("Select Data for Bar Chart")

    # Create selectboxes to choose columns for x and y axes
    x_column = st.sidebar.selectbox("X-Axis Data (Category)", df.columns)
    y_column = st.sidebar.selectbox("Y-Axis Data (Value)", df.columns)

    # Add a selectbox for highlighting a specific category
    highlight_category = st.sidebar.selectbox("Highlight Category (Optional)", ['None'] + df[x_column].unique().tolist())
    
    # Create the bar chart using Plotly Express
    if highlight_category != 'None':
        df['highlight'] = df[x_column].apply(lambda x: x == highlight_category)
        fig = px.bar(df, x=x_column, y=y_column, color='highlight', title=f"{x_column} vs {y_column}")
        fig.update_traces(marker=dict(line=dict(width=0)))
    else:
        fig = px.bar(df, x=x_column, y=y_column, title=f"{x_column} vs {y_column}")
    
    # Customize the layout (optional)
    fig.update_xaxes(title_text=x_column)
    fig.update_yaxes(title_text=y_column)

    # Display the bar chart
    st.plotly_chart(fig)

if __name__ == '__main__':
    main()
  
