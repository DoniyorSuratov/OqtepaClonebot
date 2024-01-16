import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()
class Pg:
    con = psycopg2.connect(
        dbname = os.getenv("DATABASE"),
        user= os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port = os.getenv("DB_PORT"),
        host = os.getenv("DB_HOST")
    )
    cur = con.cursor()
    query = """
        create table if not exists users_oqtepa(
            id serial primary key ,
            user_id bigint ,
            first_name varchar(255),
            username varchar(255) default null,
            phone_number varchar(30) default null,
            latitude float default null,
            longitude float default null,
            address_info varchar(255),
            created_at timestamp default current_timestamp

        )
    """
    cur.execute(query)
    con.commit()

    query = """
            create table if not exists branch_location(
                id serial primary key ,
                branch_id bigint ,
                branch_name varchar(255),
                latitude float default null,
                longitude float default null

            )
        """
    cur.execute(query)
    con.commit()




    def check_user(self, user_id):
        query = """
            SELECT user_id FROM users_oqtepa WHERE user_id = %s
        """
        self.cur.execute(query, (user_id,))
        result = self.cur.fetchone()
        return result


    def add(self , user_id , first_name , username ):
        query = """
        insert into users_oqtepa (user_id, first_name , username) values (%s , %s , %s)
        """
        params = (user_id , first_name , username,)
        self.cur.execute(query , params)
        self.con.commit()

    def branch_name(self, branch_name):
        query="""
            select branch_name from branch_location where branch_name = %s
            """
        self.cur.execute(query, (branch_name,))
        result = self.cur.fetchone()
        return result

    def latitude(self, latitude):
        query = """
        select latitude from branch_location where branch_name = %s
        """
        self.cur.execute(query,(latitude,))
        result = self.cur.fetchone()
        return result

    def longtitude(self, longtitude):
        query = """
        select longitude from branch_location where branch_name = %s
        """
        self.cur.execute(query,(longtitude,))
        result = self.cur.fetchone()
        return result



    def insert_longtitude(self, user_id,latitude, longtitude):
        query = """
            update users_oqtepa set latitude=%s, longitude = %s where user_id = %s
        """
        params = (latitude, longtitude , user_id)
        self.cur.execute(query, params)
        self.con.commit()

    def user_latitude(self, user_id):
        query = """
        select latitude from users_oqtepa where user_id = %s
        """
        self.cur.execute(query,(user_id,))
        result = self.cur.fetchone()
        return result

    def user_longtitude(self, user_id):
        query = """
        select longitude from users_oqtepa where user_id = %s
        """
        self.cur.execute(query,(user_id,))
        result = self.cur.fetchone()
        return result


    def user_info_add(self, user_id, address_info):
        query = """
        update users_oqtepa set address_info = %s where user_id = %s"""
        params = (address_info, user_id)
        self.cur.execute(query,params)
        self.con.commit()

    def add_contact(self, user_id, phone_number):
        query = """
        update users_oqtepa set phone_number = %s where user_id = %s"""
        params = (phone_number, user_id)
        self.cur.execute(query,params)
        self.con.commit()

    def show_num(self, user_id):
        query = """
        select phone_number from users_oqtepa where user_id = %s
        """
        self.cur.execute(query,(user_id,))
        result = self.cur.fetchone()
        return result

    def closest_branch_location(self, latitude, longitude):
        query = """
            SELECT latitude, longitude
            FROM (
                SELECT latitude, longitude,
                    (6371 * acos(cos(radians(%s)) * cos(radians(latitude)) *
                    cos(radians(longitude) - radians(%s)) +
                    sin(radians(%s)) * sin(radians(latitude)))) AS distance
                FROM branch_location
            ) AS subquery
            ORDER BY distance ASC
            LIMIT 5;
            """
        params = (latitude, longitude,latitude)
        self.cur.execute(query,params)
        self.cur.fetchall()