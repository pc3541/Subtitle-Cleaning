#Streamlit

import streamlit as st
import pandas as pd
import srt
import io
import pycaption
from pycaption import SCCReader, SRTWriter

bad_words = pd.read_csv("https://raw.githubusercontent.com/pc3541/Subtitle-Cleaning/main/exclusion_words.csv")

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
    filtered_df_srt = pd.DataFrame(names=["Starts","Ends","Filtered subtitles"])
    filtered_df_scc = pd.DataFrame(names=["Starts","Ends","Filtered subtitles"])
    
    if input_srt is not None:
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
        st.write("Uploaded subtitles (SRT):")
        st.dataframe(df_srt)
        st.write("")
        st.write("Filtered subtitles (SRT):")
        for word in bad_words:
            filtered_df_srt.concat(df_srt['Subtitles'].str.contains("word"))
        st.dataframe(filtered_df_srt)
    
    if input_scc is not None:
        pysubs = SCCReader().read(input_scc.getvalue().decode("utf-8"))
        final = SRTWriter().write(pysubs)
        subtitle_generator2 = srt.parse(final)
        subtitles2 = list(subtitle_generator2)
        for x in range(len(subtitles2)):
            subtitles2[x].start = srt.timedelta_to_srt_timestamp(subtitles2[x].start)
            starts_scc.append(subtitles2[x].start)
            subtitles2[x].end = srt.timedelta_to_srt_timestamp(subtitles2[x].end)
            ends_scc.append(subtitles2[x].end)
            subs_scc.append(subtitles2[x].content)
        df_scc["Starts"] = starts_scc
        df_scc["Ends"] = ends_scc
        df_scc["Subtitles"] = subs_scc
        st.write("Uploaded subtitles (SCC):")
        st.dataframe(df_scc)
        st.write("")
        st.write("Filtered subtitles (SCC):")
        for word in bad_words:
            filtered_df_scc.concat(df_scc['Subtitles'].str.contains("word"))
        st.dataframe(filtered_df_scc) 
    
if st.sidebar.button("Run cleaning"):
    run()
