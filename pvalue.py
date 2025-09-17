In order to turn a p-value, which is a probability, into a yes or no answer, data scientists often use a pre-set significance threshold. 
#The significance threshold can be any number between 0 and 1, but a common choice is 0.05. 
#P-values that are less than this threshold are considered “significant”, while larger p-values are considered “not significant”.
# P-Value for first Hypothesis Test
p_value1 = .062
# Set the correct value for p_value1_significance
p_value1_significance = 'not significant'

# P-Value for second Hypothesis Test
p_value2 = 0.013
# Set the correct value for p_value2_significance
p_value2_significance = 'significant'

#If the p-value is significant (less than 0.05), then the correct response rate is significantly different from 70% and we want to remove the question
# P-Value for first Hypothesis Test
p_value1 = .062
# Set the correct value for remove_question_1
remove_question_1 = 'no'

# P-Value for second Hypothesis Test
p_value2 = 0.013
# Set the correct value for remove_question_2
remove_question_2 = 'yes'

#Whenever we run a hypothesis test using a significance threshold, we expose ourselves to making two different kinds of mistakes: type I errors (false positives) and type II errors (false negatives):
#Null hypothesis:          	is true	        is false
#P-value significant	      Type I Error	  Correct!
#P-value not significant	  Correct!	      Type II error

#Suppose that the average score on a standardized test is 50 points. 
#A researcher wants to know whether students who take this test in an ergonomically designed chair score significantly differently from the general population of test-takers. 
#The researcher randomly assigns 100 students to take the test in an ergonomic chair. 
#Then, the researcher runs a hypothesis test with a significance threshold of 0.05 and the following null and alternative hypotheses:

#Null: The mean score for students who take the test in an ergonomic chair is 50 points.
#Alternative: The mean score for students who take the test in an ergonomic chair is not 50 points.
#Suppose that the truth (which the researcher doesn’t know) is: if every student took the test in an ergonomic chair, the average score for all test-takers would be 52 points.

#Based on their sample of only 100 students, the researcher calculates a p-value of 0.07.
# Set the correct value for outcome
outcome = 'type two'

#####
#Setting the Type I Error Rate (false positive) 
false_positives = 0
sig_threshold = 0.05

for i in range(1000):
    sim_sample = np.random.choice(['correct', 'incorrect'], size=100, p=[0.7, 0.3])
    num_correct = np.sum(sim_sample == 'correct')
    p_val = binom_test(num_correct, 100, 0.7)
    if p_val < sig_threshold:
        false_positives += 1
        
print(false_positives/1000) #Output: 0.0512

#This code does the following:
#Set the significance threshold equal to 0.05 and a counter for false positives equal to zero.
#Repeat these steps 1000 times:
#Simulate 100 learners, where each learner has a 70% chance of answering a quiz question correctly.
#Calculate the number of simulated learners who answered the question correctly. 
#Note that, because each learner has a 70% chance of answering correctly, this number will likely be around 70, but will vary every time by random chance.
#Run a binomial test for the simulated sample where the null hypothesis is that the probability of a correct answer is 70% (0.7). 
#Note that, every time we run this test, the null hypothesis is true because we simulated our data so that the probability of a correct answer is 70%.
#Add 1 to our false positives counter every time we make a type I error (the p-value is significant). -Print the proportion of our 1000 tests (on simulated samples) that resulted in a false positive.
#Note that the proportion of false positive tests is very similar to the value of the significance threshold (0.05).

#While significance thresholds allow a data scientist to control the false positive rate for a single hypothesis test, this starts to break when performing multiple tests as part of a single study.
#For example, suppose that we are writing a quiz at codecademy that is going to include 10 questions. 
#For each question, we want to know whether the probability of a learner answering the question correctly is different from 70%. We now have to run 10 hypothesis tests, one for each question.
#If the null hypothesis is true for every hypothesis test (the probability of a correct answer is 70% for every question) and we use a .05 significance level for each test, then:
#When we run a hypothesis test for a single question, we have a 95% chance of getting the right answer (a p-value > 0.05) — and a 5% chance of making a type I error.
#When we run hypothesis tests for two questions, we have only a 90% chance of getting the right answer for both hypothesis tests (.95*.95 = 0.90) — and a 10% chance of making at least one type I error.
#When we run hypothesis tests for all 10 questions, we have a 60% chance of getting the right answer for all ten hypothesis tests (0.95^10 = 0.60) — and a 40% chance of making at least one type I error.
#To address this problem, it is important to plan research out ahead of time: decide what questions you want to address and figure out how many hypothesis tests you need to run. 
#When running multiple tests, use a lower significance threshold (eg., 0.01) for each test to reduce the probability of making a type I error.

