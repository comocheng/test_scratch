%nprocshared=20
%mem=5GB
#p m062x/cc-pVTZ Opt=(ModRedun,Loose,maxcycles=900) Int(Grid=SG1) scf=(maxcycle=900) 

Gaussian input prepared by ASE

0 2
O                -1.0937066282        3.5587296325       -2.7575128590
O                -0.3844034189        1.6327528055       -0.9007747984
O                 0.3983695908        1.0772535982       -1.8014317398
C                 0.1845060623        4.0213410720       -2.4194117439
C                 1.3070420614        3.0740104700       -2.8160691164
H                 0.3577580197        5.0151669497       -2.8834255196
H                 0.1907740532        4.1713721303       -1.3163925130
H                 1.2469627967        2.8077986588       -3.8926744264
H                 2.2960915308        3.5384331713       -2.6185949874
H                -1.0794736117        3.3604206082       -3.7303510275
H                -1.1400681384        1.9848749494       -1.4357607491
H                 1.2156719633        2.0923758308       -2.2111704303

3 12 F
12 5 F
3 12 5 F

