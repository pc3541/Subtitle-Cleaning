#Streamlit

import streamlit as st
import pandas as pd
import numpy as np
import pysrt

st.sidebar.title("Subtitle Cleaning")
input_srt = st.sidebar.file_uploader("Upload SRT file:")
input_scc = st.sidebar.file_uploader("Upload SCC file:")


def run():
    st.write(input_srt)

if st.sidebar.button("Run cleaning"):
    run()
