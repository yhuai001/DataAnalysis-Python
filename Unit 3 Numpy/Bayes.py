#Bayes
import numpy as np
p_disease_and_correct = 0.99 * (1.00/100000)
p_no_disease_and_incorrect = (100000-1.00)/100000 * 0.01
print  p_disease_and_correct,p_no_disease_and_incorrect

#Bayes Theorem
import numpy as np
p_positive_given_disease = 0.99
p_disease = 0.00001
p_positive = 0.01 + 0.00001
p_disease_given_positive = p_positive * p_disease / p_positive_given_disease
print p_disease_given_positive

#Spam Filters
import numpy as np
b = 'enhancement'
a = 'spam'
p_spam = 0.2
p_enhancement_given_spam = 0.05 
p_enhancement = p_enhancement_given_spam * p_spam + 0.001 * 0.8
p_spam_enhancement = p_enhancement_given_spam * p_spam / p_enhancement 
print p_spam_enhancement 