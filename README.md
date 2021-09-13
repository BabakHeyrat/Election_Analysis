# Election_Analysis


## Project Overview
A Colorado board of Elections employee has given me the following tasks to complete the election audit of a recent local congressional election.

1. Calulate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
6. Determine the number of votes by county
7. Calculate the percentage of the votes each county won
8. Determine the county with the most votes

## Resources 
- Data Source: election_results.csv
- Software: Python 3.8.5 Visual Studio 1.60.0

## Audit Results
The analysis of the election show that:

-There were 369,711 votes cast

-The candidates were:
    
    -Charles Casper Stockham
    -Diana DeGette
    -Raymon Anthony Doane

-The candidate results were:
   
    -Charles Casper Stockham: 23.0%  of the vote (85,213 votes)
    -Diana DeGette: 73.8% of the vote (272,892 votes)
    -Raymon Anthony Doane: 3.1% of the votes (11,606 votes)

-The winner of the elction was:
    
    -Diana DeGette with 73.8% of the vote and 272,892 vptes
 
 resources/election_results.png
 
 -The counties in which the election took place were:
 
    -Jefferson
    -Denver
    -Arapahoe
    
-Counties by total votes cast and percentage of the total vote:

    -Jefferson: 10.5% of the vote, 38,855 votes cast
    -Denver: 82.8% of the vote, 306,055 votes cast
    -Arapahoe: 6.7% of the vote, 24,801 votes cast
 
 
 The largest county by vote count is:
 
    -Denver, with 82.8% of the vote (306,055 votes). 
    
  resources/counties.png
  
  ## Election-Audit Summary
  This election can be used over again for different data sets by simply swaping out the refrenced data set. 
  
  resources/variable.png
  
  As you can see in the above, the file_to_load variable can be redefined to reference any other data set; guaranteeing ease of use in swapping in and out of voting results from future elections. Granted, the csv file should be formatted in a manner in which the various rows function still refer to the same headers. 
 
