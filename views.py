from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .ai import calculate_ai_score_and_reason
from .ml_model import predict_ai_priority


def add_task(request):
    if request.method == "POST":
            title=request.POST.get("title", ""),
            description=request.POST.get("description", ""),
            priority = request.POST.get("priority", "medium")
            status=request.POST.get("status", "pending")

            task = Task.objects.create(
            title=title,
            description=description,
            priority=priority,
            status=status,
        )
        
        # numeric inputs
            task.urgency_score = int(request.POST.get("urgency_score", 5))
            task.complexity_score = int(request.POST.get("complexity_score", 5))

        # ML decides priority
            predicted_priority = predict_ai_priority(task)
            task.priority = predicted_priority

        # rule-based AI score + reason
            score, reason = calculate_ai_score_and_reason(task)
            task.ai_score = score
            task.ai_reason = reason
            task.save()
            return redirect("task_list")
    return render(request, "core/add_task.html")


# core/views.py (near top)
def calculate_ai_score_and_reason(task):
    score = 0
    reasons = []

    # priority
    if task.priority == "high":
        score += 60
        reasons.append("High priority (+60)")
    elif task.priority == "medium":
        score += 40
        reasons.append("Medium priority (+40)")
    else:
        score += 20
        reasons.append("Low priority (+20)")

    # status
    if task.status == "pending":
        score += 30
        reasons.append("Pending (+30)")
    elif task.status == "in_progress":
        score += 15
        reasons.append("In progress (+15)")
    else:  # completed or anything else
        reasons.append("Completed (+0)")

    ml_score = predict_ai_priority(task.priority, task.status)
    score += int(ml_score)
    reasons.append(f"ML predicted urgency ({ml_score})")

    return score, " | ".join(reasons)


def task_list(request):
    tasks = Task.objects.all().order_by('-ai_score','-created_at')

    return render(request, 'core/tasks.html', {'tasks': tasks})



def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')

    

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        task.title = request.POST.get("title")
        task.description = request.POST.get("description")
        task.priority = request.POST.get("priority")
        task.status = request.POST.get("status")

        score, reason = calculate_ai_score_and_reason(task)
        task.ai_score = score
        task.ai_reason = reason
        task.save()
    
        return redirect("task_list")

    return render(request, "core/edit_task.html", {"task": task})

def toggle_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if task.status == "pending":
        task.status = "in_progress"
    elif task.status == "in_progress":
        task.status = "completed"
    else:
        task.status = "pending"

    score, reason = calculate_ai_score_and_reason(task)
    task.ai_score = score
    task.ai_reason = reason
    task.save()

    return redirect("task_list")



