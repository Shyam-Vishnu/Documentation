# Neccessary packages
import pandas as pd
import streamlit as st
import numpy as np
import plotly
import plotly.express as px
from PIL import Image
import os

# Logo
img = Image.open('C:\\Users\\Shyam\\PycharmProjects\\streamlit_dokken\\wb.png')
# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Dokken Dashboard", page_icon=img, layout="wide")


# Reading the file
# df = pd.read_csv('C:\\Users\\Shyam\\PycharmProjects\\streamlit_dokken\\test.csv')
mk11_sf = pd.read_csv('C:\\Users\\Shyam\\PycharmProjects\\streamlit_dokken\\mk11_segment_flows.csv')
mk11_pp = pd.read_csv('C:\\Users\\Shyam\\PycharmProjects\\streamlit_dokken\\mk_11_pp.csv')
base_seg_flows = mk11_sf.copy()
bpp = mk11_pp.copy()


# Sidebar -- Overall
uploaded_file = st.sidebar.file_uploader("Upload Dokken Summary file", type=['csv', 'xlsx'])

# Uploading file here
df = pd.read_csv(uploaded_file)





# Weekly return rate factor
wrrf = st.sidebar.slider("Select weekly return rate factor:", min_value=0.0, max_value=1.0, step=0.1)
st.sidebar.header("Please Filter Here: Summaries")
options = st.sidebar.radio("Select Sheet:",
                           options=["Weekly Summary", "Executive Summary", "Monthly Summary", "Media Planning",
                                    "Overall Trend",
                                    "Approach"])
Week = st.sidebar.selectbox(
    "Select the Week:",
    options=df["Week"].unique()
    # default=2
)
help = st.sidebar.button("Help")
if help:
    st.sidebar.text("Download documentation")
    st.sidebar.write("https://github.com/Shyam-Vishnu/Documentation/blob/main/New%20Documentation%20file.docx",
                     unsafe_allow_html=True)

# Baseline segment flows calculations
base_seg_flows['NPCont'] = mk11_sf['NPCont'] * wrrf
base_seg_flows['NPLoyal'] = mk11_sf['NPLoyal'] * wrrf
base_seg_flows['Conti_Cont'] = mk11_sf['Conti_Cont'] * wrrf
base_seg_flows['Conti_Loyal'] = mk11_sf['Conti_Loyal'] * wrrf
base_seg_flows['Loyal_Cont'] = mk11_sf['Loyal_Cont'] * wrrf
base_seg_flows['Loyal_Loyal'] = mk11_sf['Loyal_Loyal'] * wrrf
base_seg_flows['Reaqq_Cont'] = mk11_sf['Reaqq_Cont'] * wrrf
base_seg_flows['Reaqq_Loyal'] = mk11_sf['Reaqq_Loyal'] * wrrf
base_seg_flows['Inac_Cont'] = mk11_sf['Inac_Cont'] * wrrf
base_seg_flows['Inac_Loyal'] = mk11_sf['Inac_Loyal'] * wrrf
base_seg_flows['Inac_Reacq'] = mk11_sf['Inac_Reacq'] * wrrf

# else same things * user input


# Add formulas
# bpp Baseline paid penetration = Mk11_pp * wrrf
# Multiply by quarter values

# rename excel columns
# Have 8 quarters
# If mk_11_pp = quarter 1
# st.text("BPP")
# st.dataframe(bpp)
# st.text("MK11 paid penetration")
# st.dataframe(mk11_pp)

# Calculating Quartely PP_New growths

bpp['PP_New'] = np.where(bpp['Quarter'] == 'Q1', mk11_pp['PP_New'] * 0.75,
                         np.where(bpp['Quarter'] == 'Q2', mk11_pp['PP_New'] * 0.9,
                                  np.where(bpp['Quarter'] == 'Q3', mk11_pp['PP_New'] * 0.7,
                                           np.where(bpp['Quarter'] == 'Q4', mk11_pp['PP_New'] * 0.8,
                                                    np.where(bpp['Quarter'] == 'Q5', mk11_pp['PP_New'] * 0.9,
                                                             np.where(bpp['Quarter'] == 'Q6', mk11_pp['PP_New'] * 1,
                                                                      np.where(bpp['Quarter'] == 'Q7',
                                                                               mk11_pp['PP_New'] * 1.1,
                                                                               np.where(bpp['Quarter'] == 'Q8',
                                                                                        mk11_pp['PP_New'] * 0.01,
                                                                                        mk11_pp['PP_New']))))))))

# bpp['PP_New'] = mk11_pp['PP_New']

# Calculating Quartely PP_Continous growths

bpp['PP_Continuous'] = np.where(bpp['Quarter'] == 'Q1', mk11_pp['PP_Continuous'] * 1.5,
                                np.where(bpp['Quarter'] == 'Q2', mk11_pp['PP_Continuous'] * 1.65,
                                         np.where(bpp['Quarter'] == 'Q3', mk11_pp['PP_Continuous'] * 1.2,
                                                  np.where(bpp['Quarter'] == 'Q4', mk11_pp['PP_Continuous'] * 1.3,
                                                           np.where(bpp['Quarter'] == 'Q5',
                                                                    mk11_pp['PP_Continuous'] * 1.4,
                                                                    np.where(bpp['Quarter'] == 'Q6',
                                                                             mk11_pp['PP_Continuous'] * 1.5,
                                                                             np.where(bpp['Quarter'] == 'Q7',
                                                                                      mk11_pp['PP_Continuous'] * 1.6,
                                                                                      np.where(bpp['Quarter'] == 'Q8',
                                                                                               mk11_pp[
                                                                                                   'PP_Continuous'] * 1.7,
                                                                                               mk11_pp['PP_New']))))))))

# Calculating Quartely PP_Loyal growths
bpp['PP_Loyal'] = np.where(bpp['Quarter'] == 'Q1', mk11_pp['PP_Loyal'] * 3,
                           np.where(bpp['Quarter'] == 'Q2', mk11_pp['PP_Loyal'] * 3.15,
                                    np.where(bpp['Quarter'] == 'Q3', mk11_pp['PP_Loyal'] * 2.2,
                                             np.where(bpp['Quarter'] == 'Q4', mk11_pp['PP_Loyal'] * 2.3,
                                                      np.where(bpp['Quarter'] == 'Q5',
                                                               mk11_pp['PP_Loyal'] * 2.4,
                                                               np.where(bpp['Quarter'] == 'Q6',
                                                                        mk11_pp['PP_Continuous'] * 2.5,
                                                                        np.where(bpp['Quarter'] == 'Q7',
                                                                                 mk11_pp[
                                                                                     'PP_Loyal'] * 2.6,
                                                                                 np.where(
                                                                                     bpp['Quarter'] == 'Q8',
                                                                                     mk11_pp[
                                                                                         'PP_Loyal'] * 2.8,
                                                                                     mk11_pp['PP_Loyal']))))))))

# Calculating Quartely PP_Reaqquired growths
bpp['PP_Reacquired'] = np.where(bpp['Quarter'] == 'Q1', mk11_pp['PP_Reacquired'] * 1.2,
                                np.where(bpp['Quarter'] == 'Q2', mk11_pp['PP_Reacquired'] * 1.28,
                                         np.where(bpp['Quarter'] == 'Q3', mk11_pp['PP_Reacquired'] * 0.9,
                                                  np.where(bpp['Quarter'] == 'Q4', mk11_pp['PP_Reacquired'] * 0.95,
                                                           np.where(bpp['Quarter'] == 'Q5',
                                                                    mk11_pp['PP_Reacquired'] * 1.0,
                                                                    np.where(bpp['Quarter'] == 'Q6',
                                                                             mk11_pp['PP_Reacquired'] * 1.05,
                                                                             np.where(bpp['Quarter'] == 'Q7',
                                                                                      mk11_pp[
                                                                                          'PP_Reacquired'] * 1.1,
                                                                                      np.where(
                                                                                          bpp['Quarter'] == 'Q8',
                                                                                          mk11_pp[
                                                                                              'PP_Reacquired'] * 1.15,
                                                                                          mk11_pp['PP_New']))))))))

# Calculating Quartely ARP_New growths
bpp['ARP_New'] = np.where(bpp['Quarter'] == 'Q1', mk11_pp['ARP_New'] * 0.95,
                          np.where(bpp['Quarter'] == 'Q2', mk11_pp['ARP_New'] * 1,
                                   np.where(bpp['Quarter'] == 'Q3', mk11_pp['ARP_New'] * 1.6,
                                            np.where(bpp['Quarter'] == 'Q4', mk11_pp['ARP_New'] * 1.7,
                                                     np.where(bpp['Quarter'] == 'Q5',
                                                              mk11_pp['ARP_New'] * 1.7,
                                                              np.where(bpp['Quarter'] == 'Q6',
                                                                       mk11_pp['ARP_New'] * 1.7,
                                                                       np.where(bpp['Quarter'] == 'Q7',
                                                                                mk11_pp[
                                                                                    'ARP_New'] * 1.7,
                                                                                np.where(
                                                                                    bpp['Quarter'] == 'Q8',
                                                                                    mk11_pp[
                                                                                        'ARP_New'] * 0.5,
                                                                                    mk11_pp['PP_New']))))))))

# Calculating Quartely ARP_Continuous growths
bpp['ARP_Continuous'] = np.where(bpp['Quarter'] == 'Q1', mk11_pp['ARP_Continuous'] * 1.7,
                                 np.where(bpp['Quarter'] == 'Q2', mk11_pp['ARP_Continuous'] * 1.85,
                                          np.where(bpp['Quarter'] == 'Q3', mk11_pp['ARP_Continuous'] * 2.15,
                                                   np.where(bpp['Quarter'] == 'Q4', mk11_pp['ARP_Continuous'] * 2.3,
                                                            np.where(bpp['Quarter'] == 'Q5',
                                                                     mk11_pp['ARP_Continuous'] * 2.4,
                                                                     np.where(bpp['Quarter'] == 'Q6',
                                                                              mk11_pp['ARP_Continuous'] * 2.45,
                                                                              np.where(bpp['Quarter'] == 'Q7',
                                                                                       mk11_pp[
                                                                                           'ARP_Continuous'] * 2.6,
                                                                                       np.where(
                                                                                           bpp['Quarter'] == 'Q8',
                                                                                           mk11_pp[
                                                                                               'ARP_Continuous'] * 2.75,
                                                                                           mk11_pp[
                                                                                               'ARP_Continuous']))))))))

## Calculating Quartely ARP_Loyal growths
bpp['ARP_Loyal'] = np.where(bpp['Quarter'] == 'Q1', mk11_pp['ARP_Loyal'] * 2.9,
                            np.where(bpp['Quarter'] == 'Q2', mk11_pp['ARP_Loyal'] * 3.1,
                                     np.where(bpp['Quarter'] == 'Q3', mk11_pp['ARP_Loyal'] * 3.3,
                                              np.where(bpp['Quarter'] == 'Q4', mk11_pp['ARP_Loyal'] * 3.5,
                                                       np.where(bpp['Quarter'] == 'Q5',
                                                                mk11_pp['ARP_Loyal'] * 3.5,
                                                                np.where(bpp['Quarter'] == 'Q6',
                                                                         mk11_pp['ARP_Loyal'] * 2.5,
                                                                         np.where(bpp['Quarter'] == 'Q7',
                                                                                  mk11_pp[
                                                                                      'ARP_Loyal'] * 3.5,
                                                                                  np.where(
                                                                                      bpp['Quarter'] == 'Q8',
                                                                                      mk11_pp[
                                                                                          'ARP_Loyal'] * 3.7,
                                                                                      mk11_pp['ARP_Loyal']))))))))

# Calculating Quartely ARP_Reaccquired growths
bpp['ARP_Reacquired'] = np.where(bpp['Quarter'] == 'Q1', mk11_pp['ARP_Reacquired'] * 1,
                                 np.where(bpp['Quarter'] == 'Q2', mk11_pp['ARP_Reacquired'] * 1.1,
                                          np.where(bpp['Quarter'] == 'Q3', mk11_pp['ARP_Reacquired'] * 1.2,
                                                   np.where(bpp['Quarter'] == 'Q4', mk11_pp['ARP_Reacquired'] * 1.3,
                                                            np.where(bpp['Quarter'] == 'Q5',
                                                                     mk11_pp['ARP_Reacquired'] * 1.4,
                                                                     np.where(bpp['Quarter'] == 'Q6',
                                                                              mk11_pp['ARP_Reacquired'] * 1.5,
                                                                              np.where(bpp['Quarter'] == 'Q7',
                                                                                       mk11_pp[
                                                                                           'ARP_Reacquired'] * 1.6,
                                                                                       np.where(
                                                                                           bpp['Quarter'] == 'Q8',
                                                                                           mk11_pp[
                                                                                               'ARP_Reacquired'] * 1.7,
                                                                                           mk11_pp[
                                                                                               'ARP_Reacquired']))))))))

#st.text("BPP")
#st.dataframe(bpp)
# User input


# Querying for sidebar
# Gettting df_selection here
df_selection = df.query(
    "Week == @Week"
)

df_temp = df.query(
    "Week == @Week -1"
)


# df_prev = df.query(
# "Week == @Week -1"
# )

# CURR_prev = round(df_prev["Continuous_new"]*(df_prev['Conti_Conti']+df_prev['Conti_Loyal']),2)
# st.text(CURR_prev)

#Segment Movement for Weekly active users






# ---- MAINPAGE ----
def weekly(df_selection):
    st.title("Dokken F2P Weekly Summary")
    # st.write(bsf['NPCont'])
    st.subheader("Key Metrics :bar_chart:")
    choices = ['None', 'Battle Pass', 'New Skin', 'New Map', 'New Char', 'Seasonal Event', 'Holiday Event']

    # Creating events here
    # Add even paid penetration weights
    event1, event2, event3, event4, event5 = st.columns(5)
    with event1:
        # st.subheader("RURR")
        result1 = st.selectbox("Pick Event One", choices)
        # st.subheader(RURR)

    with event2:
        result2 = st.selectbox("Pick Event Two", choices)
        # st.subheader(NURR)
    with event3:
        result3 = st.selectbox("Pick Event Three", choices)
        # st.subheader(CURR)

    with event4:
        result4 = st.selectbox("Pick Event Four", choices)
        # st.subheader(LURR)

    with event5:
        result5 = st.selectbox("Pick Event Five", choices)

    # Create Event spike wts
    wt1 = [0.01933678, 0.00043897, 0, 0.09796553, 0.01398158, 0.01522444, 0.02802534, 0.06838619, 0, 0.10353409,
           0.03459703]
    wt2 = [0.00684096, 0.04378952, 0.00252638, 0.01493058, 0.04181244, 0.00156865, 0.00559157, 0.02326289, 0.02367399,
           0.05457016, 0.00418115]
    wt3 = [0.00684096, 0.04378952, 0.00252638, 0.01493058, 0.04181244, 0.00156865, 0.00559157, 0.02326289, 0.02367399,
           0.05457016, 0.00418115]
    wt4 = [0.00684096, 0.04378952, 0.00252638, 0.01493058, 0.04181244, 0.00156865, 0.00559157, 0.02326289, 0.02367399,
           0.05457016, 0.00418115]
    wt5 = [0.03582896, 0.04769629, 0.01033588, 0.03985346, 0.01921122, 0.01358562, 0.01802036, 0.0549332, 0.01732869,
           0.04106793, 0.02651673]
    wt6 = [0.02010398, 0.04549732, 0.00277594, 0.0055021, 0.04992688, 0.00085519, 0, 0.02847288, 0.02234073, 0.09766278,
           0.01162847]
    wt_pp1 = np.array([0.0721476, 0.92807986, 0.70364341, 0.17599919, 0.03133973, 0.12042204, 0.14510639, 0.16120952])
    wt_pp2 = np.array([0.0721476, 0.92807986, 0.70364341, 0.17599919, 0.03133973, 0.12042204, 0.14510639, 0.16120952])
    wt_pp3 = np.array([0.0721476, 0.92807986, 0.70364341, 0.17599919, 0.03133973, 0.12042204, 0.14510639, 0.16120952])
    wt_pp4 = np.array([0.0721476, 0.92807986, 0.70364341, 0.17599919, 0.03133973, 0.12042204, 0.14510639, 0.16120952])
    wt_pp5 = np.array([0.0721476, 0.92807986, 0.70364341, 0.17599919, 0.03133973, 0.12042204, 0.14510639, 0.16120952])
    mf = 0
    # event1 spike
    if result1 == 'Battle pass':
        wt1 = np.array(
            [0.01933678, 0.00043897, 0, 0.09796553, 0.01398158, 0.01522444, 0.02802534, 0.06838619, 0, 0.10353409,
             0.03459703])
        wt_pp1 = np.array(
            [0.0721476, 0.92807986, 0.70364341, 0.17599919, 0.03133973, 0.12042204, 0.14510639, 0.16120952])
    elif result1 == 'New Skin':
        wt1 = np.array(
            [0.00684096, 0.04378952, 0.00252638, 0.01493058, 0.04181244, 0.00156865, 0.00559157, 0.02326289, 0.02367399,
             0.05457016, 0.00418115])
        wt_pp1 = np.array(
            [0.04994105, 0.18555615, 0.08010377, 0.15032397, 0.02006565, 0.00468963, 0.01830367, 0.02137253])
    elif result1 == 'New Map':
        wt1 = np.array([0.00684096, 0.04378952, 0.00252638, 0.01493058, 0.04181244, 0.00156865, 0.00559157, 0.02326289,
                        0.02367399, 0.05457016, 0.00418115])
        wt_pp1 = np.array(
            [0.04994105, 0.18555615, 0.08010377, 0.15032397, 0.02006565, 0.00468963, 0.01830367, 0.02137253])
    elif result1 == 'New Char':
        wt1 = np.array(
            [0.00684096, 0.04378952, 0.00252638, 0.01493058, 0.04181244, 0.00156865, 0.00559157, 0.02326289, 0.02367399,
             0.05457016, 0.00418115])
        wt_pp1 = np.array(
            [0.04994105, 0.18555615, 0.08010377, 0.15032397, 0.02006565, 0.00468963, 0.01830367, 0.02137253])
    elif result1 == 'Seasonal Event':
        wt1 = np.array(
            [0.03582896, 0.04769629, 0.01033588, 0.03985346, 0.01921122, 0.01358562, 0.01802036, 0.0549332, 0.01732869,
             0.04106793, 0.02651673])
        wt_pp1 = np.array([0.12304675, 0.22324007, 0.26435935, 0.10899468, 0, 0.0230188, 0.056025, 0.00613955])
    elif result1 == 'Holiday Event':
        wt1 = np.array(
            [0.02010398, 0.04549732, 0.00277594, 0.0055021, 0.04992688, 0.00085519, 0, 0.02847288, 0.02234073,
             0.09766278, 0.01162847])
        wt_pp1 = np.array([0.07334202, 0.13514469, 0.10050129, 0.1000663, 0, 0, 0.00338776, 0.00431145])
    elif result1 == 'None':
        wt1 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        wt_pp1 = np.array([0, 0, 0, 0, 0, 0, 0, 0])

    # st.write(wt1)
    # Event 2 spike
    if result2 == 'Battle pass':
        wt2 = np.array(
            [0.01933678, 0.00043897, 0, 0.09796553, 0.01398158, 0.01522444, 0.02802534, 0.06838619, 0, 0.10353409,
             0.03459703])
        wt_pp2 = np.array(
            [0.0721476, 0.92807986, 0.70364341, 0.17599919, 0.03133973, 0.12042204, 0.14510639, 0.16120952])
    elif result2 == 'New Skin':
        wt2 = np.array(
            [0.00684096, 0.04378952, 0.00252638, 0.01493058, 0.04181244, 0.00156865, 0.00559157, 0.02326289, 0.02367399,
             0.05457016, 0.00418115])
        wt_pp2 = np.array(
            [0.04994105, 0.18555615, 0.08010377, 0.15032397, 0.02006565, 0.00468963, 0.01830367, 0.02137253])
    elif result2 == 'New Map':
        wt2 = np.array([0.00684096, 0.04378952, 0.00252638, 0.01493058, 0.04181244, 0.00156865, 0.00559157, 0.02326289,
                        0.02367399, 0.05457016, 0.00418115])
        wt_pp2 = np.array(
            [0.04994105, 0.18555615, 0.08010377, 0.15032397, 0.02006565, 0.00468963, 0.01830367, 0.02137253])
    elif result2 == 'New Char':
        wt2 = np.array(
            [0.00684096, 0.04378952, 0.00252638, 0.01493058, 0.04181244, 0.00156865, 0.00559157, 0.02326289, 0.02367399,
             0.05457016, 0.00418115])
        wt_pp2 = np.array(
            [0.04994105, 0.18555615, 0.08010377, 0.15032397, 0.02006565, 0.00468963, 0.01830367, 0.02137253])
    elif result2 == 'Seasonal Event':
        wt2 = np.array(
            [0.03582896, 0.04769629, 0.01033588, 0.03985346, 0.01921122, 0.01358562, 0.01802036, 0.0549332, 0.01732869,
             0.04106793, 0.02651673])
        wt_pp2 = np.array([0.12304675, 0.22324007, 0.26435935, 0.10899468, 0, 0.0230188, 0.056025, 0.00613955])
    elif result2 == 'Holiday Event':
        wt2 = np.array(
            [0.02010398, 0.04549732, 0.00277594, 0.0055021, 0.04992688, 0.00085519, 0, 0.02847288, 0.02234073,
             0.09766278, 0.01162847])
        wt_pp2 = np.array([0.07334202, 0.13514469, 0.10050129, 0.1000663, 0, 0, 0.00338776, 0.00431145])
    elif result2 == 'None':
        wt2 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        wt_pp2 = np.array([0, 0, 0, 0, 0, 0, 0, 0])

    # Event 3 spike
    if result3 == 'Battle pass':
        wt3 = np.array(
            [0.01933678, 0.00043897, 0, 0.09796553, 0.01398158, 0.01522444, 0.02802534, 0.06838619, 0, 0.10353409,
             0.03459703])
        wt_pp3 = np.array(
            [0.0721476, 0.92807986, 0.70364341, 0.17599919, 0.03133973, 0.12042204, 0.14510639, 0.16120952])
    elif result3 == 'New Skin':
        wt3 = np.array(
            [0.00684096, 0.04378952, 0.00252638, 0.01493058, 0.04181244, 0.00156865, 0.00559157, 0.02326289, 0.02367399,
             0.05457016, 0.00418115])
        wt_pp3 = np.array(
            [0.04994105, 0.18555615, 0.08010377, 0.15032397, 0.02006565, 0.00468963, 0.01830367, 0.02137253])
    elif result3 == 'New Map':
        wt3 = np.array([0.00684096, 0.04378952, 0.00252638, 0.01493058, 0.04181244, 0.00156865, 0.00559157, 0.02326289,
                        0.02367399, 0.05457016, 0.00418115])
        wt_pp3 = np.array(
            [0.04994105, 0.18555615, 0.08010377, 0.15032397, 0.02006565, 0.00468963, 0.01830367, 0.02137253])
    elif result3 == 'New Char':
        wt3 = np.array(
            [0.00684096, 0.04378952, 0.00252638, 0.01493058, 0.04181244, 0.00156865, 0.00559157, 0.02326289, 0.02367399,
             0.05457016, 0.00418115])
        wt_pp3 = np.array(
            [0.04994105, 0.18555615, 0.08010377, 0.15032397, 0.02006565, 0.00468963, 0.01830367, 0.02137253])
    elif result3 == 'Seasonal Event':
        wt3 = np.array(
            [0.03582896, 0.04769629, 0.01033588, 0.03985346, 0.01921122, 0.01358562, 0.01802036, 0.0549332, 0.01732869,
             0.04106793, 0.02651673])
        wt_pp3 = np.array([0.12304675, 0.22324007, 0.26435935, 0.10899468, 0, 0.0230188, 0.056025, 0.00613955])
    elif result3 == 'Holiday Event':
        wt3 = np.array(
            [0.02010398, 0.04549732, 0.00277594, 0.0055021, 0.04992688, 0.00085519, 0, 0.02847288, 0.02234073,
             0.09766278, 0.01162847])
        wt_pp3 = np.array([0.07334202, 0.13514469, 0.10050129, 0.1000663, 0, 0, 0.00338776, 0.00431145])
    elif result3 == 'None':
        wt3 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        wt_pp3 = np.array([0, 0, 0, 0, 0, 0, 0, 0])

    # Event 4 spike
    if result4 == 'Battle pass':
        wt4 = np.array(
            [0.01933678, 0.00043897, 0, 0.09796553, 0.01398158, 0.01522444, 0.02802534, 0.06838619, 0, 0.10353409,
             0.03459703])
        wt_pp4 = np.array(
            [0.0721476, 0.92807986, 0.70364341, 0.17599919, 0.03133973, 0.12042204, 0.14510639, 0.16120952])
    elif result4 == 'New Skin':
        wt4 = np.array([0.00684096, 0.04378952, 0.00252638, 0.01493058, 0.04181244, 0.00156865, 0.00559157, 0.02326289,
                        0.02367399, 0.05457016, 0.00418115])
        wt_pp4 = np.array(
            [0.04994105, 0.18555615, 0.08010377, 0.15032397, 0.02006565, 0.00468963, 0.01830367, 0.02137253])
    elif result4 == 'New Map':
        wt4 = np.array([0.00684096, 0.04378952, 0.00252638, 0.01493058, 0.04181244, 0.00156865, 0.00559157, 0.02326289,
                        0.02367399, 0.05457016, 0.00418115])
        wt_pp4 = np.array(
            [0.04994105, 0.18555615, 0.08010377, 0.15032397, 0.02006565, 0.00468963, 0.01830367, 0.02137253])
    elif result4 == 'New Char':
        wt4 = np.array([0.00684096, 0.04378952, 0.00252638, 0.01493058, 0.04181244, 0.00156865, 0.00559157, 0.02326289,
                        0.02367399, 0.05457016, 0.00418115])
        wt_pp4 = np.array(
            [0.04994105, 0.18555615, 0.08010377, 0.15032397, 0.02006565, 0.00468963, 0.01830367, 0.02137253])
    elif result4 == 'Seasonal Event':
        wt4 = np.array([0.03582896, 0.04769629, 0.01033588, 0.03985346, 0.01921122, 0.01358562, 0.01802036, 0.0549332,
                        0.01732869, 0.04106793, 0.02651673])
        wt_pp4 = np.array([0.12304675, 0.22324007, 0.26435935, 0.10899468, 0, 0.0230188, 0.056025, 0.00613955])
    elif result4 == 'Holiday Event':
        wt4 = np.array(
            [0.02010398, 0.04549732, 0.00277594, 0.0055021, 0.04992688, 0.00085519, 0, 0.02847288, 0.02234073,
             0.09766278, 0.01162847])
        wt_pp4 = np.array([0.07334202, 0.13514469, 0.10050129, 0.1000663, 0, 0, 0.00338776, 0.00431145])
    elif result4 == 'None':
        wt4 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        wt_pp4 = np.array([0, 0, 0, 0, 0, 0, 0, 0])

    # Event 5 spike
    if result5 == 'Battle pass':
        wt5 = np.array(
            [0.01933678, 0.00043897, 0, 0.09796553, 0.01398158, 0.01522444, 0.02802534, 0.06838619, 0, 0.10353409,
             0.03459703])
        wt_pp5 = np.array(
            [0.0721476, 0.92807986, 0.70364341, 0.17599919, 0.03133973, 0.12042204, 0.14510639, 0.16120952])
    elif result5 == 'New Skin':
        wt5 = np.array([0.00684096, 0.04378952, 0.00252638, 0.01493058, 0.04181244, 0.00156865, 0.00559157, 0.02326289,
                        0.02367399, 0.05457016, 0.00418115])
        wt_pp5 = np.array(
            [0.04994105, 0.18555615, 0.08010377, 0.15032397, 0.02006565, 0.00468963, 0.01830367, 0.02137253])
    elif result5 == 'New Map':
        wt5 = np.array([0.00684096, 0.04378952, 0.00252638, 0.01493058, 0.04181244, 0.00156865, 0.00559157, 0.02326289,
                        0.02367399, 0.05457016, 0.00418115])
        wt_pp5 = np.array(
            [0.04994105, 0.18555615, 0.08010377, 0.15032397, 0.02006565, 0.00468963, 0.01830367, 0.02137253])

    elif result5 == 'New Char':
        wt5 = np.array([0.00684096, 0.04378952, 0.00252638, 0.01493058, 0.04181244, 0.00156865, 0.00559157, 0.02326289,
                        0.02367399, 0.05457016, 0.00418115])
        wt_pp5 = np.array(
            [0.04994105, 0.18555615, 0.08010377, 0.15032397, 0.02006565, 0.00468963, 0.01830367, 0.02137253])
    elif result5 == 'Seasonal Event':
        wt5 = np.array([0.03582896, 0.04769629, 0.01033588, 0.03985346, 0.01921122, 0.01358562, 0.01802036, 0.0549332,
                        0.01732869, 0.04106793, 0.02651673])
        wt_pp5 = np.array([0.12304675, 0.22324007, 0.26435935, 0.10899468, 0, 0.0230188, 0.056025, 0.00613955])
    elif result5 == 'Holiday Event':
        wt5 = np.array(
            [0.02010398, 0.04549732, 0.00277594, 0.0055021, 0.04992688, 0.00085519, 0, 0.02847288, 0.02234073,
             0.09766278, 0.01162847])
        wt_pp5 = np.array([0.07334202, 0.13514469, 0.10050129, 0.1000663, 0, 0, 0.00338776, 0.00431145])
    elif result5 == 'None':
        wt5 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        wt_pp5 = np.array([0, 0, 0, 0, 0, 0, 0, 0])
    # one_array = [1,1,1,1,1,1,1,1,1,1]
    total_wt = wt1 + wt2 + wt3 + wt4 + wt5
    total_pp_wt = wt_pp1 + wt_pp2 + wt_pp3 + wt_pp4 + wt_pp5

    final_wt = [x + 1 for x in total_wt]
    final_pp_wt = [x + 1 for x in total_pp_wt]

    # st.write(total_wt)
    # st.write(final_wt)

    df2 = pd.DataFrame(final_wt)
    df3 = df2.T

    df_pp_finalwt = pd.DataFrame(final_pp_wt)
    df_pp_final = df_pp_finalwt.T

    # Creating data frame of 106 rows with same weights
    df_weights = pd.concat([df3] * 106, ignore_index=True)
    df_pp = pd.concat([df_pp_final] * 106, ignore_index=True)

    # Mortal Kombat segment flows * wrrf
    # Segment movement for weekly active users

    df_selection['NP_Conti'] = base_seg_flows['NPCont'] * df_weights[0]
    df_selection['NP_Loyal'] = base_seg_flows['NPLoyal'] * df_weights[1]
    df_selection['Conti_Conti'] = base_seg_flows['Conti_Cont'] * df_weights[2]
    df_selection['Conti_Loyal'] = base_seg_flows['Conti_Loyal'] * df_weights[3]
    df_selection['Loyal_Conti'] = base_seg_flows['Loyal_Cont'] * df_weights[4]
    df_selection['Loyal_Loyal'] = base_seg_flows['Loyal_Loyal'] * df_weights[5]
    df_selection['Reacc_Conti'] = base_seg_flows['Reaqq_Cont'] * df_weights[6]
    df_selection['Reacc_Loyal'] = base_seg_flows['Reaqq_Loyal'] * df_weights[7]
    df_selection['Inactive_Conti'] = base_seg_flows['Inac_Cont'] * df_weights[8]
    df_selection['Inactive_Loyal'] = base_seg_flows['Inac_Loyal'] * df_weights[9]
    df_selection['Inactive_Reaccquire'] = base_seg_flows['Inac_Reacq'] * df_weights[10]

    #Weekly active players by segments


    # Paid Penetration and WARPPU
    df_selection['New Players PP'] = bpp['PP_New'] * df_pp[0]
    df_selection['Conti PP'] = bpp['PP_Continuous'] * df_pp[1]
    df_selection['Loyal PP'] = bpp['PP_Loyal'] * df_pp[2]
    df_selection['Reaccuired PP'] = bpp['PP_Reacquired'] * df_pp[3]

    # WARRPU
    df_selection['New Players WARPPU'] = bpp['ARP_New'] * df_pp[4]
    df_selection['Conti WARPPU'] = bpp['ARP_Continuous'] * df_pp[5]
    df_selection['Loyal WARPPU'] = bpp['ARP_Loyal'] * df_pp[6]
    df_selection['Reacc WARPPU'] = bpp['ARP_Reacquired'] * df_pp[7]

    st.dataframe(df_selection)
    # st.dataframe(df_temp)

    with st.expander("Definitons"):
        st.caption("CURR: Continuous user retention rate:  ")
        st.caption("NURR: New user retention rate:  ")
        st.caption("LURR: Loyal user retention rate:  ")
        st.caption("RURR: Reacq user retention rate:  ")

    # TOP KPI's
    total_players = int(df_selection["New Players"].sum())
    wsd = df_selection["Week_Start_Date"]
    continuous_players = df_selection["New Players"] * df_selection["NP_Conti"]
    # st.dataframe(df_temp)

    # Calculating columns neccessary for CURR NURR and RURR
    # def calcualtion_of_wapbs_dynamic(np,):
    # Recreate V6 to Y6 to recreate entire weekly summary
    df_selection['WAP New_Players'] = df_selection['New Players']

    # What is the value you want?
    # WAP by segments continuous







    # Weekly active players by segment calculation
    # Need dynammic approach

    # df_selection["Continuous_new"] = (df_temp['New Players_new'].iloc[0]*df_selection['NP_Conti'].iloc[0])+(df_temp['Continuous_new'].iloc[0]*df_selection['Conti_Conti'].iloc[0])+(df_temp['Loyal_new'].iloc[0]*df_selection['Loyal_Conti'].iloc[0])+(df_temp['Reacquired_new'].iloc[0]*df_selection['Reacc_Conti'].iloc[0])+(df_temp['Inactive_new'].iloc[0]*df_selection['Inactive_Conti'].iloc[0])
    # + (df_temp['Continuous_new']*df_temp['Conti_Conti']) + (df_temp['Loyal_new']*df_temp['Loyal_Conti'])+(df_temp['Reacquired_new']*df_temp['Reacc_Conti'])+(df_temp['Inactive_new']*df_temp['Inactive_Conti'])
    # df_selection["New Players_new"] =
    # df_selection["Loyal_new"] =
    # df_selection["Reacquired_new"] =
    # st.write(bsf['NPCont'])
    # st.write(bsf['NPCont'])
    # st.write(df4[0])


    # Paid penetration
    st.write(df_selection['New Players PP'])
    st.write(df_selection['Conti PP'])
    st.write(df_selection['Loyal PP'])
    st.write(df_selection['Reaccuired PP'])

    # WARPPU
    st.write("WARPPU")
    st.write(df_selection['New Players WARPPU'])
    st.write(df_selection['Conti WARPPU'])
    st.write(df_selection['Loyal WARPPU'])
    st.write(df_selection['Reacc WARPPU'])
    # CURR NURR LURR and RURR
    CURR = round(df_selection["Continuous_new"] * (df_selection['Conti_Conti'] + df_selection['Conti_Loyal']), 2)
    NURR = round(df_selection["New Players_new"] * (df_selection['NP_Conti'] + df_selection['NP_Loyal']), 2)
    LURR = round(df_selection["Loyal_new"] * (df_selection['Loyal_Conti'] + df_selection['Loyal_Loyal']), 2)
    RURR = round(df_selection["Reacquired_new"] * (df_selection['Reacc_Conti'] + df_selection['Reacc_Loyal']), 2)

    Revenue_NP = round(
        df_selection["New Players_new"] * df_selection['New Players_PP'] * df_selection['New Players_WARPPU'])
    Revenue_conti = round(
        df_selection["Continuous_new"] * df_selection['Continuous_PP'] * df_selection['Continuous_WARPPU'])
    Revenue_Loyal = round(df_selection["Loyal_new"] * df_selection['Loyal_PP'] * df_selection['Loyal_WARPPU'])
    Revenue_reaq = round(
        df_selection["Reacquired_new"] * df_selection['Reacquired_PP'] * df_selection['Reacquired_WARPPU'])
    Live_revenue = Revenue_NP + Revenue_conti + Revenue_Loyal + Revenue_reaq
    WAU = df_selection["New Players_new"] + df_selection['Continuous_new'] + df_selection['Loyal_new'] + df_selection[
        'Reacquired_new']
    Paid_Conv = ((df_selection["New Players_PP"] * df_selection['New Players_new']) + (
                df_selection["Continuous_PP"] * df_selection['Continuous_new']) + (
                             df_selection["Loyal_PP"] * df_selection['Loyal_new']) + (
                             df_selection["Reacquired_PP"] * df_selection['Reacquired_new'])) / WAU
    WARPPU = Live_revenue / (Paid_Conv * WAU)

    the_dict = {'Metrics': ['CURR', 'NURR', 'LURR', 'RURR'], 'Values': [CURR, NURR, LURR, RURR]}
    test_plot = pd.DataFrame(the_dict)
    # Not able to create this
    # initialize list of lists
    data = [['CURR', CURR], ['NURR', NURR], ['LURR', LURR], ['RURR', RURR]]
    # Create the pandas DataFrame
    df_test = pd.DataFrame(data, columns=['Metrics', 'Value'])

    curr_col, nurr_col, lurr_col, rurr_col = st.columns(4)

    with rurr_col:
        # st.subheader("RURR")
        rurr_col.metric("RURR", RURR, delta=1)
        # st.subheader(RURR)

    with nurr_col:
        nurr_col.metric("NURR", NURR, delta=1)
        # st.subheader(NURR)
    with curr_col:
        curr_col.metric("CURR", CURR, delta=2)
        # st.subheader(CURR)

    with lurr_col:
        lurr_col.metric("LURR", LURR, delta=1)
        # st.subheader(LURR)

        # Graphs go here

    # Repeat for Paid conversions and warrpu
    # Do executive summary
    # Do monthly summary
    # Format
    # Clean code
    st.bar_chart([CURR, NURR, LURR, RURR])
    # Horizontal bar plot
    st.markdown("""---""")

    st.subheader("Revenue Metrics :bar_chart:")
    with st.expander("What is the revenue model?"):
        st.text("The revenue model is an indication of revenue figures through the life cycle of the game")
        st.caption("New Player revenue: Continuous user retention rate:  ")
        st.caption("Continous Revenue: New user retention rate:  ")
        st.caption("Loyal Revenue: Loyal user retention rate:  ")
        st.caption("Reaqq Revenue: Reacq user retention rate:  ")
    # st.code()
    st.caption("Figures are given below:")
    # st.metric()
    npr, cr, lr, rr = st.columns(4)
    with npr:
        # st.subheader("RURR")
        st.metric("New Player Revenue:", Revenue_NP, delta=7)
        # st.subheader(RURR)

    with cr:
        st.metric("Continuous Revenue:", Revenue_conti, delta=12)
        # st.subheader(NURR)
    with lr:
        st.metric("Loyal Revenue:", Revenue_Loyal, delta=3)
        # st.subheader(CURR)

    with rr:
        st.metric("Reaccquired Revenue:", Revenue_reaq, delta=7)

    st.bar_chart([Revenue_NP, Revenue_conti, Revenue_Loyal, Revenue_reaq])

    st.markdown("""---""")
    st.subheader("Conversions Metrics :bar_chart:")
    with st.expander("Definitons"):
        st.caption("Live revenue: Continuous user retention rate:  ")
        st.caption("Paid conversions: New user retention rate:  ")
        st.caption("WAU: Loyal user retention rate:  ")
        st.caption("WARPPU: Reacq user retention rate:  ")
    live_rev, paid_conv, wau, warppu = st.columns(4)
    with live_rev:
        # st.subheader("RURR")
        st.metric("Live Revenue", round(Live_revenue, 2), delta=5)
        # st.subheader(RURR)

    with paid_conv:
        st.metric("Paid Conversions % ", round(Paid_Conv * 100, 2), delta=5)
        # st.subheader(NURR)
    with wau:
        st.metric("Weekly Active Users", round(WAU, 2), delta=5)
        # st.subheader(CURR)

    with warppu:
        st.metric("WARPPU", round(WARPPU, 2), delta=5)

    # st.bar_chart([Live_revenue,Paid_Conv,WAU,WARPPU])
    st.markdown("""---""")
    # st.area_chart(x_axis_val)

    # Graphs -- interactive
    st.subheader("Visualize the data")
    bar_graph, line_graph, area_chart = st.columns(3)
    with bar_graph:
        x = st.button("Bar graph")
        if x:
            st.bar_chart(CURR)

    with line_graph:
        y = st.button("Line graph")
        if y:
            st.bar_chart(CURR)
    with area_chart:
        z = st.button("Area chart")
        if z:
            st.bar_chart(CURR)

    st.subheader("Create your own Scatter visualizations")
    col1, col2 = st.columns(2)

    x_axis_val = col1.selectbox('Select the X-axis', options=df_selection.columns)
    y_axis_val = col2.selectbox('Select the Y-axis', options=df_selection.columns)

    color = st.color_picker("Select a plot color")

    plot = px.scatter(df, x=x_axis_val, y=y_axis_val)
    plot.update_traces(marker=dict(color=color))
    st.plotly_chart(plot, use_container_width=True)

    plot2 = px.line(df, x=x_axis_val, y=y_axis_val)
    plot2.update_traces(marker=dict(color=color))
    st.plotly_chart(plot2, use_container_width=True)

    plot3 = px.area(df, x=x_axis_val, y=y_axis_val)
    plot3.update_traces(marker=dict(color=color))
    st.plotly_chart(plot3, use_container_width=True)

    st.markdown("---")

    y = st.button("Preview Dataset")
    if y:
        st.dataframe(df)


def monthlysummary(df_selection):
    st.text("Monthly Summaries go here")
    total_players = int(df_selection["New Players"].sum())
    wsd = df_selection["Week_Start_Date"]
    continuous_players = df_selection["New Players"] * df_selection["NP_Conti"]
    CURR = round(df_selection["Continuous_new"] * (df_selection['Conti_Conti'] + df_selection['Conti_Loyal']), 2)
    NURR = round(df_selection["New Players_new"] * (df_selection['NP_Conti'] + df_selection['NP_Loyal']), 2)
    LURR = round(df_selection["Loyal_new"] * (df_selection['Loyal_Conti'] + df_selection['Loyal_Loyal']), 2)
    RURR = round(df_selection["Reacquired_new"] * (df_selection['Reacc_Conti'] + df_selection['Reacc_Loyal']), 2)
    Revenue_NP = round(
        df_selection["New Players_new"] * df_selection['New Players_PP'] * df_selection['New Players_WARPPU'])
    Revenue_conti = round(
        df_selection["Continuous_new"] * df_selection['Continuous_PP'] * df_selection['Continuous_WARPPU'])
    Revenue_Loyal = round(df_selection["Loyal_new"] * df_selection['Loyal_PP'] * df_selection['Loyal_WARPPU'])
    Revenue_reaq = round(
        df_selection["Reacquired_new"] * df_selection['Reacquired_PP'] * df_selection['Reacquired_WARPPU'])
    Live_revenue = Revenue_NP + Revenue_conti + Revenue_Loyal + Revenue_reaq
    # Paid_Conv =
    # WARPPU =
    # WAU =
    # WoW_ReturnRate

    # Create monthly summary

# 2nd
def executivesummary(df_selection):
    st.text("Executive summaries go here")
    st.text("Create global variables, that can be used inside weekly summary for calculation")
    st.write("Total installs:",df['New Players'].sum())
    st.write("Total Live Revenue (Net)", 8)
    st.write("Total LTV / RPI:", df['New Players'].sum()/8)
    st.write("Average WARPPU", 8)
    st.write("Average Paid Penetration", 8)
    st.write("Average WAU", 8)
    st.write("ARPWAU", 8)

    total_players = int(df_selection["New Players"].sum())
    wsd = df_selection["Week_Start_Date"]
    continuous_players = df_selection["New Players"] * df_selection["NP_Conti"]


    '''
    CURR = round(df_selection["Continuous_new"] * (df_selection['Conti_Conti'] + df_selection['Conti_Loyal']), 2)
    NURR = round(df_selection["New Players_new"] * (df_selection['NP_Conti'] + df_selection['NP_Loyal']), 2)
    LURR = round(df_selection["Loyal_new"] * (df_selection['Loyal_Conti'] + df_selection['Loyal_Loyal']), 2)
    RURR = round(df_selection["Reacquired_new"] * (df_selection['Reacc_Conti'] + df_selection['Reacc_Loyal']), 2)
    Revenue_NP = round(
        df_selection["New Players_new"] * df_selection['New Players_PP'] * df_selection['New Players_WARPPU'])
    Revenue_conti = round(
        df_selection["Continuous_new"] * df_selection['Continuous_PP'] * df_selection['Continuous_WARPPU'])
    Revenue_Loyal = round(df_selection["Loyal_new"] * df_selection['Loyal_PP'] * df_selection['Loyal_WARPPU'])
    Revenue_reaq = round(
        df_selection["Reacquired_new"] * df_selection['Reacquired_PP'] * df_selection['Reacquired_WARPPU'])
    Live_revenue = Revenue_NP + Revenue_conti + Revenue_Loyal + Revenue_reaq
    # Paid_Conv =
    # WARPPU =
    # WAU =
    # WoW_ReturnRate

    # Add executive summary formulas
    '''

def mediaPlanning():
    imgt = Image.open('C:\\Users\\Shyam\\PycharmProjects\\streamlit_dokken\\mediaplanning.png')
    st.image(imgt)


def OverallTrend(df):
    # Calculations
    df_ot = df.copy()
    total_players = int(df["New Players"].sum())
    wsd = df["Week_Start_Date"]
    continuous_players = df["New Players"] * df["NP_Conti"]
    df['CURR'] = round(df["Continuous_new"] * (df['Conti_Conti'] + df['Conti_Loyal']), 2)
    NURR = round(df["New Players_new"] * (df['NP_Conti'] + df['NP_Loyal']), 2)
    LURR = round(df["Loyal_new"] * (df['Loyal_Conti'] + df['Loyal_Loyal']), 2)
    RURR = round(df["Reacquired_new"] * (df['Reacc_Conti'] + df['Reacc_Loyal']), 2)
    Revenue_NP = round(df["New Players_new"] * df['New Players_PP'] * df['New Players_WARPPU'])
    Revenue_conti = round(df["Continuous_new"] * df['Continuous_PP'] * df['Continuous_WARPPU'])
    Revenue_Loyal = round(df["Loyal_new"] * df['Loyal_PP'] * df['Loyal_WARPPU'])
    Revenue_reaq = round(df["Reacquired_new"] * df['Reacquired_PP'] * df['Reacquired_WARPPU'])
    Live_revenue = Revenue_NP + Revenue_conti + Revenue_Loyal + Revenue_reaq
    WAU = df["New Players_new"] + df['Continuous_new'] + df['Loyal_new'] + df['Reacquired_new']
    Paid_Conv = ((df["New Players_PP"] * df['New Players_new']) + (df["Continuous_PP"] * df['Continuous_new']) + (
                df["Loyal_PP"] * df['Loyal_new']) + (df["Reacquired_PP"] * df['Reacquired_new'])) / WAU
    WARPPU = Live_revenue / (Paid_Conv * WAU)

    st.header("Overall trends across the data")
    st.markdown("---")

    plot = px.bar(df, x="Week", y="New Players")
    color = st.color_picker("Select a plot color")
    plot.update_traces(marker=dict(color=color))
    st.plotly_chart(plot, use_container_width=True)

    st.metric("2yr Ultimate ARPWAU: ", 0.93)
    st.metric("2022 ARPWAU", f'${0.664}')

    # Add all overall graphs

    '''
    plot = px.line(df_ot, x="Week", y="CURR")
    color = st.color_picker("Select a plot color")
    plot.update_traces(marker=dict(color=color))
    st.plotly_chart(plot, use_container_width=True)
    '''


def Approach():
    st.text("""Assumptions- Overall									
                    1) Brawlhalla Monthly New Players curve was considered for New Players projection									
                    2) Baseline numbers for the KPIs 'Segment transitions', 'ARPPU', 'Paid penetration' were considered same as MK11									

                        Assumptions- Live Calendar									
                        1) In each Narrative Season, a New battle Pass would be released in 1st week									
                        2) The 8 rare skins in 1st month of a Season would be equally distributed across the weeks									
                        3) Guild/Map would be released in 2nd week of 1st month of the season									
                        4) The 2 epic skins in 2nd month of a Season would be released in first and 3rd weeks									
                        5) The 2 Chars in 2nd month of a Season would be released in second and fourth weeks									
                        6) The 8 Chroma skins in 1st month of a Season would be equally distributed across the weeks									
                        7) The 2 Legend skins in 2nd month of a Season would be released in first and 3rd weeks									
                        8) Seasonal events would be held in July(summer event), Oct(Halloween event), Dec(Christmas event), March(March event)									
                        """)


# st.dataframe(mk11_sf)
# st.dataframe(bsf)
# New pages
if options == "Weekly Summary":
    weekly(df_selection)
elif options == "Executive Summary":
    executivesummary(df_selection)
elif options == "Monthly Summary":
    monthlysummary(df_selection)
elif options == "Media Planning":
    mediaPlanning()
elif options == "Overall Trend":
    OverallTrend(df)
elif options == "Approach":
    Approach()
st.markdown("""---""")

st.error("Please Upload the excel file")
