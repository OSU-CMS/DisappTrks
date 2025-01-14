import re
from omsapi import OMSAPI

class L1Rates():

    def __init__(self, outputFile='l1ETM_2023D.txt'):
        self.rates = {}
        self.out_name = outputFile
        self.max_n_ls = 1000
        self.initialize()

    #this function gives access to omsapi (this is the milliqan app so be careful)
    def initialize(self):
        my_app_id='milliqan-oms'
        my_app_secret='AvwJaQWfSMuDsOhYwPxynQMrFN7YXfPV'

        self.omsapi = OMSAPI("https://cmsoms.cern.ch/agg/api", "v1", cert_verify=False)
        self.omsapi.auth_oidc(my_app_id,my_app_secret)

    #adapted from cmstalk https://cms-talk.web.cern.ch/t/the-l1algos-endpoint-not-accessible/41148/2
    def getL1Prescales(self, run=381309):  

        query = self.omsapi.query("l1algorithmtriggers")
        query.per_page = self.max_n_ls # to get up to 10 LS in one go
        
        query.attrs(["name","bit","pre_dt_before_prescale_counter", "pre_dt_counter", "post_dt_counter", "initial_prescale", "final_prescale"])        
        rates = {}

        query.clear_filter().filter("run_number", run )  # returns data per lumisection
        data = query.data().json()['data']
        query.verbose = False

        for seed in data:
            threshold = None
            match = re.search(r'ETM(?:HF)?(\d+)', seed['attributes']['name'])
            if match:
                try:
                    threshold = int(match.group(1))
                except:
                    print("Error getting threshold for L1Seed: {}, set to None".format(seed['attributes']['name']))
            else:
                continue

            #print("Name {}, threshold {}".format(seed['attributes']['name'], threshold))

            averagePrescale = 0
            if int(seed['attributes']['pre_dt_before_prescale_counter']) > 0:
                averagePrescale = seed['attributes']['pre_dt_counter'] / seed['attributes']['pre_dt_before_prescale_counter']

            rates[(seed['attributes']['bit'])] = {
                "name": seed['attributes']['name'] ,
                "countsBeforePrescale": seed['attributes']['pre_dt_before_prescale_counter'],
                "countsAfterPrescale": seed['attributes']['pre_dt_counter'],
                "initialPrescale": seed['attributes']['initial_prescale']['prescale'],
                "finalPrescale": seed['attributes']['final_prescale']['prescale'],
                "averagePrescale": averagePrescale,
                "threshold": threshold
            }

        return rates

    #get prescales for all runs in the era
    def loopOverRuns(self, runs=[]):
        start_run, end_run = self.getRunsInEra()
        runs = [x for x in range(start_run, end_run)]
        for run in runs:
            print("Working on run {}".format(run))
            attempts = 0
            success = False
            #api can fail so give it a few tries
            while attempts < 5 and not success:
                try:
                    self.rates[run] = self.getL1Prescales(run=run)
                    success=True
                except:
                    print("Attempting to get L1Seeds for {} again, attempt {}".format(run, attempts))
                    attempts+=1


    #get the first and last runs in the era
    def getRunsInEra(self, era='Run2023D'):
        print("getting runs in era")
        q = self.omsapi.query("eras")
        q.per_page = 100
        q.clear_filter().filter("name", era)

        response = q.data()
        data = response.json()['data']

        start_run = data[0]['attributes']['start_run']
        end_run = data[0]['attributes']['end_run']

        print("start run {}, end run {}".format(start_run, end_run))

        return start_run, end_run

    #save everything into the txt file expected by the EventL1ETMProducer
    def saveL1ETM(self):
        with open(self.out_name, 'w') as fout:
            for run, info in self.rates.items():
                for L1Bit, values in info.items():
                    s_out = 'run: {} name: {} threshold: {} average_prescale: {} initial_prescale: {} final_prescale: {}'.format(run, values['name'], values['threshold'], values['averagePrescale'], values['initialPrescale'], values['finalPrescale'])
                    fout.write(s_out + '\n')


if __name__ == "__main__":

    myrates = L1Rates()
    myrates.loopOverRuns()
    myrates.saveL1ETM()