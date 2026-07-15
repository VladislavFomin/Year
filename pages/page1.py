import streamlit as st
from PIL import Image
import os
import base64
from io import BytesIO

# Настройка страницы
st.set_page_config(
    page_title="Как все начиналось или первые милости",
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
        margin: -20px -50px 30px -50px;
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
    
    div.stImage {
        display: flex !important;
        justify-content: center !important;
        width: 100% !important;
        text-align: center;
    }
    
    div.stImage img {
        display: block !important;
        margin: 0 auto !important;
        max-width: 700px !important;
        max-height: 500px !important;
        width: auto !important;
        height: auto !important;
        object-fit: contain !important;
        border-radius: 10px;
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
        <h1>Как все начиналось</h1>
    </div>
""", unsafe_allow_html=True)

# Данные для слайдера (ЗАМЕНИ НА СВОИ)
photos = [
    {"image": "images/page_one/photo_12_2026-07-07_22-32-33.jpg", "text": "Первое сообщение!!!<br> Наша первая"
                                                                          " переписка, начало знакомства, очень милые моменты"},
    {"image": "images/page_one/photo_13_2026-07-07_22-32-33.jpg", "text": "ЛЕЕЕСГОУ<br> Помню, как я предлагал тебе впервые погулять. По началу было немного неловко, но постепенно, узнавая тебя, я понимал, что ты малышка крутышка! В этот день появилось прозвище Пиздюш, я учил тебя словам йоу и лесгоу, гуляя по набережной Тагила"},
    {"image": "images/page_one/photo_14_2026-07-07_22-32-33.jpg", "text": "Сообщения после первой прогулки<br>После встречи у меня были легкие и веселые эмоции. Мне очень понравилась ты и наша встреча, как мы гуляли, шутили и смеялись, уже тогда я понял, что ты мой родной человечек"},
    {"image": "images/page_one/photo_15_2026-07-07_22-32-33.jpg", "text": "Это очень милые сообщения, написанные тобой, в аэропорту по пути в Турцию<br>На самом деле я немного переживал сможем ли мы хорошо общаться, пока ты в Турции, и переживал я напрасно"},
    {"image": "images/page_one/photo_16_2026-07-07_22-32-33.jpg", "text": "Я напрасно переживал, потому что мы будто вместе там были<br>Ты делилась со мной всем: от что было на завтрак до долгих телефонных разговоров обо всем. Это сообщение отлично передает эту картину"},
    {"image": "images/page_one/photo_17_2026-07-07_22-32-33.jpg", "text": "Появление легендарного котика(тебя)<br>Первое его упоминание в нашем чате, в будущем ставщая легендой.<br>Ты и правда этот котик! Такая милая, красивая, добрая и веселая!"},
    {"image": "images/page_one/photo_18_2026-07-07_22-32-33.jpg", "text": "Наши телефонные разговоры<br>Это всего малая часть того, сколько мы общались, я не стал добавлять все скрины звонков, потому что этот слайдер превратился бы в подборку звонков)<br>За время этих разговоров мы узнавали друг друга все больше и больше, делилсь переживаниями и просто болтали, они очень сблизили нас"},
    {"image": "images/page_one/photo_20_2026-07-07_22-32-33.jpg", "text": "Наши телефонные разговоры<br>Это всего малая часть того, сколько мы общались, я не стал добавлять все скрины звонков, потому что этот слайдер превратился бы в подборку звонков)<br>За время этих разговоров мы узнавали друг друга все больше и больше, делилсь переживаниями и просто болтали, они очень сблизили нас"},
    {"image": "images/page_one/photo_19_2026-07-07_22-32-33.jpg", "text": "Дабл ю подкатик<br>Просто мило"},
    {"image": "images/page_one/photo_21_2026-07-07_22-32-33.jpg", "text": "Упоминание Пиздюша<br>Это шуточное прозвище, появивщееся в нашу первую встречу было очень милым"},
    {"image": "images/page_one/photo_23_2026-07-07_22-32-33.jpg", "text": "Вот такой вот дабл ю завозик<br>Который в будущем станет реальностью(спойлер)"},
    {"image": "images/page_one/photo_2_2026-07-07_22-32-32.jpg", "text": "Наша первая совместная фотка!!!<br>Я приехал встретить тебя с аэропорта. Помнишь как лил жуткий дождь, а мы приехали в какой то магазинчик непонятно где и не могли еще выехать с парковки хахаах<br>Мы гуляли по парку Маяковского и сделали эту фотку для сравнения загара. Я говорил, что ты негр, а ты не верила. Очень милая прогулка на самом деле. Вернувшись с Турции ты была для меня родной, мы так общались в тгшке, что я будто с тобой в Турции был"},
    {"image": "images/page_one/photo_1_2026-07-07_22-32-32.jpg", "text": "ПЕРВОУРАААЛЬСК<br>Наша первая совместная поездка, открывшая нам замечательный город Первоуральск. Мне очень нравится тот день<br>Помню как мы удивились этому городу. Он ряльно оказался крутым. Помню как мы обошли набережную, ты поделала фоток, зашли в странной формы музей(или что это было, какой то дк). Обошли весь центральный Первоуральск, пришли в еще строящийся парк и сидели на лавчоке для поцелуев, смотря на белочек.<br>Сплошной плюс вайб"},
    {"image": "images/page_one/photo_11_2026-07-07_22-32-33.jpg", "text": "ПЕРВОУРАААЛЬСК<br>Наша первая совместная поездка, открывшая нам замечательный город Первоуральск. Мне очень нравится тот день<br>Помню как мы удивились этому городу. Он ряльно оказался крутым. Помню как мы обошли набережную, ты поделала фоток, зашли в странной формы музей(или что это было, какой то дк). Обошли весь центральный Первоуральск, пришли в еще строящийся парк и сидели на лавчоке для поцелуев, смотря на белочек.<br>Сплошной плюс вайб"},
    {"image": "images/page_one/photo_3_2026-07-07_22-32-32.jpg", "text": "ПЕРВОУРАААЛЬСК<br>Наша первая совместная поездка, открывшая нам замечательный город Первоуральск. Мне очень нравится тот день<br>Помню как мы удивились этому городу. Он ряльно оказался крутым. Помню как мы обошли набережную, ты поделала фоток, зашли в странной формы музей(или что это было, какой то дк). Обошли весь центральный Первоуральск, пришли в еще строящийся парк и сидели на лавчоке для поцелуев, смотря на белочек.<br>Сплошной плюс вайб"},
    {"image": "images/page_one/photo_4_2026-07-07_22-32-32.jpg", "text": "ПЕРВОУРАААЛЬСК<br>Наша первая совместная поездка, открывшая нам замечательный город Первоуральск. Мне очень нравится тот день<br>Помню как мы удивились этому городу. Он ряльно оказался крутым. Помню как мы обошли набережную, ты поделала фоток, зашли в странной формы музей(или что это было, какой то дк). Обошли весь центральный Первоуральск, пришли в еще строящийся парк и сидели на лавчоке для поцелуев, смотря на белочек.<br>Сплошной плюс вайб"},
    {"image": "images/page_one/photo_5_2026-07-07_22-32-32.jpg", "text": "Наши первые тагильские прогулочки<br>Очень теплые времена. Вспоминая как мы за ручку шлепаем по тагилу, проявляется теплая улыбка. Хоть и все места Тагила мы проходили на несколько раз, нам не было скучно. Мы ходили болтали абсолютно обо всем"},
    {"image": "images/page_one/photo_6_2026-07-07_22-32-32.jpg", "text": "Наши первые тагильские прогулочки<br>Очень теплые времена. Вспоминая как мы за ручку шлепаем по тагилу, проявляется теплая улыбка. Хоть и все места Тагила мы проходили на несколько раз, нам не было скучно. Мы ходили болтали абсолютно обо всем"},
    {"image": "images/page_one/photo_7_2026-07-07_22-32-32.jpg", "text": "Серая кофточка<br>Кристаллик замерз и Владосик дал ей свою серую кофтус, это было мило. Также как и в нашу первую встречу, поднимаясь на Лисью Гору я отдал тебе кофту. Было оч холодно если честно, но мне главное чтобы ты была всегда в безопасности и тепле, мой Кристаллик.<br>Вспомнил еще один случай, когда я приехал к тебе в августе, поздно вечером. Ты была только после болезни и было очень холодно. В тот день моя кофта снова оказалась на тебе"},
    {"image": "images/page_one/photo_9_2026-07-07_22-32-32.jpg", "text": "Макан сорван пукан<br>Ты такая крутышка на этой фотке! Прям самый главный милашик крутышик. В тот день кстати я впервые попробовал чипсы А4. Забегая вперед, сейчас эти чипсы мы кушаем, смотря мамочку в 16 WW"},
    {"image": "images/page_one/photo_8_2026-07-07_22-32-32.jpg", "text": "Крутые мы!<br>Фотки уже позднего Тагила ахахха. Конец августа. Я очень люблю тебя и каждый день из наших Тагильских прогулок. Это было очень теплое и значимое для нас время, тогда зародилась наша огромная любовь"},
    {"image": "images/page_one/photo_10_2026-07-07_22-32-33.jpg", "text": "Крутые мы!<br>Фотки уже позднего Тагила ахахха. Конец августа. Я очень люблю тебя и каждый день из наших Тагильских прогулок. Это было очень теплое и значимое для нас время, тогда зародилась наша огромная любовь"}
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
                            width: 100%; padding: 20px 0;">
                    <img src="data:{mime};base64,{img_str}" 
                         style="max-width: 700px; 
                                max-height: 500px; 
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

        # Текст под фото
        st.markdown(f'<div class="slider-text">💕 {photos[index]["text"]}</div>', unsafe_allow_html=True)

        # Счетчик
        st.markdown(f'<div class="counter">{index + 1} / {len(photos)}</div>', unsafe_allow_html=True)


# Отображение текущего слайда
display_slide(st.session_state.slide_index)

# Кнопки навигации
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    if st.button("⬅️ Назад", key="prev1"):
        if st.session_state.slide_index > 0:
            st.session_state.slide_index -= 1
            st.rerun()

with col3:
    if st.button("Вперед ➡️", key="next1"):
        if st.session_state.slide_index < len(photos) - 1:
            st.session_state.slide_index += 1
            st.rerun()
