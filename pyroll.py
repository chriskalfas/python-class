import pandas as pd
import numpy as np
edata = "D:/main.py/pyroll/election_data.csv"
edata_enc= pd.read_csv(edata, encoding="ISO-8859-1")
edata_enc.head()
Total_votes = edata_enc["Candidate"].count()
print(Total_votes)
per_can = edata_enc.groupby(["Candidate"]).count()
per_can
winner = per_can.max()
winner
voters_df = pd.DataFrame( 
    {"Candidate": ["Correy","Khan","Li","O'Tooley"],
     "Percentage of Votes": [(704200/3521001), (2218231/3521001),(492940/3521001),(105630/3521001)],
     "(Total Votes)": [704200, 2218231, 492940, 105630]
    }
)
print(voters_df)
print("Election Results")
print("------------------------------------------------")
print("Total Votes: " + str(Total_votes))
print(voters_df)
print()
new_edata = pd.DataFrame({
    "Election Results":[("Total Votes: " + str(Total_votes)), voters_df]
    })
new_edata.to_csv("D:/main.py/pyroll/pyroll.txt", index=False, header=True)