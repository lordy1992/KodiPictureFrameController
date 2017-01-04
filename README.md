# KodiPictureFrameController
A Kodi plug-in to create and manage image slideshows for a simple digital picture frame (running on a raspberry pi with OSMC).

# Installing / Testing
This plugin can be installed by zipping the main folder (plugin.service.picture.frame.controller). The zip file must contain that folder with
that specific name, and that folder must then contain the addon.xml file (as well as the other necessary files).

It can be a bit finnicky when installing the add-on. If editing the addon.xml file in Windows, you must ensure that the file uses unix line endings.
You can move the main folder over to a directory in OSMC running on the raspberry pi (let's say the ~/Plugins directory) and the run:

```bash
cd ~/Plugins/plugin.service.picture.frame.controller
dos2unix addon.xml
zip -r plugin.service.picture.frame.controller.zip plugin.service.picture.frame.controller
```

Then, on OSMC, to install and test:

* Go to Settings -> Add-ons -> Install from zip file
* Select "Home folder" and navigate to the "Plugins" directory
* Select the newly created zip file "plugin.service.picture.frame.controller.zip"

In order to see the log, you can go to Settings -> System -> Logging and select "Enable debug logging"
The log file is located in ~/.kodi/temp (unless you change this -- this is the default)

**Note:** This plugin uses Bottle, and you must install module.script.bottle. You can find a zip for this addon easily (it is maintained by Team Kodi) and install it. 
This must be done prior to installing this plugin.

In order to test, modifications can be made to the Python files in the add-on after it has been installed. These files are located in ~/.kodi/addons/plugin.service.picture.frame.controller
You can edit and test the Python files here. If you make changes and wish to test, go to Settings -> Add-ons -> My add-ons -> Services -> Lord of Pictures Controller.
Then click "Disable" and then "Enable"; when the service restarts, the changes will take effect.
