#Streamlit

import streamlit as st
import pandas as pd
import srt
import io
import pycaption
from pycaption import SRTReader, SCCReader

st.sidebar.title("Subtitle Cleaning")
input_srt = st.sidebar.file_uploader("Upload SRT file:", type=['srt'])
input_scc = st.sidebar.file_uploader("Upload SCC file:", type=['scc'])

def run():
    pysubs = SCCReader().read(input_scc.getvalue().decode("utf-8"))
    st.write(pysubs)
    
if st.sidebar.button("Run cleaning"):
    run()
