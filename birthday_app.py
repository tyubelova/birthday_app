import streamlit as st

st.subheader('Тебя зовут Даниэль?')
if st.button('Да я :sunglasses', type='primary'):
    st.markdown('С Днем Рожденияя!! :partying_face::partying_face: Желаю тебе всего самого-самого наилучшего, '
                'успехов в учебе и в жизни. Пусть мечты исполняются, а цели достигаются!')
    st.video('https://www.youtube.com/watch?v=gOqKwCyA0QM')
if st.button('Нет, не так'):
     st.write('Ну вот :(')
