import FWCore.ParameterSet.Config as cms

import copy
from HLTrigger.HLTfilters.hltHighLevel_cfi import *
zerobiasHLTFilter = copy.deepcopy(hltHighLevel)
zerobiasHLTFilter.throw = False
zerobiasHLTFilter.HLTPaths =['']