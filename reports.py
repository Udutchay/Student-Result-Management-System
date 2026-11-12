from results import calculate_totals_and_averages, assign_grade

def sort_students(students, sort_by="average", reverse=True):
    if sort_by == "name":
        return sorted(students, key=lambda s: s.full_name.lower())
    elif sort_by == "average":
        return sorted(students, key=lambda s: calculate_totals_and_averages(s.scores)[1], reverse=reverse)
    return students

def get_class_statistics(students):
    if not students:
        return None
    
    averages = []
    for student in students:
        _, avg = calculate_totals_and_averages(student.scores)
        averages.append(avg)
        
    highest = max(averages)
    lowest = min(averages)
    class_avg = round(sum(averages) / len(averages), 2)
    
    return {
        "highest": highest,
        "lowest": lowest,
        "class_average": class_avg
    }

def generate_report_card(student):
    total, avg = calculate_totals_and_averages(student.scores)
    grade = assign_grade(avg)
    
    report = []
    report.append("=" * 40)
    report.append("          STUDENT REPORT CARD           ")
    report.append("=" * 40)
    report.append(f"Student ID   : {student.student_id}")
    report.append(f"Full Name    : {student.full_name}")
    report.append(f"Class/Form   : {student.class_form}")
    report.append(f"Gender       : {student.gender}")
    report.append(f"Date of Birth: {student.dob}")
    report.append("-" * 40)
    report.append("SUBJECT SCORES:")
    if student.scores:
        for subj, score in student.scores.items():
            report.append(f"  - {subj.ljust(15)}: {score}")
    else:
        report.append("  No scores recorded yet.")
    report.append("-" * 40)
    report.append(f"Total Score  : {total}")
    report.append(f"Average Score: {avg}")
    report.append(f"Final Grade  : {grade}")
    report.append("=" * 40)
    
    return "\n".join(report)