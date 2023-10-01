import streamlit as st
from PIL import Image
def load_view():
    title_main='<h1 style="text-align:center; font-weight: bolder;color: #EE9322;text-shadow: 3px 1px blue;">GIỚI THIỆU CHUNG</h1>'
    st.markdown(title_main,unsafe_allow_html=True)

    #table of content
    menu="""<div class="toc">
        <h2 class='styled-heading'>Table of Contents</h2>
        <ul>
            <li><a href="#section1">1. J.J. Thomson</a></li>
            <li><a href="#section2">2. Thí nghiệm tìm ra tỷ số e/m</a></li>
            <li><a href="#section3">3. Tài liệu tham khảo</a></li>
        </ul>
    </div>"""
    st.markdown(menu,unsafe_allow_html=True)

    ses1= """<div id="section1">
        <h2 class="styled-heading">1. J.J. Thomson</h2>
        <div class="container-author">
        <div class="image">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/J.J_Thomson.jpg/250px-J.J_Thomson.jpg">
         </div>   
        <div class="text">
            <p class='styled-paragraph'>
                Joseph John Thomson là nhà Vật lý học người Anh, người đã vinh dự nhận giải Nobel Vật Lý vào năm 1906.<br>Vào năm `897, Thomson đã chỉ ra rằng các tia phát ra từ cathode được tạo bởi
                các hạt chưa biết mang điện tích âm (ngày nay, chúng ta gọi nó là electron). Với các hạt này, ông đã tính được rằng kích thước của chúng là rất nhỏ so với kích thước 1 nguyên tử và
                tỷ lệ giữa điện tích và khối lượng của hạt này là rất lớn.<br>Thomson cũng được biết tới là người đầu tiên đưa ra bằng chứng về các đồng vị của một nguyên tố bền (không phóng xạ) 
                vào năm 1913. Các thí nghiệm của ông nhằm xác định bản chất của các hạt tích điện dương, cùng với nhà Vật lý học Francis William Aston, là ứng dụng đầu tiên của phép đo khối phổ và
                dẫn tới sự phát triển của máy quang phổ khối.<br>Thomson đã được trao giải Nobel Vật lý vào năm 1906 với công trình về sự dẫn điện trong chất khí. Thomson cũng là một giáo viên,
                có 9 người trong số các học sinh, đồng nghiệp và cấp dưới (bao gồm cả con trai ông) cũng giành được giải Nobel.</p>
        </div>
        </div>
    </div>"""
    st.markdown(ses1,unsafe_allow_html=True)
    ses2="""<div id="section2">
            <h2 class="styled-heading">2. Thí nghiệm tìm ra tỷ số e/m</h2>
            <p class="styled-paragraph">Thí nghiệm này được tiến hành vào năm 1897</p>
        </div>"""
    st.markdown(ses2,unsafe_allow_html=True)
    
    ses3="""
        <div id="section3">
            <h2 class="styled-heading">3. Tài liệu liên quan</h2>
            <a href="https://youtu.be/Rb6MguN0Uj4">Video giải thích thí nghiệm</a>
            <br>
            <a href="https://youtu.be/_nLESblUAHY">Video mô phỏng thí nghiệm</a>
        </div>      
        """
    st.markdown(ses3,unsafe_allow_html=True)

    

