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
    content = io.StringIO(input_srt.getvalue().decode('utf-8'))
    data = content.read()
    st.write(data)

if st.sidebar.button("Run cleaning"):
    run()
