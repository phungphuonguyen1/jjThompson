import streamlit as st
from PIL import Image
def load_view():
    title_main='<h1 style="text-align:center; font-weight: bolder;color: #EE9322;text-shadow: 3px 1px blue;">GIỚI THIỆU CHUNG</h1>'
    st.markdown(title_main,unsafe_allow_html=True)
    #st.markdown('Thí nghiệm đo $\dfrac{e}{m}$ của J.J. Thomson',unsafe_allow_html=True)
    head2='<h2 style="text-align:left; font-weight: bolder;color: #FCF3CF;text-shadow: 3px 1px black;">J.J. Thomson</h2>'
    st.markdown(head2,unsafe_allow_html=True)
    img=Image.open("/assets/images/gettyimages-113634985.jng")
