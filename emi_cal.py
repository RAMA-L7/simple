def emi_cal(p,r,t):
    r=r/(12*100)#one month intrest
    t=t*12#one month period
    emi=(p*r*pow(1+r,t))/(pow(1+r,t)-1)
    return emi

#driver code
principal =10000;
rate= 10;
time=2;
emi=emi_cal(principal,rate,time);
print("Monthly EMI is=",emi )