import os
DB_DETAILS = {
    'dev' : {
        'SOURCE_DB' : {
            'DB_TYPE' : 'mysql',
            'DB_HOST' : '',
            'DB_NAME' : 'mysql',
            'DB_USER' : os.environ.get('SOURCE_DB_USER'),
            'DB_PASS' : os.environ.get('SOURCE_DB_PASS')
        },
        'TARGET_DB' : {
            'DB_TYPE' : 'mysql',
            'DB_HOST' : '',
            'DB_NAME' : 'postgres',
            'DB_USER' : os.environ.get('TARGET_DB_USER'),
            'DB_PASS' : os.environ.get('TARGET_DB_PASS')
        }
    }
}