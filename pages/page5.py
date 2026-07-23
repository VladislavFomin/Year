import streamlit as st
from PIL import Image
import os
import base64
from io import BytesIO

st.set_page_config(
    page_title="Особое послание",
    page_icon="💌",
    layout="wide"
)

# Скрыть хедер
st.markdown("""
    <style>
        header {display: none !important;}
        .stAppDeployButton {display: none !important;}
        .st-emotion-cache-1avcm0n {display: none !important;}
        [data-testid="stAppDeployButton"] {display: none !important;}
        .st-emotion-cache-18ni7ap {display: none !important;}
        .st-emotion-cache-1v0mbdj {display: none !important;}
        footer {display: none !important;}
        .main > div {padding-top: 0rem !important;}
        .st-emotion-cache-1r6slb0 {padding-top: 0rem !important;}
        .block-container {padding-top: 0rem !important;}
        .stApp {margin-top: 0px !important; background-color: #FFF8FA !important;}
        .main {background-color: #FFF8FA !important;}

        /* Контейнер */
        .envelope-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
            min-height: auto;
            padding-top: 20px;
            text-align: center;
        }

        /* Убираем все стандартные стили кнопок */
        div.stButton {
            display: flex !important;
            justify-content: center !important;
            width: 100% !important;
        }

        div.stButton > button {
            border: none !important;
            padding: 0 !important;
            box-shadow: none !important;
            width: 500px !important;
            height: 400px !important;
            min-width: unset !important;
            background-color: transparent !important;
            background-size: contain !important;
            background-repeat: no-repeat !important;
            background-position: center !important;
            transition: transform 0.3s ease !important;
            cursor: pointer !important;
            margin: 0 auto !important;
            display: block !important;
        }

        div.stButton > button:hover {
            transform: scale(1.05) !important;
            box-shadow: none !important;
            background-color: transparent !important;
            border-color: transparent !important;
        }

        div.stButton > button:focus,
        div.stButton > button:active,
        div.stButton > button:focus-visible {
            outline: none !important;
            box-shadow: none !important;
            background-color: transparent !important;
            border-color: transparent !important;
        }

        /* Письмо */
        .letter-container {
            width: 100%;
            max-width: 900px;
            margin: 20px auto 0 auto;
            padding: 25px 20px;
            background: white;
            border-radius: 15px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
            border: 2px solid #F0C4D0;
            animation: fadeIn 0.6s ease;
            text-align: center;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .letter-container h2 {
            color: #D4839E;
            font-family: 'Georgia', serif;
            text-align: center;
            margin-bottom: 15px;
            font-size: 1.7em;
        }

        .letter-container p {
            font-family: 'Georgia', serif;
            color: #5C2E3E;
            font-size: 1.12em;
            line-height: 1.8;
            text-align: left;
            margin: 0;
            word-wrap: break-word;
        }

        .hint {
            color: #B88A9A;
            font-size: 1em;
            margin-top: 15px;
            font-family: 'Georgia', serif;
            text-align: center !important;
            width: 100% !important;
            display: block !important;
        }

        .hint.hidden {
            display: none;
        }

    </style>
""", unsafe_allow_html=True)

# Инициализация состояния
if "envelope_open" not in st.session_state:
    st.session_state.envelope_open = False

# Меню
st.markdown("""
    <div style="background: white; padding: 15px 30px; border-radius: 10px; 
                box-shadow: 0 2px 10px rgba(0,0,0,0.05); margin-bottom: 0px;
                display: flex; gap: 20px; flex-wrap: wrap; justify-content: center;">
        <a href="/" target="_self" style="color: #7A4B5E; text-decoration: none; font-size: 1.1em; 
           font-weight: 500; padding: 8px 20px; border-radius: 20px; transition: all 0.3s ease;">🏠 Главная</a>
        <a href="/page1" target="_self" style="color: #7A4B5E; text-decoration: none; font-size: 1.1em; 
           font-weight: 500; padding: 8px 20px; border-radius: 20px; transition: all 0.3s ease;">📸 Как все начиналось</a>
        <a href="/page2" target="_self" style="color: #7A4B5E; text-decoration: none; font-size: 1.1em; 
           font-weight: 500; padding: 8px 20px; border-radius: 20px; transition: all 0.3s ease;">🎉 Общажные вайбики</a>
        <a href="/page3" target="_self" style="color: #7A4B5E; text-decoration: none; font-size: 1.1em; 
           font-weight: 500; padding: 8px 20px; border-radius: 20px; transition: all 0.3s ease;">💕 Дом там где ты</a>
        <a href="/page4" target="_self" style="color: #7A4B5E; text-decoration: none; font-size: 1.1em; 
           font-weight: 500; padding: 8px 20px; border-radius: 20px; transition: all 0.3s ease;">💝 Особенные моменты</a>
    </div>
""", unsafe_allow_html=True)

# Пути к картинкам
ENVELOPE_CLOSED = "images/letter_close.jfif"
ENVELOPE_OPEN = "images/letter_open.jfif"


# Функция для конвертации картинки в base64
def get_image_base64(image_path):
    if os.path.exists(image_path):
        img = Image.open(image_path)
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode()
    return None


# Центрирующий контейнер
col1, col2, col3 = st.columns([1, 10, 1])
with col2:
    st.markdown('<div class="envelope-container">', unsafe_allow_html=True)

    if not st.session_state.envelope_open:
        # Закрытый конверт
        img_base64 = get_image_base64(ENVELOPE_CLOSED)
        if img_base64:
            st.markdown(f'''
                <style>
                    div.stButton > button {{
                        background-image: url("data:image/png;base64,{img_base64}") !important;
                    }}
                    div.stButton > button:hover {{
                        background-image: url("data:image/png;base64,{img_base64}") !important;
                    }}
                    div.stButton > button:focus {{
                        background-image: url("data:image/png;base64,{img_base64}") !important;
                    }}
                    div.stButton > button:active {{
                        background-image: url("data:image/png;base64,{img_base64}") !important;
                    }}
                </style>
            ''', unsafe_allow_html=True)

        if st.button("", key="envelope_btn", use_container_width=True):
            st.session_state.envelope_open = True
            st.rerun()

        st.markdown('<p class="hint">👆 Нажми на конверт, чтобы открыть</p>', unsafe_allow_html=True)

    else:
        # Открытый конверт
        img_base64 = get_image_base64(ENVELOPE_OPEN)
        if img_base64:
            st.markdown(f'''
                <style>
                    div.stButton > button {{
                        background-image: url("data:image/png;base64,{img_base64}") !important;
                    }}
                    div.stButton > button:hover {{
                        background-image: url("data:image/png;base64,{img_base64}") !important;
                    }}
                    div.stButton > button:focus {{
                        background-image: url("data:image/png;base64,{img_base64}") !important;
                    }}
                    div.stButton > button:active {{
                        background-image: url("data:image/png;base64,{img_base64}") !important;
                    }}
                </style>
            ''', unsafe_allow_html=True)

        if st.button("", key="envelope_btn_close", use_container_width=True):
            st.session_state.envelope_open = False
            st.rerun()

        st.markdown("""
                    <div class="letter-container">
                      <h2>❤️ Моя любимая ❤️</h2>
                        <p>
                            Любимая, я очень рад, что год назад мы с тобой начали отношения. Это лучший год за всю мою жизнь!
                    Вспоминая весь этот год у меня разбегаются глаза, от количества крутейших дней.
                    <br>
                    Каждый день проведенный с тобой для меня награда. Я рад делить с тобой радость, веселые моменты,
                    грусть и все все остальное. Я точно знаю что вместе мы можем все!
                    <br>
                    За этот год мы познакомились, влюбились и невероятно любим друг друга. Мы провели 365 отличнейших
                    дней, получили миллион классных эмоций, посетили много клевых мест, нашли совместные интересы и
                    хобби. Проблемы, возникавшие на нашем пути, мы преодолеваем также вместе как и делим радость.
                    <br>
                    Неважно были ли мы сегодня в каком то крутом месте или просто лежали дома, смотря сериал, для меня
                    любой день с тобой очень важен и ценен. Я помню каждый из этих дней. Как мы встречали новый год,
                    пересматривая старые мультики, собирая легои кушая вкусности. Как мы ходили в кино на Чебурашку, фильм про пожары, про акул, как мы
                    в мегаполисе сделали фотки после просмотра Чебурашки, и носим эти фотки под чехлом по сей день.
                    Помню как мы ждали лето, ведь была очень холодная зима и помню как мы обрадовались, когда снег начал
                    сходить. Помню как мы пошли гулять весной, в марте, когда было +20, снега еще было много. Мы пришли
                    в парк ургупса, гуляли по плотинке. Помню как ты думала что с работой. Помню как я подбадривал тебя
                    на этот счет. Помню как ты переживала из за диплома и как ты его отлично защитила. 
                    Помню как ждали и наконец то поехали в Первоуральск. Я могу еще долго вспоминать и перечислять
                    ведь каждое мгновение для меня очень ценно. Я очень ценю тебя и твою любовь.
                    <br>
                    Я люблю тебя! Я всегда стараюсь делать так, чтобы у тебя все было хорошо.
                    Мне важно чтобы ты себя хорошо чувствовала, кушала, не мерзла зимой и так далее, ты моя
                    частичка, мой драгоценный Кристаллик.
                    <br>
                    Этот год был понастоящему крутым. Он был полон любви, внимания и заботы! Я очень благодарен тебе,
                    любовь моя. Впереди нас ждет еще сотня таких лет. Я очень тебя люблю!
                     
                    <br><br>
                    С любовью, твой, любимый 💕
                        </p>   
                    </div>
                """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
