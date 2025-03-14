import data
import build_data
import unittest
from data import CountyDemographics
from hw3 import *
# These two values are defined to support testing below. The
# data within these structures should not be modified. Doing
# so will affect later tests.
#
# The data is defined here for visibility purposes in the context
# of this course.
full_data = build_data.get_data()

ex = [CountyDemographics(
    # age
    {'Percent 65 and Older': 17.5,
         'Percent Under 18 Years': 18.1,
         'Percent Under 5 Years': 4.8},
    # county
    'San Luis Obispo County',
    # education
    {"Bachelor's Degree or Higher": 31.5,
               'High School or Higher': 89.6},
    # ethnicities
    {'American Indian and Alaska Native Alone': 1.4,
                 'Asian Alone': 3.8,
                 'Black Alone': 2.2,
                 'Hispanic or Latino': 22.0,
                 'Native Hawaiian and Other Pacific Islander Alone': 0.2,
                 'Two or More Races': 3.4,
                 'White Alone': 89.0,
                 'White Alone, not Hispanic or Latino': 69.5},
    # income
    {'Median Household Income': 58697,
            'Per Capita Income': 29954,
            'Persons Below Poverty Level': 14.3},
    # population
    {'2010 Population': 269637,
                '2014 Population': 279083,
                'Population Percent Change': 3.5,
                'Population per Square Mile': 81.7},
    # state
    'CA'
)]
reduced_data = [
    data.CountyDemographics(
        {'Percent 65 and Older': 13.8,
         'Percent Under 18 Years': 25.2,
         'Percent Under 5 Years': 6.0},
        'Autauga County',
        {"Bachelor's Degree or Higher": 20.9,
         'High School or Higher': 85.6},
        {'American Indian and Alaska Native Alone': 0.5,
         'Asian Alone': 1.1,
         'Black Alone': 18.7,
         'Hispanic or Latino': 2.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 1.8,
         'White Alone': 77.9,
         'White Alone, not Hispanic or Latino': 75.6},
        {'Per Capita Income': 24571,
         'Persons Below Poverty Level': 12.1,
         'Median Household Income': 53682},
        {'2010 Population': 54571,
         '2014 Population': 55395,
         'Population Percent Change': 1.5,
         'Population per Square Mile': 91.8},
        'AL'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.0},
        'Crawford County',
        {"Bachelor's Degree or Higher": 14.3,
         'High School or Higher': 82.2},
        {'American Indian and Alaska Native Alone': 2.5,
         'Asian Alone': 1.6,
         'Black Alone': 1.6,
         'Hispanic or Latino': 6.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 2.8,
         'White Alone': 91.5,
         'White Alone, not Hispanic or Latino': 85.6},
        {'Per Capita Income': 19477,
         'Persons Below Poverty Level': 20.2,
         'Median Household Income': 39479},
        {'2010 Population': 61948,
         '2014 Population': 61697,
         'Population Percent Change': -0.4,
         'Population per Square Mile': 104.4},
        'AR'),
    data.CountyDemographics(
        {'Percent 65 and Older': 17.5,
         'Percent Under 18 Years': 18.1,
         'Percent Under 5 Years': 4.8},
        'San Luis Obispo County',
        {"Bachelor's Degree or Higher": 31.5,
         'High School or Higher': 89.6},
        {'American Indian and Alaska Native Alone': 1.4,
         'Asian Alone': 3.8,
         'Black Alone': 2.2,
         'Hispanic or Latino': 22.0,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 3.4,
         'White Alone': 89.0,
         'White Alone, not Hispanic or Latino': 69.5},
        {'Per Capita Income': 29954,
         'Persons Below Poverty Level': 14.3,
         'Median Household Income': 58697},
        {'2010 Population': 269637,
         '2014 Population': 279083,
         'Population Percent Change': 3.5,
         'Population per Square Mile': 81.7},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 11.5,
         'Percent Under 18 Years': 21.7,
         'Percent Under 5 Years': 5.8},
        'Yolo County',
        {"Bachelor's Degree or Higher": 37.9,
         'High School or Higher': 84.3},
        {'American Indian and Alaska Native Alone': 1.8,
         'Asian Alone': 13.8,
         'Black Alone': 3.0,
         'Hispanic or Latino': 31.5,
         'Native Hawaiian and Other Pacific Islander Alone': 0.6,
         'Two or More Races': 5.0,
         'White Alone': 75.9,
         'White Alone, not Hispanic or Latino': 48.3},
        {'Per Capita Income': 27730,
         'Persons Below Poverty Level': 19.1,
         'Median Household Income': 55918},
        {'2010 Population': 200849,
         '2014 Population': 207590,
         'Population Percent Change': 3.4,
         'Population per Square Mile': 197.9},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 19.6,
         'Percent Under 18 Years': 25.6,
         'Percent Under 5 Years': 4.9},
        'Butte County',
        {"Bachelor's Degree or Higher": 17.9,
         'High School or Higher': 89.2},
        {'American Indian and Alaska Native Alone': 1.0,
         'Asian Alone': 0.3,
         'Black Alone': 0.2,
         'Hispanic or Latino': 5.8,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 2.3,
         'White Alone': 96.1,
         'White Alone, not Hispanic or Latino': 90.6},
        {'Per Capita Income': 20995,
         'Persons Below Poverty Level': 15.7,
         'Median Household Income': 41131},
        {'2010 Population': 2891,
         '2014 Population': 2622,
         'Population Percent Change': -9.4,
         'Population per Square Mile': 1.3},
        'ID'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.9},
        'Pettis County',
        {"Bachelor's Degree or Higher": 15.2,
         'High School or Higher': 81.8},
        {'American Indian and Alaska Native Alone': 0.7,
         'Asian Alone': 0.7,
         'Black Alone': 3.4,
         'Hispanic or Latino': 8.3,
         'Native Hawaiian and Other Pacific Islander Alone': 0.3,
         'Two or More Races': 1.9,
         'White Alone': 92.9,
         'White Alone, not Hispanic or Latino': 85.5},
        {'Per Capita Income': 19709,
         'Persons Below Poverty Level': 18.4,
         'Median Household Income': 38580},
        {'2010 Population': 42201,
         '2014 Population': 42225,
         'Population Percent Change': 0.1,
         'Population per Square Mile': 61.9},
        'MO'),
    data.CountyDemographics(
        {'Percent 65 and Older': 18.1,
         'Percent Under 18 Years': 21.6,
         'Percent Under 5 Years': 6.5},
        'Weston County',
        {"Bachelor's Degree or Higher": 17.2,
         'High School or Higher': 90.2},
        {'American Indian and Alaska Native Alone': 1.7,
         'Asian Alone': 0.4,
         'Black Alone': 0.7,
         'Hispanic or Latino': 4.2,
         'Native Hawaiian and Other Pacific Islander Alone': 0.0,
         'Two or More Races': 2.2,
         'White Alone': 95.0,
         'White Alone, not Hispanic or Latino': 91.5},
        {'Per Capita Income': 28764,
         'Persons Below Poverty Level': 11.2,
         'Median Household Income': 55461},
        {'2010 Population': 7208,
         '2014 Population': 7201,
         'Population Percent Change': -0.1,
         'Population per Square Mile': 3.0},
        'WY')
    ]

class TestCases(unittest.TestCase):
    pass

    # Part 1
    def test_population_total_1(self):
      expected = 655813
      #expected from reduced data
      value = population_total(reduced_data)
      self.assertEqual(expected, value)

    def test_population_total_2(self):
      expected = 318857056
      value = population_total(full_data)
      self.assertEqual(expected, value)
    # test population_total

    # Part 2
    def test_filter_by_state(self):
        state = 'AL'
        e = [data.CountyDemographics(
        {'Percent 65 and Older': 13.8,
         'Percent Under 18 Years': 25.2,
         'Percent Under 5 Years': 6.0},
        'Autauga County',
        {"Bachelor's Degree or Higher": 20.9,
         'High School or Higher': 85.6},
        {'American Indian and Alaska Native Alone': 0.5,
         'Asian Alone': 1.1,
         'Black Alone': 18.7,
         'Hispanic or Latino': 2.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 1.8,
         'White Alone': 77.9,
         'White Alone, not Hispanic or Latino': 75.6},
        {'Per Capita Income': 24571,
         'Persons Below Poverty Level': 12.1,
         'Median Household Income': 53682},
        {'2010 Population': 54571,
         '2014 Population': 55395,
         'Population Percent Change': 1.5,
         'Population per Square Mile': 91.8},
        'AL'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.0},
        'Crawford County',
        {"Bachelor's Degree or Higher": 14.3,
         'High School or Higher': 82.2},
        {'American Indian and Alaska Native Alone': 2.5,
         'Asian Alone': 1.6,
         'Black Alone': 1.6,
         'Hispanic or Latino': 6.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 2.8,
         'White Alone': 91.5,
         'White Alone, not Hispanic or Latino': 85.6},
        {'Per Capita Income': 19477,
         'Persons Below Poverty Level': 20.2,
         'Median Household Income': 39479},
        {'2010 Population': 61948,
         '2014 Population': 61697,
         'Population Percent Change': -0.4,
         'Population per Square Mile': 104.4},
        'AR')]
        A = filter_by_state(e, state)
        expected = ['AL']
        self.assertEqual(expected, A)
    # test filter_by_state

    # Part 3
    # test population_by_education
    def test_population_by_education_1(self):
        bd = "Bachelor's Degree or Higher"
        e = [
    data.CountyDemographics(
        {'Percent 65 and Older': 13.8,
         'Percent Under 18 Years': 25.2,
         'Percent Under 5 Years': 6.0},
        'Autauga County',
        {"Bachelor's Degree or Higher": 20.9,
         'High School or Higher': 85.6},
        {'American Indian and Alaska Native Alone': 0.5,
         'Asian Alone': 1.1,
         'Black Alone': 18.7,
         'Hispanic or Latino': 2.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 1.8,
         'White Alone': 77.9,
         'White Alone, not Hispanic or Latino': 75.6},
        {'Per Capita Income': 24571,
         'Persons Below Poverty Level': 12.1,
         'Median Household Income': 53682},
        {'2010 Population': 54571,
         '2014 Population': 55395,
         'Population Percent Change': 1.5,
         'Population per Square Mile': 91.8},
        'AL')]
        expected = 11577.555
        A = population_by_education(e, bd)
        self.assertEqual(expected, A)

    def test_population_by_education_2(self):
        bd = "Bachelor's Degree or Higher"
        e = []
        expected = 0
        A = population_by_education(e, bd)
        self.assertEqual(expected, A)


    # test population_by_ethnicity
    def test_population_by_ethnicity(self):
        self.assertAlmostEqual(population_by_ethnicity(ex, 'Black Alone'),6139.826)

    def test_population_by_ethnicity_2(self):
        self.assertAlmostEqual(population_by_ethnicity(ex, 'Black'),[])


    # test population_below_poverty_level
    def test_population_below_poverty_level(self):
        self.assertAlmostEqual(population_below_poverty_level(ex),39908.869)

    def test_population_below_poverty_level_2(self):
        nl = []
        self.assertAlmostEqual(population_below_poverty_level(nl),[])

    # Part 4
    # test percent_by_education
    def test_percent_education(self):
        self.assertEqual(percent_by_education(ex,"Bachelor's Degree or Higher"), 31.5)

    def test_percent_education_2(self):
        self.assertEqual(percent_by_education(ex,"Degree"), 0)


    # test percent_by_ethnicity
    def test_percent_ethnicity(self):
        self.assertEqual(percent_by_ethnicity(ex,'Two or More Races'), 3.4)

    def test_percent_ethnicity_2(self):
        self.assertEqual(percent_by_ethnicity(ex,'Race'), 0)


    # test percent_below_poverty_level
    def test_percent_below_poverty_level(self):
        self.assertEqual(percent_below_poverty_level(ex), 14.3)

    def test_percent_below_poverty_level_2(self):
        nl = []
        self.assertEqual(percent_below_poverty_level(nl), 0)
    # Part 5

    # test education_greater_than
    def test_ed_greater_than(self):
        self.assertEqual(education_greater_than(ex, "Bachelor's Degree or Higher",0),ex)

    def test_ed_greater_than_2(self):
        self.assertEqual(education_greater_than(ex, "Bachelor's Degree or Higher",60),[])
    # test education_less_than
    def test_ed_less_than_1(self):
        self.assertEqual(education_less_than(ex, "Bachelor's Degree or Higher", 60), ex)

    def test_ed_less_than_2(self):
        self.assertEqual(education_less_than(ex, "Bachelor's Degree or Higher", 0), [])


    # test ethnicity_greater_than
    def test_eth_greater_than(self):
        self.assertEqual(ethnicity_greater_than(ex, "Two or More Races", 0), ex)

    def test_eth_greater_than_2(self):
        self.assertEqual(ethnicity_greater_than(ex, "Two or More Races", 60), [])
    # test ethnicity_less_than
    def test_eth_less_than_1(self):
        self.assertEqual(ethnicity_less_than(ex, "Two or More Races", 60), ex)

    def test_eth_less_than_2(self):
        self.assertEqual(ethnicity_less_than(ex, "Two or More Races", 0), [])


    # test below_poverty_level_greater_than
    def test_below_poverty_level_greater_than(self):
        self.assertEqual(below_poverty_level_greater_than(ex, 0),ex)

    def test_below_poverty_level_greater_than_2(self):
        self.assertEqual(below_poverty_level_greater_than(ex, 30), [])
    # test below_poverty_level_less_than
    def test_below_poverty_level_less_than(self):
        self.assertEqual(below_poverty_level_less_than(ex, 30),ex)

    def test_below_poverty_level_less_than_2(self):
        self.assertEqual(below_poverty_level_less_than(ex, 0),[])


if __name__ == '__main__':
    unittest.main()
