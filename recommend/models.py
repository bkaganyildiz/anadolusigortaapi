# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.db import models

# Create your models here.

class RecommendationResult(models.Model):
    name = models.CharField(max_length=100, blank=False)
    bayes_values = models.TextField(blank=True)
    mlp_values = models.TextField(blank=True)
    dt_values = models.TextField(blank=True)
    number_of_features = models.TextField(blank=True)
    picture = models.TextField(blank=True)

    def set_bayes(self, list):
        self.bayes_values = json.dumps(list)
    def set_mlp(self, list):
        self.mlp_values = json.dumps(list)
    def set_dt(self, list):
        self.dt_values = json.dumps(list)
    def set_features(self, list):
        self.number_of_features = json.dumps(list)
    def get_bayes(self):
        return json.dump(self.bayes_values)
    def get_bayes(self):
        return json.dump(self.bayes_values)
    def get_mlp(self):
        return json.dump(self.bayes_values)
    def get_dt(self):
        return json.dump(self.bayes_values)
    def get_features(self):
        return json.dump(self.bayes_values)

    def __unicode__(self):
        return self.name