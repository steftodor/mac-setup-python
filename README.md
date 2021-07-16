# Mac Setup

I created this python script to configure my MacBook after reinstalling it. 
It can download and install Homebrew, install brew and casks packages, Visual Studio Code extensions, Mac App Store Apps, configure the location of items in the Dock, certain MacOS System settings, and other commands. 

All configuration is done in the configs file.
For the purposes of modularity, you select the modules that you wish to run, the only required section is `python3 setup.py` with everything after representing a diffrent module. A breakdown is listed bellow.

`python3 setup.py osx installbrew brew cask code appStore dock other`

- osx - Preforms Config of system preferences based on json file
- installbrew - installs Homebrew
- brew - instals brew packages based on json file
- cask - installs brew cask packages 
- code - installs Visual Studio Code Extensions 
- appStore - installs App Store Apps
- dock - configures dock based on json file 
- other - runs the commands listed in the json files


