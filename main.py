#Streamlit

import streamlit as st
import pandas as pd
import numpy as np
import Subtitle
import io

st.sidebar.title("Subtitle Cleaning")
input_srt = st.sidebar.file_uploader("Upload SRT file:")
input_scc = st.sidebar.file_uploader("Upload SCC file:")


def run():
    srt = Subtitle(input_srt)
    srt_file = srt.open()
    df = pd.read_csv(srt_file, delim_whitespace=True, header=None)
    print(df)

if st.sidebar.button("Run cleaning"):
    run()
