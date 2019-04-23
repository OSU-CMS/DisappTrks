#! /
import sys

mChargino = sys.argv[1]
mNeutralino = sys.argv[2]
ctau = sys.argv[3]

slha_file_name = "FakeDecay_chargino_"+mChargino+"GeV_neutralino_" + mNeutralino + "GeV_Isajet780.slha"
slha_file = open("Fakedecay_SLHA/"+slha_file_name,"w+")

slha_file.write(
'''
#  ISAJET SUSY parameters in SUSY Les Houches Accord 2 format
#  Created by ISALHA 2.0 Last revision: C. Balazs 21 Apr 2009
Block SPINFO   # Program information
     1   ISASUGRA from ISAJET          # Spectrum Calculator
     2   7.80   29-OCT-2009 12:50:36   # Version number
Block MODSEL   # Model selection
     1     3   # Minimal anomaly mediated (AMSB) model
Block SMINPUTS   # Standard Model inputs
     1     1.27843697E+02   # alpha_em^(-1)
     2     1.16570000E-05   # G_Fermi
     3     1.17200002E-01   # alpha_s(M_Z)
     4     9.11699982E+01   # m_{Z}(pole)
     5     4.19999981E+00   # m_{b}(m_{b})
     6     1.73070007E+02   # m_{top}(pole)
     7     1.77699995E+00   # m_{tau}(pole)
Block MINPAR   # SUSY breaking input parameters
     1     1.50000000E+03   # m_0
     2     3.50800000E+04   # m_{3/2}
     3     5.00000000E+00   # tan(beta)
     4     1.00000000E+00   # sign(mu)
Block EXTPAR   # Non-universal SUSY breaking parameters
     0     1.26820216E+16   # Input scale
Block MASS   # Scalar and gaugino mass spectrum
#  PDG code   mass                 particle
        24     8.04229965E+01   #  W^+
        25     1.09165016E+02   #  h^0
        35     1.69811304E+03   #  H^0
        36     1.68658362E+03   #  A^0
        37     1.69844373E+03   #  H^+
   1000001     1.64875269E+03   #  dnl
   1000002     1.64692371E+03   #  upl
   1000003     1.64875269E+03   #  stl
   1000004     1.64692432E+03   #  chl
   1000005     1.36096313E+03   #  b1
   1000006     1.00422571E+03   #  t1
   1000011     1.49030664E+03   #  el-
   1000012     1.48858191E+03   #  nuel
   1000013     1.49030664E+03   #  mul-
   1000014     1.48858191E+03   #  numl
   1000015     1.48539880E+03   #  tau1
   1000016     1.48676428E+03   #  nutl
   1000021     8.64298706E+02   #  glss '''
+
'''
   1000022     %.8E   #  z1ss ''' %float(mNeutralino)
+
'''
   1000023     3.20083069E+02   #  z2ss'''
+
'''
   1000024     %.8E   #  w1ss ''' %float(mChargino)
+
'''
   1000025    -7.42030518E+02   #  z3ss
   1000035     7.49072571E+02   #  z4ss
   1000037     7.49086609E+02   #  w2ss
   2000001     1.65904858E+03   #  dnr
   2000002     1.65516052E+03   #  upr
   2000003     1.65904858E+03   #  str
   2000004     1.65516113E+03   #  chr
   2000005     1.65050024E+03   #  b2
   2000006     1.37387744E+03   #  t2
   2000011     1.49084143E+03   #  er-
   2000013     1.49084143E+03   #  mur-
   2000015     1.48991235E+03   #  tau2
Block ALPHA   # Effective Higgs mixing parameter
         -1.98805586E-01   # alpha
Block STOPMIX   # stop mixing matrix
  1  1     6.12325780E-02   # O_{11}
  1  2    -9.98123527E-01   # O_{12}
  2  1     9.98123527E-01   # O_{21}
  2  2     6.12325780E-02   # O_{22}
Block SBOTMIX   # sbottom mixing matrix
  1  1     9.99970913E-01   # O_{11}
  1  2     7.62549881E-03   # O_{12}
  2  1    -7.62549881E-03   # O_{21}
  2  2     9.99970913E-01   # O_{22}
Block STAUMIX   # stau mixing matrix
  1  1     5.97260058E-01   # O_{11}
  1  2     8.02047670E-01   # O_{12}
  2  1    -8.02047670E-01   # O_{21}
  2  2     5.97260058E-01   # O_{22}
Block NMIX   # neutralino mixing matrix
  1  1     1.02890544E-02   #
  1  2    -9.93297398E-01   #
  1  3     1.09105095E-01   #
  1  4    -3.67495306E-02   #
  2  1    -9.96177256E-01   #
  2  2    -1.99755784E-02   #
  2  3    -7.35215694E-02   #
  2  4     4.27322201E-02   #
  3  1     2.25971118E-02   #
  3  2    -5.08868955E-02   #
  3  3    -7.03913569E-01   #
  3  4    -7.08099306E-01   #
  4  1     8.37496892E-02   #
  4  2    -1.01842113E-01   #
  4  3    -6.97993875E-01   #
  4  4     7.03859687E-01   #
Block UMIX   # chargino U mixing matrix
  1  1    -9.88591433E-01   # U_{11}
  1  2     1.50621936E-01   # U_{12}
  2  1    -1.50621936E-01   # U_{21}
  2  2    -9.88591433E-01   # U_{22}
Block VMIX   # chargino V mixing matrix
  1  1    -9.98679578E-01   # V_{11}
  1  2     5.13723604E-02   # V_{12}
  2  1    -5.13723604E-02   # V_{21}
  2  2    -9.98679578E-01   # V_{22}
Block GAUGE Q=  1.13725037E+03   #
     1     3.57492119E-01   # g`
     2     6.52496159E-01   # g_2
     3     1.22099471E+00   # g_3
Block YU Q=  1.13725037E+03   #
  3  3     8.78648043E-01   # y_t
Block YD Q=  1.13725037E+03   #
  3  3     6.93556666E-02   # y_b
Block YE Q=  1.13725037E+03   #
  3  3     5.13891652E-02   # y_tau
Block HMIX Q=  1.13725037E+03   # Higgs mixing parameters
     1     7.33976440E+02   # mu(Q)
     2     5.00000000E+00   # tan(beta)(M_GUT)
     3     2.51144409E+02   # Higgs vev at Q
     4     2.84456425E+06   # m_A^2(Q)
Block MSOFT Q=  1.13725037E+03   # DRbar SUSY breaking parameters
     1     3.23079498E+02   # M_1(Q)
     2     9.78689346E+01   # M_2(Q)
     3    -7.54845886E+02   # M_3(Q)
    31     1.48517932E+03   # MeL(Q)
    32     1.48517932E+03   # MmuL(Q)
    33     1.48340161E+03   # MtauL(Q)
    34     1.48875891E+03   # MeR(Q)
    35     1.48875891E+03   # MmuR(Q)
    36     1.48529724E+03   # MtauR(Q)
    41     1.61164856E+03   # MqL1(Q)
    42     1.61164856E+03   # MqL2(Q)
    43     1.33004492E+03   # MqL3(Q)
    44     1.61942517E+03   # MuR(Q)
    45     1.61942517E+03   # McR(Q)
    46     9.72402039E+02   # MtR(Q)
    47     1.62276147E+03   # MdR(Q)
    48     1.62276147E+03   # MsR(Q)
    49     1.62246484E+03   # MbR(Q)
Block AU Q=  1.13725037E+03   #
  1  1     6.08556396E+02   # A_u
  2  2     6.08556396E+02   # A_c
  3  3     6.08556396E+02   # A_t
Block AD Q=  1.13725037E+03   #
  1  1     1.45460706E+03   # A_d
  2  2     1.45460706E+03   # A_s
  3  3     1.45460706E+03   # A_b
Block AE Q=  1.13725037E+03   #
  1  1     3.71930389E+02   # A_e
  2  2     3.71930389E+02   # A_mu
  3  3     3.71930389E+02   # A_tau
'''
)

slha_file.close()


decay_file_name = "geant4_chargino_" + mChargino + "GeV_ctau_" + ctau + "cm_neutralino_" + mNeutralino + "GeV_3bd.slha"
decay_file = open("geant4_fakedecay/"+decay_file_name,"w+")

c = 29.979245800  #cm/ns
width = 1.97326979e-14/float(ctau)

decay_file.write(
'''
# This file is read by SimG4Core/CustomPhysics/src/CustomParticleFactory.cc
# The strings "decay", "pdg code", and "block", with correct capitalization, are used
# to control the data input, so do not use these in any comments.
#
#
# Get values for chargino and neutralino masses from:
# 
BLOCK MASS
#  PDG code   mass   particle
   1000022   %.8E   # ~neutrailino(1)
   1000024   %.8E   # ~chargino(1)+
  -1000024   %.8E   # ~chargino(1)-

Block



# Set chargino lifetime
# and decay:  chargino -> neutralino + neutralino + mu
# chargino ctau  = %d cm
# chargino  tau  = %.11e ns
# chargino width = %.11e GeV
#       PDG       Width               #
DECAY  1000024  %.11e # +chargino decay
#   BR       NDA      ID1      ID2      ID3
   1.0000    3     1000022     -13      1000022
Block


#       PDG       Width               #
DECAY  -1000024  %.11e # -chargino decay
#   BR       NDA      ID1      ID2      ID3
   1.0000    3     1000022     13       1000022
Block


EOF
'''  % (  float(mNeutralino) , float(mChargino) , float(mChargino) , int(ctau) , float(ctau)/c , width , width , width) )
decay_file.close()
