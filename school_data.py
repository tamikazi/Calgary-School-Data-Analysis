# school_data.py
# Tahmid Kazi
#
# A terminal-based application for computing and printing statistics based on given input.
# Detailed specifications are provided via the Assignment 3 git repository.

import numpy as np
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

# Array of school names
school_names = np.array(["Centennial High School", "Robert Thirsk School", "Louise Dean School", "Queen Elizabeth High School", 
"Forest Lawn High School", "Crescent Heights High School", "Western Canada High School", "Central Memorial High School", 
"James Fowler High School", "Ernest Manning High School", "William Aberhart High School", "National Sport School", "Henry Wise Wood High School", 
"Bowness High School", "Lord Beaverbrook High School", "Jack James High School", "Sir Winston Churchill High School", "Dr. E. P. Scarlett High School", 
"John G Diefenbaker High School", "Lester B. Pearson High School"])

# Array of school codes
school_codes = np.array(["1224", "1679", "9626", "9806", "9813", "9815", "9816", "9823", "9825", "9826", "9829", "9830", "9836", "9847", 
"9850", "9856", "9857", "9858", "9860", "9865"])

# 3 dimensional array storing the school data in given_data.py (years, schools, grades)
data = np.array([year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022]).reshape(10, 20, 3)

# Build dictionary mapping school names to school codes
schools_dictionary = {}
for x, y in zip(school_names, school_codes):
    schools_dictionary[x] = y

def get_school_data():
    """
    Prompts the user to enter the name or numerical code of a school and then retrieve the corresponding data. 

    Raises:
        ValueError: Requires the user to input a valid name or code, otherwise will print an error message and re-prompt the user.

    Returns:
        tuple: A tuple containing the school name (str), code (str) and index (int)
    """

    while True:
        try:
            input1 = input("Please enter the high school name or school code: ")
            if input1 in school_names:
                name = input1
                code = schools_dictionary[input1]
                break
            elif input1 in school_codes:
                code = input1
                name = " ".join([x for x, y in schools_dictionary.items() if y == input1]) # Finds the school name (key) associated with the school code (value) in the schools_dictionary
                break
            else:
                raise ValueError()
        except ValueError:
                print("You must enter a valid school name or code.")

    index = np.where(school_names == name)[0][0]
    return name, code, index

def school_stats(name, code, index):
    """
    Prints enrollment statistics for the user specified school.

    Args:
        name (str): Name of the school.
        code (str): Numerical code of the school.
        index (int): Index of the school in the data array
    """
    # Subarray view of the data array based on the user's selected school.
    school = data[:, index, :]

    # Prints school name and code
    print("""School Name: {0}, School Code: {1}""".format(name, code))

    # Loops through and prints the mean enrollment per grade across all years.
    for i, mean in enumerate(np.nanmean(school, axis=0)):
        print("Mean enrollment for Grade 1{0}: {1}".format(i, int(mean)))

    # Calculates and prints the maximum enrollment for a single grade.
    print("Highest enrollment for a single grade:", int(np.nanmax(school)))

    # Calculates and prints the minimum enrollment for a single grade.
    print("Lowest enrollment for a single grade:", int(np.nanmin(school)))

    # Loops through and prints the total enrollment per year across all grades
    for i in range(10):
        school_year_totals = int(np.nansum(data[i, index, :3]))
        print("Total enrollment for 20{0}: {1}".format((i + 13), school_year_totals))

    # Calculates and prints the total 10 year enrolment and the mean total enrollment over 10 years.
    ten_year_total = int(np.nansum(school))
    print("Total 10 year enrollment:", ten_year_total)
    print("Mean total enrollment over 10 years:", int(ten_year_total / 10))

    # Determines if the school has any enrolment values above 500 using a masking operation:
    #   If yes, it will calculate and print the median value of all the enrollment values above 500.
    #   If no, it will print that there are no enrollments over 500.
    if np.any(school > 500):
        print("For all enrollments over 500, the median value was:", int(np.nanmedian(school[school > 500])))
    else:
        print("No enrollments over 500.")

def general_stats():
    """Prints the general enrollment data for all schools"""

    print("Mean enrollment in 2013:", int(np.nanmean(year_2013)))

    print("Mean enrollment in 2022:", int(np.nanmean(year_2022)))

    print("Total graduating class of 2022:", int(np.nansum(data[9, :, 2])))

    print("Highest enrollment for a single grade:", int(np.nanmax(data)))

    print("Lowest enrollment for a single grade:", int(np.nanmin(data)))

def main():
    """Main function to run the enrollment program."""
    print("ENSF 592 School Enrollment Statistics")

    # Prints shape and dimensions of the full data array
    print("Shape of full data array:", data.shape)
    print("Dimensions of full data array:", data.ndim)

    # Prompts for user for input through the get_school_data function and gets the values for school name, code and index.
    name, code, index = get_school_data()

    # Passes the school name, code and index into the school_stats function for calculations and printing.
    print("\n***Requested School Statistics***\n")
    school_stats(name, code, index)
    
    # Calls the general_stats function to calculate and print the general stats.
    print("\n***General Statistics for All Schools***\n")
    general_stats()

if __name__ == '__main__':
    main()