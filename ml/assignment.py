#1) Given a list of numbers with some missing values represented as None, replace the missing values with the mean of the non-missing numbers.Example Input:[10, None, 30, None, 50]
print('1)')
def replace_none_with_mean(numbers):
    non_missing_numbers = [num for num in numbers if num is not None]
    mean_value = sum(non_missing_numbers) / len(non_missing_numbers) if non_missing_numbers else 0
    
    return [mean_value if num is None else num for num in numbers]
numbers = [10, None, 30, None, 50]
result = replace_none_with_mean(numbers)
print(result)
print(' ')


#---------------------------------------------------------------------------------------
#2 Implement a function to scale a list of numbers using Min-Max Scaling. Use the formula: scaled(x)=x-min/max-min Example Input:[20, 40, 60, 80, 100]

print("2)")
def min_max_scale(numbers):
    min_value = min(numbers)
    max_value = max(numbers)
    scaled_numbers = [(x - min_value) / (max_value - min_value) for x in numbers]
    return scaled_numbers
numbers = [20, 40, 60, 80, 100]
scaled_numbers = min_max_scale(numbers)
print(scaled_numbers)
print(' ')

#---------------------------------------------------------------------------------------
#3) Implement a function to binarize a list of numbers given a threshold. All values greater than or equal to the threshold should become 1, and all others should become 0.Example Input: [1.5, 2.3, 0.8, 3.0], threshold = 2.0

print("3)")
def binarize(numbers, threshold):
    return [1 if num >= threshold else 0 for num in numbers]
numbers = [1.5, 2.3, 0.8, 3.0]
threshold = 2.0
binarized_numbers = binarize(numbers, threshold)
print(binarized_numbers)
print(' ')
#---------------------------------------------------------------------------------------

#4) Given a function f(x)=2x+3, write a function to approximate f(x) by calculating the outputs for a given list of inputs.Example Input: inputs = [1, 2, 3]

print("4)")
def approximate_function(inputs):
    return [2 * x + 3 for x in inputs]
inputs = [1, 2, 3]
outputs = approximate_function(inputs)
print(outputs)
print(' ')
#---------------------------------------------------------------------------------------
#5) Write a function to standardize a list of numbers by subtracting the mean and dividing by the standard deviation.Example Input:[10, 20, 30, 40]

print("5)")
import math
def standardize(numbers):
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    std_dev = math.sqrt(variance)
    standardized_numbers = [(x - mean) / std_dev for x in numbers]
    return standardized_numbers
numbers = [10, 20, 30, 40]
standardized_numbers = standardize(numbers)
print(standardized_numbers)
print(' ')
#---------------------------------------------------------------------------------------
#6) Given a list of data points and their corresponding labels, create a concept representation as a dictionary where keys are unique labels and values are lists of points belonging to each label.Example Input:data = [1, 2, 3, 4, 5], labels = ["A", "B", "A", "B", "A"]

print("6)")
def create_concept_representation(data, labels):
    concept_representation = {}
    for point, label in zip(data, labels):
        if label not in concept_representation:
            concept_representation[label] = []
        concept_representation[label].append(point)
    return concept_representation
data = [1, 2, 3, 4, 5]
labels = ["A", "B", "A", "B", "A"]
concept_representation = create_concept_representation(data, labels)
print(concept_representation)
print(' ')
#--------------------------------------------
#7) Write a function that categorizes a given machine learning task based on its description. The categories are "Supervised Learning" or "Unsupervised Learning" Example Input: "Predict the price of a house based on features like size, location, and age."

print("7)")
def categorize_task(description):
    supervised_phrases = ["predict", "classification", "target variable", "labeled data"]
    unsupervised_phrases = ["cluster", "group", "pattern", "grouping", "dimensionality reduction", "anomaly detection"]
    description = description.lower()
    for phrase in supervised_phrases:
        if phrase in description:
            return "Supervised Learning"
    for phrase in unsupervised_phrases:
        if phrase in description:
            return "Unsupervised Learning"
    return "Supervised Learning"
description = "Predict the price of a house based on features like size, location, and age."
category = categorize_task(description)
print(category)
print(' ')
#---------------------------------------------------------------------------------------
#8) Write a function that categorizes a given machine learning task based on its description. The categories are "Supervised Learning" or "Unsupervised Learning" "Group customers based on their purchasing patterns."

print("8)")
def categorize_task(description):
    description = description.lower()
    supervised_keywords = ["predict", "classification", "labels", "target"]
    unsupervised_keywords = ["group", "cluster", "patterns", "dimension reduction", "anomaly detection"]
    if any(keyword in description for keyword in unsupervised_keywords):
        return "Unsupervised Learning"
    if any(keyword in description for keyword in supervised_keywords):
        return "Supervised Learning"
    return "Unsupervised Learning"
description = "Group customers based on their purchasing patterns."
category = categorize_task(description)
print(category)
print(' ')
#---------------------------------------------------------------------------------------
#9) Predict Y using a Simple Linear Model. Task: Write a function that calculates the predicted y value given the slope m, intercept c,and an input x using the formula for a line:y=mx+c
#Input:
#Three values:
#m (float): The slope of the line.
#c (float): The y-intercept of the line.
#x (float): The input value.
#Output: A single float value representing y

print("9)")
def predict_y(m, c, x):
    y = m * x + c
    return y
m = 2.5  # slope
c = 3.0  # y-intercept
x = 4.0  # input value
y = predict_y(m, c, x)
print("Predicted y:", y)
print(' ')
#---------------------------------------------------------------------------------------

#10) Given an array of integers representing raw data, remove duplicates and sort the data in ascending order. Write a function to accomplish this.Example Input:[4, 2, 2, 8, 3, 3, 1]

print("10)")
def remove_duplicates_and_sort(data):
    unique_data = sorted(set(data))
    return unique_data
data = [4, 2, 2, 8, 3, 3, 1]
sorted_data = remove_duplicates_and_sort(data)
print(sorted_data)
