# vim:ts=8:sw=8:tw=0:noet

from builtins import *

import logging as log
import re

import roman

cancer_diag_ranges = ['C00-D49', 'C00-C97', 'C00-C75', 'C00-C14', 'C15-C26', 'C30-C39', 'C40-C41', 'C43-C44', 'C45-C49',
                      'C51-C58', 'C60-C63', 'C64-C68', 'C69-C72', 'C73-C75', 'C76-C80', 'C81-C96', 'D00-D09', 'D10-D36',
                      'D37-D48', 'C50-C50', 'C97-C97']

cancer_chapters_roman = list(map(roman.toRoman, range(1, 23)))  # chapter 22 added in 2020


class ICD10CodesHelper:

   def isCancerCode(code : str) -> bool:
      if code in ['C7A', 'C7B', 'D3A']:
         return True
      m = re.search(r'^(?P<block>[A-Z])(?P<code>\d{1,2})(\.(?P<subcode>\d+))?$', code)
      if m:
         log.debug("ICD-10 block detected: %s, code: %s, subcode %s" % (m.group('block'), m.group('code'), m.group('subcode')))
         if m.group('block') == 'C' or (m.group('block') == 'D' and int(m.group('code')) <= 48):
            return True
         else:
            return False

      # now we deal with ranges
      m = re.search(r'^(?P<blockA>[A-Z]\d{1,2}(\.\d+)?)-(?P<blockB>[A-Z]\d{1,2}(\.\d+)?)$', code)
      if m:
         log.debug("ICD-10 range of blocks detected: from %s to %s" % (m.group('blockA'), m.group('blockB')))
         if ICD10CodesHelper.isCancerCode(m.group('blockA')) or ICD10CodesHelper.isCancerCode(m.group('blockB')):
             return True
         else:
             return False

      # this is unparsable
      return None

   def isCancerChapter(code : str) -> bool:
      if code not in cancer_chapters_roman:
         return None
      log.debug("ICD10 chapter detected: %s" % (code))
      if code == "II":
         return True
      else:
         return False
