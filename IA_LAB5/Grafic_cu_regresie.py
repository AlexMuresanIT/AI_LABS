#REGRESIA LINIARA 1
import matplotlib.pyplot as plt
from scipy import stats as st

"""x=[5,7,8,7,2,17,2,9,4,11,12,9,6,11]
y=[99,86,87,88,111,86,103,87,94,78,77,85,86,100]

a,b,r,p,std_err=st.linregress(x,y)
print("panta= ",a,"constanta=",b)
print("r=",r,"p= ",p,"eroarea standard=",std_err)

def linia_y(x):
    return a*x+b

model_matematic=list(map(linia_y,x))
print(model_matematic)

plt.scatter(x,y,color="blue")
plt.plot(x,model_matematic,color="green")
plt.show()"""

#REGRESIE LINIARA 2
x=[5,7,8,7,2,17,2,9,4,11,12,9,6,11]
y=[99,86,87,88,111,86,103,87,94,78,77,85,86,100]

a,b,r,p,std_err=st.linregress(x,y)

def linia_y(x):
    return a*x+b

model_matematic=list(map(linia_y,x))

x_viitor=10
estim_y=linia_y(x_viitor)
print("Estimare=",estim_y)
p1=[x_viitor,0]
p2=[x_viitor,estim_y]
p3=[0,estim_y]

v1=[p1[0],p2[0]]
v2=[p1[1],p2[1]]
v3=[p2[0],p3[0]]
v4=[p2[1],p3[1]]

plt.scatter(x,y,color="blue")
plt.plot(x,model_matematic,"green")
plt.plot(v1,v2,color="green",linestyle="--")
plt.plot(v3,v4,color="green",linestyle="--")
plt.show()
