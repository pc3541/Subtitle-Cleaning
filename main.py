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

    
    stringio2 = io.StringIO(input_scc.getvalue().decode("utf-8"))
    data2 = stringio2.read()
    pysubs = SCCReader().read(data2)
    data3 = pysubs.get_captions(lang="en-US")
    df2 = pd.DataFrame(data3)
    st.dataframe(df2)    
    
if st.sidebar.button("Run cleaning"):
    run()
