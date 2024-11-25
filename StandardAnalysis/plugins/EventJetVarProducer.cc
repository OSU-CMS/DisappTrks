#ifndef EVENT_JET_VAR_PRODUCER
#define EVENT_JET_VAR_PRODUCER

#include "TH2D.h"
#include "TH1D.h"
#include "TFile.h"
#include "OSUT3Analysis/AnaTools/interface/EventVariableProducer.h"
#include "TLorentzVector.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "OSUT3Analysis/AnaTools/interface/DataFormat.h"
#include "OSUT3Analysis/AnaTools/interface/ValueLookupTree.h"
#include "OSUT3Analysis/AnaTools/interface/CommonUtils.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"

struct PhysicsObject
{
  PhysicsObject (double eta, double phi) : eta_ (eta), phi_ (phi) {};
  template<class T> PhysicsObject (T obj) : eta_ (obj.eta ()), phi_ (obj.phi ()) {};

  const double eta () const { return eta_ ; };
  const double phi () const { return phi_; };

  private:
    double eta_;
    double phi_;
};

class EventJetVarProducer : public EventVariableProducer {
public:
  EventJetVarProducer (const edm::ParameterSet &);
  ~EventJetVarProducer ();

private:
  void AddVariables(const edm::Event &, const edm::EventSetup &);
  edm::EDGetTokenT<vector<TYPE(jets)> >             tokenJets_;
  edm::EDGetTokenT<vector<TYPE(mets)> >             tokenMets_;
  edm::EDGetTokenT<vector<pat::PackedCandidate> >   tokenPFCands_;
  edm::EDGetTokenT<vector<pat::PackedCandidate> >   tokenLostTracks_;
  edm::EDGetTokenT<vector<TYPE(hardInteractionMcparticles)> > tokenMcparticles_;
  edm::EDGetTokenT<edm::TriggerResults>             tokenTriggerBits_;
  edm::EDGetTokenT<vector<TYPE(muons)> >            tokenMuons_;
  std::string                                       jetVetoMap_;

  double genGluinoMass_, genNeutralinoMass_, genCharginoMass_;

  bool isFirstEvent_;

  bool IsValidJet(const TYPE(jets) & jet);
  bool IsValidHTJet(const TYPE(jets) & jet);

  unsigned getNTracks (const edm::Handle<vector<pat::PackedCandidate> > &, const edm::Handle<vector<pat::PackedCandidate> > &, const vector<PhysicsObject> &, double &, unsigned &, unsigned &) const;
  bool isInJet (const pat::PackedCandidate &, const vector<PhysicsObject> &) const;
  bool hasChargino (const edm::Handle<vector<TYPE(hardInteractionMcparticles)> > &) const;
  bool hasNeutralino (const edm::Handle<vector<TYPE(hardInteractionMcparticles)> > &) const;
  void findGenMasses (const edm::Handle<vector<TYPE(hardInteractionMcparticles)> > &);
  uint32_t packTriggerFires (const edm::Event &event, const edm::Handle<edm::TriggerResults> &) const;
  bool jetLooseSelection (const TYPE(jets)&, const vector<TYPE(muons)> &) const;
  bool jetTightID (const TYPE(jets)&) const;

  vector<string> triggerNames;
};

EventJetVarProducer::EventJetVarProducer(const edm::ParameterSet &cfg) :
  EventVariableProducer(cfg),
  jetVetoMap_ (cfg.getParameter<edm::FileInPath> ("jetVetoMap").fullPath()),
  isFirstEvent_ (true)
{
  tokenJets_        =  consumes<vector<TYPE(jets)> >             (collections_.getParameter<edm::InputTag>  ("jets"));
  tokenMets_        =  consumes<vector<TYPE(mets)> >             (collections_.getParameter<edm::InputTag>  ("mets"));
  tokenPFCands_     =  consumes<vector<pat::PackedCandidate> >   (collections_.getParameter<edm::InputTag>  ("pfCandidates"));
  tokenLostTracks_  =  consumes<vector<pat::PackedCandidate> >   (collections_.getParameter<edm::InputTag>  ("lostTracks"));
  tokenMcparticles_ =  consumes<vector<TYPE(hardInteractionMcparticles)> > (collections_.getParameter<edm::InputTag>  ("hardInteractionMcparticles"));
  tokenTriggerBits_ =  consumes<edm::TriggerResults>(collections_.getParameter<edm::InputTag>("triggers"));
  tokenMuons_       =  consumes<vector<TYPE(muons)> >            (collections_.getParameter<edm::InputTag>  ("muons"));
  triggerNames = cfg.getParameter<vector<string> >("triggerNames");
}

EventJetVarProducer::~EventJetVarProducer() {}

bool
EventJetVarProducer::IsValidJet(const TYPE(jets) & jet) {

  if (!(jet.pt() > 30))         return false;
  if (!(fabs(jet.eta()) < 4.5)) return false;
  if (!anatools::jetPassesTightLepVeto (jet)) return false;

  return true;
}

bool
EventJetVarProducer::IsValidHTJet(const TYPE(jets) & jet) {
  if (!(jet.pt() > 20))         return false;
  if (!(fabs(jet.eta()) < 5.2)) return false;
  if (!anatools::jetPassesTightLepVeto (jet)) return false;

  return true;
}

void
EventJetVarProducer::AddVariables (const edm::Event &event, const edm::EventSetup &setup) {

  edm::Handle<vector<TYPE(jets)> > jets;
  if (!event.getByToken (tokenJets_, jets)) {
    clog << "ERROR:  Could not find jets collection." << endl;
    return;
  }

  edm::Handle<vector<TYPE(mets)> > mets;
  if (!event.getByToken (tokenMets_, mets)) {
    clog << "ERROR:  Could not find mets collection." << endl;
    return;
  }

  edm::Handle<vector<pat::PackedCandidate> > pfCands;
  if (!event.getByToken (tokenPFCands_, pfCands)) {
    clog << "ERROR:  Could not find pfCandidates collection." << endl;
    return;
  }

  edm::Handle<vector<TYPE(muons)> > muons;
  if (!event.getByToken (tokenMuons_, muons)) {
    clog << "ERROR:  Could not find muons collection." << endl;
    return;
  }

  edm::Handle<vector<pat::PackedCandidate> > lostTracks;
  event.getByToken (tokenLostTracks_, lostTracks);

  edm::Handle<vector<TYPE(hardInteractionMcparticles)> > mcParticles;
  event.getByToken (tokenMcparticles_, mcParticles);

  edm::Handle<edm::TriggerResults> triggerBits;
  event.getByToken(tokenTriggerBits_, triggerBits);

  TFile* f_jetVeto = TFile::Open(jetVetoMap_.c_str(), "read");
  TH2D* jetVetoMap = (TH2D*)f_jetVeto->Get("jetvetomap");

  jetVetoMap->SetDirectory(0);
  f_jetVeto->Close();
  delete f_jetVeto;

  vector<PhysicsObject> validJets;
  double dijetMaxDeltaPhi         = -999.;  // default is large negative value
  double deltaPhiMetJetLeading    =  999.;  // default is large positive value
  double deltaPhiMetJetSubleading =  999.;
  double ptJetLeading    = -999;
  double ptJetSubleading = -999;
  double phiJetLeading = -999;
  double phiJetSubleading = -999;

  int idx1 = -1;
  for (const auto &jet1 : *jets) {
    idx1++;
    if (!IsValidJet(jet1)) continue;
    int idx2 = -1;
    if (jet1.pt() > ptJetSubleading) {
      double dPhi = fabs(deltaPhi(jet1, mets->at(0)));
      if (jet1.pt() > ptJetLeading) {
        ptJetSubleading = ptJetLeading;
        phiJetSubleading = phiJetLeading;
        deltaPhiMetJetSubleading = deltaPhiMetJetLeading;
        ptJetLeading = jet1.pt();
        phiJetLeading = jet1.phi();
        deltaPhiMetJetLeading = dPhi;
      } else {
        ptJetSubleading = jet1.pt();
        phiJetSubleading = jet1.phi();
        deltaPhiMetJetSubleading = dPhi;
      }
    }
    for (const auto &jet2 : *jets) {
      idx2++;
      if (idx2 <= idx1)              continue;  // Avoid double-counting.
      if (!IsValidJet(jet2)) continue;
      double dPhi = fabs(deltaPhi(jet1.phi(), jet2.phi()));
      if (dPhi > dijetMaxDeltaPhi) {
        dijetMaxDeltaPhi = dPhi;
      }
    }
    validJets.emplace_back (jet1);
  }

  double ht = 0., mht_x = 0., mht_y = 0.;

  for (const auto &jet : *jets) {
    if (!IsValidHTJet(jet)) continue;
    ht += jet.pt();
    mht_x -= jet.px();
    mht_y -= jet.py();
  }

  double htJets = ht, mhtJets_x = mht_x, mhtJets_y = mht_y;

  for (const auto &pfCand : *pfCands) {
    if(abs(pfCand.pdgId()) == 11) {
      ht += pfCand.pt();
      mht_x -= pfCand.px();
      mht_y -= pfCand.py();
    }
  }

  double htNoMu = ht, mhtNoMu_x = mht_x, mhtNoMu_y = mht_y;

  for (const auto &pfCand : *pfCands) {
    if(abs(pfCand.pdgId()) == 13) {
      ht += pfCand.pt();
      mht_x -= pfCand.px();
      mht_y -= pfCand.py();
    }
  }

  double trackRho = 0.0;
  unsigned nTracksInsideJets = 0, nTracksOutsideJets = 0;
  unsigned nTracks = getNTracks (pfCands, lostTracks, validJets, trackRho, nTracksInsideJets, nTracksOutsideJets);

  bool hasCharginoFlag = hasChargino (mcParticles), hasNeutralinoFlag = hasNeutralino (mcParticles);

  bool jetIn_hem1516 = false;
  bool jetOpposite_hem1516 = false;
  bool metJet_hem1516 = false;

  bool passJetVeto2022 = true;

  for (const auto &jet1 : *jets) {
    if (jetLooseSelection(jet1, *muons)) {
      if (jetVetoMap->GetBinContent(jetVetoMap->FindFixBin(jet1.eta(), jet1.phi())) > 0){
        passJetVeto2022 = false;
      } 
    }
    if (jet1.eta() >= -3.0 && jet1.eta() <= -1.3) {
      if (jet1.phi() >= -1.57 && jet1.phi() <= -0.87) jetIn_hem1516 = true;
      if (jet1.phi() >= -1.57 + 3.14159 && jet1.phi() <= -0.87 + 3.14159) jetOpposite_hem1516 = true;
      if (jet1.phi() >= -1.57 + 3.14159 && jet1.phi() <= -0.87 + 3.14159 && mets->at(0).phi() >= -1.57 && mets->at(0).phi() <= -0.87) metJet_hem1516 = true;
    }
  }

  delete jetVetoMap;

  findGenMasses(mcParticles);

  (*eventvariables)["nJets"]            = validJets.size ();
  (*eventvariables)["dijetMaxDeltaPhi"] = dijetMaxDeltaPhi;
  (*eventvariables)["ptJetLeading"]     = ptJetLeading;
  (*eventvariables)["ptJetSubleading"]  = ptJetSubleading;
  (*eventvariables)["phiJetLeading"]     = phiJetLeading;
  (*eventvariables)["phiJetSubleading"]  = phiJetSubleading;
  (*eventvariables)["deltaPhiMetJetLeading"]     = deltaPhiMetJetLeading;
  (*eventvariables)["deltaPhiMetJetSubleading"]  = deltaPhiMetJetSubleading;

  (*eventvariables)["eventUnixTime"]  = event.time ().unixTime ();
  (*eventvariables)["runNumber"]  = event.run ();

  (*eventvariables)["HT"] = ht;
  (*eventvariables)["MHT"] = hypot(mht_x, mht_y);
  (*eventvariables)["HTJets"] = htJets;
  (*eventvariables)["MHTJets"] = hypot(mhtJets_x, mhtJets_y);
  (*eventvariables)["HTNoMu"] = htNoMu;
  (*eventvariables)["MHTNoMu"] = hypot(mhtNoMu_x, mhtNoMu_y);

  (*eventvariables)["nTracks"]  = nTracks;
  (*eventvariables)["nTracksInsideJets"]  = nTracksInsideJets;
  (*eventvariables)["nTracksOutsideJets"]  = nTracksOutsideJets;
  (*eventvariables)["trackRho"]  = trackRho;

  (*eventvariables)["isCharginoChargino"]  = (hasCharginoFlag ? !hasNeutralinoFlag : false);
  (*eventvariables)["isCharginoNeutralino"]  = (hasCharginoFlag ? hasNeutralinoFlag : false);
  (*eventvariables)["numberOfCharginos"]  = (hasCharginoFlag ? (hasNeutralinoFlag ? 1 : 2) : 0);

  (*eventvariables)["genCharginoMass"] = genCharginoMass_;
  (*eventvariables)["genNeutralinoMass"] = genNeutralinoMass_;
  (*eventvariables)["genGluinoMass"] = genGluinoMass_;

  (*eventvariables)["packedTriggerFiresBit"] = (triggerBits.isValid () ? packTriggerFires(event, triggerBits) : 0);

  (*eventvariables)["jetInHEM1516"] = jetIn_hem1516;
  (*eventvariables)["jetOppositeHEM1516"] = jetOpposite_hem1516;
  (*eventvariables)["metJetHEM1516"] = metJet_hem1516;
  (*eventvariables)["jetVeto2022"] = passJetVeto2022;

  isFirstEvent_ = false;
}

unsigned
EventJetVarProducer::getNTracks (const edm::Handle<vector<pat::PackedCandidate> > &pfCands, const edm::Handle<vector<pat::PackedCandidate> > &lostTracks, const vector<PhysicsObject> &jets, double &trackRho, unsigned &nTracksInsideJets, unsigned &nTracksOutsideJets) const
{
  unsigned nTracks = 0.0;
  TH2D *etaPhi = new TH2D ("etaPhi", ";#phi;#eta", 20, -3.142, 3.142, 20, -2.5, 2.5);
  for (const auto &pfCand : *pfCands)
    {
      if (pfCand.charge () && pfCand.numberOfHits () > 0)
        {
          nTracks++;
          if (isInJet (pfCand, jets))
            nTracksInsideJets++;
          else
            nTracksOutsideJets++;
          etaPhi->Fill (pfCand.phi (), pfCand.eta ());
        }
    }
  if (lostTracks.isValid ())
    {
      if (isFirstEvent_)
        clog << "[EventJetVarProducer] using lost tracks collection..." << endl;
      nTracks += lostTracks->size ();
      for (const auto &lostTrack : *lostTracks)
        etaPhi->Fill (lostTrack.phi (), lostTrack.eta ());
    }
  else
    if (isFirstEvent_)
      clog << "[EventJetVarProducer] NOT using lost tracks collection..." << endl;

  set<double> trackNumberDensity;
  for (int iPhi = 1; iPhi <= etaPhi->GetXaxis ()->GetNbins (); iPhi++)
    {
      for (int iEta = 1; iEta <= etaPhi->GetYaxis ()->GetNbins (); iEta++)
        {
          double phiWidth = etaPhi->GetXaxis ()->GetBinWidth (iPhi),
                 etaWidth = etaPhi->GetYaxis ()->GetBinWidth (iEta),
                 area = phiWidth * etaWidth,
                 number = etaPhi->GetBinContent (iPhi, iEta);

          trackNumberDensity.insert (number / area);
        }
    }
  delete etaPhi;

  unsigned i = 0, n = trackNumberDensity.size ();
  trackRho = 0.0;
  for (set<double>::const_iterator numberDensity = trackNumberDensity.cbegin (); i <= n / 2.0 && numberDensity != trackNumberDensity.cend (); numberDensity++, i++)
    {
      if (n % 2 && i == (n - 1) / 2)
        trackRho = *numberDensity;
      if (!(n % 2) && (i == (n / 2) - 1 || i == n / 2))
        trackRho += *numberDensity;
    }
  if (!(n % 2))
    trackRho /= 2.0;

  return nTracks;
}

bool
EventJetVarProducer::isInJet (const pat::PackedCandidate &cand, const vector<PhysicsObject> &jets) const
{
  for (const auto &jet : jets)
    if (deltaR (cand, jet) < 0.4)
      return true;
  return false;
}

bool
EventJetVarProducer::hasChargino (const edm::Handle<vector<TYPE(hardInteractionMcparticles)> > &mcParticles) const
{
  if (mcParticles.isValid ())
    {
      unsigned i = 0;
      for (const auto &mcParticle : *mcParticles)
        {
          if (abs (mcParticle.pdgId ()) == 1000024)
            return true;
          if ((++i) >= 10)
            break;
        }
    }
  else
    if (isFirstEvent_)
      clog << "[EventJetVarProducer] NOT determining generated signal event type..." << endl;
  return false;
}

bool
EventJetVarProducer::hasNeutralino (const edm::Handle<vector<TYPE(hardInteractionMcparticles)> > &mcParticles) const
{
  if (mcParticles.isValid ())
    {
      unsigned i = 0;
      for (const auto &mcParticle : *mcParticles)
        {
          if (abs (mcParticle.pdgId ()) == 1000022 || abs(mcParticle.pdgId ()) == 1000023)
            return true;
          if ((++i) >= 10)
            break;
        }
    }
  else
    if (isFirstEvent_)
      clog << "[EventJetVarProducer] NOT determining generated signal event type..." << endl;
  return false;
}

void
EventJetVarProducer::findGenMasses (const edm::Handle<vector<TYPE(hardInteractionMcparticles)> > &mcParticles)
{
  genCharginoMass_ = -1.;
  genNeutralinoMass_ = -1.;
  genGluinoMass_ = -1.;

  if(mcParticles.isValid()) {
    for(const auto &mcParticle : *mcParticles) {
      if(genGluinoMass_ < 0.     && abs(mcParticle.pdgId()) == 1000021) genGluinoMass_ = mcParticle.mass();
      if(genNeutralinoMass_ < 0. && abs(mcParticle.pdgId()) == 1000022) genNeutralinoMass_ = mcParticle.mass();
      if(genCharginoMass_ < 0.   && abs(mcParticle.pdgId()) == 1000024) genCharginoMass_ = mcParticle.mass();
    }
  }
}

uint32_t
EventJetVarProducer::packTriggerFires (const edm::Event &event, const edm::Handle<edm::TriggerResults> &triggerBits) const
{

  const edm::TriggerNames &allTriggerNames = event.triggerNames(*triggerBits);

  uint32_t value = 0;

  // for all paths in the full list of paths stored in the event...
  for(unsigned i = 0; i < allTriggerNames.size(); i++) {
      string thisName = allTriggerNames.triggerName(i);

      // check if they match the j'th trigger you're interested in
      for(unsigned int j = 0; j < triggerNames.size(); j++) {
        if(thisName.find(triggerNames[j]) == 0) {
          // and set the j'th bit to its fire status
          value |= (triggerBits->accept(i) & 0x1) << j;
          break;
        }
      }
  }
  // if you never found a path you're interested in in allTriggerNames, then it's safe to say it didn't fire
  return value;
}

bool 
EventJetVarProducer::jetLooseSelection (const TYPE(jets) &jet, const vector<TYPE(muons)> &muons) const
{
  // jet pt cut
  if ( jet.pt() < 15 ) return false;
  
  // jet em fraction < 0.9
  if ( jet.neutralEmEnergyFraction() < 0.9 ) return false;

  // dR(jet, muon) > 0.2
  for (auto& muon: muons){
    double dR = deltaR(jet, muon);
    if ( dR < 0.2 ) return false;
  }

  //Add JET tight ID
  if (!jetTightID(jet)) return false;
  
  //Add Jet PU ID once suggestions are given by Jets Group https://twiki.cern.ch/twiki/bin/viewauth/CMS/PileupJetID
  
  return true;

}

//Jet Tight ID for 2022 as defined https://twiki.cern.ch/twiki/bin/view/CMS/JetID13p6TeV
bool 
EventJetVarProducer::jetTightID (const TYPE(jets)& jet) const
{
  bool result = anatools::jetPassesTightLepVeto(jet); // This automatically uses the correct jet ID criteria
  return result;
}



#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(EventJetVarProducer);


#endif
