# Election_Analysis

## Overiew of this election audit analysis
A Colorado Board of Elections employee has assigned the following tasks to complete an audit of the recent local congressional election.

1. Calculate the total number of votes cast
2. Calculate the number of votes cast from each county.
3. Calculate the percentage of the votes cast from each country.
4. Determine the county with the largest voter turnout.
5. Get a complete list of candidates who received votes
6. Calculate the total number of votes that each candidate received.
7. Calculate the percentage of votes each candidate won.
8. Determine the winner of the election base on the popular vote.

The results were produced by analyzing a comma-separated value (CSV) file that contained the election data.

A python script was created to examine the file contents, row-by-row, and tally the election results.  The results were presented on-screen to the computer terminal, and were written to a text file.  The on-screen data was used to confirm that the data written to the text file was complete and correct.

Finally, a brief analysis was performed within Microsoft Excel to confirm that the script accurately counted the data.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.13, Visual Studio Code 1.70.1, OS: Windows_NT x64 10.0.19043

## Election-Audit Results
The analysis of the election shows that:

* There were 369,711 votes cast in the election
* The counties that participated in the election were:
	* Jefferson: 10.5% (38,855)
	* Denver: 82.8% (306,055)
	* Arapahoe: 6.7% (24,801)
* Denver had the largest voter turnout.
* The candidates were:
	* Charles Casper Stockham
	* Diana DeGette
	* Raymon Anthony Doane
* The candidate results were:
	* Charles Casper Stockham: 23.0% (85,213)
	* Diana DeGette: 73.8% (272,892)
	* Raymon Anthony Doane: 3.1% (11,606)
* The winner of the election was:
	* Diana DeGette, who received 73.8% of the vote and 272,892 votes.
	
## Terminal Results
The python script operation produced the following output at the operator terminal:

![Script output at Terminal](Resources/Git-BASH.png)

## Text File Results
The python script produced the following text file report of the election results:

![Text file output](Resources/text_file.png)

# Election-Audit Conclusion
The python script was succussfully utilized to analyze the election data and produce a report that provides relevant details of the participating counties, candidates, and the election results.

## Future Extensions
The python script was successfully applied to the audit of this local congressional election.

With some small changes, the script could be applied to city, town, or state elections. These changes would account for the scope and type of election to present the results with meaningful labels and outcomes.  For example, the CSV file might contain the results for a town mayoral election with results reported across different town precincts.

```
# 1: Create a county list and county votes dictionary.
county_names = []
county_votes = {}


# 2: Track the largest county and county voter turnout.
largest_turnout_county_name = ""
largest_turnout = 0
```
These variable can be renamed to track data within precincts.

```
# 1: Create a list of precincts and precinct-votes dictionary.
precinct_names = []
precinct_votes = {}


# 2: Track the largest precinct voter turnout.
largest_turnout_precinct_name = ""
largest_turnout = 0
```

Similar changes can be made to the main result processing loops to use the new variables and prepare the results report using the correct labelling for the election.

```
    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:
        # 6b: Retrieve the county vote count.
        county_vote = county_votes.get(county_name)
```
This loop could be updated to process the precinct data.

```
    # 6a: Write a for loop to get the precinct from the precinct dictionary.
    for precinct_name in precinct_votes:
        # 6b: Retrieve the precinct vote count.
        precinct_vote = precinct_votes.get(precinct_name)
```
And finally, the reported output can be updated to present the results in a meaningful way.

```
    # 7: Print the county with the largest turnout to the terminal.
    largest_turnout_results = (
        f"-------------------------\n"
        f"Largest County Turnout: {largest_turnout_county_name}\n"
        f"-------------------------\n")
```

The report would contain labels indicating the precinct data.

```
    # 7: Print the precinct with the largest turnout to the terminal.
    largest_turnout_results = (
        f"-------------------------\n"
        f"Largest Precinct Turnout: {largest_turnout_precinct_name}\n"
        f"-------------------------\n")
```


