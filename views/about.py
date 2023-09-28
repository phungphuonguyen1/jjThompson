import streamlit as st
from def_file import *
def user_input_features():
    Voltage=st.slider('Voltage: ',0.0,10.0, 3.0)
    Distance=st.slider('Distance: ',0.01,0.1, 0.05,step=0.01)
    B_field=st.slider('10^6*B_field: ',1.0,10.0,step=0.1)
    X1=st.slider('x1: ',0.1,1.0,0.2,step=0.01)
    X2=st.slider('x2: ',0.1,1.0,0.2,step=0.01)
    features=[float(Voltage),float(Distance),float(X1),float(X2),float(B_field/10**6)]
    return features

def load_view():    
    st.title('Calculation page')
    title_main='''<h1 style="text-align:center; font-weight: bolder;color: #EE9322;text-shadow: 3px 1px blue;">
        Tính toán cho thí nghiệm
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
        unsafe_allow_html=True
    )

    # input explaination:
    ls1="""<ul>
            <li>Interaction polymer-nanoparticle: amplitube</li>
            <li>Interaction nanoparticle-nanoparticle: amplitube</li>
            <li>Diameter of nanoparticle: size of nanoparticle (sperical, in nanometer)</li>
            <li>Phi: represented by mass of nanoparticle per total volume</li>
            <li>Length of polymer chain: in nanometer</li>
            <li>Distance: range should be small (less than length of polymer chain)</li>
        </ul>"""


    with st.expander("Input explaination"):
        st.markdown(ls1,unsafe_allow_html=True)

    input = user_input_features()

    if st.button("Mô phỏng"):
        #ax.style.use('dark_background')
        df=path_function(input[0],input[1],input[2],input[3],input[4])
        #path
        st.write(df)
        fig,ax=plt.subplots()
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
        ax.text(-0.1,(input[1]/2)*1.3,'E={} V/m,$x_1$={}m,\n$x_2$={}m,$v_0={}m/s$'.format(E_field,x1,x2,vx),fontsize = 12, bbox = dict(facecolor = 'lightblue', alpha = 0.5))
        ax.set_title("Simulation")
        #ax.axis("off")

        #facilities
        ax.hlines(y=D/2, xmin=0, xmax=x1, linewidth=4, color='black')
        ax.hlines(y=-D/2, xmin=0, xmax=x1, linewidth=4, color='black')

        ax.vlines(x=x1+x2, ymin=-D/2, ymax=1.5*(y1+y2), linewidth=3, color='black')
        ax.hlines(y=0, xmin=0, xmax=x1+x2, linestyles='dotted',color='black')

        #distance note
        # x1
        ax.plot((0,x1),(-1.3*D/2,-1.3*D/2), 'gray',) # arrow line
        ax.plot((0,0),(-1.3*D/2,-1.3*D/2), 'gray', marker='<',) # lower arrowhead
        ax.plot((x1,x1),(-1.3*D/2,-1.3*D/2), 'gray', marker='>',) # upper arrowhead
        ax.text(x1/2.5,-1.5*D/2,"x1={}".format(x1))

        #x2
        ax.plot((x1,x2+x1),(-1.3*D/2,-1.3*D/2), 'gray',) # arrow line
        ax.plot((x1,x1),(-1.3*D/2,-1.3*D/2), 'gray', marker='<',) # lower arrowhead
        ax.plot((x2+x1,x2+x1),(-1.3*D/2,-1.3*D/2), 'gray', marker='>',) # upper arrowhead
        ax.text(x1+x2/2.5,-1.5*D/2,"x2={}".format(x2))

        #D
        ax.plot((-0.1,-0.1),(-D/2,D/2), 'gray',) # arrow line
        ax.plot((-0.1,-0.1),(-D/2,-D/2), 'gray', marker='v',) # lower arrowhead
        ax.plot((-0.1,-0.1),(D/2,D/2), 'gray', marker='^',) # upper arrowhead
        ax.text(-0.15,-D/10,"D={}".format(D),rotation=90)

        # Display the plot in Streamlit
        st.pyplot(fig)


    
