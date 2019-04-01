# Start app
import fabric

# Establish connection
connection = fabric.Connection('web-server')

# Test nginx configuration
def main():
    nginx_test()
    nginx_status()

def nginx_test():
    result = connection.sudo('nginx -t')

def nginx_status():
    result = connection.sudo('service nginx status')

main()
