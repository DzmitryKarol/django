import psycopg2

def test(username):
    db = psycopg2.connect(host="172.20.0.2", user="postgres", password="postgres", database='postgres')
    cursor = db.cursor()
    query = f"select id from auth_user where username = '{username}'"
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)
    db.close()



class DataBase:
    def check_user_in_db(self, username):
        db = psycopg2.connect(host="172.20.0.2", user="postgres", password="postgres", database='postgres')
        cursor = db.cursor()
        query = "select username, id from auth_user"
        perm = 'select user_id, count(*) FROM public.auth_user_user_permissions group by user_id'
        cursor.execute(query)
        result = cursor.fetchall()
        created_user = ''
        created_user_id = ''
        for i in result:
            name = i[0]
            if name == username:
                created_user = name
                created_user_id = i[1]
            else:
                continue
        assert created_user == username, 'user was not created'
        cursor.execute(perm)
        result = cursor.fetchall()
        assert result[0][0] == created_user_id, f'userID is incorrect {created_user_id} != {result[0][0]}'
        assert result[0][1] == 28, 'no permissions'
        db.close()

    def delete_user(self, username):
        db = psycopg2.connect(host="172.20.0.2", user="postgres", password="postgres", database='postgres')
        cursor = db.cursor()
        find_user = f"select id from auth_user where username = '{username}'"
        cursor.execute(find_user)
        result = cursor.fetchall()
        user_id = result[0][0]
        delete_permissions = f"delete from auth_user_user_permissions where user_id = {user_id}"
        print(delete_permissions)
        cursor.execute(delete_permissions)
        delete_user = f"delete from auth_user where id = {user_id}"
        cursor.execute(delete_user)
        db.commit()
        cursor.execute(find_user)
        result = cursor.fetchall()
        assert result == [], f'user is not deleted, result = {result}'
        db.close()
