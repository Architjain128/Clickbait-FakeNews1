import streamlit as st
import pandas as pd
import numpy as np
import pickle
import joblib

# model_predicting_cb=None
# model_predicting_fakness_w=None
# model_predicting_fakness_wo=None

def load_model(file):
    return joblib.load(file)

@st.cache
def models():
    global model_predicting_cb
    global model_predicting_fakness_w
    global model_predicting_fakness_wo
    model_predicting_cb=load_model("../clickbait/stkwxgbr300_20k_0.03390061132923085.pkl")
    model_predicting_fakness_w=load_model("../fakenews/lr300_44k_w.pkl")
    model_predicting_fakness_wo=load_model("../fakenews/lr300_44k_wo.pkl")

def no_page():
    st.error("### Oops! Error loading models")

def explore_page():
    st.write("""
            # Explore page
            ## Model Explanation
            Random data
            ## Report
            Random data
            ## Dataset Used
            Random data
    """)

def show_prediction_page():
    st.write("## User Inputs")
    title= st.text_input("Input your article's title here: ")
    text= st.text_area("Input your article's text here: ")
    run = st.button("Predict")
    if run:
        title=title.strip()
        text=text.strip()
        st.write('## Predictions')
        val1=False
        val2=False
        if title and text:
            
            a=[1.62315589,-0.21419005,-0.18933802,0.94358362,0.76692209,1.25057842
,0.76343049,-0.59837671,0.06850355,-0.23938363,0.86735141,0.12270347
,-0.8690553,-0.6668661,1.77945807,0.04781884,0.00463446,0.07138224
,0.42559705,-1.19420127,-0.65631063,-0.92380461,-1.33903449,-1.32577622
,-0.45885412,0.8335707,1.12825951,0.81772734,-0.36010959,0.74410593
,-0.45862512,0.00723896,0.26071703,0.49215683,0.25508232,-1.82924775
,-0.88984028,0.97064041,0.17224416,-0.69758148,-1.02683924,0.32391759
,-0.04542423,-0.6402912,1.76766735,-0.02559988,-0.67093501,-1.5837954
,-1.19182555,-0.13742073,-0.5694766,1.58880062,0.63715493,0.09100472
,0.78834539,1.07093329,1.1029774,-0.09917982,1.90974157,0.33725387
,-0.19762127,-1.49845978,1.54296857,0.31210803,-0.23608811,0.94084999
,0.06015424,-0.25219065,0.45296727,0.29225877,-0.61481224,-1.64691593
,-1.28283783,1.94372894,-1.10339876,0.43288246,-0.5899659,-0.56372822
,-2.72491803,-0.86701875,0.04616808,0.16401762,1.54377607,0.53693517
,0.42064212,0.55880056,-0.63942602,-0.0178306,-0.86091956,0.34778789
,-1.73054293,1.4324032,1.31721547,0.88735456,1.89059579,-0.1772891
,-0.2173015,-0.45018157,-0.44509028,-0.16639943,0.06770733,1.1772588
,-1.39621901,-0.98636876,-1.05091785,0.96623841,-0.12324381,0.11361667
,0.5140284,-0.51129956,-0.74146262,-0.22191284,1.50055566,1.31428851
,-1.79556962,0.41622911,-0.77395779,-1.50607246,0.01264079,-0.06034453
,-0.16598678,-0.45855385,-2.73920099,1.56925357,0.49172873,1.56274674
,-0.91062881,-0.59052094,-1.06672064,-0.61881732,-0.575119,-0.89494313
,-2.2050111,0.61014343,-0.74116983,0.48497453,-1.28132485,0.64515627
,-1.12927553,-0.03993792,-0.98545828,0.57326723,-0.45376023,-0.72531144
,0.06438864,-0.3241475,0.26247647,-0.77660309,0.51060457,0.62630683
,1.04779038,0.60352645,0.58115033,1.01786776,-0.32799109,0.64423597
,-0.37117066,-0.5740827,0.70290475,-0.52803841,-0.16432115,-0.72432615
,0.92287839,-0.07943492,1.05440183,-1.10199601,-0.26589363,0.83415799
,0.76174786,-1.26149259,-0.71313113,0.90174149,-0.32524968,-0.84781572
,-1.34712616,0.12579317,2.36115371,0.71044055,-2.24412563,-0.29133158
,-0.45820532,-0.68077007,1.92617915,-1.0395339,-1.80356282,0.94286123
,-0.25771149,1.07345057,-0.03771827,-0.61807116,-2.74293682,1.32020206
,0.31193135,-0.70430367,-0.47503922,-0.26878851,-1.33827667,-0.23201189
,-0.93389301,0.53240215,0.1421402,1.15116863,-0.95357388,-1.14556289
,0.18949668,-0.15121837,0.34372547,-1.0310975,-1.68064715,0.05116517
,-1.29005541,0.63338022,-0.16242286,-1.58539526,0.67064729,1.59122898
,1.72559189,2.74945787,0.293009,0.63670127,0.59607052,0.3222102
,0.15821899,1.76997722,1.38757141,-0.02022422,-0.49003955,0.49846037
,2.04139333,0.56631461,-1.34241535,1.12594239,0.46366717,0.45292994
,-0.30322558,-1.73528488,-2.16088468,0.74318095,0.78378931,-0.27292575
,-0.17883573,1.30192653,-0.55534671,0.81999268,-0.05996466,0.52437281
,-0.09750153,0.31300697,-0.10891697,-0.27858463,0.26213474,-0.53598963
,-0.20683946,1.40985139,0.59723043,-0.17386284,0.97770304,0.59264902
,-0.8579551,0.63768111,-1.41784114,2.10799061,0.93439128,0.30146023
,1.31511966,0.30401149,-0.02475375,-0.03033941,-0.56210118,0.6453622
,-0.6583538,0.15624084,-0.33758842,-1.29774887,-0.12492184,-0.53807247
,2.17478722,-0.47957131,0.76787483,0.24210658,0.6166398,1.65284917
,1.18275903,1.13630666,-1.58955007,0.52901289,-0.01007092,0.43853659
,-0.37930201,-0.85786294,0.40845912,-0.28854326,-0.32507199,1.0968834
,-0.49449959,0.90435752,-0.08601171,1.14283232,0.96380777,-0.36289566]

            aaa=model_predicting_cb.predict(np.array(a).reshape(1,-1))
            st.write(""" Clickbait Score""",aaa[0]*100)
        
            if val1:
                st.write("This is a Real news considering Clickbait score")
            else:
                st.write("This is a Fake news considering Clickbait score")

            if val2:
                st.write("This is a Real news without considering Clickbait score")
            else:
                st.write("This is a Fake news without considering Clickbait score")
        else:
            st.error("Empty input fields")



# models()
model_predicting_cb=load_model("../clickbait/stkwxgbr300_20k_0.03390061132923085.pkl")
model_predicting_fakness_w=load_model("../fakenews/lr300_44k_w.pkl")
model_predicting_fakness_wo=load_model("../fakenews/lr300_44k_wo.pkl")
st.sidebar.header('Navigation')
page = st.sidebar.selectbox("Select the page you want to see", ["Predict","Explore" ])
# if model_predicting_fakness_wo==None or model_predicting_fakness_w==None or model_predicting_cb==None:
#     page="error"
st.title("ClickBait and Fakeness Detector")
st.write("This app detects whether clickbait score of text helps us in predicating its fakeness.")
if page == "Explore":
    explore_page()
elif page == "Predict":
    show_prediction_page()
else:
    no_page()