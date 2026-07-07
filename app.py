import streamlit as st
import pandas as pd
st.set_page_config(page_title='Karyamas Plantation - FIMS',layout='wide')
if 'login' not in st.session_state: st.session_state.login=False
USERS={'admin':'admin123'}
if not st.session_state.login:
    st.title('Karyamas Plantation')
    st.subheader('Fertilizer Inventory Management System')
    u=st.text_input('Username')
    p=st.text_input('Password',type='password')
    if st.button('Sign In'):
        if USERS.get(u)==p:
            st.session_state.login=True
            st.rerun()
        else:
            st.error('Username / Password salah')
    st.stop()
st.title('Dashboard Stok Pupuk')
st.sidebar.file_uploader('Upload Excel JAN-MEI',type=['xlsx'])
st.info('Template awal.')
