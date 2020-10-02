# Election_Analysis

## Overview of Election Audit
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
6. Calculate total number of of votes per county.
7. Determine the total percantage of votes per county.
8. Print results to the terminal 
9. Write a text file named election_results.txt containing Election results, total cost, county results, largest county turn out, candidate results, and finnaly with winner with their respective vote count and percentage of votes.   

## Resources
- Data Source: election_results.csv
- Software: Python 3.8.5, Visual Studio Code version: 1.49.2

## Election Audit Results
The analysis of the election shows that:
- There were 367,11 votes cast in the election
- The counties were:
    - Jefferson
    - Denver
    - Arpahoe
- The counties results were:
    - Jefferson county contributed 11% of the votes with a total of 38,855 votes
    - Denver county contributed 83% of the votes with a total of 306,055 votes
    - Arapahoe county contributed 7% of the votes with a total of 24,801 votes
- The county with the most votes was:
    - Denver with 83% of the votes and a total of 306,055 votes
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham recieved 23.05% of the vote and 85,213 number of the votes.
    - Diana DeGette recieved 73.81% of the vote and recieved 272,892 number of votes.
    - Raymon Anthony Doane recieved 3.14% of the vote and recieved 11,606 number of votes.
- The winner of the election was:
    - Diana DeGette, who recieved 73.81% of the vote and 272,892 number of votes.

## Election Audit Summary
This Script would be very usefull and easily adaptable to 
reading any csv containing at least a column of Ballot ID's and their related Candidate choice. This script runs quickly and is built to run as efficecntly as possible for large sets of data. It ensures this by collecting and storing all necicary values within one iteration.  The sudo script also allows for easy modification as it clearly explains the logic of the process at every step making it flexible and easy to refactor. For excample, if we would like to include more columns and or operations one would simply need to add a `list` object or `counter` object before the iteration begins. We can see this easily spelled out for us below
![alt text](https://github.com/sebcampos/Election_Analysis/blob/master/Resources/Screen%20Shot%202020-10-02%20at%2012.31.54%20PM.png?raw=True)

Then through out the iteration or `for` loop seen below  we can add our    `if` statments to collect the relevant data. 

![alt text](https://github.com/sebcampos/Election_Analysis/blob/master/Resources/Screen%20Shot%202020-10-02%20at%2012.33.18%20PM.png?raw=True)
In thie case we see that the iteration focuses on these values
- Ballot Id
- County
- Candidate

Potentially if there was other data we would want one could simply add to this list with one accumulator/counter and one `if` statment! This script will solve all your election csv data analysis needs!