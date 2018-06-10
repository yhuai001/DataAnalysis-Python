#Side By Side Bars

from matplotlib import pyplot as plt

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
middle_school_a = [80, 85, 84, 83, 86]
middle_school_b = [73, 78, 77, 82, 86]

def create_x(t, w, n, d):
    return [t*x + w*n for x in range(d)]
school_a_x = create_x(2, 0.8, 1, 5)
school_b_x = create_x(2, 0.8, 2, 5)

plt.figure(figsize=(10,8))
ax = plt.subplot()  
plt.bar(school_a_x, middle_school_a)
plt.bar(school_b_x,middle_school_b)
middle_x = [ (a + b) / 2.0 for a, b in zip(school_a_x, school_b_x)]

ax.set_xticks(middle_x)
ax.set_xticklabels(unit_topics)

plt.legend(["Middle School A", "Middle School B"])
plt.title('Test Averages on Different Units')
plt.ylabel('test average')
plt.xlabel('unit')
plt.show()
plt.savefig('my_side_by_side.png')