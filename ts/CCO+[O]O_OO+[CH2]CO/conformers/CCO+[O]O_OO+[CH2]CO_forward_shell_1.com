%nprocshared=20
%mem=5GB
#p m062x/cc-pVTZ Opt=(ModRedun,Loose,maxcycles=900) Int(Grid=SG1) scf=(maxcycle=900) 

Gaussian input prepared by ASE

0 2
O                -5.5015679115        0.9867233723        7.6389317097
O                -2.1018067177        2.1907665579        6.4037719144
O                -2.6761779255        2.4042875171        5.2391367631
C                -5.1576508787        2.3093170007        7.3292233330
C                -5.0108881555        2.5762884105        5.8374215568
H                -5.9161761612        3.0129659408        7.7402667188
H                -4.2066781986        2.5362097298        7.8557963965
H                -3.7910905163        2.1229901788        5.4133614520
H                -5.7810088117        2.0559562667        5.2298327773
H                -5.0213215796        3.6642878459        5.6143873393
H                -6.0717970517        0.6564487873        6.8962931596
H                -2.0512553281        3.0934647512        6.8076546682

5 8 F
8 3 F
5 8 3 F
