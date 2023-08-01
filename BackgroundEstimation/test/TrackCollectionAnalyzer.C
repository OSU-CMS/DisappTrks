class TrackCollection : public edm::EDAnalyzer{
    public:
        TrackPlotsExample( const edm::ParameterSet &)

    private:
    void beginJob( const edm::EventSetup & );
    void analyze( const edm::Event & event, const edm::EventSetup & );
    void endJob();
    edm::InputTag src_;
    TFile * outputFile_;
    TH1F * h_pt, * h_eta, * h_phi, * h_iso;
};

void TrackCollection::beginJob( const EventSetup & ) {
    outputFile_ = new TFile("output.root" , "RECREATE");
    h_pt = new TH1F( "pt" , "p_{t}", 50, 0, 20);
    h_eta = new TH1F( "eta" , "#eta",  50, -3, 3);
    h_phi = new TH1F( "phi", "#phi", 50 , -M_PI, M_PI);
}

void TrackCollection::analyze(const Event& event, const EventSetup& es){
    Handle<TrackCollection> tracks;
    event.getByLabel( src_, tracks);
    for (TrackCollection::const_iterator track = track->begin();
         track != tracks->end(); ++ track){
        h_pt->Fill( track->pt() ) ;
        h_eta->Fill( track->eta()) ;
        h_phi -> Fill( track->phi()) ;
    }
}

void TrackCollection::endJob() {
    cout << " >> Saving histograms " << endl;
    outputFile_->Write();
    outputFile_->Close();
}
