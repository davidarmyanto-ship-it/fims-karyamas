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
uploaded_file = 
    key="upload_excel"
)

if uploaded_file is None:
    st.info("Silakan upload file Excel.")
    st.stop()

sheet = st.sidebar.selectbox(
    "Pilih Bulan",
    ["JAN 26","FEB 26","MAR 26","APR 26","MEI 26"]
)

df = pd.read_excel(uploaded_file, sheet_name=sheet)

st.success(f"Berhasil membaca {sheet}")

st.dataframe(df)
    "Upload Excel JAN-MEI",
    type=["xlsx"]
)

if uploaded_file is None:
    st.info("Silakan upload file Excel.")
    st.stop()

sheet = st.sidebar.selectbox(
    "Pilih Bulan",
    ["JAN 26","FEB 26","MAR 26","APR 26","MEI 26"]
)

try:

    df = pd.read_excel(
        uploaded_file,
        sheet_name=sheet
    )

    st.success(f"Sheet {sheet} berhasil dibaca")

    st.write(df.head())

except Exception as e:

    st.error(e)
