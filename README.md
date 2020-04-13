# Invidious add-on

Play media on KODI from https://invidious.snopyta.org.

## Installation

While you could install the plugin through the KODI graphical user interface, it may be quicker to ssh into the box and do:

```
cd /storage/.kodi/addons/
wget -c https://github.com/probonopd/plugin.video.invidious/archive/master.zip -O plugin.video.invidious.zip
unzip plugin.video.invidious.zip
mv plugin.video.invidious-master plugin.video.invidious
killall kodi.bin
```
