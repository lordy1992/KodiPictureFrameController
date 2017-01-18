from bottle import route, run, template, TEMPLATE_PATH
import os

TEMPLATE_PATH.insert(0, '/home/osmc/.kodi/addons/plugin.service.picture.frame.controller/views')

@route('/')
def home():
    playlists = next(os.walk('/home/osmc/Pictures'))[1]
    activeList = os.readlink('/home/osmc/Pictures/ActiveSlideshow')
    params = {'dirs': playlists, 'active': activeList}
    return template('index.tpl', params)

@route('/upload', method='POST')
def handle_upload():
	upload = request.files.get('upload')
	name, ext = os.path.splitext(upload.filename)
	if ext not in ('.bmp', '.jpg', '.jpeg', '.gif', '.png', '.tiff', '.mng', '.ico', '.pcx'):
		return 'File extension is not allowed.'

	upload.save('/home/osmc/Pictures/TestDir')

 
if __name__ == '__main__':
    run(host='', port=8080, debug=True)
