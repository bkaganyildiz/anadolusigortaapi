import inspect, random, time
from enum import IntEnum

class ChoiceEnum(IntEnum):

    @classmethod
    def choices(cls):
        # get all members of the class
        members = inspect.getmembers(cls, lambda m: not(inspect.isroutine(m)))
        # filter down to just properties
        props = [m for m in members if not(m[0][:2] == '__')]
        # format into django choice tuple
        choices = tuple([(str(p[1].value), p[0]) for p in props])
        return choices

    @classmethod
    def randomize(cls):
        # get all members of the class
        members = inspect.getmembers(cls, lambda m: not (inspect.isroutine(m)))
        # filter down to just properties
        props = [m for m in members if not (m[0][:2] == '__')]
        # format into django choice tuple
        choices = tuple([(str(p[1].value), p[0]) for p in props])
        return random.choice(choices)

def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
    return strTimeProp(start, end, '%Y/%m/%d %I:%M%p', prop)

print randomDate("2008/1/12 1:30PM", "2009/1/1 4:50AM", random.random())

def random_coordinate(startx, endx, starty, endy):
    points = (str(random.uniform(startx, endx)), str(random.uniform(starty, endy)))


# def get_matrix_data(test):
#     customers = Customer.objects.filter(isTest=test).order_by("index")
#     customers_list = []
#     for customer in customers:
#         customer_list = []
#         customer_list.append(getattr(L0, customer.subtype[3:]).value)
#         customer_list.append(customer.number_of_houses)
#         customer_list.append(customer.size_household)
#         customer_list.append(getattr(L1, customer.avg_age[3:]).value)
#         customer_list.append(getattr(L2, customer.maintype[3:]).value)
#         customer_list.append(getattr(L3, customer.roman_catholic[3:]).value)
#         customer_list.append(getattr(L3, customer.protestant[3:]).value)
#         customer_list.append(getattr(L3, customer.other_religion[3:]).value)
#         customer_list.append(getattr(L3, customer.no_religion[3:]).value)
#         customer_list.append(getattr(L3, customer.married[3:]).value)
#         customer_list.append(getattr(L3, customer.living_together[3:]).value)
#         customer_list.append(getattr(L3, customer.other_relation[3:]).value)
#         customer_list.append(getattr(L3, customer.singles[3:]).value)
#         customer_list.append(getattr(L3, customer.household_without_children[3:]).value)
#         customer_list.append(getattr(L3, customer.household_with_children[3:]).value)
#         customer_list.append(getattr(L3, customer.high_level_education[3:]).value)
#         customer_list.append(getattr(L3, customer.medium_level_education[3:]).value)
#         customer_list.append(getattr(L3, customer.lower_level_education[3:]).value)
#         customer_list.append(getattr(L3, customer.high_status[3:]).value)
#         customer_list.append(getattr(L3, customer.entrepreneur[3:]).value)
#         customer_list.append(getattr(L3, customer.farmer[3:]).value)
#         customer_list.append(getattr(L3, customer.middle_management[3:]).value)
#         customer_list.append(getattr(L3, customer.skilled_labourers[3:]).value)
#         customer_list.append(getattr(L3, customer.unskilled_labourers[3:]).value)
#         customer_list.append(getattr(L3, customer.social_class_a[3:]).value)
#         customer_list.append(getattr(L3, customer.social_class_b1[3:]).value)
#         customer_list.append(getattr(L3, customer.social_class_b2[3:]).value)
#         customer_list.append(getattr(L3, customer.social_class_c[3:]).value)
#         customer_list.append(getattr(L3, customer.social_class_d[3:]).value)
#         customer_list.append(getattr(L3, customer.rented_house[3:]).value)
#         customer_list.append(getattr(L3, customer.home_owners[3:]).value)
#         customer_list.append(getattr(L3, customer.one_car[3:]).value)
#         customer_list.append(getattr(L3, customer.two_car[3:]).value)
#         customer_list.append(getattr(L3, customer.no_car[3:]).value)
#         customer_list.append(getattr(L3, customer.national_health_service[3:]).value)
#         customer_list.append(getattr(L3, customer.private_health_insurance[3:]).value)
#         customer_list.append(getattr(L3, customer.income_less_30[3:]).value)
#         customer_list.append(getattr(L3, customer.income_30_45[3:]).value)
#         customer_list.append(getattr(L3, customer.income_45_75[3:]).value)
#         customer_list.append(getattr(L3, customer.income_75_122[3:]).value)
#         customer_list.append(getattr(L3, customer.income_more_123[3:]).value)
#         customer_list.append(getattr(L3, customer.average_income[3:]).value)
#         customer_list.append(getattr(L3, customer.purchasing_power_class[3:]).value)
#         customer_list.append(getattr(L4, customer.private_insurance[3:]).value)
#         customer_list.append(getattr(L4, customer.firms_insurance[3:]).value)
#         customer_list.append(getattr(L4, customer.agriculture_insurance[3:]).value)
#         customer_list.append(getattr(L4, customer.car_policies[3:]).value)
#         customer_list.append(getattr(L4, customer.van_policies[3:]).value)
#         customer_list.append(getattr(L4, customer.motorcycle_policies[3:]).value)
#         customer_list.append(getattr(L4, customer.lorry_policies[3:]).value)
#         customer_list.append(getattr(L4, customer.trailer_policies[3:]).value)
#         customer_list.append(getattr(L4, customer.tractor_policies[3:]).value)
#         customer_list.append(getattr(L4, customer.agricultural_machines_policies[3:]).value)
#         customer_list.append(getattr(L4, customer.moped_policies[3:]).value)
#         customer_list.append(getattr(L4, customer.life_insurances[3:]).value)
#         customer_list.append(getattr(L4, customer.private_accident_insurance[3:]).value)
#         customer_list.append(getattr(L4, customer.family_accidents_insurance[3:]).value)
#         customer_list.append(getattr(L4, customer.fire_policies[3:]).value)
#         customer_list.append(getattr(L4, customer.surfboard_policies[3:]).value)
#         customer_list.append(getattr(L4, customer.boat_policies[3:]).value)
#         customer_list.append(getattr(L4, customer.bicycle_policies[3:]).value)
#         customer_list.append(getattr(L4, customer.property_insurance_policies[3:]).value)
#         customer_list.append(getattr(L4, customer.social_security_insurance_policies[3:]).value)
#         customer_list.append(getattr(L4, customer.disability_insurance[3:]).value)
#         customer_list.append(getattr(L4, customer.disability_insurance[3:]).value)
#         customer_list.append(getattr(L4, customer.disability_insurance[3:]).value)
#         customer_list.append(getattr(L4, customer.disability_insurance[3:]).value)
#         customer_list.append(customer.number_private_insurance)
#         customer_list.append(customer.number_firms_insurance)
#         customer_list.append(customer.number_agriculture_insurance)
#         customer_list.append(customer.number_car_policies)
#         customer_list.append(customer.number_van_policies)
#         customer_list.append(customer.number_motorcycle_policies)
#         customer_list.append(customer.number_lorry_policies)
#         customer_list.append(customer.number_trailer_policies)
#         customer_list.append(customer.number_tractor_policies)
#         customer_list.append(customer.number_agricultural_machines_policies)
#         customer_list.append(customer.number_moped_policies)
#         customer_list.append(customer.number_life_insurances)
#         customer_list.append(customer.number_private_accident_insurance)
#         customer_list.append(customer.number_family_accidents_insurance)
#         customer_list.append(customer.number_disability_insurance)
#         customer_list.append(customer.number_fire_policies)
#         customer_list.append(customer.number_surfboard_policies)
#         customer_list.append(customer.number_boat_policies)
#         customer_list.append(customer.number_bicycle_policies)
#         customer_list.append(customer.number_property_insurance_policies)
#         customer_list.append(customer.number_social_security_insurance_policies)
#         customer_list.append(customer.number_mobile_home_policies)
#         print (len(customer_list))
#         customers_list.append(customers_list)
#     return customers_list



