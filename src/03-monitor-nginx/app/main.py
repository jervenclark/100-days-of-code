# Start app

import fabric

connection = fabric.Connection('localhost')

result = connection.run('uname -s')

print(result)
