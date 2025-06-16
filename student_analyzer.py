# This is a list of dictionaries representing student data with various attributes.
student_data = [
    {
        "name": "Alice",
        "age": 20,
        "grade": "A",
        "subjects": ["Math", "Science", "English"],
        "attendance": 95
    },
    {
        "name": "Bob",
        "age": 22,
        "grade": "B",
        "subjects": ["History", "Math", "Art"],
        "attendance": 88
    },
    {
        "name": "Charlie",
        "age": 21,
        "grade": "C",
        "subjects": ["Science", "English", "Physical Education"],
        "attendance": 92
    }
]
def analyze_students(data):
    """
    Analyzes student data to calculate average age, attendance, and grade distribution.
    
    Args:
        data (list): List of dictionaries containing student information.
    
    Returns:
        dict: A dictionary with average age, average attendance, and grade distribution.
    """
    total_age = 0
    total_attendance = 0
    grade_distribution = {}

    for student in data:
        total_age += student["age"]
        total_attendance += student["attendance"]
        grade = student["grade"]
        if grade in grade_distribution:
            grade_distribution[grade] += 1
        else:
            grade_distribution[grade] = 1

    average_age = total_age / len(data)
    average_attendance = total_attendance / len(data)

    return {
        "average_age": average_age,
        "average_attendance": average_attendance,
        "grade_distribution": grade_distribution
    }
# Example usage
if __name__ == "__main__":
    analysis_result = analyze_students(student_data)
    print("Average Age:", analysis_result["average_age"])
    print("Average Attendance:", analysis_result["average_attendance"])
    print("Grade Distribution:", analysis_result["grade_distribution"])
# This code defines a function to analyze student data and prints the results.
# The function calculates the average age, average attendance, and the distribution of grades among students.

        
       
    