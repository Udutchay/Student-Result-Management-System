import json
import os

FILENAME = "students.json"


def load_data():
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "r") as f:
                return json.load(f)
        except:
            return []
    return []


def save_data(students):
    with open(FILENAME, "w") as f:
        json.dump(students, f, indent=4)

def calculate_results(scores):
    if not scores:
        return 0, 0
    total = sum(scores.values())
    average = total / len(scores)
    return total, round(average, 2)


def get_grade(avg):
    if avg >= 70:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 45:
        return "D"
    else:
        return "F"

def main():
   
    students = load_data()

    while True:
        print("\n=== STUDENT RESULT SYSTEM ===")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Record / Update Scores (At least 5 subjects)")
        print("4. View Student Report Card")
        print("5. Save and Exit")
        
        choice = input("\nChoose an option (1-5): ").strip()
        
        if choice == "1":
            print("\n--- Add New Student ---")
            student_id = input("Enter Student ID: ").strip()
            
            
            exists = False
            for s in students:
                if s["student_id"] == student_id:
                    exists = True
                    break
            if exists:
                print("Error: A student with this ID already exists!")
                continue

            name = input("Enter Full Name: ").strip()
            class_form = input("Enter Class/Form: ").strip()
            gender = input("Enter Gender: ").strip()
            dob = input("Enter Date of Birth: ").strip()
            
            new_student = {
                "student_id": student_id,
                "name": name,
                "class": class_form,
                "gender": gender,
                "dob": dob,
                "scores": {}  
            }
            
            students.append(new_student)
            save_data(students)
            print("Student added successfully!")

        elif choice == "2":
            print("\n--- Registered Students ---")
            if not students:
                print("No students found.")
            else:
                for s in students:
                    print(f"ID: {s['student_id']} | Name: {s['name']} | Class: {s['class']}")

        elif choice == "3":
            print("\n--- Record Scores ---")
            student_id = input("Enter Student ID: ").strip()
            
            student = None
            for s in students:
                if s["student_id"] == student_id:
                    student = s
                    break
            
            if not student:
                print("Student not found!")
                continue
            
            print(f"Entering scores for {student['name']}")
            scores = {}
            
            for i in range(5):
                subj_name = input(f"Enter Subject {i+1} Name: ").strip()
                while True:
                    try:
                        score_val = float(input(f"Enter score for {subj_name} (0-100): "))
                        if 0 <= score_val <= 100:
                            scores[subj_name] = score_val
                            break
                        else:
                            print("Score must be between 0 and 100.")
                    except ValueError:
                        print("Please enter a valid number.")
            
            student["scores"] = scores
            save_data(students)
            print("Scores saved successfully!")

        elif choice == "4":
            print("\n--- View Report Card ---")
            student_id = input("Enter Student ID: ").strip()
            
            student = None
            for s in students:
                if s["student_id"] == student_id:
                    student = s
                    break
            
            if not student:
                print("Student not found!")
                continue
            
            total, avg = calculate_results(student["scores"])
            grade = get_grade(avg) if student["scores"] else "N/A"
            
            print("\n" + "=" * 30)
            print("        REPORT CARD")
            print("=" * 30)
            print(f"ID   : {student['student_id']}")
            print(f"Name : {student['name']}")
            print(f"Class: {student['class']}")
            print("-" * 30)
            print("Subject Scores:")
            if student["scores"]:
                for subj, sc in student["scores"].items():
                    print(f"  - {subj}: {sc}")
            else:
                print("  No scores recorded yet.")
            print("-" * 30)
            print(f"Total Score  : {total}")
            print(f"Average Score: {avg}")
            print(f"Final Grade  : {grade}")
            print("=" * 30)

        elif choice == "5":
            save_data(students)
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()