import streamlit as st
from PIL import Image
import os
import base64
from io import BytesIO

# Настройка страницы
st.set_page_config(
    page_title="Общажные вайбики",
    page_icon="❤️",
    layout="wide"
)

# CSS для страницы
st.markdown("""
    <style>
    /* Скрыть верхний хедер с Deploy и меню */
        header {
            display: none !important;
        }

        /* Скрыть сайдбар */
        .css-1d391kg {
            display: none !important;
        }

        /* Скрыть footer */
        footer {
            display: none !important;
        }

        /* Скрыть кнопку Deploy */
        .stAppDeployButton {
            display: none !important;
        }

        /* Скрыть меню гамбургер */
        .st-emotion-cache-1avcm0n {
            display: none !important;
        }

        /* Скрыть всё что связано с deploy */
        [data-testid="stAppDeployButton"] {
            display: none !important;
        }

        /* Скрыть верхнюю панель навигации */
        .st-emotion-cache-18ni7ap {
            display: none !important;
        }

        /* Скрыть меню навигации */
        .st-emotion-cache-1v0mbdj {
            display: none !important;
        }

        /* Убрать пустое место сверху (основное) */
        .main > div {
            padding-top: 0rem !important;
        }

        /* Убрать отступ у основного блока */
        .st-emotion-cache-1r6slb0 {
            padding-top: 0rem !important;
        }

        /* Убрать все отступы сверху */
        .block-container {
            padding-top: 0rem !important;
        }

        /* Убрать верхний отступ у всего приложения */
        .stApp {
            margin-top: 0px !important;
        }

        /* Установить белый фон */
        .stApp {
            background-color: white !important;
        }

        .main {
            background-color: white !important;
        }

        .st-emotion-cache-1r6slb0 {
            background-color: white !important;
        }

    /* Хедер */
    .custom-header {
        background: linear-gradient(135deg, #F8B4C8, #E8A0BF);
        padding: 20px 0;
        margin: -20px -20px 30px -20px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(232, 160, 191, 0.2);
        border-bottom: 3px solid #D4839E;
    }

    .custom-header h1 {
        color: #5C2E3E;
        font-size: 2.5em;
        font-family: 'Georgia', serif;
        margin: 0;
        text-shadow: 1px 1px 3px rgba(255,255,255,0.3);
        letter-spacing: 2px;
    }

    /* Меню */
    .menu {
        background: white;
        padding: 15px 30px;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        margin-bottom: 30px;
        display: flex;
        gap: 20px;
        flex-wrap: wrap;
        justify-content: center;
    }

    .menu a {
        color: #7A4B5E;
        text-decoration: none;
        font-size: 1.1em;
        font-weight: 500;
        padding: 8px 20px;
        border-radius: 20px;
        transition: all 0.3s ease;
    }

    .menu a:hover {
        background: #F8B4C8;
        color: white;
    }

    /* Контейнер для слайдера */
    .slider-container {
        max-width: 800px;
        margin: 0 auto;
        background: white;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }

    .slider-text {
        text-align: center;
        font-size: 1.2em;
        color: #5C2E3E;
        padding: 20px;
        background: #FFF8FA;
        border-radius: 10px;
        margin-top: 20px;
        min-height: 80px;
        font-family: 'Georgia', serif;
        line-height: 1.6;
    }

    /* Кнопки навигации */
    .nav-buttons {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: 20px;
    }

    .stButton > button {
        background: linear-gradient(135deg, #E8A0BF, #D4839E) !important;
        color: white !important;
        font-weight: bold !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 10px 30px !important;
        transition: all 0.3s ease !important;
    }

    .stButton > button:hover {
        transform: scale(1.05) !important;
        box-shadow: 0 4px 15px rgba(212, 131, 158, 0.4) !important;
    }

    /* Счетчик фото */
    .counter {
        text-align: center;
        color: #B88A9A;
        font-size: 0.9em;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Меню
st.markdown("""
    <div class="menu">
        <a href="/" target="_self">🏠 Главная</a>
        <a href="/page1" target="_self">📸 Как все начиналось</a>
        <a href="/page2" target="_self">🎉 Общажные вайбики</a>
        <a href="/page3" target="_self">💕 Дом там где ты</a>
        <a href="/page4" target="_self">💝 Особенные моменты</a>
        <a href="/page5" target="_self">💌 Особое послание</a>
    </div>
""", unsafe_allow_html=True)

# Заголовок
st.markdown("""
    <div class="custom-header">
        <h1>Общажные вайбики</h1>
    </div>
""", unsafe_allow_html=True)

# Данные для слайдера (ЗАМЕНИ НА СВОИ)
photos = [
    {"image": "images/page_two/photo_5_2026-07-07_22-33-39.jpg", "text": "После Тагила началась общажная эра. Не менее теплое и значимое время. После Тагила и всех его пройденных парках, мы приезаем в Екатеринбург. Гуляя по нему, мы все также плюс вайбим, шутим, смеемся, одним словом кайфуем<br>В день фотографии, мы попали под ливень в центре, насковзь промокли и замерзли, но сейчас вспоминая это, я чувствую только тепло"},
    {"image": "images/page_two/photo_6_2026-07-07_22-33-39.jpg", "text": "После Тагила началась общажная эра. Не менее теплое и значимое время. После Тагила и всех его пройденных парках, мы приезаем в Екатеринбург. Гуляя по нему, мы все также плюс вайбим, шутим, смеемся, одним словом кайфуем<br>В день фотографии, мы попали под ливень в центре, насковзь промокли и замерзли, но сейчас вспоминая это, я чувствую только тепло"},
    {"image": "images/page_two/photo_4_2026-07-07_22-33-39.jpg", "text": "После просмотра пузатая в 16<br>АХАХХА что за фотка<br>Дни, вечера и ночи проведенные вместе в моей/твоей комнаты общаге - легенды. Мы открыли для себя шоу мама в 16, изначально захейтив его, а сейчас нам только новые выпуски да подавай. Кушали твою вкусную еду, сочнейшие бургеры и оооооочень вкусная картошка отдельный вид исскуства"},
    {"image": "images/page_two/photo_7_2026-07-07_22-33-39.jpg", "text": "ЛЕЕЕЕСГОУ<br>Проба машинки и стабильно лысый Владос"},
    {"image": "images/page_two/photo_9_2026-07-07_22-33-39.jpg", "text": "ТУПА МЫ<br>К сожалению я нашел не так много фоток с того времени. Оно и понятно на самом деле, мы редко гуляли и виделись. Зачастую мы гуляли по вечерам по вторчику, рядом с общагой. Но дни проведенные именно в общаге с тобой, отдельно ценны, т.к на фоне того что мы мало видились, я очень скучал, хоть и находясь так близко друг к другу. И именно дни, когда у нас получалось встретиться в комнате общаги особенно телпые и сильные<br>Я очень люблю тебя Кристаллик! Общажный этап был по своему крут и ценен для нас! "}
]

# Инициализация индекса
if "slide_index" not in st.session_state:
    st.session_state.slide_index = 0


# Функция для отображения слайда
def display_slide(index):
    if 0 <= index < len(photos):
        if os.path.exists(photos[index]["image"]):
            image = Image.open(photos[index]["image"])
            buffered = BytesIO()
            fmt = "PNG" if photos[index]["image"].lower().endswith(".png") else "JPEG"
            image.save(buffered, format=fmt)
            img_str = base64.b64encode(buffered.getvalue()).decode()
            mime = "image/png" if fmt == "PNG" else "image/jpeg"
            st.markdown(
                f'''
                <div style="display: flex; justify-content: center; align-items: center; 
                            width: 100%; padding: 10px 0; max-height: 60vh;">
                    <img src="data:{mime};base64,{img_str}" 
                         style="max-width: 100%; 
                                max-height: 55vh; 
                                width: auto; 
                                height: auto; 
                                object-fit: contain; 
                                border-radius: 10px; 
                                display: block;
                                box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                </div>
                ''',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f'<div style="text-align: center; padding: 100px 20px; background: #FFF8FA; border-radius: 10px; color: #B88A9A;">🖼️ [ФОТО {index + 1} НЕ НАЙДЕНО]</div>',
                unsafe_allow_html=True)


# Отображение текущего слайда
display_slide(st.session_state.slide_index)

# Кнопки навигации
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    if st.button("⬅️ Назад", key="prev1", use_container_width=True):
        if st.session_state.slide_index > 0:
            st.session_state.slide_index -= 1
            st.rerun()

with col3:
    if st.button("Вперед ➡️", key="next1", use_container_width=True):
        if st.session_state.slide_index < len(photos) - 1:
            st.session_state.slide_index += 1
            st.rerun()

st.markdown(f'<div class="slider-text">💕 {photos[st.session_state.slide_index]["text"]}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="counter">{st.session_state.slide_index + 1} / {len(photos)}</div>', unsafe_allow_html=True)