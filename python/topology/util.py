import numpy as np
# i2r DC resistive loss
def I2R(current,resistance):
    return current*current*resistance
# parallel combination of impedance
def parallel(A,B):
    return A*B/(A+B)
# best E24 resistor to achieve a target ratio
# (1+R1/R2)=target
def rdivE24(target):
    # standard E24 resistors
    E24=np.array([[1.0,1.1,1.2,1.3,1.5,1.6,1.8,2.0,2.2,2.4,2.7,3.0,3.3,3.6,3.9,4.3,4.7,5.1,5.6,6.2,6.8,7.5,8.2,9.1]])
    #E24=np.array([[1.0,1.1,1.2,1.3]])
    Rpref=np.array([[1.0e0,1.0e1,1.0e2,1.0e3,1.0e4,1.0e5,1.0e6]]) # decade option
    idx = np.int_(np.log10(target)) # index the decade based on the log value of ratio for ratio >9.1/1
    E24inv=1.0/E24 # invert standard E24
    #print idx

    rat = 1.0+E24inv.T.dot(E24*Rpref[0,idx]) # compute possible ratio matrix
    ratdiff = np.abs(rat-target) # compute difference between target and ratio matrix

    indices=np.where(ratdiff==ratdiff.min()) # get indices of minimum difference
    return [E24[0,indices[0]],E24[0,indices[1]]] # return resistor values of minimum indices

# type 2 op amp compensator 2 poles, 1 zero
def type2(fp0,fp1,fz1,R1):

    C1 = 1.0/(2.0*3.14*R1*fp0)
    R2 = fp0*R1/fz1
    C2 = fz1/(2.0*3.14*fp0*fp1)

    return C1,R2,C2

def type2OTA(fp0,fp1,fz1,R1):
    return 0
