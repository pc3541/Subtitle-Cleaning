#Streamlit

import streamlit as st
import pandas as pd
import numpy as np
import pysrt

st.sidebar.title("Subtitle Cleaning")
input_file = st.sidebar.file_uploader("Upload SRT file:")
input_scc = st.sidebar.file_uploader("Upload SCC file:")


def run():
    starts = []
    ends = []
    subtitles = []
    df = pd.DataFrame()
    input_file = list(uploader.value.values())[0]
    content = input_file['content']
    content = io.StringIO(content.decode('utf-8'))
    subs = pysrt.open(content)
    for sub in subs:
        starts.append(sub.start)
        ends.append(sub.end)
        subtitles.append(sub.text)
    df["Starts"] = starts
    df["Ends"] = ends
    df["Subtitles"] = subtitles
    print(df)

if st.sidebar.button("Run cleaning"):
    run()
