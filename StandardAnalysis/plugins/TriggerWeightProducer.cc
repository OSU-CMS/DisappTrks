#ifndef TRIGGER_WEIGHT_PRODUCER
#define TRIGGER_WEIGHT_PRODUCER

#include <unordered_map>
#include <string>
#include <unordered_set>
#include <vector>

#include "FWCore/Common/interface/TriggerNames.h"

#include "OSUT3Analysis/AnaTools/interface/EventVariableProducer.h"
#include "OSUT3Analysis/Collections/interface/DisappearingTrack.h"

#include "TFile.h"
#include "TGraphAsymmErrors.h"
#include "TVector2.h"
#include "TString.h"

class TriggerWeightProducer : public EventVariableProducer
{
public:
  TriggerWeightProducer(const edm::ParameterSet &);
  ~TriggerWeightProducer();

private:
  edm::EDGetTokenT<vector<TYPE(mets)> > metsToken_;
  edm::EDGetTokenT<vector<TYPE(muons)> > muonsToken_;
  edm::EDGetTokenT<vector<osu::Track> > tracksToken_;
  edm::EDGetTokenT<TYPE(triggers)> triggersToken_;

  string efficiencyFile_;
  string dataset_;
  string target_;

  edm::ParameterSetID triggerNamesPSetID_;
  unordered_map<string, unordered_set<unsigned> > triggerIndices_;
  vector<string> inclusiveMetTriggers_;

  bool produceMetLeg_;
  bool produceTrackLeg_;
  bool produceGrandOr_;

  TGraphAsymmErrors * metLegNumerator_;
  TGraphAsymmErrors * metLegDenominator_;
  TGraphAsymmErrors * trackLegNumerator_;
  TGraphAsymmErrors * trackLegDenominator_;
  TGraphAsymmErrors * grandOrNumerator_;
  TGraphAsymmErrors * grandOrDenominator_;

  bool isFirstEvent_;

  void FindEfficiency(TGraphAsymmErrors *, double, double &, double &, double &);
  const TVector2 getPFMETNoMu(const vector<TYPE(mets)> &, const vector<TYPE(muons)> &) const;
  const osu::Track &getLeadTrack (const vector<osu::Track> &) const;
  bool passesInclusiveMetTriggers (const edm::Event &, const edm::TriggerResults &);

  void AddVariables(const edm::Event &, const edm::EventSetup &);
};

TriggerWeightProducer::TriggerWeightProducer(const edm::ParameterSet &cfg) :
  EventVariableProducer (cfg),
  efficiencyFile_       (cfg.getParameter<edm::FileInPath> ("efficiencyFile").fullPath()),
  dataset_              (cfg.getParameter<string> ("dataset")),
  target_               (cfg.getParameter<string> ("target")),
  inclusiveMetTriggers_ (cfg.getParameter<vector<string> > ("inclusiveMetTriggers")),
  produceMetLeg_        (cfg.getParameter<bool> ("produceMetLeg")),
  produceTrackLeg_      (cfg.getParameter<bool> ("produceTrackLeg")),
  produceGrandOr_       (cfg.getParameter<bool> ("produceGrandOr")),
  metLegNumerator_      (NULL),
  metLegDenominator_    (NULL),
  trackLegNumerator_    (NULL),
  trackLegDenominator_  (NULL),
  grandOrNumerator_     (NULL),
  grandOrDenominator_   (NULL),
  isFirstEvent_         (true)
{
  metsToken_            = consumes<vector<TYPE(mets)> >  (collections_.getParameter<edm::InputTag> ("mets"));
  muonsToken_           = consumes<vector<TYPE(muons)> > (collections_.getParameter<edm::InputTag> ("muons"));
  tracksToken_          = consumes<vector<osu::Track> >  (collections_.getParameter<edm::InputTag> ("tracks"));
  triggersToken_        = consumes<TYPE(triggers)>       (collections_.getParameter<edm::InputTag> ("triggers"));

  triggerNamesPSetID_.reset ();
  triggerIndices_.clear ();
}

TriggerWeightProducer::~TriggerWeightProducer()
{
  if (metLegNumerator_)
    delete metLegNumerator_;
  if (metLegDenominator_)
    delete metLegDenominator_;
  if (trackLegNumerator_)
    delete trackLegNumerator_;
  if (trackLegDenominator_)
    delete trackLegDenominator_;
  if (grandOrNumerator_)
    delete grandOrNumerator_;
  if (grandOrDenominator_)
    delete grandOrDenominator_;
}

void TriggerWeightProducer::AddVariables(const edm::Event &event, const edm::EventSetup &setup) {

  if(!produceMetLeg_ && !produceTrackLeg_ && !produceGrandOr_) {
    if(isFirstEvent_) {
      clog << "[TriggerWeightProducer] No weights requested to be produced. Moving on!" << endl;
      isFirstEvent_ = false;
    }
    return;
  }

  if(event.isRealData() || efficiencyFile_ == "" || dataset_ == "" || target_ == "") {
    if (isFirstEvent_) {
      clog << "[TriggerWeightProducer] NOT applying trigger reweighting (isRealData: " << (event.isRealData () ? "true" : "false")
           << ", efficiencyFile_: \"" << efficiencyFile_
           << "\", dataset_: \"" << dataset_
           << "\", target_: \"" << target_ << "\")" << endl;
      isFirstEvent_ = false;
    }

    if(produceMetLeg_) {
      (*eventvariables)["metLegWeight"] = 1;
      (*eventvariables)["metLegWeightMCUp"] = 1;
      (*eventvariables)["metLegWeightMCDown"] = 1;
      (*eventvariables)["metLegWeightDataUp"] = 1;
      (*eventvariables)["metLegWeightDataDown"] = 1;
    }

    if(produceTrackLeg_) {
      (*eventvariables)["trackLegWeight"] = 1;
      (*eventvariables)["trackLegWeightMCUp"] = 1;
      (*eventvariables)["trackLegWeightMCDown"] = 1;
      (*eventvariables)["trackLegWeightDataUp"] = 1;
      (*eventvariables)["trackLegWeightDataDown"] = 1;
    }

    if(produceGrandOr_) {
      (*eventvariables)["grandOrWeight"] = 1;
      (*eventvariables)["grandOrWeightMCUp"] = 1;
      (*eventvariables)["grandOrWeightMCDown"] = 1;
      (*eventvariables)["grandOrWeightDataUp"] = 1;
      (*eventvariables)["grandOrWeightDataDown"] = 1;
    }

    return;
  }

  if (isFirstEvent_) {
    TFile * fin = TFile::Open(efficiencyFile_.c_str());
    if(!fin || fin->IsZombie()) {
      clog << "ERROR [TriggerWeightProducer]: Could not find file: " << efficiencyFile_
           << "; would cause a seg fault." << endl;
      exit(1);
    }

    if(produceMetLeg_) {
      metLegNumerator_   = (TGraphAsymmErrors*)fin->Get((TString)dataset_ + "/metLeg");
      metLegDenominator_ = (TGraphAsymmErrors*)fin->Get((TString)target_ + "/metLeg");
      if(!metLegNumerator_   || !metLegDenominator_) {
        clog << "ERROR [TriggerWeightProducer]: Could not find requested MetLeg efficiency graphs: " << endl
           << "\t" << dataset_ << "/metLeg," << endl
           << "\t" << target_ << "/metLeg" << endl
           << "Would cause a seg fault." << endl;
        exit(1);
      }
    }
    if(produceTrackLeg_) {
      trackLegNumerator_   = (TGraphAsymmErrors*)fin->Get((TString)dataset_ + "/trackLeg");
      trackLegDenominator_ = (TGraphAsymmErrors*)fin->Get((TString)target_ + "/trackLeg");
      if(!trackLegNumerator_   || !trackLegDenominator_) {
        clog << "ERROR [TriggerWeightProducer]: Could not find requested TrackLeg efficiency graphs: " << endl
           << "\t" << dataset_ << "/trackLeg," << endl
           << "\t" << target_ << "/trackLeg" << endl
           << "Would cause a seg fault." << endl;
        exit(1);
      }
    }
    if(produceGrandOr_) {
      grandOrNumerator_    = (TGraphAsymmErrors*)fin->Get((TString)dataset_ + "/grandOr");
      grandOrDenominator_  = (TGraphAsymmErrors*)fin->Get((TString)target_ + "/grandOr");
      if(!grandOrNumerator_   || !grandOrDenominator_) {
        clog << "ERROR [TriggerWeightProducer]: Could not find requested GrandOr efficiency graphs: " << endl
           << "\t" << dataset_ << "/grandOr," << endl
           << "\t" << target_ << "/grandOr" << endl
           << "Would cause a seg fault." << endl;
        exit(1);
      }
    }

    fin->Close ();
    delete fin;
  }

  edm::Handle<vector<TYPE(mets)> > mets;
  if(!event.getByToken(metsToken_, mets)) {
    edm::LogWarning ("disappTrks_TriggerWeightProducer") << "Could not find mets collection. Skipping trigger weights...";
    return;
  }

  edm::Handle<vector<TYPE(muons)> > muons;
  if(!event.getByToken(muonsToken_, muons)) {
    edm::LogWarning ("disappTrks_TriggerWeightProducer") << "Could not find muons collection. Skipping trigger weights...";
    return;
  }

  const TVector2 metNoMu = getPFMETNoMu(*mets, *muons);
  double metNoMuPt = metNoMu.Mod();

  double numerator = 0.0, numeratorUp = 0.0, numeratorDown = 0.0;
  double denominator = 0.0, denominatorUp = 0.0, denominatorDown = 0.0;

  // met leg
  if(produceMetLeg_) {
    FindEfficiency(metLegNumerator_, metNoMuPt, numerator, numeratorUp, numeratorDown);
    FindEfficiency(metLegDenominator_, metNoMuPt, denominator, denominatorUp, denominatorDown);

    double metWeight = (denominator > 0) ? numerator / denominator : 0.;
    double metWeightMCUp = (denominatorUp > 0) ? numerator / denominatorUp : 0.;
    double metWeightMCDown = (denominatorDown > 0) ? numerator / denominatorDown : 0.;
    double metWeightDataUp = (denominator > 0) ? numeratorUp / denominator : 0.;
    double metWeightDataDown = (denominator > 0) ? numeratorDown / denominator : 0.;

    (*eventvariables)["metLegWeight"] = metWeight;
    (*eventvariables)["metLegWeightMCUp"] = metWeightMCUp;
    (*eventvariables)["metLegWeightMCDown"] = metWeightMCDown;
    (*eventvariables)["metLegWeightDataUp"] = metWeightDataUp;
    (*eventvariables)["metLegWeightDataDown"] = metWeightDataDown;
  }

  // track leg
  if(produceTrackLeg_) {
    edm::Handle<vector<osu::Track> > tracks;
    if(!event.getByToken(tracksToken_, tracks)) {
      edm::LogWarning ("disappTrks_TriggerWeightProducer") << "Could not find tracks collection. Skipping trigger weights...";
      return;
    }

    edm::Handle<edm::TriggerResults> triggers;;
    if(!event.getByToken(triggersToken_, triggers)) {
      edm::LogWarning ("disappTrks_TriggerWeightProducer") << "Could not find triggers collection. Skipping trigger weights...";
      return;
    }

    double trackWeight = 1.0;
    double trackWeightMCUp = 1.0;
    double trackWeightMCDown = 1.0;
    double trackWeightDataUp = 1.0;
    double trackWeightDataDown = 1.0;

    if (!passesInclusiveMetTriggers (event, *triggers)) {
      if (!tracks->empty ()) {
        const osu::Track &leadTrack = getLeadTrack(*tracks);

        FindEfficiency(trackLegNumerator_, leadTrack.pt (), numerator, numeratorUp, numeratorDown);
        FindEfficiency(trackLegDenominator_, leadTrack.pt (), denominator, denominatorUp, denominatorDown);
      }

      trackWeight = (denominator > 0) ? numerator / denominator : 0.;
      trackWeightMCUp = (denominatorUp > 0) ? numerator / denominatorUp : 0.;
      trackWeightMCDown = (denominatorDown > 0) ? numerator / denominatorDown : 0.;
      trackWeightDataUp = (denominator > 0) ? numeratorUp / denominator : 0.;
      trackWeightDataDown = (denominator > 0) ? numeratorDown / denominator : 0.;
    }

    (*eventvariables)["trackLegWeight"] = trackWeight;
    (*eventvariables)["trackLegWeightMCUp"] = trackWeightMCUp;
    (*eventvariables)["trackLegWeightMCDown"] = trackWeightMCDown;
    (*eventvariables)["trackLegWeightDataUp"] = trackWeightDataUp;
    (*eventvariables)["trackLegWeightDataDown"] = trackWeightDataDown;
  }

  // grand OR of triggers
  if(produceGrandOr_) {
    FindEfficiency(grandOrNumerator_, metNoMuPt, numerator, numeratorUp, numeratorDown);
    FindEfficiency(grandOrDenominator_, metNoMuPt, denominator, denominatorUp, denominatorDown);

    double grandOrWeight = (denominator > 0) ? numerator / denominator : 0.;
    double grandOrWeightMCUp = (denominatorUp > 0) ? numerator / denominatorUp : 0.;
    double grandOrWeightMCDown = (denominatorDown > 0) ? numerator / denominatorDown : 0.;
    double grandOrWeightDataUp = (denominator > 0) ? numeratorUp / denominator : 0.;
    double grandOrWeightDataDown = (denominator > 0) ? numeratorDown / denominator : 0.;

    (*eventvariables)["grandOrWeight"] = grandOrWeight;
    (*eventvariables)["grandOrWeightMCUp"] = grandOrWeightMCUp;
    (*eventvariables)["grandOrWeightMCDown"] = grandOrWeightMCDown;
    (*eventvariables)["grandOrWeightDataUp"] = grandOrWeightDataUp;
    (*eventvariables)["grandOrWeightDataDown"] = grandOrWeightDataDown;
  }

  if (isFirstEvent_) {
    clog << "[TriggerWeightProducer] Applying trigger reweighting (isRealData: " << (event.isRealData () ? "true" : "false")
         << ", efficiencyFile_: \"" << efficiencyFile_
         << "\", dataset_: \"" << dataset_
         << "\", target_: \"" << target_ << "\")" << endl;
    isFirstEvent_ = false;
  }

}

void TriggerWeightProducer::FindEfficiency(TGraphAsymmErrors * graph, double value,
                                           double& efficiency, double& efficiencyUp, double& efficiencyDown) {

  // If the x-axis value is out of bounds, use the boundary efficiency
  double xmin, ymin, xmax, ymax;
  graph->ComputeRange(xmin, ymin, xmax, ymax);
  if(value < xmin) value = xmin + 1.e-6;
  if(value > xmax) value = xmax - 1.e-6;

  double x, y;

  for(int i = 0; i < graph->GetN(); i++) {
    graph->GetPoint(i, x, y);
    if(graph->GetErrorX(i) > fabs(value - x)) {
      efficiency = y;
      efficiencyUp = y + graph->GetErrorYhigh(i);
      efficiencyDown = y - graph->GetErrorYlow(i);
      return;
    }
  }

  // If you didn't find the graph bin (shouldn't be possible?), return zeros

  efficiency = 0;
  efficiencyUp = 0;
  efficiencyDown = 0;

  return;
}

const TVector2 TriggerWeightProducer::getPFMETNoMu(const vector<TYPE(mets)> &mets, const vector<TYPE(muons)> &muons) const {
  TVector2 metNoMu(0, 0);
  for(const auto &met : mets) {
    metNoMu += TVector2(met.px(), met.py());
    for(const auto &muon : muons) {
      if(muon.isLooseMuon()) metNoMu += TVector2(muon.px(), muon.py());
    }
  }

  return metNoMu;
}

const osu::Track &
TriggerWeightProducer::getLeadTrack (const vector<osu::Track> &tracks) const
{
  double leadPt = -1.0;
  int leadIndex = -1;
  for (unsigned i = 0; i < tracks.size (); i++)
    {
      if (tracks.at (i).pt () > leadPt)
        {
          leadPt = tracks.at (i).pt ();
          leadIndex = i;
        }
    }

  return tracks.at (leadIndex);
}

bool
TriggerWeightProducer::passesInclusiveMetTriggers (const edm::Event &event, const edm::TriggerResults &triggers)
{
  bool flag = false;
  const edm::TriggerNames &triggerNames = event.triggerNames (triggers);
  if (triggerNamesPSetID_ != triggerNames.parameterSetID ())
    {
      triggerIndices_.clear ();
      triggerNamesPSetID_ = triggerNames.parameterSetID ();
    }
  if (triggerIndices_.empty ())
    {
      for (unsigned i = 0; i < triggerNames.size (); i++)
        {
          string name = triggerNames.triggerName (i);
          bool pass = triggers.accept (i);

          for (unsigned triggerIndex = 0; triggerIndex != inclusiveMetTriggers_.size (); triggerIndex++)
            {
              if (name.find (inclusiveMetTriggers_.at (triggerIndex)) == 0)
                {
                  triggerIndices_[inclusiveMetTriggers_.at (triggerIndex)];
                  triggerIndices_.at (inclusiveMetTriggers_.at (triggerIndex)).insert (i);
                  flag = flag || pass;
                }
            }
        }
    }
  else
    {
      for (unsigned triggerIndex = 0; triggerIndex != inclusiveMetTriggers_.size (); triggerIndex++)
        {
          if (!triggerIndices_.count (inclusiveMetTriggers_.at (triggerIndex)))
            continue;
          for (const auto &i : triggerIndices_.at (inclusiveMetTriggers_.at (triggerIndex)))
            {
              bool pass = triggers.accept (i);
              flag = flag || pass;
            }
        }
    }

  return flag;
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(TriggerWeightProducer);

#endif
