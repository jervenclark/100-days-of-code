from fabric import Connection

connection = Connection('ikebukuro_web')

result = cconnection.run('free -m')
