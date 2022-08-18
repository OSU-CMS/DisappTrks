#ifndef NETWORKOUTPUT_H
#define NETWORKOUTPUT_H

#include <vector>

using namespace std;


class NetworkOutput
{
  public:
    
    NetworkOutput () {};
    ~NetworkOutput () {};

    const float getOutput(int ID) const{
      return networkOutput_.at(ID);
    }

    const std::vector<float> scores() const { return this->networkOutput_; };


    void setOutput(int ID, const float networkOutput){
      networkOutput_[ID] = std::move(networkOutput);
    }

    void addOutput(const float networkOutput){
      networkOutput_.push_back(networkOutput);
    }

    

  private:
    std::vector<float> networkOutput_;

};

#endif
