#include "DisappTrks/StandardAnalysis/plugins/DEdxAnalyzer.h"

DEdxAnalyzer::DEdxAnalyzer (const edm::ParameterSet &cfg) :
  tracks_ (cfg.getParameter<edm::InputTag> ("tracks")),
  dEdx_ (cfg.getParameter<edm::InputTag> ("dEdx"))
{
  vector<double> pLogBins, dEdxLogBins;
  logSpace (200, 1.0, 2.3, pLogBins);
  logSpace (200, -1.0, 1.0, dEdxLogBins);

  TH1::SetDefaultSumw2();
  twoDHists_["dedxVsP"] = fs_->make<TH2D> ("dedxVsP", ";p [GeV];#LTdE/dx#GT [MeV/cm]", 200, 0.0, 200.0, 200, 0.0, 10.0);
  twoDHists_["dedxVsPLog"] = fs_->make<TH2D> ("dedxVsPLog", ";p [GeV];#LTdE/dx#GT [MeV/cm]", pLogBins.size () - 1, pLogBins.data (), 200, 0.0, 10.0);
  twoDHists_["dedxLogVsP"] = fs_->make<TH2D> ("dedxLogVsP", ";p [GeV];#LTdE/dx#GT [MeV/cm]", 200, 0.0, 200.0, dEdxLogBins.size () - 1, dEdxLogBins.data ());
  twoDHists_["dedxLogVsPLog"] = fs_->make<TH2D> ("dedxLogVsPLog", ";p [GeV];#LTdE/dx#GT [MeV/cm]", pLogBins.size () - 1, pLogBins.data (), dEdxLogBins.size () - 1, dEdxLogBins.data ());

  tracksToken_ = consumes<vector<reco::Track> > (tracks_);
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
  edm::Handle<edm::ValueMap<reco::DeDxData> > dEdx;
  event.getByToken (dEdxToken_, dEdx);

  for (unsigned i = 0; i < tracks->size (); i++)
    {
      const edm::Ref<vector<reco::Track> > trackRef (tracks, i);
      const reco::DeDxData &dEdxData = (*dEdx)[trackRef];

      twoDHists_.at ("dedxVsP")->Fill (trackRef->p (), dEdxData.dEdx ());
      twoDHists_.at ("dedxVsPLog")->Fill (trackRef->p (), dEdxData.dEdx ());
      twoDHists_.at ("dedxLogVsP")->Fill (trackRef->p (), dEdxData.dEdx ());
      twoDHists_.at ("dedxLogVsPLog")->Fill (trackRef->p (), dEdxData.dEdx ());
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

DEFINE_FWK_MODULE (DEdxAnalyzer);
