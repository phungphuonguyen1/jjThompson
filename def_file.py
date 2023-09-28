import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
def x1_inside(v_x,t):
  return v_x*t

def y1_inside(v_0x,radi,e,bfi,t1,v_ini,d):
  y= 0.5*radi*e*(t1**2)
  #if radi*(x1_inside(v_0x,t1)*bfi)**2>= V:
  if radi*(x1_inside(v_0x,t1)*bfi)**2>= v_ini:
    return d/2
  else:
    return y

# outside Electric_field
def y2_outside(radi,t2,x1,bfield,t1_fi,e,v_ini):
  if radi*(x1*bfield)**2>=v_ini:
    return 0
  else:
    vy_final_inside= radi*e*t1_fi
    return vy_final_inside*t2
  
def x2_outside(v_x,t2):
  return v_x*t2


def path_function(voltage,distance,x_1,x_2,b):
    ELECTRON_CHARGE= 1.6e-19
    ELECTRON_MASS = 9.1e-31
    # Calculate other factors
    ratio =ELECTRON_CHARGE/ELECTRON_MASS
    E_field=voltage/distance
    acceleration1=ratio*E_field
    vx= E_field/b
    t1_final=x_1/vx
    t2_final=x_2/vx
    #calculate y1, y2
    y1=y1_inside(vx,ratio,E_field,b,t1_final,voltage,distance)
    y2=y2_outside(ratio,t2_final,x_1,b,t1_final,E_field,voltage)

    x_array=[]
    y_array=[]
    time_step1=t1_final/3000
    time_step2=t2_final/3000
    for i in range (0,6000):
      if (i<3000):
        time=i*time_step1
        if (ratio*(x1_inside(vx,time)*b)**2>=voltage):
          break
        else:
          x_array.append(x1_inside(vx,time))
          y_array.append(y1_inside(vx,ratio,E_field,b,time,voltage,distance))
      else:
        time=(i-3000)*time_step2
        if(y2==0):
          break
        else:
          x_array.append(x_1+x2_outside(vx,time))
          y_array.append(y1+y2_outside(ratio,time,x_1,b,t1_final,E_field,voltage))
    df = pd.DataFrame({'x': x_array, 'y': y_array})

    #path
    plt.plot(x_array,y_array,"r")

    #note
    plt.text(-0.1,(distance/2)*1.3,'E={} V/m,$x_1$={}m,\n$x_2$={}m,$v_0={}m/s$'.format(E_field,x_1,x_2,vx),fontsize = 12,
             bbox = dict(facecolor = 'lightblue', alpha = 0.5))
    plt.title("Simulation")
    plt.axis("off")

    #facilities
    plt.hlines(y=distance, xmin=0, xmax=x_1, linewidth=4, color='black')
    plt.hlines(y=-distance, xmin=0, xmax=x_1, linewidth=4, color='black')

    plt.vlines(x=x_1+x_2, ymin=-distance, ymax=1.5*(y1_inside(vx,ratio,E_field,b,t1_final)+y2_outside(ratio,t2_final,x_1,b,t1_final,E_field)), linewidth=3, color='black')
    plt.hlines(y=0, xmin=0, xmax=x_1+x_2, linestyles='dotted',color='black')

    #distance note
    # x_1
    plt.plot((0,x_1),(-1.3*distance,-1.3*distance), 'gray',) # arrow line
    plt.plot((0,0),(-1.3*distance,-1.3*distance), 'gray', marker='<',) # lower arrowhead
    plt.plot((x_1,x_1),(-1.3*distance,-1.3*distance), 'gray', marker='>',) # upper arrowhead
    plt.text(x_1/2.5,-1.5*distance,"x_1={}".format(x_1))

    #x_2
    plt.plot((x_1,x_2+x_1),(-1.3*distance/2,-1.3*distance/2), 'gray',) # arrow line
    plt.plot((x_1,x_1),(-1.3*distance/2,-1.3*distance/2), 'gray', marker='<',) # lower arrowhead
    plt.plot((x_2+x_1,x_2+x_1),(-1.3*distance/2,-1.3*distance/2), 'gray', marker='>',) # upper arrowhead
    plt.text(x_1+x_2/2.5,-1.5*distance/2,"x_2={}".format(x_2))

    #D
    plt.plot((-0.1,-0.1),(-distance/2,distance/2), 'gray',) # arrow line
    plt.plot((-0.1,-0.1),(-distance/2,-distance/2), 'gray', marker='v',) # lower arrowhead
    plt.plot((-0.1,-0.1),(distance/2,distance/2), 'gray', marker='^',) # upper arrowhead
    plt.text(-0.15,-distance/10,"D={}".format(distance),rotation=90)

    # v_0
    plt.show()
    #circle1 = plt.Circle((-0.05, 0), D/10, color='r')
    #plt.show()
    return df


# Tunable input
'''V=0.43 # Hieu dien the giua 2 dau ban tu (voltage) # 2-20
D= 0.05 # Khoang cach giua 2 ban tu (meter) # 0.01-0.1
x_1=0.2 # chieu dai ban tu (meter) #
x2= 0.2 # khoang cach den man chan (meter) #
B_field=0.001 # magnetic field (tesla)

m= path_function(V,D,x_1,x2,B_field)
plt.show()
print(m)'''