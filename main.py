#Streamlit

import streamlit as st
import pandas as pd
import numpy as np
import srt
import io

st.sidebar.title("Subtitle Cleaning")
input_srt = st.sidebar.file_uploader("Upload SRT file:")
input_scc = st.sidebar.file_uploader("Upload SCC file:")


def run():
    for sub in srt.parse(input_srt):
        print(sub)
    df = pd.read_csv(srt_file, delim_whitespace=True, header=None)
    print(df)

if st.sidebar.button("Run cleaning"):
    run()
