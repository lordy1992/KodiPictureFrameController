import xbmc
import time

if __name__ == '__main__':
    monitor = xbmc.Monitor()

    while not monitor.abortRequested():
        # TODO: Do something useful
        if monitor.waitForAbort(10):
            # Currently, just wait for 10 seconds or until the service is aborted
            break
        xbmc.log("Current time: %s" % time.time(), level=xbmc.LOGDEBUG)