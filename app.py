from charts import pie_chart, bar_chart, line_chart, histogram_chart, scatter_chart, box_chart, heatmap_chart, area_chart, count_chart, violin_chart

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("tarantino.csv")
# Title
st.title("Tarantino Movies Dashboard")

# Sidebar Filters
st.sidebar.header("Filters")
movies = st.sidebar.multiselect(
    "Select Movie", 
    df['movie'].unique(), 
    default=df['movie'].unique()
)

filtered_df = df[df['movie'].isin(movies)]

# Example Chart: Bar Chart
st.subheader("Profanity Counts Across Movies")
movie_counts = filtered_df['movie'].value_counts().reset_index()
movie_counts.columns = ['movie', 'count']

fig, ax = plt.subplots()
sns.barplot(x="movie", y="count", data=movie_counts, ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)
chart_type = st.sidebar.selectbox(
    "Select Chart Type",
    ["Pie", "Bar", "Line", "Histogram", "Scatter", "Box", "Heatmap", "Area", "Count", "Violin"]
)
if chart_type == "Pie":
    pie_chart(filtered_df)
elif chart_type == "Bar":
    bar_chart(filtered_df)
elif chart_type == "Line":
    line_chart(filtered_df)
elif chart_type == "Histogram":
    histogram_chart(filtered_df)
elif chart_type == "Scatter":
    scatter_chart(filtered_df)
elif chart_type == "Box":
    box_chart(filtered_df)
elif chart_type == "Heatmap":
    heatmap_chart(filtered_df)
elif chart_type == "Area":
    area_chart(filtered_df)
elif chart_type == "Count":
    count_chart(filtered_df)
elif chart_type == "Violin":
    violin_chart(filtered_df)
from filters import movie_filter, type_filter, time_filter

# Apply filters step by step
filtered_df = movie_filter(df)
filtered_df = type_filter(filtered_df)
filtered_df = time_filter(filtered_df)
