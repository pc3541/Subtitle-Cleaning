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
    st.write(subtitles)
    for sub in subtitles:
        starts.append(sub.start)
        ends.append(sub.end)
        subtitles.append(sub.content)
    df["Starts"] = starts
    df["Ends"] = ends
    df["Subtitles"] = subtitles
    print(df)

if st.sidebar.button("Run cleaning"):
    run()
