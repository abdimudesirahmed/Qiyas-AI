import numpy as np
print("NumPy imported successfully!")
arr = np.array([1, 2, 3, 4])
print(arr * 2)

grades = np.array([
[85, 90, 88],
[70, 65, 60],
[95, 92, 98]
])
print(grades)

attendance = np.ones((5, 7))
print(attendance)

employee_ids = np.arange(1000, 1010)
time = np.linspace(0, 24, 6)
print(employee_ids)
print(time)

sales = np.array([[200,300, 250], [400, 500, 450]])
print(sales.shape)
print(sales.ndim)
print(sales.size)


ages= np.linspace(1, 25, 5)
print(ages)
print(ages.ndim)
print(ages.shape)


sales = np.array([
[200, 300, 250],
[400, 500, 450],
[150, 200, 180]
])

print(sales[0,1])
print(sales[:,0])
print(sales[:2,2:])
print(sales[1:, :1])

sales = np.array([
    [120, 150, 180],
    [200, 220, 210],
    [170, 160, 190]
])
print("TA:", sales[1, 1])
print("All morning:", sales[:, 0])
print("All evening:", sales[:, 2:])
print("AM Sales:", sales[0, :])
print("T and W  Sales:", sales[1:, :])
print("Afternoon and evening Sales:", sales[:, 1:])



scores = np.array([
    [80, 75, 90],
    [65, 70, 60],
    [95, 88, 92],
    [72, 78, 85]
])
print("sara's physics grade:", scores[1, 1])
print("all math grades:", scores[:, 0])
print("all chemistry grades:", scores[:, 2])
print("john's all scores:", scores[2, :])
print("first 2 students:", scores[:2, :])


average = np.mean(scores, axis=0)
print("Average scores for each subject:", average)
average = np.mean(scores, axis=1)
print("Average scores for each student:", average)