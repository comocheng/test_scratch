%nprocshared=20
%mem=5GB
#p m062x/cc-pVTZ opt=(ts,calcfc,noeigentest,maxcycles=900) freq scf=(maxcycle=900) IOP(7/33=1,2/16=3) 

Gaussian input prepared by ASE

0 2
O                 0.9944890000       -1.0295300000       -0.5032380000
O                -1.5728100000       -0.6080300000        0.4633420000
O                -1.5423100000        0.4689550000       -0.4051360000
C                 1.2944280000        0.0009320000        0.4351960000
C                 0.7012190000        1.2872860000       -0.0372880000
H                 0.8992760000       -0.2567830000        1.4231760000
H                 2.3824470000        0.1143590000        0.5285210000
H                -0.6583230000        1.1296230000       -0.0382620000
H                 0.8700380000        2.1221180000        0.6378070000
H                 0.8982450000        1.5180070000       -1.0795670000
H                 1.5635140000       -1.7820020000       -0.3266600000
H                -0.9640270000       -1.2257940000        0.0278000000


