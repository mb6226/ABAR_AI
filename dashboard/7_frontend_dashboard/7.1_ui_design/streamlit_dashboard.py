import streamlit as st
import requests

st.set_page_config(page_title="ABAR_AI Dashboard", layout="wide")
st.title("داشبورد پیش‌بینی قیمت (LSTM)")

st.sidebar.header("منو")
st.sidebar.markdown("- پیش‌بینی قیمت\n- داده‌ها\n- تست\n- آموزش")

st.markdown("---")
st.header("پیش‌بینی قیمت بعدی با مدل LSTM")

prices_input = st.text_area("۱۰ قیمت آخر را با ویرگول وارد کنید:", "10000,10010,10020,10030,10040,10050,10060,10070,10080,10090")

if st.button("پیش‌بینی کن!"):
    try:
        prices = [float(x) for x in prices_input.split(",") if x.strip()]
        if len(prices) < 10:
            st.error("حداقل ۱۰ مقدار لازم است.")
        else:
            response = requests.post(
                "http://127.0.0.1:8000/predict",
                json={"prices": prices}
            )
            if response.status_code == 200:
                result = response.json()
                st.success(f"قیمت پیش‌بینی شده: {result['predicted_price']}")
            else:
                st.error(f"خطا: {response.text}")
    except Exception as e:
        st.error(f"ورودی نامعتبر یا خطا: {e}")

st.markdown("---")
st.info("این یک نمونه ساده از داشبورد عملی است. برای توسعه بیشتر می‌توانید بخش‌های نمودار و گزارش را اضافه کنید.")
