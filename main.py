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
    starts_srt = []
    ends_srt = []
    subs_srt = []
    starts_scc = []
    ends_scc = []
    subs_scc = []
    df_srt = pd.DataFrame()
    df_scc = pd.DataFrame()
    
    stringio = io.StringIO(input_srt.getvalue().decode("utf-8"))
    data = stringio.read()
    subtitle_generator = srt.parse(data)
    subtitles = list(subtitle_generator)
    for x in range(len(subtitles)):
        subtitles[x].start = srt.timedelta_to_srt_timestamp(subtitles[x].start)
        starts_srt.append(subtitles[x].start)
        subtitles[x].end = srt.timedelta_to_srt_timestamp(subtitles[x].end)
        ends_srt.append(subtitles[x].end)
        subs_srt.append(subtitles[x].content)
    df_srt["Starts"] = starts_srt
    df_srt["Ends"] = ends_srt
    df_srt["Subtitles"] = subs_srt
    st.write("Uploaded subtitles:")
    st.dataframe(df_srt)
    st.write("")
    st.write("Filtered subtitles (keyword: 'you'):")
    filtered = df_srt[df_srt['Subtitles'].str.contains("you")]
    st.dataframe(filtered)
    
    stringio2 = io.StringIO(input_scc.getvalue().decode("utf-8"))
    data2 = stringio2.read()
    pysubs = SCCReader().read(data2)
    data3 = pysubs.get_captions(lang="en-US")
    df2 = pd.DataFrame(data3)
    st.dataframe(df2)    
    
if st.sidebar.button("Run cleaning"):
    run()
