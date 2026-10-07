# AI-Driven Task Prioritization System

An AI-powered task management web application built with Django that helps users prioritize tasks based on task priority, status, urgency, and complexity.

## 🚀 Features

- Create, edit, and delete tasks
- Track task completion status
- AI-based task prioritization
- ML-based urgency prediction
- AI priority score and explanation
- Priority-based task management
- Clean and responsive user interface
- SQLite database for local development

## 🤖 AI / ML Approach

The system combines machine learning prediction with rule-based scoring to determine task importance.

The prioritization considers:

- Task priority
- Task status
- Urgency score
- Complexity score
- ML-predicted urgency

The system also provides an explanation for the generated AI score so users can understand why a task received its priority.

## 🛠️ Tech Stack

- Python
- Django
- Machine Learning
- SQLite
- HTML
- CSS
- JavaScript

## 📂 Project Structure

```text
ai-task-prioritization-system/
│
├── manage.py
├── ai_task_manager/
├── core/
│   ├── models.py
│   ├── views.py
│   ├── ml_model.py
│   ├── ai.py
│   ├── templates/
│   └── static/
│
└── README.md
