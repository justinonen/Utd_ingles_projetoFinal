import datetime
import shutil
import pandas as pd


def record_attendance(file_name):
    """
    Prompts the user for student name, course name, and attendance status.
    Saves the attendance record to a text file with timestamp.
    """
    student = input("Student name: ")
    course = input("Course name: ")
    present = input("Present (Y/N)? ").strip().upper()
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    student = student.replace(' ', '_')
    status = "Present" if present == "Y" else "Absent"
    # entry = f"{timestamp} - Student: {student} | Course: {course} | Status: {status}\n"

    # entry = f"Student: {student} | Course: {course} | {timestamp} | Status: {status}\n"
    entry = f"{student} {course} {timestamp} {status}\n"

    with open(file_name, "a", encoding="utf-8") as file:
        file.write(entry)
    print("Attendance recorded successfully!")


def view_attendance(file_name):
    """
    Displays all attendance records stored in the text file.
    """
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            print("\n--- Attendance Records ---")
            print(file.read())
    except FileNotFoundError:
        print("No attendance records found.")
        entry = "Student Course Date Time Status\n"
        with open(file_name, "a", encoding="utf-8") as file:
            file.write(entry)


def delete_attendance(file_name):
    """
    Deletes the record containing the username of a course on a given date
    """
    temporary_file = file_name+"_temp"
    student = input("Student name: ")
    course = input("Course name: ")
    timestamp = input("Enter the date in the format (dd/mm/aaaa): ")
    call_time = input("Enter the call time in the format (hh:mm): ")
    status = input("Enter the status (Present/Absent)")
    line_to_delete = f"{student} {course} {timestamp} {call_time} {status}\n"
    print(f"{line_to_delete}")
    with open(file_name, "r", encoding="utf-8") as file, \
            open(temporary_file, "w", encoding="utf-8") as file_writing:
        deleted = False
        for line in file:
            if line != line_to_delete:
                file_writing.write(line)
            else:
                deleted = True

    # Replaces the original file with the temporary one
    shutil.move(temporary_file, file_name)
    if deleted:
        print(f"The line {line_to_delete} was removed from {file_name}.")
    else:
        print(f"The line {line_to_delete} was not removed from {file_name}.")


def menu():
    """
    Main menu loop for user interaction.
    """
    file_name = "student_attendance.txt"
    while True:
        print("\n1 - Record Attendance")
        print("2 - View Attendance")
        print("3 - delete attendance")
        print("4 - Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            record_attendance(file_name)
        elif choice == "2":
            view_attendance(file_name)
        elif choice == "3":
            delete_attendance(file_name)
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

    excel_file = "student_attendance.xlsx"
    try:
        # For a tab-separated file, use sep='\t'
        # df = pd.read_csv(file_name, sep='\t')
        df = pd.read_csv(file_name, sep=' ')

        # Save the DataFrame to an Excel file (.xlsx)
        # index=False to not include the DataFrame index as a column in Excel
        df.to_excel(excel_file, index=False)
        print(f'File "{file_name}" successfully converted to "{excel_file}"')
    except FileNotFoundError:
        print(f'Error: File "{file_name}" not found.')
    except Exception as e:
        print(f'An error occurred: {e}')


if __name__ == "__main__":
    file_name = "student_attendance.txt"
    view_attendance(file_name)
    menu()
