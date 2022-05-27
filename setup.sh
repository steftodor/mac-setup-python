#!/bin/bash
 

# Install via HomeBrew
declare -a viaHB=('wget' 'neofetch' 'youtube-dl' 'poppler' 'dockutil' 'mas' '--cask rectangle' '--cask spotify' '--cask visual-studio-code' '--cask discord' '--cask zoom' '--cask obs' '--cask arduino' '--cask whatsapp' '--cask ultimaker-cura')

# Install via gem
declare -a viaGEM=('pdfunite')

# Install via MacApp Store
declare -a viaMAS=('937984704' '360593530' '1333542190' '497799835' '424389933')

# Extensions to be installed in Visual Studio Code
declare -a vsCodeExt=('ms-python.python' 'ms-python.vscode-pylance' 'ms-toolsai.jupyter' 'njpwerner.autodocstring' 'Gruntfuggly.todo-tree' 'ritwickdey.LiveServer' 'streetsidesoftware.code-spell-checker' 'mikeburgh.xml-format' 'ZainChen.json' 'vsciot-vscode.vscode-arduino' 'PKief.material-icon-theme' 'zhuangtongfa.material-theme')

# Install homebrew
curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh

# Screensaver settings
defaults -currentHost write com.apple.screensaver moduleDict -dict moduleName Computer Name path System/Library/Screen Savers/Computer Name.appex type 0
defaults -currentHost write com.apple.screensaver idleTime 300

# Display sleep settings 
sudo pmset -c displaysleep 30
sudo pmset -b displaysleep 5

# Keyboard / Trackpad / Mouse settings
defaults -currentHost write NSGlobalDomain com.apple.mouse.tapBehavior -int 1
defaults write -g com.apple.swipescrolldirection -bool false
defaults write -g InitialKeyRepeat -int 12
defaults write -g KeyRepeat -int 3
defaults write -g ApplePressAndHoldEnabled -bool false








# Install through Homebrew
for app in ${viaHB[@]}; do
   brew install $app
done

# Install through gem
for app in ${viaGEM[@]}; do
   gem install $app
done

# Install through MacAppStore
for app in ${viaMAS[@]}; do
   mas install $app
done

# Install vsCode Extentions
for ext in ${vsCodeExt[@]}; do
   code --install-extension $ext
done