import streamlit as st
from def_file import *
from matplotlib.animation import FuncAnimation
import io
import base64
import time
from PIL import Image

def user_input_features():
    Voltage=st.slider('V (V): ',0.0,10.0, 3.0)
    Distance=st.slider('D (m): ',0.01,0.1, 0.05,step=0.01)
    #B_field=st.slider('B (10^5 T): ',0.5,10.0,step=0.1)
    B_field = st.slider(r'B ($10^5$ T): ', 0.5, 10.0, step=0.1)
    X1=st.slider(r'$l_1$ (m): ',0.1,1.0,0.2,step=0.01)
    X2=st.slider(r'$l_2$ (m): ',0.1,1.0,0.2,step=0.01)
    features=[float(Voltage),float(Distance),float(X1),float(X2),float(B_field/10**5)]
    return features

def load_view():    
    title_main='''<h1 class="styled-heading">
        Chương trình mô phỏng thí nghiệm đo tỷ sổ khối lượng/ điện tích của J. J. Thomson
    </h1>'''
    st.markdown(title_main,unsafe_allow_html=True)
    
    st.markdown(
        '''
        <style>
        .streamlit-expanderHeader {
            background-color: lightblue;
            color: black; # Adjust this for expander header color
            border-radius: 20px;
            text-align:center;
        }
        .streamlit-expanderContent {
            background-color: white;
            color: black; # Expander content color
        }
        </style>
        ''',
        unsafe_allow_html=True)
    # input explaination:
    # input explaination:
    ls1=  r"""
    <ul>
            <li>V: Điện thế của bản tụ (V)</li>
            <li>D: Khoảng cách giữa 2 bản tụ (m)</li>
            <li>B: Độ lớn cường độ từ trường (T)</li>
            <li> l_1: Chiều dài bản tụ (m)</li>
            <li> l_2: Khoảng cách từ bản tụ đến màn chắn (m)</li>
        </ul>
    """
    st.write("Giải thích các thông số đầu vào:")     
    st.markdown(ls1,unsafe_allow_html=True)
    col1,col2= st.columns([1,2])
    with col1: 
        input = user_input_features()
    with col2:
        '''hed22='<h2 class="styled-heading">Hình vẽ mô phỏng thí nghiệm thực tế</h2>'
        st.markdown(hed22,unsafe_allow_html=True)
        image=Image.open("Specific-Charge-Ratio-03.png")
        st.image(image,caption="Hình vẽ mô tả thí nghiệm J.J. Thomson 1897")'''
        m= """ <div class="container-single">
                    <h2 class="styled-heading">Hình vẽ mô phỏng thí nghiệm thực tế</h2>
                    <img src="https://thefactfactor.com/wp-content/uploads/2019/11/Specific-Charge-Ratio-03.png">
                </div>
            """
        st.markdown(m,unsafe_allow_html=True)
        
    col3,col4=st.columns([2,1])
    if col1.button("Mô phỏng"):
        with col3:
            df = path_function(input[0], input[1], input[2], input[3], input[4])
            #st.pyplot(plt)
            fig, ax = plt.subplots()
            ax.plot(df['x'],df['y'],"r")
            voltage=input[0]
            E_field=input[0]/input[1]

            vx= E_field/input[4]
            ELECTRON_CHARGE= 1.6e-19
            ELECTRON_MASS = 9.1e-31
            # Calculate other factors
            ratio =ELECTRON_CHARGE/ELECTRON_MASS
            D=input[1]
            x1=input[2]
            x2=input[3]
            B_field=input[4]
            t1_final=x1/vx
            t2_final=x2/vx
            y1=y1_inside(vx,ratio,E_field,B_field,t1_final,voltage,D)
            y2=y2_outside(ratio,t2_final,x1,B_field,t1_final,E_field,voltage)

            #note
            #ax.text(-0.1,(input[1]/2)*1.3,'E={} V/m,$x_1$={}m,\n$x_2$={}m,$v_0={}m/s$'.format(E_field,x1,x2,vx),fontsize = 12, bbox = dict(facecolor = 'lightblue', alpha = 0.5))
            #ax.set_title("Simulation")
            ax.axis("off")

            #facilities
            ax.hlines(y=D/2, xmin=0, xmax=x1, linewidth=4, color='black')
            ax.hlines(y=-D/2, xmin=0, xmax=x1, linewidth=4, color='black')
            ax.text(0.9*x1/2,(1.1*D)/2,"+")
            ax.vlines(x=x1+x2, ymin=-D/2, ymax=1.5*max((y1+y2),D/2), linewidth=3, color='black')
            ax.hlines(y=0, xmin=0, xmax=x1+x2, linestyles='dotted',color='black')
            ax.text(0.9*x1/2,(-1.1*D)/2,"_")
            
            #distance note
            # x1
            ax.plot((0,x1),(-1.3*D/2,-1.3*D/2), 'gray',) # arrow line
            ax.plot((0,0),(-1.3*D/2,-1.3*D/2), 'gray', marker='<',) # lower arrowhead
            ax.plot((x1,x1),(-1.3*D/2,-1.3*D/2), 'gray', marker='>',) # upper arrowhead
            ax.text(x1/2.5,-1.5*D/2,"$l_1$={}".format(x1))

            #x2
            ax.plot((x1,x2+x1),(-1.3*D/2,-1.3*D/2), 'gray',) # arrow line
            ax.plot((x1,x1),(-1.3*D/2,-1.3*D/2), 'gray', marker='<',) # lower arrowhead
            ax.plot((x2+x1,x2+x1),(-1.3*D/2,-1.3*D/2), 'gray', marker='>',) # upper arrowhead
            ax.text(x1+x2/2.5,-1.5*D/2,"$l_2$={}".format(x2))

            #D
            ax.plot((-0.1,-0.1),(-D/2,D/2), 'gray',) # arrow line
            ax.plot((-0.1,-0.1),(-D/2,-D/2), 'gray', marker='v',) # lower arrowhead
            ax.plot((-0.1,-0.1),(D/2,D/2), 'gray', marker='^',) # upper arrowhead
            ax.text(-0.15,-D/10,"D={}".format(D),rotation=90)

            #y2
            ax.plot((x1+x2+0.05,x1+x2+0.05),(0,y1+y2), 'gray',) # arrow line
            ax.plot((x1+x2+0.05,x1+x2+0.05),(0,0), 'gray', marker='v',) # lower arrowhead
            ax.plot((x1+x2+0.05,x1+x2+0.05),(y2+y1,y2+y1), 'gray', marker='^',) # upper arrowhead
            ax.text(x1+x2+0.075,(y1+y2)/6,"$y_1 + y_2$={:.6f}".format(y1+y2),rotation=90)
            
            # Display the plot in Streamlit
            st.pyplot(fig)
        with col4:
            #st.write(pd.DataFrame({'data':[E_field,x1,x2,D,voltage]}))
            st.markdown("""
                |       | Giá trị |
                | ----------- | ----------- |
                | **Điện trường**    | {} V/m|
                | **Từ trường**   | {} T|
                | **Điện thế** | {} V|
                | **D** | {} m|
                | **$l_1$**| {} m|
                | **$l_2$** | {} m|
                | **$v_x$** | {:.1f} m/s|
                | **$y_1$** | {:.6f}  m|
                | **$y_2$** | {:.6f} m|
            """.format(E_field,B_field,voltage,D,x1,x2,vx,y1,y2))
            #st.markdown("**e/m: {} C/kg**".format(ratio))
            st.markdown("<br>",unsafe_allow_html=True)
            st.markdown('$\dfrac{e}{m}$'+'= {}'.format(ratio))




    
