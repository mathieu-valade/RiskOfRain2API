from django.db import connection


def idseq(model_class):
    return '{}_id_seq'.format(model_class._meta.db_table)


def reset_sequence(model_class, value=1):
    cursor = connection.cursor()
    sequence = idseq(model_class)
    cursor.execute("ALTER SEQUENCE {} RESTART WITH {};".format(sequence, value))
