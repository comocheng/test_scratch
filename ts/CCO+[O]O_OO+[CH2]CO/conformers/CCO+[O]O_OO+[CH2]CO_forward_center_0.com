%nprocshared=20
%mem=5GB
#p m062x/cc-pVTZ Opt=(ts,calcfc,noeigentest,ModRedun,maxcycles=900) scf=(maxcycle=900) 

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

1 2 F
1 4 F
1 6 F
1 7 F
1 9 F
1 10 F
1 11 F
1 12 F
2 4 F
2 6 F
2 7 F
2 9 F
2 10 F
2 11 F
2 12 F
4 6 F
4 7 F
4 9 F
4 10 F
4 11 F
4 12 F
6 7 F
6 9 F
6 10 F
6 11 F
6 12 F
7 9 F
7 10 F
7 11 F
7 12 F
9 10 F
9 11 F
9 12 F
10 11 F
10 12 F
11 12 F

