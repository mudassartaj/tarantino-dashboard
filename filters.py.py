import streamlit as st

# Filter by Movie
def movie_filter(df):
    movies = st.sidebar.multiselect(
        "Select Movie",
        df['movie'].unique(),
        default=df['movie'].unique()
    )
    return df[df['movie'].isin(movies)]

# Filter by Event Type (Profanity / Death)
def type_filter(df):
    types = st.sidebar.multiselect(
        "Select Event Type",
        df['type'].unique(),
        default=df['type'].unique()
    )
    return df[df['type'].isin(types)]

# Filter by Timeline (Minutes into Movie)
def time_filter(df):
    min_time, max_time = int(df['minutes_in'].min()), int(df['minutes_in'].max())
    selected_range = st.sidebar.slider(
        "Select Time Range",
        min_time, max_time,
        (min_time, max_time)
    )
    return df[(df['minutes_in'] >= selected_range[0]) & (df['minutes_in'] <= selected_range[1])]
