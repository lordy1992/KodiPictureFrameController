from bottle import route, run, template, request, redirect, TEMPLATE_PATH
import frame_dao
import os, subprocess

TEMPLATE_PATH.insert(0, '/home/osmc/.kodi/addons/plugin.service.picture.frame.controller/views')
frameDao = frame_dao.PlaylistDao()

@route('/')
def home():
    playlists = frameDao.getPlaylists()
    activeList = frameDao.getActivePlaylist()
    params = {'dirs': playlists, 'active': activeList}
    return template('index.tpl', params)

@route('/upload', method='POST')
def handle_upload():
    upload = request.files.get('upload')
    selectedPlaylist = request.forms.get('selectedPlaylist')
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.bmp', '.jpg', '.jpeg', '.gif', '.png', '.tiff', '.mng', '.ico', '.pcx'):
        return 'File extension is not allowed.'
    
    newPath = frameDao.getPlaylistPath(selectedPlaylist)
    upload.save(newPath)

@route('/set-active', method='POST')
def handle_set_playlist():
    selectedPlaylist = request.forms.get('selectedPlaylist')
    frameDao.setActivePlaylist(selectedPlaylist)
    redirect('/')

if __name__ == '__main__':
    run(host='', port=8080, debug=True)
