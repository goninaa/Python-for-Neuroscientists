


def compare_subjects_within_student(subj1_all_students,
                                    subj2_all_students):
    """
    Compare the two subjects with their students and print out the "preferred"
    subject for each student. Single-subject students shouldn't be printed.
    """
    for student, grades in subj1_all_students.items():
        if student in subj2_all_students.keys() and student != ('subject'):
            if max(subj1_all_students[student]) > max(subj2_all_students[student]):
                print (student, subj1_all_students['subject'])
            elif max(subj1_all_students[student]) < max(subj2_all_students[student]):
                print (student, subj2_all_students['subject'])
            elif max(subj1_all_students[student]) == max(subj2_all_students[student]):
                print (student, subj2_all_students['subject'], 'and', subj1_all_students['subject'] )


if __name__ == '__main__':
    # Question 3

    """data- students grades organized in subject dictionaries. 
    the students names are the keys and their grades are the values (first exam is first).
    each dictionry inclueds subject key which its value is the subject name. """
    history = {
        'nir': [80, 75], 
        'irit': [100, 93], 
        'ben': [80, 75],
        'dafna': [66, 60], 
        'yoni': [94, 89], 
        'sara': [80, 75],
        'subject': 'history'
    }

    maths = {
        'nir': [74, 79],
        'irit': [84, 95],
        'ben': [80, 82],
        'dafna': [92, 100], 
        'maayan': [96, 93],
        'sara': [86, 77],
        'subject': 'maths'
    }
    subj1_all_students = history
    subj2_all_students = maths
    print("Question 3 solution: ")
    compare_subjects_within_student(subj1_all_students, subj2_all_students)

            

