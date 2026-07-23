import streamlit as st
from PIL import Image
import os
import base64
from io import BytesIO

# Настройка страницы
st.set_page_config(
    page_title="Наша первая встреча",
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
        <h1>Дом там где ты</h1>
    </div>
""", unsafe_allow_html=True)

# Данные для слайдера (ЗАМЕНИ НА СВОИ)
photos = [
    "images/page_three/photo_17_2026-07-07_22-35-23.jpg", "images/page_three/photo_2_2026-07-07_22-33-39.jpg",
    "images/page_three/photo_8_2026-07-07_22-33-39.jpg", "images/page_three/photo_3_2026-07-07_22-33-39.jpg",
    "images/page_three/photo_2_2026-07-07_22-35-23.jpg", "images/page_three/photo_1_2026-07-07_22-35-23.jpg", "images/page_three/photo_7_2026-07-07_22-35-23.jpg",
    "images/page_three/photo_8_2026-07-07_22-35-23.jpg", "images/page_three/photo_6_2026-07-07_22-35-23.jpg",
    "images/page_three/photo_4_2026-07-07_22-35-23.jpg", "images/page_three/photo_3_2026-07-07_22-35-23.jpg",
    "images/page_three/photo_12_2026-07-07_22-35-23.jpg", "images/page_three/photo_11_2026-07-07_22-35-23.jpg",
    "images/page_three/photo_10_2026-07-07_22-35-23.jpg", "images/page_three/photo_56_2026-07-07_22-35-23.jpg", "images/page_three/photo_14_2026-07-07_22-35-23.jpg",
    "images/page_three/photo_18_2026-07-07_22-35-23.jpg", "images/page_three/photo_22_2026-07-07_22-35-23.jpg",
    "images/page_three/photo_23_2026-07-07_22-35-23.jpg", "images/page_three/photo_24_2026-07-07_22-35-23.jpg",
    "images/page_three/photo_21_2026-07-07_22-35-23.jpg", "images/page_three/photo_33_2026-07-07_22-35-23.jpg", "images/page_three/photo_15_2026-07-07_22-35-23.jpg",
    "images/page_three/photo_16_2026-07-07_22-35-23.jpg", "images/page_three/photo_26_2026-07-07_22-35-23.jpg",
    "images/page_three/photo_37_2026-07-07_22-35-23.jpg",
    "images/page_three/photo_36_2026-07-07_22-35-23.jpg", "images/page_three/photo_35_2026-07-07_22-35-23.jpg",
    "images/page_three/photo_38_2026-07-07_22-35-23.jpg", "images/page_three/photo_32_2026-07-07_22-35-23.jpg",
    "images/page_three/photo_29_2026-07-07_22-35-23.jpg", "images/page_three/photo_30_2026-07-07_22-35-23.jpg",
    "images/page_three/photo_31_2026-07-07_22-35-23.jpg", "images/page_three/photo_34_2026-07-07_22-35-23.jpg",
    "images/page_three/photo_28_2026-07-07_22-35-23.jpg", "images/page_three/photo_39_2026-07-07_22-35-23.jpg",
    "images/page_three/photo_44_2026-07-07_22-35-23.jpg",
    "images/page_three/photo_41_2026-07-07_22-35-23.jpg", "images/page_three/photo_40_2026-07-07_22-35-23.jpg",
    "images/page_three/photo_43_2026-07-07_22-35-23.jpg", "images/page_three/photo_53_2026-07-07_22-35-23.jpg",
    "images/page_three/photo_54_2026-07-07_22-35-23.jpg", "images/page_three/photo_48_2026-07-07_22-35-23.jpg",
    "images/page_three/photo_49_2026-07-07_22-35-23.jpg", "images/page_three/photo_47_2026-07-07_22-35-23.jpg",
    "images/page_three/photo_1_2026-07-08_00-10-04.jpg", "images/page_three/photo_45_2026-07-07_22-35-23.jpg",
    "images/page_three/photo_55_2026-07-07_22-35-23.jpg", "images/page_three/photo_2_2026-07-08_00-10-04.jpg",
    "images/page_three/photo_3_2026-07-08_00-10-04.jpg", "images/page_three/photo_4_2026-07-08_00-10-04.jpg"
]

fixed_text = "В этом разделе я решил написать все одним текстом, так как фотографий просто море. Я еле выбрал самые крутые фотки, этот раздел можно сделать огромным, гиганстким. Он длится пол года, также как тагильский и общажный вместе. Но по насыщенности это просто небо и земля.<br>Пойдем по порядку. Отдельного внимания заслуживает сам момент, как мы съехали на квартиру. Это было каким то новогодним чудом, буквально идеальный для нас вариант. Помню как это было все в новинку и так интересно, как мы переезжали, начинали строить свой быт. После общажного этапа, и крайне малого количества времени, что мы проводили друг с другом, мы стали жить вместе. Это стало великоплено. Моя любовь всегда со мной, мы всегда вместе, и не важно заняты мы или нет, по возвращению домой всегда улыбка на лице. Ведь ты и я всегда ждем друг друга дома.<br>Наш первый совместный новый год был потрясающий, мы сделали крутецкий стол, тепло встретили новый год, и с придыханием открывали подарки. Проснувшись на следующий день мы собирали вместе лего. Это стало началом нашего совместного плюс вайба. Мы нашли много совместных время провождений, натсольные игры, лего, пазлы. В новогодние каникулы мы с тобой проводили вечера гуляя, по холодным заснеженным улочкам города, и тепло сидя дома, просматривая фильмы, сериалы, играя в морской бой, кости и карты.<br>Подборка смешных фоточек. Как мы играем/бесимся это тоже очень клево, мы крутыши.<br>За эти пол года, что мы вместе живем мы посетили кучу мест. Театр, киношки, зарубы в боулинге, зоопарк, океанариум Сысерть, Первоуральск, вело прогулки и бесчисленное множество пеших прогулок. Каждый проведенный с тобой день я очень люблю. Все эти фотографии я могу описывать на страницы текста, ведь смотря на каждую из этих фото, мое сердце начинает биться быстрее, вспоминая каждый проведенный вместе день!<br>Я очень люблю тебя, моя душа!"

# Инициализация индекса
if "slide_index" not in st.session_state:
    st.session_state.slide_index = 0


# Функция для отображения слайда
def display_slide(index):
    if 0 <= index < len(photos):
        image_path = photos[index]  # теперь это просто строка

        if os.path.exists(image_path):
            image = Image.open(image_path)
            buffered = BytesIO()
            fmt = "PNG" if image_path.lower().endswith(".png") else "JPEG"
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
                unsafe_allow_html=True
            )

        # Счётчик
        st.markdown(f'<div class="counter">{index + 1} / {len(photos)}</div>', unsafe_allow_html=True)

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

# Текст под фото
st.markdown(f'<div class="slider-text">💕 {fixed_text}</div>', unsafe_allow_html=True)



