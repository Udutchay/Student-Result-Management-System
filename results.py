def calculate_totals_and_averages(scores):
    if not scores:
        return 0, 0.0
    total = sum(scores.values())
    average = total / len(scores)
    return total, round(average, 2)

def assign_grade(average):
    if average >= 70:
        return 'A'
    elif average >= 60:
        return 'B'
    elif average >= 50:
        return 'C'
    elif average >= 45:
        return 'D'
    else:
        return 'F'