from DBcm import UseDataBase

config['database'] = {'host': '127.0.0.1',
                      'user': '',
                      'password':'',
                      'database':''}


with UseDataBase(config['database']) as cursor:
    # сюда ебашишь запрос
    sql = """insert cock"""
    #отправляешь данные в бд
    cursor.execute(sql, ())