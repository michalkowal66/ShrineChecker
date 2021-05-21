# Shrine Checker

## About Shrine Checker project

Shrine Checker is an app that can be used to track appearence of perks
in the Shrine of Secrets in Dead by Daylight game.  
The app is written in Python, using mainly PyQt5 and BeautifulSoup4 libraries.  
Currently the application can be run only on Windows.

## Using Shrine Checker

### Initialization

On first run application creates a local directory in `Documents`, where it downloads all necessary data  
(such as perks names, images, current shrine) from [Dead by Daylight wikipedia](https://deadbydaylight.fandom.com/wiki/Dead_by_Daylight_Wiki) and creates local files.  

### Adding and removing perks to the list
  
After initialization the application is ready to use. Using a dropbox in the top left corner choose  
perks that You'd like to be notified about, and click `Add` button, the perk should appear then in the list below.  
Perks can be then removed by simply selecting the perk in the list and pressing `remove` button.

### Current Shrine of Secrets

On the right side of the screen 4 perks of current Shrine of Secrets are displayed.  
One can see perks' descriptions simply hovering mouse over their images. 

### Match notification

Once some perks are added and the app is minimized to tray, every 2 hours (or more, depending on settings)  
the application refreshes in the background and checks, whether some perks in the list are available in the  
Shrine of Secrets. If there are any matches, it displays a notification in the top right corner of the screen.

### Default settings

The application automatically adds itself to startup and minimizes to tray on `close window` button.  
Application intervals are set to 2 hours.

### Adjusting settings

Using the button with cog wheel icon, placed in the top right corner of the screen, settings screen can be accessed.  
Settings like minimize to tray on exit, run with startup, change refresh interval, and redownload local data  
can be accessed from there, and changed according to preference.
