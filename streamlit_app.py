
import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')


import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
# Load your data
df = pd.read_csv("https://raw.githubusercontent.com/Kanz385/inter/main/PCOS_data.csv")

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
import plotly.graph_objects as go
import plotly.express as px

# Load data from the provided URL
df = pd.read_csv("https://raw.githubusercontent.com/Kanz385/inter/main/PCOS_data.csv")

def main():
    st.title("Interactive Visualizations")

    # Sidebar for user input
    st.sidebar.header("Choose Visualization")
    visualization = st.sidebar.radio("Select Visualization", ["Bar Chart", "Histogram"])

    if visualization == "Bar Chart":
        bar_chart()
    elif visualization == "Histogram":
        histogram()

    # Button to toggle data
    if st.button('Toggle Data'):
        st.dataframe(df)

def bar_chart():
    st.subheader("Interactive Bar Chart")
    
    x_column = st.sidebar.selectbox("X-Axis Data (Category)", df.columns)
    y_column = st.sidebar.selectbox("Y-Axis Data (Value)", df.columns)
    highlight_category = st.sidebar.selectbox("Highlight Category (Optional)", ['None'] + df[x_column].unique().tolist())
    
    if highlight_category != 'None':
        filtered_data = df[df[x_column] == highlight_category]
    else:
        filtered_data = df

    fig = go.Figure()
    fig.add_trace(go.Bar(x=filtered_data[x_column], y=filtered_data[y_column], marker_color='blue'))
    fig.update_layout(title=f"{x_column} vs {y_column}", xaxis_title=x_column, yaxis_title=y_column)
    st.plotly_chart(fig)

def histogram():
    st.subheader("Interactive Histogram")
    
    column_to_plot = st.sidebar.selectbox("Choose column to visualize", df.columns)
    grouping_column = st.sidebar.selectbox("Group by column (optional)", ["None"] + df.select_dtypes(include=['object', 'category']).columns.tolist())
    
    color_param = None if grouping_column == "None" else grouping_column
    
    fig = px.histogram(df, x=column_to_plot, color=color_param, title=f"Distribution of {column_to_plot}")
    st.plotly_chart(fig)

if __name__ == '__main__':
    main()
