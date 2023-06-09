# Insurance-charge-prediction
Using conditional statements to predict the insurance charges, another approach to model calling other than pickling

for the cleaned dataset, the following changes have been made:
# sex: female = 1, male = 0
# smoking: yes = 1, no = 0
# region: northeast,  southeast, southwest, northwest : 0,1,2,3
# bmi 0,1,2:( <=27.74),(>27.74 - =<33.155), (>33.155) ; 27.74 and 33.154 are the two median halves of the column
# age: <39 == 0 ; >39 == 1 ; average age is 39

In order to, utilize the project, just change the arbitrary values in testing to your desired values.
If you wish to only use conditions/pickle for production, just remove the other part
