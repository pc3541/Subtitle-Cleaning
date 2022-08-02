#Streamlit

import streamlit as st
import pandas as pd
import numpy as np
import pysrt
import io

st.sidebar.title("Subtitle Cleaning")
input_srt = st.sidebar.file_uploader("Upload SRT file:")
input_scc = st.sidebar.file_uploader("Upload SCC file:")


def run():
    dataframe = pd.read_csv(inpurt_srt)
    st.write(dataframe)

if st.sidebar.button("Run cleaning"):
    run()
