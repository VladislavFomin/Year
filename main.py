import streamlit as st
from PIL import Image
import os

# Настройка страницы
st.set_page_config(
    page_title="Наша история любви",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed"
)
# e67edd, #eb9de4

# CSS для стилизации
st.markdown("""
    <style>
    /* Скрыть весь хедер */
    header {
        visibility: hidden !important;
        height: 0 !important;
    }
    
    /* Основные стили */
    .main {
        padding: 0;
    }
    /* Стили для хедера */
    .custom-header {
        background: linear-gradient(180deg, #F8B4C8, #E8A0BF);
        padding: 30px 0;
        margin: -20px -20px 30px -20px; /* Растягиваем на всю ширину */
        text-align: center;
        box-shadow: 0 4px 15px rgba(255, 105, 180, 0.3);
        border-bottom: 3px solid #D4839E;
    }

    .custom-header h1 {
        color: #f0e9ef;
        font-size: 3em;
        font-family: 'Georgia', serif;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        #text-shadow: 1px 1px 3px rgba(255,255,255,0.3);
        letter-spacing: 2px;
    }

    .custom-header p {
        color: #FFE4E9;
        font-size: 1.2em;
        margin: 5px 0 0 0;
        font-family: 'Georgia', serif;
    }

    /* Убираем отступы у страницы */
    .main > div {
        padding-top: 0 !important;
    }
    /* Заголовок */
    .main-title {
        text-align: center;
        font-size: 3em;
        color: black;
        font-weight: bold;
        margin-bottom: 30px;
        font-family: 'Georgia', serif;
    }

    /* Блоки с розовой рамкой */
    .block-container {
        padding: 20px;
        margin: 10px;
        background-color: #FFF8FA;
        box-shadow: 0 4px 8px rgba(255, 105, 180, 0.2);
        transition: transform 0.3s ease;
        text-align: center;
    }

    .block-container:hover {
        transform: scale(1.02);
    }

    /* Описание над рамкой */
    .block-title {
        text-align: center;
        font-size: 1.5em;
        color: #7A4B5E;
        font-weight: bold;
        margin-bottom: 15px;
        font-family: 'Georgia', serif;
        position: relative;
        padding-bottom: 10px;
    }
    
    .block-title:after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 60px;
        height: 3px;
        background: linear-gradient(90deg, #F8B4C8, #E8A0BF);
        border-radius: 2px;
    }

    /* Контейнер для фото */
    .photo-container {
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: #FFE4E9;
        border-radius: 10px;
        min-height: 200px;
        margin-bottom: 15px;
    }
    
    /* Центрирование и стили для всех кнопок */
div.stButton {
    display: flex !important;
    justify-content: center !important;
    width: 100% !important;
}

div.stButton > button {
    background: linear-gradient(135deg, #E8A0BF, #D4839E) !important;
    color: white !important;
    font-weight: bold !important;
    border: none !important;
    border-radius: 25px !important;
    padding: 10px 30px !important;
    min-width: 200px !important;
    width: auto !important;
    transition: all 0.3s ease !important;
    cursor: pointer !important;
}

div.stButton > button:hover {
    transform: scale(1.05) !important;
    box-shadow: 0 4px 15px rgba(212, 131, 158, 0.4) !important;
}

/* Кнопка внизу страницы (отдельная, большего размера) */
.bottom-button {
    text-align: center;
    margin-top: 40px;
    margin-bottom: 30px;
}

.bottom-button div.stButton > button {
    padding: 15px 50px !important;
    font-size: 1.2em !important;
    min-width: 250px !important;
}
    
    /* Отступы для блоков */
    .row-blocks {
        margin-bottom: 30px;
    }

    /* Центрирование 4-го блока */
    .center-block {
        display: flex;
        justify-content: center;
    }

    .center-block .block-container {
        max-width: 400px;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# Хедер сайта
st.markdown("""
    <div class="custom-header">
        <h1>❤️ Наша история любви ❤️</h1>
        <p>365 дней счастья</p>
    </div>
""", unsafe_allow_html=True)

# Разделение на колонки для первых 3 блоков
col1, col2, col3 = st.columns(3)

# Блок 1
with col1:
    st.markdown('<p class="block-title">Как все начиналось</p>', unsafe_allow_html=True)
    with st.container():
        # Место для фото
        st.image("images/page_one/photo_8_2026-07-07_22-32-32.jpg", use_container_width=True)
        # Кнопка
        if st.button("Любовь", key="btn1", use_container_width=True):
            st.switch_page("pages/page1.py")
    st.markdown('</div>', unsafe_allow_html=True)

# Блок 2
with col2:
    st.markdown('<p class="block-title">Общажные вайбы</p>', unsafe_allow_html=True)
    with st.container():
        # Место для фото
        st.image("images/page_two/photo_9_2026-07-07_22-33-39.jpg", use_container_width=True)
        # Кнопка
        if st.button("Любовь", key="btn2", use_container_width=True):
            st.switch_page("pages/page2.py")
        st.markdown('</div>', unsafe_allow_html=True)

# Блок 3
with col3:
    st.markdown('<p class="block-title">Дом там где ты</p>', unsafe_allow_html=True)
    with st.container():
        # Место для фото
        st.image("images/page_three/photo_43_2026-07-07_22-35-23.jpg", use_container_width=True)
        # Кнопка
        if st.button("Любовь", key="btn3", use_container_width=True):
            st.switch_page("pages/page3.py")
        st.markdown('</div>', unsafe_allow_html=True)

# 4-й блок - по центру
st.markdown('<p class="block-title" style="margin-top: 20px;">Особенные моменты</p>', unsafe_allow_html=True)
st.markdown('<div class="center-block">', unsafe_allow_html=True)
with st.container():
    # Место для фото
    st.image("images/page_three/photo_32_2026-07-07_22-35-23.jpg", use_container_width=True)
    # Кнопка
    if st.button("Любовь", key="btn4", use_container_width=True):
        st.switch_page("pages/page4.py")
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Отдельная кнопка внизу
st.markdown('<div class="bottom-button">', unsafe_allow_html=True)
if st.button("💌 Особое послание", key="bottom_btn"):
    st.switch_page("pages/page5.py")
st.markdown('</div>', unsafe_allow_html=True)

st.balloons()