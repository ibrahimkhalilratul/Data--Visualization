# interface.py
import streamlit as st
from main import (
    load_data, clean_data,
    create_scatter_plot, create_line_chart, create_bar_chart, create_histogram,
    create_pie_chart, create_heatmap, create_box_plot, create_violin_plot, create_area_chart
)

# Streamlit app
st.title("📊 Advanced Data Processing and Visualization")

# Upload Excel or CSV file
uploaded_file = st.file_uploader("Upload an Excel or CSV file", type=["xlsx", "xls", "csv"])
if uploaded_file is not None:
    # Load data
    df = load_data(uploaded_file)
    st.write("### Data Preview")
    st.write(df.head())

    # Data Cleaning and Transformation
    st.write("### Data Cleaning and Transformation")
    query = st.text_input("Enter your data processing query (e.g., 'remove missing values', 'filter Sales > 100', 'rename MinTemp to Min', 'sort Revenue ascending', 'aggregate Region sum')")

    if query:
        df, message = clean_data(df, query)
        st.write(f"### {message}")
        st.write("### Processed Data Preview")
        st.write(df.head())

    # Visualization options
    st.write("### Visualization Options")
    chart_type = st.selectbox(
        "Choose a chart type",
        [
            "Scatter Plot", "Line Chart", "Bar Chart", "Histogram",
            "Pie Chart", "Heatmap", "Box Plot", "Violin Plot", "Area Chart"
        ]
    )

    if chart_type == "Scatter Plot":
        x_axis = st.selectbox("Select X-axis", df.columns)
        y_axis = st.selectbox("Select Y-axis", df.columns)
        fig = create_scatter_plot(df, x_axis, y_axis)
        st.plotly_chart(fig)

    elif chart_type == "Line Chart":
        x_axis = st.selectbox("Select X-axis", df.columns)
        y_axis = st.selectbox("Select Y-axis", df.columns)
        fig = create_line_chart(df, x_axis, y_axis)
        st.plotly_chart(fig)

    elif chart_type == "Bar Chart":
        x_axis = st.selectbox("Select X-axis", df.columns)
        y_axis = st.selectbox("Select Y-axis", df.columns)
        fig = create_bar_chart(df, x_axis, y_axis)
        st.plotly_chart(fig)

    elif chart_type == "Histogram":
        column = st.selectbox("Select a column", df.columns)
        fig = create_histogram(df, column)
        st.plotly_chart(fig)

    elif chart_type == "Pie Chart":
        column = st.selectbox("Select a column", df.columns)
        fig = create_pie_chart(df, column)
        st.plotly_chart(fig)

    elif chart_type == "Heatmap":
        x_axis = st.selectbox("Select X-axis", df.columns)
        y_axis = st.selectbox("Select Y-axis", df.columns)
        values = st.selectbox("Select Values", df.columns)
        fig = create_heatmap(df, x_axis, y_axis, values)
        st.plotly_chart(fig)

    elif chart_type == "Box Plot":
        x_axis = st.selectbox("Select X-axis", df.columns)
        y_axis = st.selectbox("Select Y-axis", df.columns)
        fig = create_box_plot(df, x_axis, y_axis)
        st.plotly_chart(fig)

    elif chart_type == "Violin Plot":
        x_axis = st.selectbox("Select X-axis", df.columns)
        y_axis = st.selectbox("Select Y-axis", df.columns)
        fig = create_violin_plot(df, x_axis, y_axis)
        st.plotly_chart(fig)

    elif chart_type == "Area Chart":
        x_axis = st.selectbox("Select X-axis", df.columns)
        y_axis = st.selectbox("Select Y-axis", df.columns)
        fig = create_area_chart(df, x_axis, y_axis)
        st.plotly_chart(fig)