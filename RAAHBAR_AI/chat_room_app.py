import streamlit as st
from modules.memory_manager import MemoryManager
from modules.chat_manager import ChatManager

st.set_page_config(page_title="RAAHBAR AI Chat Room", layout="wide")

st.title("💬 RAAHBAR AI Chat Room")

USERS = ["user1", "user2", "copilot", "raahbar"]

if "memory" not in st.session_state:
    st.session_state.memory = MemoryManager()
if "chat" not in st.session_state:
    st.session_state.chat = ChatManager(st.session_state.memory)
if "history" not in st.session_state:
    st.session_state.history = []
if "current_user" not in st.session_state:
    st.session_state.current_user = USERS[0]

col1, col2 = st.columns([1, 4])

with col1:
    st.header("👤 انتخاب کاربر")
    user = st.selectbox("User", USERS, index=USERS.index(st.session_state.current_user))
    st.session_state.current_user = user
    st.write(f"شما به عنوان: {user}")

with col2:
    st.header("🗨️ گفتگو")
    chat_box = st.empty()
    msg = st.text_input("پیام خود را بنویسید:", key="msg_input")
    if st.button("ارسال پیام") and msg.strip():
        st.session_state.chat.send_message(user, msg)
        st.session_state.history.append((user, msg))
        # پاسخ خودکار راهبر
        if user != "raahbar":
            response = f"[RAAHBAR] پیام شما '{msg}' دریافت شد."
            st.session_state.chat.send_message("raahbar", response)
            st.session_state.history.append(("raahbar", response))
        # پاسخ خودکار copilot
        if user != "copilot":
            copilot_response = f"[Copilot] پیام '{msg}' توسط {user} دریافت شد."
            st.session_state.chat.send_message("copilot", copilot_response)
            st.session_state.history.append(("copilot", copilot_response))
        st.rerun()
    # نمایش تاریخچه
    history = st.session_state.chat.get_history()
    for u, m in history:
        st.markdown(f"**{u}:** {m}")
