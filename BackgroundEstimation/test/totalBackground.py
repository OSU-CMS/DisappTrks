#!/usr/bin/env python

import math

from bkgdEstimate_2015 import nLeptons as nLeptons2015
from bkgdEstimate_2015 import nLeptonsError as nLeptonsError2015
from bkgdEstimate_2015 import nFakes as nFakes2015
from bkgdEstimate_2015 import nTotal as nTotal2015
from bkgdEstimate_2015 import nTotalError as nTotalError2015

from bkgdEstimate_2016 import nLeptons as nLeptons2016
from bkgdEstimate_2016 import nLeptonsError as nLeptonsError2016
from bkgdEstimate_2016 import nFakes as nFakes2016
from bkgdEstimate_2016 import nTotal as nTotal2016
from bkgdEstimate_2016 import nTotalError as nTotalError2016

totalLepton  =  nLeptons2015      +  nLeptons2016["BC"]      +  nLeptons2016["DEFGH"]
totalFake    =  nFakes2015[0]  +  nFakes2016["BC"][0]  +  nFakes2016["DEFGH"][0]
totalTotal   =  nTotal2015        +  nTotal2016["BC"]        +  nTotal2016["DEFGH"]
totalLeptonError  =  math.hypot  (math.hypot  (nLeptonsError2015,  nLeptonsError2016["BC"]),  nLeptonsError2016["DEFGH"])
totalFakeError    =  math.hypot  (math.hypot  (nFakes2015[1],   nFakes2016["BC"][1]),   nFakes2016["DEFGH"][1])
totalTotalError   =  math.hypot  (math.hypot  (nTotalError2015,    nTotalError2016["BC"]),    nTotalError2016["DEFGH"])

print "Total lepton background: " + str (totalLepton) + " +- " + str (totalLeptonError)
print "Total fake background:   " + str (totalFake) + " +- " + str (totalFakeError)
print "Total total:             " + str (totalTotal) + " +- " + str (totalTotalError)
