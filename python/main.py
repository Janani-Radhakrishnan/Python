from sample import Database
db = Database(host='localhost', user='root', password='')
db.show_databases()
db.create_database('vgulg_eng2')
db.use_database('vglug_eng2')
table_schema = "id INT, name VARCHAR(200), age INT"
db.create_table('test', table_schema)
db.insert_data('test', 'id, name, age', "1, 'Janani', 20")
db.fetch_data('test')
db.close_connection()