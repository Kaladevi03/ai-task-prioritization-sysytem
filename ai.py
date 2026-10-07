def calculate_ai_score_and_reason(task):
    score = 0
    reasons = []

    # Priority
    if task.priority == "high":
        score += 60
        reasons.append("High priority (+60)")
    elif task.priority == "medium":
        score += 40
        reasons.append("Medium priority (+40)")
    else:
        score += 20
        reasons.append("Low priority (+20)")

    # Status
    if task.status == "pending":
        score += 30
        reasons.append("Pending (+30)")
    elif task.status == "in_progress":
        score += 15
        reasons.append("In progress (+15)")

    # NEW: urgency
    score += task.urgency_score * 2
    reasons.append(f"Urgency ({task.urgency_score} × 2)")

    # NEW: complexity
    score += task.complexity_score * 1.5
    reasons.append(f"Complexity ({task.complexity_score} × 1.5)")

    return score, " | ".join(reasons)


