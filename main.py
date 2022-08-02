#Streamlit

import streamlit as st
import pandas as pd
import numpy as np
import srt
import io

st.sidebar.title("Subtitle Cleaning")
input_srt = st.sidebar.file_uploader("Upload SRT file:", type=['srt'])
input_scc = st.sidebar.file_uploader("Upload SCC file:")


def run():
    starts = []
    ends = []
    subtitles = []
    df = pd.DataFrame()
    stringio = io.StringIO(input_srt.getvalue().decode("utf-8"))
    data = stringio.read()
    subtitle_generator = srt.parse(data)
    subtitles = list(subtitle_generator)
    for x in range(len(subtitles)):
        starts.append(subtitles[x].start)
        ends.append(subtitles[x].end)
        subtitles.append(subtitles[x].content)
    df["Starts"] = starts
    df["Starts"] = df["Starts"].dt.days
    st.write(df["Starts"])
    df["Ends"] = ends
    df["Ends"] = df["Ends"].dt.days
    st.write(df["Ends"])
    df["Subtitles"] = subtitles
    st.write(df)

if st.sidebar.button("Run cleaning"):
    run()
