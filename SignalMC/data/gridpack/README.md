# How to create new gridpacks

The first step is to clone the genproductions repository in your home folder with (to use the gridpack generation script, no CMSSW environment can be defined)

`git clone https://github.com/cms-sw/genproductions.git`

After that, copy the folders in **~/CMSSW_VERSION/src/DisappTrks/SignalMC/data/gridpack/** to **~/genproductions/bin/MadGraph5_aMCatNLO/cards/** (you can create a folder
called AMSB_processes in **~/genproductions/bin/MadGraph5_aMCatNLO/cards/** and save the gridpack cards folders inside it). A small modification in line 176 of file
runcmsgrid_LO.sh is needed, otherwise the LHE file will not save the particles' time of flight. 
Just change `./madevent/bin/madevent add_time_of_flight events.lhe.gz` to `./madevent/bin/madevent add_time_of_flight events.lhe` (apparently it is not needed
anymore since it was already changed in the repository https://github.com/cms-sw/genproductions/pull/3070; nevertheless, it is always a good idea to check).

After performing the step above, go into the MadGraph5_aMCatNLO folder `cd ~/genproductions/bin/MadGraph5_aMCatNLO`, and use the command below to generate the
gridpack:

`./gridpack_generation.sh <name of process card without _proc_card.dat> <folder containing cards relative to current location>`

e.g.

`./gridpack_generation.sh AMSB_chargino_M700GeV_ctau100cm cards/AMSB_processes/100cm/AMSB_chargino_M700GeV_ctau100cm`

Wait for a while and the gridpack compressed file will be inside **~/genproductions/bin/MadGraph5_aMCatNLO**.
