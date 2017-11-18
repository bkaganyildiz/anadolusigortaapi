from .models import Customer
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("subtype", "number_of_houses", "size_household", "avg_age", "maintype",
            "roman_catholic", "protestant", "other_religion", "no_religion", "married",
            "living_together", "other_relation", "singles", "household_without_children", "household_with_children",
            "high_level_education", "medium_level_education", "lower_level_education", "high_status", "entrepreneur",
            "farmer", "middle_management", "skilled_labourers", "unskilled_labourers", "social_class_a",
            "social_class_b1", "social_class_b2", "social_class_c", "social_class_d", "rented_house",
            "home_owners", "one_car", "two_car", "no_car", "national_health_service",
            "private_health_insurance", "income_less_30", "income_30_45", "income_45_75", "income_75_122",
            "income_more_123", "average_income", "purchasing_power_class", "private_insurance", "firms_insurance",
            "agriculture_insurance", "car_policies", "van_policies", "motorcycle_policies", "lorry_policies",
            "trailer_policies", "tractor_policies", "agricultural_machines_policies", "moped_policies", "life_insurances",
            "private_accident_insurance", "family_accidents_insurance", "disability_insurance", "fire_policies", "surfboard_policies",
            "boat_policies", "bicycle_policies", "property_insurance_policies", "social_security_insurance_policies")
