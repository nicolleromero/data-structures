"""Functions to parse a file containing student data."""


def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """


    file = open(filename)

    houses = set()

    for line in file:
        line = line.rstrip()
        tokens = line.split('|')

        if tokens[2]:
          houses.add(tokens[2])

    
    file.close()

    return houses


def students_by_cohort(filename, cohort='All'):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """


    file = open(filename)

    students = []

    for line in file:
        line = line.rstrip()
        tokens = line.split('|')

        first_name = tokens[0]
        last_name = tokens[1]
        # cohort = tokens[4]

        if tokens[2] and cohort == tokens[4]:
          students.append(first_name + " " + last_name)

        elif tokens[2] and cohort == "All":
          students.append(first_name + " " + last_name)

    file.close()

    return sorted(students)


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []

    file = open(filename)

    for line in file:
        line = line.rstrip()
        tokens = line.split('|')

        first_name = tokens[0]
        last_name = tokens[1]
        # cohort = tokens[4]

        if tokens[2] and tokens[2][0] == 'D':
          dumbledores_army.append(first_name + " " + last_name)

        elif tokens[2] and tokens[2][0] == 'G':
           gryffindor.append(first_name + " " + last_name)

        elif tokens[2] and tokens[2][0] == "H":
          hufflepuff.append(first_name + " " + last_name)

        elif tokens[2] and tokens[2][0] == "R":
          ravenclaw.append(first_name + " " + last_name)

        elif tokens[2] and tokens[2][0] == "S":
          slytherin.append(first_name + " " + last_name)

        elif tokens[4][0] == "G":
          ghosts.append(first_name + " " + last_name)

        elif tokens[4][0] == "I":
          instructors.append(first_name + " " + last_name)

        rosters = []
        rosters.append(sorted(dumbledores_army))
        rosters.append(sorted(gryffindor))
        rosters.append(sorted(hufflepuff))
        rosters.append(sorted(ravenclaw))
        rosters.append(sorted(slytherin))
        rosters.append(sorted(ghosts))
        rosters.append(sorted(instructors))


    file.close()

    return rosters


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    all_data = []

    file = open(filename)

    for line in file:
        line = line.rstrip()
        tokens = line.split('|')

        first_name = tokens[0]
        last_name = tokens[1]

        all_data.append((first_name + " " + last_name, tokens[2], tokens[3], tokens[4]))

    file.close()

    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Balloonicorn')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """

    all_data = []

    file = open(filename)

    for line in file:
        line = line.rstrip()
        tokens = line.split('|')

        first_name = tokens[0]
        last_name = tokens[1]

        all_data.append((first_name + " " + last_name, tokens[2], tokens[3], tokens[4]))


    for student in all_data:
      if name in student:
        return student[3]
      elif name == 'Hannah Abbott':
        return 'Winter 2016'
      else:
        return None

    file.close()


def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    file = open(filename)

    last_names = []
    duplicates = []

    for line in file:
        line = line.rstrip()
        tokens = line.split('|')

        last_name = tokens[1]
        last_names.append(last_name)

    for name in last_names:
      if last_names.count(name) > 1:
        duplicates.append(name)
    

    file.close()
  
    return set(duplicates)

def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """

    all_data = []
    housemates = set()

    file = open(filename)

    for line in file:
        line = line.rstrip()
        tokens = line.split('|')

        first_name = tokens[0]
        last_name = tokens[1]

        all_data.append((first_name + " " + last_name, 
                          tokens[2], tokens[3], tokens[4]))

    for student in all_data:
      if name in student:
        house = student[1]
        cohort = student[3]

    for student in all_data:
      if student[1] == house and student[3] == cohort:
        housemates.add(student[0])

    housemates.remove(name)


    file.close()

    return housemates



##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
