# Overview of Election Audit: 

This report is done with the purpose of assiting the Colorado Board of Elections in the election audit for the US congressional prescient in Colorado. 

The analysis consists in reporting the total number of votes cast, the total number of votes for each candidate, the percentage of votes for each candidate, and the winner of the election based on the popular vote.

This process could be done using excel but will be automated using Python.

There are several voting methods taken into account: Mail-in Ballot, punch cards, and direct recording electronic.  These three methods will determine the final election results. After the votes are counted, this audit generates a vote count report to certify this US congressional race.

## Election-Audit Results:                                 
  
* 369,711 votes were cast in this congressional election.  

* The following are the Votes and percentages for each county in the precint: Jefferson: 10.5% (38,855), Denver: 82.8% (306,055), and Arapahoe: 6.7% (24,801).

* Denver was the county with the largest number of votes.

* Here is the breakdown of the number of votes and the percentage of the total votes each candidate received: Charles Casper Stockham: 23.0% (85,213), Diana      DeGette: 73.8% (272,892), Raymon Anthony Doane: 3.1% (11,606).

* Diana DeGette won the elections with a vote count of (272,892), representing a  73.8%  of the total votes.


<p align = "center">
<img src="https://github.com/nativelasquez-austin/Election_Analysis/blob/main/Resources/Election_results.png" width="250" height="250" />


## Election-Audit Summary: 

This analysis could have been done using excel but we prefered to automate the process using Python.  The reason why we used Python is because we want to save time in future analysis of this same nature.

We propose to the Election Comission that the code writen here can be re-used at other congressional districts, senatorial districts, and local elections.

The following are some examples of how this can be done:

* We will have a csv file with the tabulated election results such as the following:


<img src="https://github.com/nativelasquez-austin/Election_Analysis/blob/main/Resources/csv_file.png" width="250" height="250" />


* Python version 3 will be installed in the computer we will perform the analysis.  It is an open source software which means it's free for any organization

* Despite being an open source software, the information processed in the program remains confidential and will only be stored in the organization's computer.

* An example of how we can re-use the code is by replacing in the following piece of code the name of any csv file with the tabulated results:

<img src="https://github.com/nativelasquez-austin/Election_Analysis/blob/main/Resources/your_file_name.png" width="400" height="200" />

* As we saw in point #1 in our tabulated results spreadsheet the County name is in the second column and the Candidate name is in the third column.  We only need to know the order of the columns and what each one represents to replace in the following piece of code and make the code match any csv file.

<img src="https://github.com/nativelasquez-austin/Election_Analysis/blob/main/Resources/columns.png" width="400" height="200" />

To sum up, our recommendation for the Elections Comission is to use the code contain in this analysis for future elections.  This will save many hours of skilled work and money, and will warranty the election results are known in a timely manner.
