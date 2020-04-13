# Invidious add-on

Play media on KODI from https://invidious.snopyta.org. Invidious is an alternative front-end to YouTube. No need to enter API keys nor a Google account.

## Installation

While you could install the plugin through the KODI graphical user interface, it may be quicker to ssh into the box and do:

```
cd /storage/.kodi/addons/
wget -c https://github.com/probonopd/plugin.video.invidious/archive/master.zip -O plugin.video.invidious.zip
unzip plugin.video.invidious.zip
mv plugin.video.invidious-master plugin.video.invidious
killall kodi.bin
```

## TODO

Pull requests are welcome. This is really easy Python code, after all.

* Implement search
* Implement "subscription" to topics/search terms set in the settings of the add-on 
* Implement managing subscriptions through the Invidious API
* Implement watch history, preferences through the Invidious API
* Metadata for the add-on, e.g., abstract, icon, screenshots, etc.

## References

* https://kodi.wiki/view/Add-on_development
* https://github.com/omarroth/invidious/wiki/API
