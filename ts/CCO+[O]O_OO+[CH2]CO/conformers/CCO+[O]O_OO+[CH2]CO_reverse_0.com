%nprocshared=20
%mem=5GB
#p m062x/cc-pVTZ opt=(ts,calcfc,noeigentest,maxcycles=900) freq scf=(maxcycle=900) IOP(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 2
O                -0.8242300000       -1.1865570000       -0.3932570000
O                 1.6109360000       -0.4585640000        0.4631710000
O                 1.4666460000        0.5432680000       -0.4021530000
C                -1.3012730000       -0.1198090000        0.4338300000
C                -0.8191060000        1.2356860000       -0.0305250000
H                -2.3932090000       -0.1559300000        0.4797550000
H                -0.9213830000       -0.3380280000        1.4317890000
H                -1.1620590000        1.4500610000       -1.0450130000
H                -1.1735060000        2.0244850000        0.6327130000
H                -0.9878120000       -0.9555400000       -1.3122730000
H                 0.9963460000       -1.1384540000        0.1145270000
H                 0.3370810000        1.2329610000       -0.0634070000



