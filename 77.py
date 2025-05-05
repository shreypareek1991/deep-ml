"""
https://www.deep-ml.com/problems/77

Task: Implement Performance Metrics Calculation
In this task, you are required to implement a function performance_metrics(actual, predicted) that computes various performance metrics for a binary classification problem. 
These metrics include:
Confusion Matrix
Accuracy
F1 Score
Specificity
Negative Predictive Value
The function should take in two lists:
actual: The actual class labels (1 for positive, 0 for negative).
predicted: The predicted class labels from the model.
Output
The function should return a tuple containing:
confusion_matrix: A 2x2 matrix.
accuracy: A float representing the accuracy of the model.
f1_score: A float representing the F1 score of the model.
specificity: A float representing the specificity of the model.
negative_predictive_value: A float representing the negative predictive value.
Constraints
All elements in the actual and predicted lists must be either 0 or 1.
Both lists must have the same length.
Example:
Input:
actual = [1, 0, 1, 0, 1]
predicted = [1, 0, 0, 1, 1]
print(performance_metrics(actual, predicted))
Output:
([[2, 1], [1, 1]], 0.6, 0.667, 0.5, 0.5)
Reasoning:
The function calculates the confusion matrix, accuracy, F1 score, specificity, and negative predictive value based on the input labels. 
The resulting values are rounded to three decimal places as required.
"""

def performance_metrics(actual: list[int], predicted: list[int]) -> tuple:
    
    TP=0
    FP=0
    TN=0
    FN=0

    for y,y_hat in zip(actual, predicted):
        if y == y_hat:
            if y == 0:
                TN+=1
            else:
                TP+=1
        else :
            if y_hat == 1:
                FP+=1
            else:
                FN+=1        


    specificity = TN/(TN+FP)
    npv = TN/(TN+FN)
    f1 = TP/(TP+0.5*(FP+FN))
    accuracy = (TP+TN)/(TP+TN+FP+FN)
    cm = [[TP,FN],[FP,TN]]

    res = [cm, accuracy, f1, specificity, npv]

    return [round(r, 3) if not isinstance(r, list) else r for r in res]
