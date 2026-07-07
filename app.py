import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Karyamas Plantation - FIMS",
    layout="wide"
)

# ---------------- LOGIN ----------------
if "login" not in st.session_state:
    st.session_state.login = False

USERS = {
    "admin": "admin123"
}

if not st.session_state.login:

    st.title("Karyamas Plantation")
    st.subheader("Fertilizer Inventory Management System")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Sign In"):

        if USERS.get(username) == password:
            st.session_state.login = True
            st.rerun()
        else:
            st.error("Username / Password salah")

    st.stop()

# ---------------- DASHBOARD ----------------

st.title("Dashboard Stok Pupuk")

uploaded_file = st.sidebar.file_uploader(
    "Upload Excel JAN-MEI",
    type=["xlsx"],
    key="upload_excel"
)

if uploaded_file is None:
    st.info("Silakan upload file Excel.")
    st.stop()

sheet = st.sidebar.selectbox(
    "Pilih Bulan",
    [
        "JAN 26",
        "FEB 26",
        "MAR 26",
        "APR 26",
        "MEI 26"
    ]
)

try:

    df = pd.read_excel(
        uploaded_file,
        sheet_name=sheet
    )

    st.success(f"Berhasil membaca sheet {sheet}")

    st.dataframe(
        df,
        use_container_width=True
    )

except Exception as e:

    st.error(e)
