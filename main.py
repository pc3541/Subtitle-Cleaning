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
    subs = []
    df = pd.DataFrame()
    stringio = io.StringIO(input_srt.getvalue().decode("utf-8"))
    data = stringio.read()
    subtitle_generator = srt.parse(data)
    subtitles = list(subtitle_generator)
    for x in range(len(subtitles)):
        subtitles[x].start = srt.timedelta_to_srt_timestamp(subtitles[x].start)
        starts.append(subtitles[x].start)
        subtitles[x].end = srt.timedelta_to_srt_timestamp(subtitles[x].end)
        ends.append(subtitles[x].end)
        subs.append(subtitles[x].content)
    df["Starts"] = starts
    df["Ends"] = ends
    df["Subtitles"] = subs
    st.write(df)
    
if st.sidebar.button("Run cleaning"):
    run()
