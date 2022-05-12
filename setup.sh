#!/bin/bash
 

# Install via HomeBrew
declare -a viaHB=('wget' 'neofetch' 'youtube-dl' 'poppler' 'dockutil' 'mas' '--cask rectangle' '--cask spotify' '--cask visual-studio-code' '--cask discord' '--cask zoom' '--cask obs' '--cask arduino' '--cask whatsapp' '--cask ultimaker-cura')

# Install via gem
declare -a viaGEM=('pdfunite')

# Install via MacApp Store
declare -a viaMAS=()

# Extensions to be installed in Visual Studio Code
declare -a vsCodeExt=('ms-python.python' 'ms-python.vscode-pylance' 'ms-toolsai.jupyter' 'njpwerner.autodocstring' 'Gruntfuggly.todo-tree' 'ritwickdey.LiveServer' 'streetsidesoftware.code-spell-checker' 'mikeburgh.xml-format' 'ZainChen.json' 'vsciot-vscode.vscode-arduino' 'vscode-icons-team.vscode-icons')

# Install homebrew
curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh





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