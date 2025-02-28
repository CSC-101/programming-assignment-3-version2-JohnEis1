from build_data import CountyDemographics

# task one
# Finds the total population in 2014
#input a list of instances of the class CountyDemographics output int
def population_total(counties: list[CountyDemographics]) -> int:
    pop_tot = 0
    for num in counties:
        pop_tot += num.population.get('2014 Population')
    return pop_tot

# Task two
#This function fliters by state
#Input a list of instances of the class CountyDemographics output a list with the given state name looked for
def filter_by_state(counties: list[CountyDemographics], state:str)->list[CountyDemographics]:
    NL = []
    for name in counties:
        if name.state == state:
            NL.append(name)
    return NL


# Task three
#Each one of these functions is given a parameter of type float(except population_below_poverty_level
#which on takes one parameter of a list of instances of the class CountyDemographics) and
#a list of instances of the class CountyDemographics parameter looks for a certain percentage then
#mutilpes it by the total 2014 Population
#Input a list of instances of the class CountyDemographics out put an int of new percent of population
def population_by_education(counties: list[CountyDemographics], bd: str) -> float:
    pop_ed = 0
    for num in counties:
        if bd not in num.education:
            return []
        per = num.education.get(bd)/100
        pop_ed += num.population.get('2014 Population')*per
    return pop_ed

def population_by_ethnicity(counties: list[CountyDemographics], ek: str) -> float:
    pop_race = 0
    for num in counties:
        if ek not in num.ethnicities:
            return []
        per = num.ethnicities.get(ek) / 100
        pop_race += num.population.get('2014 Population') * per
    return pop_race

def population_below_poverty_level(counties: list[CountyDemographics]) -> float:
    if len(counties) == 0:
        return []
    pop_bp = 0
    for num in counties:
        per = num.income.get('Persons Below Poverty Level')/100
        pop_bp += num.population.get('2014 Population')*per
    return pop_bp

#Task four
#Each one of these functions is given a parameter of type float(except population_below_poverty_level
#which on takes one parameter of a list of instances of the class CountyDemographics) and
#a list of instances of the class CountyDemographics parameter, and then utilizes 2 functions, population_total()
#and the other is the corresponding sub-population finder function to find the percentage of the sub-
#population in the total
#Input a list of instances of the class CountyDemographics and float(except, percent_below_poverty_level)
#Output is a float that represents the total percentage
def percent_by_education(counties: list[CountyDemographics], bd: str) -> float:
    total_population = population_total(counties)
    try:
        total_bd = population_by_education(counties, bd)
    except KeyError as e:
        print(e)
        return 0
    total_per = (total_bd * 100) / total_population
    return total_per

def percent_by_ethnicity(counties:list[CountyDemographics], key:str) -> float:
    total_population = population_total(counties)
    try:
        total_key = population_by_ethnicity(counties,key)
    except KeyError as e:
        print(e)
        return 0
    total_per = (total_key * 100) / total_population
    return total_per

def percent_below_poverty_level(counties:list[CountyDemographics]) -> float:
    if len(counties) == 0:
        return 0
    total_population = population_total(counties)
    try:
        total_key = population_below_poverty_level(counties)
        print(total_key)

    except KeyError as e:
        print(e)
        return 0
    total_per = (total_key * 100) / total_population

    return total_per

#Task five
#These functions check if a given percentage of a county is greater or less than a certain threshold.
#input list of instances of the class CountyDemographics, string as a key, and a float as a perecentage
#output  list of instances of the class CountyDemographics of the  list of instances of the class CountyDemographics
#that fit in the given percentage
#a
def education_greater_than(counties: list[CountyDemographics], ek:str, g:float) -> list[CountyDemographics]:
    nl = []
    for county in counties:
        if county.education[ek] > g:
            nl.append(county)
    return nl

def education_less_than(counties:list[CountyDemographics], ek:str, l:float) -> list[CountyDemographics]:
    nl = []
    for county in counties:
        if county.education[ek] < l:
            nl.append(county)
    return nl
#b
def ethnicity_greater_than(counties: list[CountyDemographics], ek:str, g:float) -> list[CountyDemographics]:
    nl = []
    for county in counties:
        if county.ethnicities[ek] > g:
            nl.append(county)
    return nl
def ethnicity_less_than(counties: list[CountyDemographics], ek:str, l:float) -> list[CountyDemographics]:
    nl = []
    for county in counties:
        if county.ethnicities[ek] < l:
            nl.append(county)
    return nl
#c
def below_poverty_level_greater_than(counties:list[CountyDemographics], value:float) -> list[CountyDemographics]:
    nl = []
    for county in counties:
        if county.income['Persons Below Poverty Level'] > value:
            nl.append(county)
    return nl
def below_poverty_level_less_than(counties:list[CountyDemographics], value:float) -> list[CountyDemographics]:
    nl = []
    for county in counties:
        if county.income['Persons Below Poverty Level'] < value:
            nl.append(county)
    return nl




