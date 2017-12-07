#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/MuonReco/interface/MuonSelectors.h"

#include "DisappTrks/StandardAnalysis/plugins/DEdxAnalyzer.h"

DEdxAnalyzer::DEdxAnalyzer (const edm::ParameterSet &cfg) :
  tracks_ (cfg.getParameter<edm::InputTag> ("tracks")),
  electrons_ (cfg.getParameter<edm::InputTag> ("electrons")),
  muons_ (cfg.getParameter<edm::InputTag> ("muons")),
  dEdx_ (cfg.getParameter<edm::InputTag> ("dEdx")),
  minPt_ (cfg.getParameter<double> ("minPt")),
  vetoElectronsOrMuons_ (cfg.getParameter<string> ("vetoElectronsOrMuons"))
{
  vector<double> pLogBins, dEdxLogBins;
  logSpace (200, 1.0, 3.3, pLogBins);
  logSpace (200, -1.0, 1.0, dEdxLogBins);

  TH1::SetDefaultSumw2();
  twoDHists_["dedxVsP"] = fs_->make<TH2D> ("dedxVsP", ";p [GeV];#LTdE/dx#GT [MeV/cm]", 200, 0.0, 200.0, 200, 0.0, 10.0);
  twoDHists_["dedxVsPLog"] = fs_->make<TH2D> ("dedxVsPLog", ";p [GeV];#LTdE/dx#GT [MeV/cm]", pLogBins.size () - 1, pLogBins.data (), 200, 0.0, 10.0);
  twoDHists_["dedxLogVsP"] = fs_->make<TH2D> ("dedxLogVsP", ";p [GeV];#LTdE/dx#GT [MeV/cm]", 200, 0.0, 200.0, dEdxLogBins.size () - 1, dEdxLogBins.data ());
  twoDHists_["dedxLogVsPLog"] = fs_->make<TH2D> ("dedxLogVsPLog", ";p [GeV];#LTdE/dx#GT [MeV/cm]", pLogBins.size () - 1, pLogBins.data (), dEdxLogBins.size () - 1, dEdxLogBins.data ());

  tracksToken_ = consumes<vector<reco::Track> > (tracks_);
  electronsToken_ = consumes<vector<reco::GsfElectron> > (electrons_);
  muonsToken_ = consumes<vector<reco::Muon> > (muons_);
  dEdxToken_ = consumes<edm::ValueMap<reco::DeDxData> > (dEdx_);
}

DEdxAnalyzer::~DEdxAnalyzer ()
{
}

void
DEdxAnalyzer::analyze (const edm::Event &event, const edm::EventSetup &setup)
{
  edm::Handle<vector<reco::Track> > tracks;
  event.getByToken (tracksToken_, tracks);
  edm::Handle<vector<reco::GsfElectron> > electrons;
  event.getByToken (electronsToken_, electrons);
  edm::Handle<vector<reco::Muon> > muons;
  event.getByToken (muonsToken_, muons);
  edm::Handle<edm::ValueMap<reco::DeDxData> > dEdx;
  event.getByToken (dEdxToken_, dEdx);

  vector<SlimTrack> selectedTracks;
  for (unsigned i = 0; i < tracks->size (); i++)
    {
      const edm::Ref<vector<reco::Track> > trackRef (tracks, i);
      const reco::DeDxData &dEdxData = (*dEdx)[trackRef];

      if (trackRef->pt () < minPt_)
        continue;
      if (vetoElectronsOrMuons_ == "electrons" && isNearElectron (*trackRef, *electrons))
        continue;
      if (vetoElectronsOrMuons_ == "muons" && isNearMuon (*trackRef, *muons))
        continue;
      if (vetoElectronsOrMuons_ == "both" && (isNearElectron (*trackRef, *electrons) || isNearMuon (*trackRef, *muons)))
        continue;

      selectedTracks.push_back (SlimTrack (*trackRef, dEdxData.dEdx ()));

    }
  clog << "found " << selectedTracks.size () << " tracks in " << event.id () << endl;
  if (selectedTracks.empty ())
    return;

  /*unsigned selectedIndex = 0;
  if (selectedTracks.size () > 1)
    {
      do
        {
          if (selectedIndex > selectedTracks.size () - 1)
            clog << endl << "try again..." << endl;
          for (unsigned i = 0; i < selectedTracks.size (); i++)
            {
              const SlimTrack &track = selectedTracks.at (i);
              clog << "  (" << setw (2) << i << ") pt: " << track.pt << " GeV, eta: " << track.eta << ", phi: " << track.phi << endl;
            }
          clog << "which track would you like to plot?: ";
          cin >> selectedIndex;
        }
      while (selectedIndex > selectedTracks.size () - 1);
    }
  const SlimTrack &selectedTrack = selectedTracks.at (selectedIndex);*/

  for (const auto &selectedTrack : selectedTracks)
    {
      twoDHists_.at ("dedxVsP")->Fill (selectedTrack.p, selectedTrack.dEdx);
      twoDHists_.at ("dedxVsPLog")->Fill (selectedTrack.p, selectedTrack.dEdx);
      twoDHists_.at ("dedxLogVsP")->Fill (selectedTrack.p, selectedTrack.dEdx);
      twoDHists_.at ("dedxLogVsPLog")->Fill (selectedTrack.p, selectedTrack.dEdx);
    }
}

void
DEdxAnalyzer::logSpace (const unsigned n, const double a, const double b, vector<double> &bins) const
{
  double step = (b - a) / ((double) n);

  bins.clear ();
  for (double i = a; i < b + 0.5 * step; i += step)
    bins.push_back (pow (10.0, i));
}

bool
DEdxAnalyzer::isNearElectron (const reco::Track &track, const vector<reco::GsfElectron> &leptons) const
{
  for (const auto &lepton : leptons)
    {
      if (deltaR (track, lepton) < 0.15)
        return true;
    }
  return false;
}

bool
DEdxAnalyzer::isNearMuon (const reco::Track &track, const vector<reco::Muon> &leptons) const
{
  for (const auto &lepton : leptons)
    {
      if (!muon::isLooseMuon (lepton))
        continue;
      if (deltaR (track, lepton) < 0.15)
        return true;
    }
  return false;
}

DEFINE_FWK_MODULE (DEdxAnalyzer);
