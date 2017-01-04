from bottle import route, run, template

@route('/')
def home():
    return "Hello world!"

@route('/hello/<name>')
def greet(name):
    return template('Hello {{name}}!', name=name)
    
if __name__ == '__main__':
    run(host='', port=8080, debug=True)
