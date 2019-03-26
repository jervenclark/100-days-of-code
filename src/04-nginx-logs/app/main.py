# Start app
import fabric, pprint
import StringIO

# Establish connection
connection = fabric.Connection('web-server')

# Read nginx logs
def main():
    result = connection.run('ls /var/log/nginx')
    logs   = result.stdout.split("\n")
    for log in logs:
        read_logs(log)

def read_logs(log):
    fd = StringIO.StringIO()
    remote = '/var/log/nginx/' + log
    connection.get(remote, './' + log)
    # connection.get('/var/log/nginx/' + log, fd)
    content=fd.getvalue()
    pprint.pprint(content)

main()
