def app(environ, start_response):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    body = 'Hello, world!'
    start_response(status, headers )
    return body

'''
	body = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
	'''