# oracle 접속 모듈을 만들어 보세요
#
# 단일 셀렉트(파라미터 있는거 , 없는거)
# 다건 셀렉트 (파라미터 있는거 , 없는거)
# 업데이트
# 인서트


import cx_Oracle


class DBManager:

    def __init__(self):
        self.conn = None
        self.get_connection()

    def __del__(self):
        try:
            print("소멸자")
            if self.conn:
                self.conn.close()
        except Exception as err:
            print("__del__ 예외", err)

    def get_connection(self):
        self.conn = cx_Oracle.connect("java", "oracle", "127.0.0.1:1521/XE", encoding="utf-8")

        return self.conn

    # def db_close(self) -> None:
    #     try:
    #         if self.conn:
    #             self.conn.close()
    #     except Exception as err:
    #         print(err)
    def makeDictFactory(self, cursor):
        columnNames = [d[0] for d in cursor.description]

        def createRow(*args):
            return dict(zip(columnNames, args))

        return createRow

    def selectOne(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        output = None
        for row in cursor:
            for i in range(len(row)):
                # print(row[i], end=" ")
                output = row[i]
        cursor.close()
        # self.db_close()
        return output

    def selectOneParam (self, query, t):

        cursor = self.conn.cursor()
        cursor.execute(query, t)
        output = None
        for row in cursor:
            for i in range(len(row)):
                # print(row[i], end=" ")
                output = row[i]
        cursor.close()
        return output

    def selectList(self, query):

        cursor = self.conn.cursor()
        cursor.execute(query)
        cursor.rowfactory = self.makeDictFactory(cursor)
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def selectListParam(self, query, t):
        cursor = self.conn.cursor()
        cursor.execute(query, t)
        cursor.rowfactory = self.makeDictFactory(cursor)
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def insert(self, query, t):
        cursor = self.conn.cursor()
        cursor.execute(query, t)
        self.conn.commit()
        cursor.close()

    def merge(self, query, t):
        cursor = self.conn.cursor()
        cursor.execute(query, t)
        self.conn.commit()
        cursor.close()

    def update(self, query, t):
        cursor = self.conn.cursor()
        cursor.execute(query, t)
        self.conn.commit()
        cursor.close()

if __name__ == '__main__':
    print("connect test")
    try:
        manager = DBManager()
        conn = manager.get_connection()
        print(conn.version)
    except Exception as e:
        print(str(e))
    finally:
        print("connect test 종료")
else:
    print("db 모듈 임포트")

