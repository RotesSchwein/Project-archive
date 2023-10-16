import MySQLdb
from MySQLdb.cursors import DictCursor

if __name__ == '__main__':
    connect = MySQLdb.Connect(
        host = 'database-3.cvxc3cjk1v8t.us-east-1.rds.amazonaws.com',
        port = 3306,
        user = 'admin',
        password = 'michael0808!',
        db = "random_schema_1",
        charset = 'utf8mb4'
    )

    _cursor = connect.cursor(DictCursor)

    q = """
        INSERT INTO user (
        name, nickname, email, phone_number
        )
        VALUES (
        '홍길동',
        'Hong Gil-dong',
        'hgd@gmail.com',
        '010-1234-5678'
        )
        """

    _cursor.execute(q)
    connect.commit()

    q = """
        SELECT id, name, nickname, email, phone_number, created_date, updated_date
        FROM user WHERE name = '홍길동'
        """

    _cursor.execute(q)

    _rows = _cursor.fetchall()
    print(_rows)