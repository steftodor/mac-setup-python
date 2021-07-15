import sys
import os
import json

with open('./config.json') as configFile:
    config = json.load(configFile)

################################################### System Settings ###################################################
if "osx" in sys.argv:
    #print("[OSX]: Wallpaper")
    #os.system('''osascript -e 'tell application "Finder" to set desktop picture to POSIX file "'''+config["OSXsettings"]["wallpaper_path"]+''''"''')
    print("[OSX]: Screensaver")
    os.system('''defaults -currentHost write com.apple.screensaver moduleDict -dict moduleName '''+ config["OSXsettings"]["screensaver_moduleName"]+'''path '''+ config["OSXsettings"]["screensaver_path"] +''' type 0''')
    os.system("defaults -currentHost write com.apple.screensaver idleTime " + config["OSXsettings"]["screensaver_idleTime"])

    print("[OSX]: Display Sleep")
    os.system("sudo pmset -c displaysleep " + config["OSXsettings"]["displaySleep_charger"])
    os.system("sudo pmset -b displaysleep " + config["OSXsettings"]["displaySleep_battery"])

    print("[OSX]: Keyboard and Mouse/Trackpad")
    os.system("defaults -currentHost write NSGlobalDomain com.apple.mouse.tapBehavior -int " + config["OSXsettings"]["trackpad_tapBehavior"])
    os.system("defaults write -g com.apple.swipescrolldirection -bool " + config["OSXsettings"]["scrollDirection"])
    os.system("defaults write -g InitialKeyRepeat -int " + config["OSXsettings"]["InitialKeyRepeat"])
    os.system("defaults write -g KeyRepeat -int " + config["OSXsettings"]["KeyRepeat"])
    os.system("defaults write -g ApplePressAndHoldEnabled -bool " + config["OSXsettings"]["ApplePressAndHoldEnabled"])

    print("[OSX]: DOCK SETTINGS")
    os.system("defaults write com.apple.Dock autohide-delay -float " + config["OSXsettings"]["dock_Autohide-delay"])
    os.system("defaults write com.apple.dock show-recents -bool " + config["OSXsettings"]["dock_show-recents"])
    os.system("defaults write com.apple.dock autohide -bool " + config["OSXsettings"]["dock_autohide"])
    os.system("killall Dock")
else:
    print("[OSX]: SKIPPING")


################################################### Install Homebrew ###################################################

if "installbrew" in sys.argv:
    os.system('''/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"''')
else:
    print("[installbrew]: SKIPPING")

################################################### Install Homebrew Packages ###################################################
if "brew" in sys.argv:
    for b in config["brew"]:
        os.system("brew install " + b)
else:
    print("[brew]: SKIPPING")

################################################### Install Homebrew Cask Packages ###################################################
if "cask" in sys.argv:
    for c in config["cask"]:
        os.system("brew install --cask " + c)
else:
    print("[cask]: SKIPPING")

################################################### Install Visual Studio Code Extensions ###################################################
if "code" in sys.argv:
    for e in config["codeExtension"]:
        os.system("code --install-extension " + e)
else:
    print("[code]: SKIPPING")

################################################### Install AppStore Apps ###################################################
if "appStore" in sys.argv:
    for a in config["appStore"]:
        os.system("mas install " + a)
else:
    print("[appStore]: SKIPPING")

################################################### Setup Dock Applicationsm###################################################
os.system("dockutil --remove all")
if "dock" in sys.argv:
    print("[DOCK]: Starting Dock Setup")
    for app in config["dockOrder"]:
        os.system("dockutil --add " + app)
else:
    print("[DOCK]: SKIPPING")

################################################### Runs other commands ###################################################
if "other" in sys.argv:
    for other in config["other"]:
        os.system(other)
else:
    print("[other]: SKIPPING")