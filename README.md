# ScaledConversions
# Final HCI 584 Project

Scaled Conversions converts standard scores, t-scores, and z-scores into scaled scores. Originally designed for use in a neuropsychology practice, reporting all test results in the same format allows for direct comparisons between tests and provides a clearer picture about the patient's level of functioning within each cognitive domain. 

In this project file, you will find two scripts necessary to produce the final product, an excel workbook containing the tests names, original scores, and converted scores. 

> 1. define_tests.py: Enter the tests administered. Produces file test_lists.p
> 2. convert_scores.py: Enter the original scores. Produces file ScoreConversions.xlsx

# Requirements

- Python 3.7 or higher
- Microsoft Excel
- [https://github.com/JBiars/ScaledConversions]

All packages used in this program are part of the Python Standard Library. No separate installations are required. 
The program can be run through the Command-Line Interface, Anaconda, or Visual Studio Code. Visual Studio Code is recommended.

# Usage

The user must begin by running define_tests.py. This program will prompt the user to enter tests for each cognitive domain in order:
 - Language
 - Spatial
 - Memory
 - Attention
 - Executive Function
 
The user will press 1 to indicate they want to add another test and press 0 when they have finished entering tests for that domain. 
After the user indicates they have finished entering tests for the final domain, Executive Function, the program will ask if they need to add any additional tests. By following the prompts, the user can either choose to add more tests to a specific domain by pressing 1 and selecing the domain they want or they can indicate that they have finished by pressing 0. This will generate the test_lists.p file.
 
The user then runs convert_scores.py to open the test_lists.p file and begin entering the original scores to be converted. After all the scores have been entered, the program will perform the necessary calculations and store the results in the excel workbook ScoreConversions.xlsx. 

# Known Issues
Although there are no known bugs at this time, there is also no way to delete a test, replace a score type, or replace an original score once it has been entered. If an error is made, the user will need to start over. 

# Acknowledgements
Thank you to Dr. Chris Harding, Iowa State University, for his assistance with this project. 






