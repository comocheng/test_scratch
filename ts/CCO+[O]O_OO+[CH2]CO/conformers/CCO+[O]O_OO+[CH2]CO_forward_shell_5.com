%nprocshared=20
%mem=5GB
#p m062x/cc-pVTZ Opt=(ModRedun,Loose,maxcycles=900) Int(Grid=SG1) scf=(maxcycle=900) 

Gaussian input prepared by ASE

0 2
O                -2.6156828507        0.1305973189        0.8447057638
O                 0.0471479896        1.4240872245        3.9236109952
O                -0.5726367246        0.6957047059        3.0195921322
C                -1.9681024134        1.1387991277        0.1184316352
C                -0.8930055176        1.8692469478        0.9114873120
H                -1.5201556540        0.6863146836       -0.7949441410
H                -2.7287080778        1.8658735164       -0.2363352129
H                -0.9294742644        1.4619162195        2.2176966361
H                -1.0367880017        2.9702346002        0.9394734992
H                 0.1404638424        1.6142129932        0.5954091348
H                -2.1998283769        0.1029347257        1.7458751417
H                 1.0027416979        1.3591482351        3.6722174345

5 8 F
8 3 F
5 8 3 F

