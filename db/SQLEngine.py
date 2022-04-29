import psycopg2

class SQLEngine:
    
    def __init__(self, host, dbname, user, password, sslmode):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
        self.sslmode = sslmode
        self.conn_str = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
        self.connection = None
        self.cursor = None
        
    def connect(self):
        self.connection = psycopg2.connect(self.conn_str) 
        self.cursor = self.connection.cursor()
        
    def closeConnection(self):
        self.cursor.close()
        self.connection.close()
        
    def query(self, qry):
        self.connect()
        self.cursor.execute(qry)
        records = self.cursor.fetchall()
        self.closeConnection()
        return records
    
    def insert(self, table, cols, data):
        
        #at present, this assumes that the data is coming in a pandas dataframe
        #cols will be a list of columns
        #table will be a string
        
        self.connect()
        insert_str = 'insert into {table} ({cols}) values {data}'
        insert_str = insert_str.replace('{table}', table)
        
        col_str = ','.join(cols)
        insert_str = insert_str.replace('{cols}', col_str)
        
        rows_lst = []
        for row in data.values.tolist():
            enquoted_data = []
            for item in row:
                enquoted_data.append("'{}'".format(item))
            row_str = '({})'.format(','.join(enquoted_data))
            rows_lst.append(row_str)
        data_str = ','.join(rows_lst)
        insert_str = insert_str.replace('{data}', data_str)
        
        self.cursor.execute(insert_str)
        self.connection.commit()
        
        self.closeConnection()
        
    def executeSP(self, sp_name, sp_parameters):
        
        self.connect()
        
        enquoted_params = []
        for param in sp_parameters:
            enquoted_params.append("'{}'".format(param))
        
        exec_str = 'call {}({})'.format(sp_name, ','.join(enquoted_params))
        
        #print(exec_str)
        
        self.cursor.execute(exec_str)
        self.connection.commit()
        
        self.closeConnection()
        