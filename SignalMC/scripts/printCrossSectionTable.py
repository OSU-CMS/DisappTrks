#!/usr/bin/env python

from OSUT3Analysis.Configuration.Measurement import Measurement
from DisappTrks.SignalMC.signalCrossSecs import *

print "\\begin{tabular}{llll}"
print "  \\hline"
print "  $m (\\Pchipm)$ [$\\GeV$] & $\\sigma (\\Pp\\Pp {\\rightarrow} \\Pchipm \\Pchimp)$ [$\\mathrm{pb}$] & $\\sigma (\\Pp\\Pp {\\rightarrow} \\Pchiz \\Pchipm)$ [$\\mathrm{pb}$] & total $\\sigma$ [$\\mathrm{pb}$] \\\\"
print "  \\hline"

for mass in sorted (signal_cross_sections.keys ()):
  cnX = chargino_neutralino_cross_sections[mass]
  ccX = chargino_chargino_cross_sections[mass]
  totalX = signal_cross_sections[mass]

  cn = Measurement (cnX['value'], cnX['error'])
  cc = Measurement (ccX['value'], ccX['error'])
  total = Measurement (totalX['value'], totalX['error'])

  cn.setUncertainty ((cn.uncertainty () - 1.0) * cn.centralValue ())
  cc.setUncertainty ((cc.uncertainty () - 1.0) * cc.centralValue ())
  total.setUncertainty ((total.uncertainty () - 1.0) * total.centralValue ())

  #cn *= 1.0e3
  #cc *= 1.0e3
  #total *= 1.0e3

  cn.printTeX ()
  cc.printTeX ()
  total.printTeX ()

  print "  $" + str (mass) + "$ & $" + str (cc) + "$ & $" + str (cn) + "$ & $" + str (total) + "$ \\\\"

print "  \\hline"
print "\\end{tabular}"
