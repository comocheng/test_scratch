%nprocshared=20
%mem=5GB
#p m062x/cc-pVTZ opt=(calcfc,maxcycles=900) freq IOP(7/33=1,2/16=3) scf=(maxcycle=900) 

Gaussian input prepared by ASE

0 2
O                -1.1168690561       -0.0498555829        1.1220790719
C                -0.2142128540       -0.4671144783        0.1301755459
C                 0.1650604872        0.6092462846       -0.8779213745
H                 0.6806686578       -0.8549726478        0.6439828738
H                -0.6317039701       -1.3271242236       -0.4357948032
H                 0.5513527823        0.2706144942       -1.8435371072
H                -0.4104544090        1.5381759872       -0.9078458121
H                -1.7836698538        0.5237731865        0.6814644771



