import os

IMAGE_ROOT_DIR = "/home/osmc/Pictures"
ACTIVE_SLIDESHOW_NAME = "ActiveSlideshow"
    
class PlaylistDao:
    def getActivePlaylist(self):
        activePath = self.getRootSubdir(ACTIVE_SLIDESHOW_NAME)
        return os.readlink(activePath)
        
    def getPlaylists(self):
        playlists = next(os.walk(IMAGE_ROOT_DIR))[1]
        playlists.remove(ACTIVE_SLIDESHOW_NAME)
        return playlists
        
    def createSlideshow(self, name):
        directoryName = self.getRootSubdir(name)
        if not os.path.exists(directoryName):
            os.makedirs(directoryName)
            return True
        else:
            return False
    
    def renamePlaylist(self, oldPlaylist, newName):
        activePlaylist = self.getActivePlaylist()
        newDir = self.getRootSubdir(oldPlaylist)
        os.rename(newDir, self.getRootSubdir(newName))
        activeLinkName = self.getRootSubdir(ACTIVE_SLIDESHOW_NAME)
        os.remove(activeLinkName)
        os.symlink(newDir, activeLinkName)

    def getPlaylistPath(self, playlist):
        return self.getRootSubdir(playlist)
    
    def setActivePlaylist(self, playlist):
        newActiveDir = self.getRootSubdir(playlist)
        if os.path.exists(newActiveDir):
            activeLinkName = self.getRootSubdir(ACTIVE_SLIDESHOW_NAME)
            os.remove(activeLinkName)
            os.symlink(newActiveDir, activeLinkName)
            return True
        return False
    
    def getRootSubdir(self, path):
        return os.path.join(IMAGE_ROOT_DIR, path)