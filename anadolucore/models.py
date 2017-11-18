# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .choices import (
        L0,
        L1,
        L2,
        L3,
        L4
    )

# Create your models here.
class Customer(models.Model):
    isTest = models.BooleanField(default=False)
    index = models.IntegerField(default=0)
    subtype = models.CharField(max_length=3, choices=L0.choices(), default=L0.High_Income_expensive_child)
    number_of_houses = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(10), MinValueValidator(1)]
     )
    size_household = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(6), MinValueValidator(1)]
     )
    avg_age = models.CharField(max_length=3, choices=L1.choices(), default=L1.years_20_30)
    maintype = models.CharField(max_length=3, choices=L2.choices(), default=L2.Average_Family)
    roman_catholic   = models.CharField(max_length=3, choices=L3.choices(), default=L3.percent_0)
    protestant   = models.CharField(max_length=3, choices=L3.choices(), default=L3.percent_0)
    other_religion   = models.CharField(max_length=3, choices=L3.choices(), default=L3.percent_0)
    no_religion   = models.CharField(max_length=3, choices=L3.choices(), default=L3.percent_0)
    married   = models.CharField(max_length=3, choices=L3.choices(), default=L3.percent_0)
    living_together   = models.CharField(max_length=3, choices=L3.choices(), default=L3.percent_0)
    other_relation   = models.CharField(max_length=3, choices=L3.choices(), default=L3.percent_0)
    singles   = models.CharField(max_length=3, choices=L3.choices(), default=L3.percent_0)
    household_without_children   = models.CharField(max_length=3, choices=L3.choices(), default=L3.percent_0)
    household_with_children   = models.CharField(max_length=3, choices=L3.choices(), default=L3.percent_0)
    high_level_education   = models.CharField(max_length=3, choices=L3.choices(), default=L3.percent_0)
    medium_level_education   = models.CharField(max_length=3, choices=L3.choices(), default=L3.percent_0)
    lower_level_education   = models.CharField(max_length=3, choices=L3.choices(), default=L3.percent_0)
    high_status   = models.CharField(max_length=3, choices=L3.choices(), default=L3.percent_0)
    entrepreneur   = models.CharField(max_length=3, choices=L3.choices(), default=L3.percent_0)
    farmer   = models.CharField(max_length=3, choices=L3.choices(), default=L3.percent_0)
    middle_management = models.CharField(max_length=3, choices=L3.choices(), default=L3.percent_0)
    skilled_labourers = models.CharField(max_length=3, choices=L3.choices(), default=L3.percent_0)
    unskilled_labourers = models.CharField(max_length=3, choices=L3.choices(), default=L3.percent_0)
    social_class_a = models.CharField(max_length=3, choices=L3.choices(), default=L3.percent_0)
    social_class_b1 = models.CharField(max_length=3, choices=L3.choices(), default=L3.percent_0)
    social_class_b2 = models.CharField(max_length=3, choices=L3.choices(), default=L3.percent_0)
    social_class_c = models.CharField(max_length=3, choices=L3.choices(), default=L3.percent_0)
    social_class_d = models.CharField(max_length=3, choices=L3.choices(), default=L3.percent_0)
    rented_house = models.CharField(max_length=3, choices=L3.choices(), default=L3.percent_0)
    home_owners = models.CharField(max_length=3, choices=L3.choices(), default=L3.percent_0)
    one_car = models.CharField(max_length=3, choices=L3.choices(), default=L3.percent_0)
    two_car = models.CharField(max_length=3, choices=L3.choices(), default=L3.percent_0)
    no_car = models.CharField(max_length=3, choices=L3.choices(), default=L3.percent_0)
    national_health_service = models.CharField(max_length=3, choices=L3.choices(), default=L3.percent_0)
    private_health_insurance = models.CharField(max_length=3, choices=L3.choices(), default=L3.percent_0)
    income_less_30 = models.CharField(max_length=3, choices=L3.choices(), default=L3.percent_0)
    income_30_45 = models.CharField(max_length=3, choices=L3.choices(), default=L3.percent_0)
    income_45_75 = models.CharField(max_length=3, choices=L3.choices(), default=L3.percent_0)
    income_75_122 = models.CharField(max_length=3, choices=L3.choices(), default=L3.percent_0)
    income_more_123 = models.CharField(max_length=3, choices=L3.choices(), default=L3.percent_0)
    average_income = models.CharField(max_length=3, choices=L3.choices(), default=L3.percent_0)
    purchasing_power_class = models.CharField(max_length=3, choices=L3.choices(), default=L3.percent_0)
    private_insurance = models.CharField(max_length=3, choices=L4.choices(), default=L4.financial_0)
    firms_insurance = models.CharField(max_length=3, choices=L4.choices(), default=L4.financial_0)
    agriculture_insurance = models.CharField(max_length=3, choices=L4.choices(), default=L4.financial_0)
    car_policies = models.CharField(max_length=3, choices=L4.choices(), default=L4.financial_0)
    van_policies = models.CharField(max_length=3, choices=L4.choices(), default=L4.financial_0)
    motorcycle_policies = models.CharField(max_length=3, choices=L4.choices(), default=L4.financial_0)
    lorry_policies = models.CharField(max_length=3, choices=L4.choices(), default=L4.financial_0)
    trailer_policies = models.CharField(max_length=3, choices=L4.choices(), default=L4.financial_0)
    tractor_policies = models.CharField(max_length=3, choices=L4.choices(), default=L4.financial_0)
    agricultural_machines_policies = models.CharField(max_length=3, choices=L4.choices(), default=L4.financial_0)
    moped_policies = models.CharField(max_length=3, choices=L4.choices(), default=L4.financial_0)
    life_insurances = models.CharField(max_length=3, choices=L4.choices(), default=L4.financial_0)
    private_accident_insurance = models.CharField(max_length=3, choices=L4.choices(), default=L4.financial_0)
    family_accidents_insurance = models.CharField(max_length=3, choices=L4.choices(), default=L4.financial_0)
    disability_insurance = models.CharField(max_length=3, choices=L4.choices(), default=L4.financial_0)
    fire_policies = models.CharField(max_length=3, choices=L4.choices(), default=L4.financial_0)
    surfboard_policies = models.CharField(max_length=3, choices=L4.choices(), default=L4.financial_0)
    boat_policies = models.CharField(max_length=3, choices=L4.choices(), default=L4.financial_0)
    bicycle_policies = models.CharField(max_length=3, choices=L4.choices(), default=L4.financial_0)
    property_insurance_policies = models.CharField(max_length=3, choices=L4.choices(), default=L4.financial_0)
    social_security_insurance_policies = models.CharField(max_length=3, choices=L4.choices(), default=L4.financial_0)
    number_private_insurance = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(12), MinValueValidator(1)]
    )
    number_firms_insurance = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(12), MinValueValidator(1)]
    )
    number_agriculture_insurance = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(12), MinValueValidator(1)]
    )
    number_car_policies = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(12), MinValueValidator(1)]
    )
    number_van_policies = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(12), MinValueValidator(1)]
    )
    number_motorcycle_policies = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(12), MinValueValidator(1)]
    )
    number_lorry_policies = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(12), MinValueValidator(1)]
    )
    number_trailer_policies = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(12), MinValueValidator(1)]
    )
    number_tractor_policies = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(12), MinValueValidator(1)]
    )
    number_agricultural_machines_policies = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(12), MinValueValidator(1)]
    )
    number_moped_policies = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(12), MinValueValidator(1)]
    )
    number_life_insurances = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(12), MinValueValidator(1)]
    )
    number_private_accident_insurance = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(12), MinValueValidator(1)]
    )
    number_family_accidents_insurance = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(12), MinValueValidator(1)]
    )
    number_disability_insurance = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(12), MinValueValidator(1)]
    )
    number_fire_policies = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(12), MinValueValidator(1)]
    )
    number_surfboard_policies = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(12), MinValueValidator(1)]
    )
    number_boat_policies = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(12), MinValueValidator(1)]
    )
    number_bicycle_policies = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(12), MinValueValidator(1)]
    )
    number_property_insurance_policies = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(12), MinValueValidator(1)]
    )
    number_social_security_insurance_policies = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(12), MinValueValidator(1)]
    )
    number_mobile_home_policies = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(1), MinValueValidator(0)]
    )

