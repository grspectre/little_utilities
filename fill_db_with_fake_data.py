import psycopg2
from random import randint
import json
from utils.str_utils import generate_sentence


def generate_data() -> tuple[str, int, str]:
    data = []
    for _ in range(randint(10, 30)):
        data.append(generate_sentence(randint(6, 15)))
    return generate_sentence(randint(3, 6)), randint(0, 10000000), json.dumps(data)


def insert_random_data_rows(count: int) -> None:
    connection = None
    try:
        connection = psycopg2.connect('dbname=postgres user=postgres password=example')
        cursor = connection.cursor()
        for _ in range(count):
            db_id = insert_random_data_row(connection, cursor)
            print('Added row with id: {}'.format(db_id))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


def insert_random_data_row(conn, cur) -> int:
    sql = "INSERT INTO test_table2(name, int_value, data) VALUES (%s, %s, %s) RETURNING id"
    cur.execute(sql, generate_data())
    ins_id = cur.fetchone()[0]
    conn.commit()
    return ins_id


def main() -> None:
    insert_random_data_rows(250000)


if __name__ == '__main__':
    main()
