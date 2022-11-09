import ROOT

from Analysis import Analysis
from Analysis import AnalysisHelpers
from Analysis import Constants
import numpy as np
import scipy

#======================================================================

class ZAnalysis(Analysis.Analysis):
  """Analysis searching for events where Z bosons decay to two leptons of same flavour and opposite charge.
  """
  def __init__(self, store):
    super(ZAnalysis, self).__init__(store)
  
  def initialize(self):
      self.hist_invMass         =  self.addStandardHistogram("invMassZ")
      self.hist_leptn           =  self.addStandardHistogram("lep_n")

      self.hist_leadleptpt      =  self.addStandardHistogram("leadlep_pt")
      self.hist_leadlepteta     =  self.addStandardHistogram("leadlep_eta")
      self.hist_leadleptE       =  self.addStandardHistogram("leadlep_E")
      self.hist_leadleptphi     =  self.addStandardHistogram("leadlep_phi")
      self.hist_leadleptch      =  self.addStandardHistogram("leadlep_charge")
      self.hist_leadleptID      =  self.addStandardHistogram("leadlep_type")
      self.hist_leadleptptc     =  self.addStandardHistogram("leadlep_ptconerel30")
      self.hist_leadleptetc     =  self.addStandardHistogram("leadlep_etconerel20")
      self.hist_leadlepz0       =  self.addStandardHistogram("leadlep_z0")
      self.hist_leadlepd0       =  self.addStandardHistogram("leadlep_d0")

      self.hist_trailleptpt     =  self.addStandardHistogram("traillep_pt")
      self.hist_traillepteta    =  self.addStandardHistogram("traillep_eta")
      self.hist_trailleptE      =  self.addStandardHistogram("traillep_E")
      self.hist_trailleptphi    =  self.addStandardHistogram("traillep_phi")
      self.hist_trailleptch     =  self.addStandardHistogram("traillep_charge")
      self.hist_trailleptID     =  self.addStandardHistogram("traillep_type")
      self.hist_trailleptptc    =  self.addStandardHistogram("traillep_ptconerel30")
      self.hist_trailleptetc    =  self.addStandardHistogram("traillep_etconerel20")
      self.hist_traillepz0      =  self.addStandardHistogram("traillep_z0")
      self.hist_traillepd0      =  self.addStandardHistogram("traillep_d0")

      self.hist_njets           =  self.addStandardHistogram("n_jets")       
      self.hist_jetspt          =  self.addStandardHistogram("jet_pt")       
      self.hist_jetm            =  self.addStandardHistogram("jet_m")        
      self.hist_jetJVT          =  self.addStandardHistogram("jet_jvt")      
      self.hist_jeteta          =  self.addStandardHistogram("jet_eta")

      self.hist_etmiss          = self.addStandardHistogram("etmiss")
  
  def analyze(self):
      # retrieving objects
      eventinfo = self.Store.getEventInfo()
      weight = eventinfo.scalefactor()*eventinfo.eventWeight() if not self.getIsData() else 1
      self.countEvent("no cut", weight)
      
      # apply standard event based selection
      if not AnalysisHelpers.StandardEventCuts(eventinfo): return False
      self.countEvent("EventCuts", weight)

      # Get the leptons
      goodLeptons = AnalysisHelpers.selectAndSortContainer(self.Store.getLeptons(), isGoodLepton, lambda p: p.pt())

      # Get the jets
      jets = AnalysisHelpers.selectAndSortContainer(self.Store.getJets(), AnalysisHelpers.isGoodJet, lambda p: p.pt())

      # get the missing ET
      etmiss    = self.Store.getEtMiss()

      # Event selection here
      if not len(goodLeptons) == 2: return False
      self.countEvent("2 leptons", weight)

      # Lepton charge
      if goodLeptons[0].charge() == goodLeptons[1].charge() : return False
      self.countEvent("lepton charge", weight)
      
      # Lepton Type
      lep_sum = abs(goodLeptons[0].pdgId()) + abs(goodLeptons[1].pdgId())
      if not (lep_sum == 22 or lep_sum == 26) : return False
      self.countEvent("lepton type", weight)

      # Start the histogramming

      # Missing Et Histograms
      self.hist_etmiss.Fill(etmiss.et(), weight)

      # lepton histograms
      self.hist_leptn.Fill(len(goodLeptons), weight)

      # event histograms
      #fit_histogram = self.hist_invMass
      self.hist_invMass.Fill((goodLeptons[0].tlv() + goodLeptons[1].tlv()).M(), weight)
      #fitting a gaussian for this histogram
      #self.hist_invMass.Fit("gaus")
      
      
        
      
      
      self.hist_invMass.Fill((goodLeptons[0].tlv() + goodLeptons[1].tlv()).M(), weight)

      return True
  
  def finalize(self):
      pass

  def ZWindow(self, lep1, lep2):
      return abs((lep1.tlv()+lep2.tlv()).M() - Constants.Z_Mass)

def isGoodLepton(Lepton):
    if not Lepton.isoetconerel20() < 0.15: return False
    if not Lepton.isoptconerel30() < 0.15: return False
    return True;
