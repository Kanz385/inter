

import streamlit as st
import pandas as pd
import plotly.express as px

df_url = "https://raw.githubusercontent.com/Kanz385/inter/main/streamlit_app.py"
# For now, I'm commenting it out
df = pd.read_csv('/Users/kanzmroue/Desktop/MSBA 325 fz/PCOS_data.csv')

# Sample DataFrame for testing (please replace this with your actual data)
df = pd.DataFrame({
    'BMI': [25, 30, 35, 40],
    'Weight (Kg)': [70, 80, 90, 100]
})


def display_bmi_vs_weight():
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
    fig.update_layout(margin=dict(t=40))
    st.plotly_chart(fig)


def display_bar_chart():
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
    else:
        fig = px.bar(df, x=x_column, y=y_column, title=f"{x_column} vs {y_column}")
    fig.update_layout(margin=dict(t=40))
    st.plotly_chart(fig)


def main():
    # Select which visualization to display
    app_mode = st.selectbox("Choose a Visualization:", ["BMI vs. Weight", "Interactive Bar Chart"])
    if app_mode == "BMI vs. Weight":
        display_bmi_vs_weight()
    elif app_mode == "Interactive Bar Chart":
        display_bar_chart()


if __name__ == '__main__':
    main()

