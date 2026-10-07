import numpy as np
from sklearn.linear_model import LogisticRegression

# priority: high=2, medium=1, low=0
# status: pending=2, in_progress=1, completed=0

X = np.array([
    [2, 2],  # high + pending
    [2, 1],  # high + in_progress
    [1, 2],  # medium + pending
    [1, 1],  # medium + in_progress
    [0, 2],  # low + pending
    [0, 1],  # low + in_progress
    [0, 0],  # completed
])

y = np.array([90, 80, 70, 60, 40, 30, 10])

model = LogisticRegression()
model.fit(X, y)

def predict_ai_priority(task):
    priority =task.priority
    description = task.description
    status = task.status
    complexity =task.complexity_score

    return predicted_priority
    