import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# 1. Pie Chart
def pie_chart(df):
    st.subheader("Pie Chart: Profanity vs Deaths")
    type_counts = df['type'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=90)
    st.pyplot(fig)

# 2. Histogram
def histogram_chart(df):
    st.subheader("Histogram: Frequency of Events Across Timeline")
    fig, ax = plt.subplots()
    sns.histplot(df['minutes_in'], bins=20, kde=True, ax=ax)
    ax.set_xlabel("Minutes into Movie")
    ax.set_ylabel("Count")
    st.pyplot(fig)

# 3. Line Chart
def line_chart(df):
    st.subheader("Line Chart: Events Over Movie Timeline")
    fig, ax = plt.subplots()
    sns.lineplot(x="minutes_in", y="type", data=df, ax=ax)
    st.pyplot(fig)

# 4. Bar Chart
def bar_chart(df):
    st.subheader("Bar Chart: Profanity Counts Across Movies")
    movie_counts = df['movie'].value_counts().reset_index()
    movie_counts.columns = ['movie', 'count']
    fig, ax = plt.subplots()
    sns.barplot(x="movie", y="count", data=movie_counts, ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

# 5. Scatter Plot
def scatter_chart(df):
    st.subheader("Scatter Plot: Profanity vs Deaths per Scene")
    df['is_death'] = df['type'].apply(lambda x: 1 if x.lower()=='death' else 0)
    df['is_profanity'] = df['type'].apply(lambda x: 1 if x.lower()=='profanity' else 0)
    fig, ax = plt.subplots()
    sns.scatterplot(x="is_profanity", y="is_death", data=df, ax=ax)
    st.pyplot(fig)

# 6. Box Plot
def box_chart(df):
    st.subheader("Box Plot: Spread of Events Across Movies")
    fig, ax = plt.subplots()
    sns.boxplot(x="movie", y="minutes_in", data=df, ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

# 7. Heatmap
def heatmap_chart(df):
    st.subheader("Heatmap: Correlation Between Features")
    df['is_death'] = df['type'].apply(lambda x: 1 if x.lower()=='death' else 0)
    df['is_profanity'] = df['type'].apply(lambda x: 1 if x.lower()=='profanity' else 0)
    corr = df[['minutes_in','is_death','is_profanity']].corr()
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

# 8. Area Chart
def area_chart(df):
    st.subheader("Area Chart: Cumulative Profanity Over Time")
    profanity_df = df[df['type']=='profanity']
    profanity_df['count'] = 1
    profanity_df = profanity_df.groupby('minutes_in')['count'].sum().cumsum()
    fig, ax = plt.subplots()
    ax.fill_between(profanity_df.index, profanity_df.values, alpha=0.4)
    ax.set_xlabel("Minutes into Movie")
    ax.set_ylabel("Cumulative Count")
    st.pyplot(fig)

# 9. Count Plot
def count_chart(df):
    st.subheader("Count Plot: Frequency of Categories")
    fig, ax = plt.subplots()
    sns.countplot(x="type", data=df, ax=ax)
    st.pyplot(fig)

# 10. Violin Plot
def violin_chart(df):
    st.subheader("Violin Plot: Distribution of Event Intensity per Movie")
    fig, ax = plt.subplots()
    sns.violinplot(x="movie", y="minutes_in", data=df, ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)
