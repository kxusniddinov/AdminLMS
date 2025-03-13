from django.db import connection
from contextlib import closing


def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
    ]


def get_faculties():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM admin_app_faculty""")
        faculties = dict_fetchall(cursor)
        return faculties


def get_chairs():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM admin_app_chair""")
        chairs = dict_fetchall(cursor)
        return chairs


def get_groups():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT admin_app_group.id, admin_app_group.name, admin_app_faculty.name as faculty
        from admin_app_group LEFT JOIN admin_app_faculty ON admin_app_group.faculty_id = admin_app_faculty.id
        """)
        groups = dict_fetchall(cursor)
        return groups


def get_subjects():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM admin_app_subject""")
        subjects = dict_fetchall(cursor)
        return subjects


def get_teachers():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT admin_app_teacher.id, admin_app_teacher.first_name, admin_app_teacher.last_name,
        admin_app_teacher.age, admin_app_chair.name as chair_name, admin_app_subject.name as subject_name FROM 
        admin_app_teacher LEFT JOIN admin_app_chair ON admin_app_teacher.chair_id = admin_app_chair.id
        LEFT JOIN admin_app_subject ON admin_app_teacher.subject_id = admin_app_subject.id
        """)
        teachers = dict_fetchall(cursor)
        return teachers


def get_students():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT admin_app_student.id, admin_app_student.first_name, admin_app_student.last_name, 
        admin_app_student.age, admin_app_group.name as group_name, admin_app_student.image as image FROM admin_app_student
        LEFT JOIN admin_app_group ON admin_app_student.group_id = admin_app_group.id
        """)
        student = dict_fetchall(cursor)
        return student
