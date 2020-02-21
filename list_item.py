import psycopg2 as pg2


class ListItem:
    def __init__(self, user_id, my_id=None):
        self.db_host = 'packy.db.elephantsql.com'
        self.db_user = 'htcazxfd'
        self.db_name = 'htcazxfd'
        self.db_port = 5432
        self.db_psswd = 'UE5AaV5whqnbKyD5jL9MusNCvV1yaX7T'
        self.conn = None

        self.user_id = user_id
        self.my_id = my_id


class FriendsListItem(ListItem):
    def __init__(self, user_id, my_id=None):
        super(FriendsListItem, self).__init__(user_id,  my_id)

    def get_info(self):
        self.conn = pg2.connect(host=self.db_host, database=self.db_name, user=self.db_user, password=self.db_psswd,
                                port=self.db_port)
        c = self.conn.cursor()
        c.execute("""
                SELECT u.username, u.date_of_birth, u.account_creation, f.since
                FROM users u
                JOIN friends f
                ON f.user_1 = {} OR f.user_2 = {}
                WHERE u.user_id = {}
        """.format(self.my_id, self.my_id, self.my_id))
        info = c.fetchone()
        self.username = info[0]
        self.date_of_birth = info[1]
        self.account_creation = info[2]
        self.since_date = info[3]
        c.close()
        self.conn.commit()
        self.conn.close()


class GameListItem(ListItem):
    def __init__(self, user_id, my_id=None):
        super(GameListItem, self).__init__(user_id, my_id)
        self.gp_id, self.platform, self.price, self.release_date, self.name, self.genre, self.for_kids, self.author, self.description = [None for _ in range(9)]

    def get_info(self):
        self.conn = pg2.connect(host=self.db_host, database=self.db_name, user=self.db_user, password=self.db_psswd,
                                port=self.db_port)
        c = self.conn.cursor()
        c.execute("""
                SELECT gp.gp_id, g.name, p.name AS pname, gp.price, gp.release_date, g.genre, g.for_kids, g.author, g.description
                FROM games_platforms gp
                JOIN games g
                ON g.game_id = gp.game_id
                JOIN platforms p
                ON p.plat_id = gp.plat_id
                WHERE gp.game_id = {}
        """.format(self.my_id))
        info = c.fetchone()
        self.gp_id, self.name, self.platform, self.price, self.release_date, self.genre, self.for_kids, self.author, self.description = info
        c.close()
        self.conn.commit()
        self.conn.close()

    def do_user_own_this(self):
        self.conn = pg2.connect(host=self.db_host, database=self.db_name, user=self.db_user, password=self.db_psswd,
                                port=self.db_port)
        c = self.conn.cursor()
        c.execute("""
                SELECT * 
                FROM users_games ug
                JOIN games_platforms gp
                ON gp.gp_id = ug.gp_id
                JOIN games g
                ON g.game_id = gp.game_id
                WHERE g.game_id = {} AND ug.user_id = {};
        """.format(self.my_id, self.user_id))
        own = c.fetchone()

        c.close()
        self.conn.commit()
        self.conn.close()

        return not (own is None)


class CurrencyListItem(ListItem):
    def __init__(self, user_id, my_name):
        super(CurrencyListItem, self).__init__(user_id, my_name)
        self.my_name = my_name
        self.value = 1

    def get_info(self):
        self.conn = pg2.connect(host=self.db_host, database=self.db_name, user=self.db_user, password=self.db_psswd,
                                port=self.db_port)
        c = self.conn.cursor()
        c.execute("""
                SELECT value_in_pln
                FROM currencies
                WHERE name = {}
        """.format(self.my_name))
        value = c.fetchone()
        self.value = value[0]

        c.close()
        self.conn.commit()
        self.conn.close()

