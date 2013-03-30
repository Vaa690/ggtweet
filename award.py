#!/usr/bin/env python
# encoding: utf-8
"""
AwardModel.py

Created by Matt Derry on 2013-02-04.
"""

import sys
import os
import string

class AwardModel(object):
   "A class representing the category, winner, show, and presenter of an award"
   def __init__(self, category=None, winner=None, show=None, presenter=None):
      self.category = category
      self.winner = winner
      self.show = show
      self.presenter = presenter
      self.score = 0

   def __gt__(self, award):
      return self.score > award.score

   def __lt__(self, award):
      return self.score < award.score

   def __ge__(self, award):
      return self.score >= award.score

   def __le__(self, award):
      return self.score <= award.score

   def __eq__(self, award):
      return self.score == award.score

   def len(self):
      length = 0
      if category is not None:
         length = length + 1
      if show is not None:
         length = length + 1
      if presenter is not None:
         length = length + 1
      if winner is not None:
         length = length + 1

      return length

   def compareAwards(self, award):
      similarity = 0
      if lower(strip(self.category)) == lower(strip(award.category):
         similarity = similarity + 1
      
      if lower(strip(self.winner)) == lower(strip(award.winner)):
         similarity = similarity + 1

      if lower(strip(self.show)) == lower(strip(award.show)):
         similarity = similarity + 1

      if lower(strip(self.presenter)) == lower(strip(award.presenter)):
         similarity = similarity + 1

      return similarity