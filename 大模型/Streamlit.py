import streamlit as st

# 标题
st.title("通告", text_alignment="center")
st.header("今天是个大日子", text_alignment="center")
st.subheader("胡少29岁大喜之日", text_alignment="center")

# 文本
st.write(
    "又是一年诞辰，祝你新的一岁顺遂安康。认识这么多年，你一直是我心里那个靠得住的人 —— 靠谱、真诚，认定的事就全力以赴。今天是你的日子，希望你能好好放松一下，把烦恼都放下，只留开心。")
st.write(
    "愿你在新的一岁里：事业更上一层楼，想要的都慢慢实现；身体健健康康，日子过得热气腾腾；身边有人懂你、陪你、挺你。无论走多远，兄弟都在。")
st.write("有空咱们聚一聚，好好喝一杯，庆祝你又长大一岁！")

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
st.image(str(BASE_DIR / "resource" / "Pictures" / "R-C.jpg"))

st.audio(str(BASE_DIR / "resource" / "儿歌多多 - 生日快乐 (粤语儿歌).mp3"))
