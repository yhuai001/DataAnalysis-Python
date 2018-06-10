import numpy as np
my_list = [92, 94, 88, 91, 87]
test_1 = np.array([92, 94, 88, 91, 87])

np.genfromtxt('test_2.csv', delimiter=',')

test_1 = np.array([92, 94, 88, 91, 87])
test_2 = np.array([79, 100, 86, 93, 91])
test_3 = np.array([87, 85, 72, 90, 92])

test_3_fixed = np.array(test_3) + 2

total_grade = test_1 + test_2 + test_3_fixed
final_grade = total_grade/3
print final_grade

coin_toss = np.array([1, 0, 0, 1, 0])
coin_toss_again = np.array([[1, 0, 0, 1, 0], [0, 0, 1, 1, 1]])
print coin_toss_again

#Select 1D
test_1 = np.array([92, 94, 88, 91, 87])
test_2 = np.array([79, 100, 86, 93, 91])
test_3 = np.array([87, 85, 72, 90, 92])

jeremy_test_2 = test_2[3]
manual_adwoa_test_1 = test_1[1:3]

#Select 2D
student_scores = np.array([[92, 94, 88, 91, 87],
                           [79, 100, 86, 93, 91],
                           [87, 85, 72, 90, 92]])

tanya_test_3 = student_scores[2,0]
cody_test_scores = student_scores [0:3,4]


#Logical 
porridge = np.array([79, 65, 50, 63, 56, 90, 85, 98, 79, 51])
cold = porridge[porridge < 60]
hot = porridge[porridge > 80]
just_right = porridge[(porridge > 60) & (porridge < 80)]

print porridge,cold,hot,just_right


#Review
temperatures = np.genfromtxt('temperature_data.csv', delimiter=',')

print temperatures

temperatures_fixed = temperatures + 3

print temperatures_fixed

monday_temperatures = temperatures_fixed[0,:]

thursday_friday_morning = temperatures_fixed[3:5,1]

temperature_extremes = temperatures_fixed[(temperatures_fixed < 50) | (temperatures_fixed > 60)]