%nprocshared=20
%mem=5GB
#p m062x/cc-pVTZ Opt=(ModRedun,Loose,maxcycles=900) Int(Grid=SG1) scf=(maxcycle=900) 

Gaussian input prepared by ASE

0 2
O                -5.9996237853        0.7365130250        8.0934638519
O                -3.4663489210       -0.4372934546        8.8221747712
O                -3.0242228537        0.6326981027        9.4478832718
C                -5.4301967042        1.9390799409        7.6541032689
C                -4.3732433010        2.4581065739        8.6193734009
H                -4.9823393131        1.7969850904        6.6448104913
H                -6.2253946542        2.7057576884        7.5401998369
H                -3.3920442035        1.5196123551        8.7916797335
H                -3.8926245073        3.3864960574        8.2450820278
H                -4.7773064839        2.6214087306        9.6409707971
H                -6.6273993400        0.4469775031        7.3808478091
H                -4.3488315695       -0.6041941957        9.2391990723

5 8 F
8 3 F
5 8 3 F

