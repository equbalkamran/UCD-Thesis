# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 11:07:10 2022

@author: Dell
"""

import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objects as go
from PIL import Image
st.set_page_config(layout="wide")
rd = pd.read_csv('thesis_dataset.csv')
#%%
def std_error(data):
  return (np.std(data, ddof=1) / np.sqrt(np.size(data)))
#%%
st.header(" DNI Patient Data Visualisation System by UCD")
st.write("This application shows the data of one individual patient based on the MRN Number given by the user.")
st.subheader(" School of Electronics Engineering, University College Dublin and The Mater Misericordiae University Hospital")
st.warning("Security Warning.")
mrn = st.sidebar.text_input("Enter the MRN no of the patient:", "1")
mrn=int(mrn)
#rd['DOB']=pd.to_datetime(rd['DOB']).apply(lambda x: x.date())
#rd['Surgical date']=pd.to_datetime(rd['Surgical date']).apply(lambda x: x.date())
password=st.sidebar.text_input("Please enter the password :", value="password",type="password")
if password=='MaterUCD':
    
    if mrn in rd['MRN']:
        st.success("MRN has been found")
        n=rd.index[rd['MRN'] == mrn]
        n=n[0]
        dashboard=st.sidebar.checkbox('Dashboard')
        editt=st.sidebar.checkbox('Edit Patient Data')
        imgg=st.sidebar.checkbox('Show Images')
        countt=st.sidebar.checkbox('Show Cohort Counts')
        st.subheader('Patient Details')
        col1, col2 = st.columns(2)
        col1.write('**Name: John/Jane Doe**')
        col2.write('**MRN: '+str(mrn)+'**')
        col1.write(' **Date of Birth: '+str(rd.iloc[n]['DOB'])+str('**'))
        col2.write('**Surgical Date: '+str(rd.iloc[n]['Surgical date'])+str('**'))
        col1.write('**Age at Surgery: '+str(rd.iloc[n]['Age at surgery'])+' years**')
        col2.write('**Target site: '+str(rd.iloc[n]['Target'])+str('**'))
        col1.write('_____________________________________________________________________________________________________')
       
        
        
        
        col2.write("")
        col2.write("")
        col2.write("")
        col2.write("")
        col2.write("")
        col2.write("")
        col2.write("")
        col2.write("")
        col2.write("")
        df=pd.DataFrame(columns=['Baseline','6mon','1year'])
        if dashboard:
            col1.header('*Dashboard*')
            timeline=["Baseline","6 months","1 year"]
            
            w=550
            h=500
            df.loc['PDQ 39']=[rd['PDQ39 pre'].count(),rd['6 mon PDQ39'].count(),rd['1 yr PDQ39'].count()]
            led=[rd.iloc[n]['Lpre-op LED'],rd.iloc[n]['LED @ 6 mon'],rd.iloc[n]['LED @ 1 yr']]
            avgled=[rd['Lpre-op LED'].mean(),rd['LED @ 6 mon'].mean(),rd['LED @ 1 yr'].mean()]
            stdled=[std_error(rd['Lpre-op LED']),std_error(rd['LED @ 6 mon']),std_error(rd['LED @ 1 yr'])]
            fig=go.Figure()
            fig.add_trace(go.Scatter(x=timeline,y=led,mode='lines+markers',name='Patient Score'))
            fig.add_trace(go.Scatter(x=timeline,y=avgled,mode='lines+markers',line={'dash': 'dash', 'color': 'grey'},
                                     name='Average Score',error_y=dict(type='data',array=stdled,visible=True)))
            fig.update_layout(title="LED Results",xaxis_title="TimeFrame",yaxis_title="Score",width=w,height=h)
            col2.plotly_chart(fig)
            df.loc['LED']=[rd['Lpre-op LED'].count(),rd['LED @ 6 mon'].count(),rd['LED @ 1 yr'].count()]
    
            pdq=[rd.iloc[n]['PDQ39 pre'],rd.iloc[n]['6 mon PDQ39'],rd.iloc[n]['1 yr PDQ39']]
            avgpdq=[rd['PDQ39 pre'].mean(),rd['6 mon PDQ39'].mean(),rd['1 yr PDQ39'].mean()]
            stdpdq=[std_error(rd['PDQ39 pre']),std_error(rd['6 mon PDQ39']),std_error(rd['1 yr PDQ39'])]
            fig=go.Figure()
            fig.add_trace(go.Scatter(x=timeline,y=pdq,mode='lines+markers',name='Patient Score'))
            fig.add_trace(go.Scatter(x=timeline,y=avgpdq,mode='lines+markers',line={'dash': 'dash', 'color': 'grey'},
                                     name='Average Score',error_y=dict(type='data',array=stdpdq,visible=True)))
            fig.update_layout(title="PDQ 39 Results",xaxis_title="TimeFrame",yaxis_title="Score",width=w,height=h)
            col1.plotly_chart(fig)
            
    
            minibest=[rd.iloc[n]['MiniBest'],rd.iloc[n]['MiniBest @6mon'],rd.iloc[n]['MiniBest @1yr']]
            avgminibest=[rd['MiniBest'].mean(),rd['MiniBest @6mon'].mean(),rd['MiniBest @1yr'].mean()]
            stdminibest=[std_error(rd['MiniBest']),std_error(rd['MiniBest @6mon']),std_error(rd['MiniBest @1yr'])]
            fig=go.Figure()
            fig.add_trace(go.Scatter(x=timeline,y=minibest,mode='lines+markers',name='Patient Score'))
            fig.add_trace(go.Scatter(x=timeline,y=avgminibest,mode='lines+markers',line={'dash': 'dash', 'color': 'grey'},
                                     name='Average Score',error_y=dict(type='data',array=stdminibest,visible=True)))
            fig.update_layout(title="Minibest Results",xaxis_title="TimeFrame",yaxis_title="Score",width=w,height=h)
            col2.plotly_chart(fig)
            df.loc['MiniBest']=[rd['MiniBest'].count(),rd['MiniBest @6mon'].count(),rd['MiniBest @1yr'].count()]
    
            off_offscore=[rd.iloc[n]['6 mon OFF/OFF'],rd.iloc[n]['1 yr OFF/OFF']]
            avgoff_offscore=[rd['6 mon OFF/OFF'].mean(),rd['1 yr OFF/OFF'].mean()]
            stdoff_offscore=[std_error(rd['6 mon OFF/OFF']),std_error(rd['1 yr OFF/OFF'])]
            on_offmedscore=[rd.iloc[n]['6 mon OFFm/Ons'],rd.iloc[n]['1 yr on OFFm/Ons']]
            avgon_offmedscore=[rd['6 mon OFFm/Ons'].mean(),rd['1 yr on OFFm/Ons'].mean()]
            stdon_offmedscore=[std_error(rd['6 mon OFFm/Ons']),std_error(rd['1 yr on OFFm/Ons'])]
            score= [100*(i-j)/i for i, j in zip(off_offscore, on_offmedscore)]
            avgscore= [100*(i-j)/i for i, j in zip(avgoff_offscore, avgon_offmedscore)]
            stdscore= [100*(i-j)/i for i, j in zip(stdoff_offscore, stdon_offmedscore)]
            fig=go.Figure()
            fig.add_trace(go.Scatter(x=["6 months","1 year"],y=score,mode='lines+markers',name='Patient Score'))
            fig.add_trace(go.Scatter(x=["6 months","1 year"],y=avgscore,mode='lines+markers',line={'dash': 'dash', 'color': 'grey'},
                                     name='Average Score',error_y=dict(type='data',array=stdscore,visible=True)))
            fig.update_layout(title="Stim Only Response",xaxis_title="TimeFrame",yaxis_title="Score",width=w,height=h)
            col1.plotly_chart(fig)
            
    
            moca=[rd.iloc[n]['MOCA'],rd.iloc[n]['MOCA @ 6mon'],rd.iloc[n]['MOCA @1yr']]
            avgmoca=[rd['MOCA'].mean(),rd['MOCA @ 6mon'].mean(),rd['MOCA @1yr'].mean()]
            stdmoca=[std_error(rd['MOCA']),std_error(rd['MOCA @ 6mon']),std_error(rd['MOCA @1yr'])]
            fig=go.Figure()
            fig.add_trace(go.Scatter(x=timeline,y=moca,mode='lines+markers',name='Patient Score'))
            fig.add_trace(go.Scatter(x=timeline,y=avgmoca,mode='lines+markers',line={'dash': 'dash', 'color': 'grey'},
                                     name='Average Score',error_y=dict(type='data',array=stdmoca,visible=True)))
            fig.update_layout(title="MOCA Results",xaxis_title="TimeFrame",yaxis_title="Score",width=w,height=h)
            col2.plotly_chart(fig)
            df.loc['MOCA']=[rd['MOCA'].count(),rd['MOCA @ 6mon'].count(),rd['MOCA @1yr'].count()]
    
            offoff=[rd.iloc[n]['UPDRS III OFF'],rd.iloc[n]['6 mon OFF/OFF'],rd.iloc[n]['1 yr OFF/OFF']]
            avgoffoff=[rd['UPDRS III OFF'].mean(),rd['6 mon OFF/OFF'].mean(),rd['1 yr OFF/OFF'].mean()]
            stdoffoff=[std_error(rd['UPDRS III OFF']),std_error(rd['6 mon OFF/OFF']),std_error(rd['1 yr OFF/OFF'])]
            fig=go.Figure()
            fig.add_trace(go.Scatter(x=timeline,y=offoff,mode='lines+markers',name='Patient Score'))
            fig.add_trace(go.Scatter(x=timeline,y=avgoffoff,mode='lines+markers',line={'dash': 'dash', 'color': 'grey'},
                                     name='Average Score',error_y=dict(type='data',array=stdoffoff,visible=True)))
            fig.update_layout(title="UPDRS III OFF/OFF Results",xaxis_title="TimeFrame",yaxis_title="Score",width=w,height=h)
            col1.plotly_chart(fig)
            
    
    
            rd['AIDS %'] = rd['AIDS %'].apply(pd.to_numeric, args=('coerce',))
            rd['AIDS % @ 6mon'] = rd['AIDS % @ 6mon'].apply(pd.to_numeric, args=('coerce',))
            rd['AIDS % @1yr'] = rd['AIDS % @1yr'].apply(pd.to_numeric, args=('coerce',))
            aids=[rd.iloc[n]['AIDS %'],rd.iloc[n]['AIDS % @ 6mon'],rd.iloc[n]['AIDS % @1yr']]
            avgaids=[rd['AIDS %'].mean(),rd['AIDS % @ 6mon'].mean(),rd['AIDS % @1yr'].mean()]
            stdaids=[std_error(rd['AIDS %']),std_error(rd['AIDS % @ 6mon']),std_error(rd['AIDS % @1yr'])]
            fig=go.Figure()
            fig.add_trace(go.Scatter(x=timeline,y=aids,mode='lines+markers',name='Patient Score'))
            fig.add_trace(go.Scatter(x=timeline,y=avgaids,mode='lines+markers',line={'dash': 'dash', 'color': 'grey'},
                                     name='Average Score',error_y=dict(type='data',array=stdaids,visible=True)))
            fig.update_layout(title="AIDS Results",xaxis_title="TimeFrame",yaxis_title="Score",width=w,height=h)
            col2.plotly_chart(fig)
            df.loc['AIDS']=[rd['AIDS %'].count(),rd['AIDS % @ 6mon'].count(),rd['AIDS % @1yr'].count()]
            
            
            updrs1=[rd.iloc[n]['UPDRS I'],rd.iloc[n]['UPDRS I 6mon'],rd.iloc[n]['UPDRS I @ 1yr']]
            avgupdrs1=[rd['UPDRS I'].mean(),rd['UPDRS I 6mon'].mean(),rd['UPDRS I @ 1yr'].mean()]
            stdupdrs1=[std_error(rd['UPDRS I']),std_error(rd['UPDRS I 6mon']),std_error(rd['UPDRS I @ 1yr'])]
            updrs2=[rd.iloc[n]['UPDRS II'],rd.iloc[n]['UPDRS II6mon'],rd.iloc[n]['UPDRS II @1yr']]
            avgupdrs2=[rd['UPDRS II'].mean(),rd['UPDRS II6mon'].mean(),rd['UPDRS II @1yr'].mean()]
            stdupdrs2=[std_error(rd['UPDRS II']),std_error(rd['UPDRS II6mon']),std_error(rd['UPDRS II @1yr'])]
            updrs_off_off=[rd.iloc[n]['UPDRS III OFF'],rd.iloc[n]['6 mon OFF/OFF'],rd.iloc[n]['1 yr OFF/OFF']]
            avg_off_off=[rd['UPDRS III OFF'].mean(),rd['6 mon OFF/OFF'].mean(),rd['1 yr OFF/OFF'].mean()]
            std_off_off=[std_error(rd['UPDRS III OFF']),std_error(rd['6 mon OFF/OFF']),std_error(rd['1 yr OFF/OFF'])]
            updrs_on_on=[rd.iloc[n]['UPDRS III ON'],rd.iloc[n]['6 mon  ON/ON'],rd.iloc[n]['1 yr  ON/ON']]
            avg_on_on=[rd['UPDRS III ON'].mean(),rd['6 mon  ON/ON'].mean(),rd['1 yr  ON/ON'].mean()]
            std_on_on=[std_error(rd['UPDRS III ON']),std_error(rd['6 mon  ON/ON']),std_error(rd['1 yr  ON/ON'])]
            
            df.loc['UPDRS I']=[rd['UPDRS I'].count(),rd['UPDRS I 6mon'].count(),rd['UPDRS I @ 1yr'].count()]
            df.loc['UPDRS II']=[rd['UPDRS II'].count(),rd['UPDRS II6mon'].count(),rd['UPDRS II @1yr'].count()]
            df.loc['UPDRS OFF']=[rd['UPDRS III OFF'].count(),rd['6 mon OFF/OFF'].count(),rd['1 yr OFF/OFF'].count()]
            df.loc['UPDRS ON']=[rd['UPDRS III ON'].count(),rd['6 mon  ON/ON'].count(),rd['1 yr  ON/ON'].count()]
            
            fig=go.Figure()
            
            fig.add_trace(go.Scatter(x=timeline,y=updrs1,mode='lines+markers',name='UPDRS I'))
            fig.add_trace(go.Scatter(x=timeline,y=updrs2,mode='lines+markers',name='UPDRS II'))
            fig.add_trace(go.Scatter(x=timeline,y=updrs_off_off,mode='lines+markers',name='UPDRS III OFF'))
            fig.add_trace(go.Scatter(x=timeline,y=updrs_on_on,mode='lines+markers',name='UPDRS III ON'))
            fig.update_layout(title="UPDRS Scores",xaxis_title="Timeframe",yaxis_title="Score",width=w,height=h)
            
            fig.add_trace(go.Scatter(x=timeline,y=avgupdrs1,mode='lines+markers',line={'dash': 'dash', 'color': 'blue'},
                                     name='Average UPDRS I',error_y=dict(type='data',array=stdupdrs1,visible=True)))
            fig.add_trace(go.Scatter(x=timeline,y=avgupdrs2,mode='lines+markers',line={'dash': 'dash', 'color': 'red'},
                                     name='Average UPDRS II',error_y=dict(type='data',array=stdupdrs2,visible=True)))
            fig.add_trace(go.Scatter(x=timeline,y=avg_off_off,mode='lines+markers',line={'dash': 'dash', 'color': 'green'},
                                     name='Average UPDRS III OFF',error_y=dict(type='data',array=std_off_off,visible=True)))
            fig.add_trace(go.Scatter(x=timeline,y=avg_on_on,mode='lines+markers',line={'dash': 'dash', 'color': 'violet'},
                                     name='Average UPDRS III ON',error_y=dict(type='data',array=std_on_on,visible=True)))
            col1.plotly_chart(fig)
            col1.warning('Some of the AIDS Scores were not available. ')
            col2.warning('They have been converted to 0. ')
            
            st.write('_____________________________________________________________________________________________________________________________')
        if imgg:
            img1 = Image.open('img1.png')
            img2=Image.open('img2.png')
            col1.image(img1,caption='Shared Image 1')
            col2.image(img2,caption='Shared Image 2')
            st.write('_____________________________________________________________________________________________________________________________')
        if countt:
            st.sidebar.table(df)
        if editt:
            st.header('Modification of existing patient data')
            st.warning('If permission error occurs, please ensure the excel file is not open in your system')
            rd.replace('Not available',np.nan,inplace=True)
            edit_timeframe=st.selectbox(
                label='Select the timeframe of data to be edited',
                options=('post surgery','6 mon','1 year'))
            modification_form=st.form('Modification of exisiting patient data')
            if edit_timeframe=='post surgery':
                edit_param=modification_form.selectbox('Select the parameter to edit',rd.columns[6:30])
            elif edit_timeframe=='6 mon':
                edit_param=modification_form.selectbox('Select the parameter to edit',rd.columns[39:39+24])
            else:
                edit_param=modification_form.selectbox('Select the parameter to edit',rd.columns[67:67+24])
            new_param=modification_form.number_input(
                label='Enter the new value for '+edit_param,
                value=rd.iloc[n][edit_param])
            rd.at[n,edit_param]=new_param
            save_data=modification_form.form_submit_button()
            if save_data:
                rd.to_csv('thesis_dataset.csv',index=False)
                st.experimental_rerun()
            st.write('_____________________________________________________________________________________________________________________________')
    else:
        st.error('Sorry! Wrong Password. Please Try Again')
