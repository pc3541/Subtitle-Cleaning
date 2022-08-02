#Streamlit

import streamlit as st
import pandas as pd
import numpy as np
import pysrt

st.sidebar.title("Subtitle Cleaning")
input_srt = st.sidebar.file_uploader("Upload SRT file:")
input_scc = st.sidebar.file_uploader("Upload SCC file:")


def run():
    subs = pysrt.open(input_srt)
    for sub in subs:
        print(sub.text)
        print()
    df = pd.read_csv(subs)
    print(df)

if st.sidebar.button("Run cleaning"):
    run()
