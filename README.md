# Roblox Cache Cleaner
Having a lot of Roblox UWP instances open and close many times is really painful, as it can create hundreds of gigabytes of sound cache and log cache, and if thats not the problem for people with high-capacity drives, some people might experience issues like running out of space on low capacity drives, wich might cause a lot of problems. This program would continiously (you can specify the delay) clear the cache that roblox makes to keep the drive empty and fresh

Can be used with tools like [RAM](https://github.com/ic3w0lf22/Roblox-Account-Manager)

# WARNING
Before you can actually use RCC, you need to set it up first.
Also note, that this program is for UWP roblox only, but it can also clear you temp folder.

First, you have to make sure that you have Python 3.6 or higher installed, [which can be done with the official website](https://www.python.org/), because it is necessary for the program to work (might change it to .exe soon)

Second, you have to make sure that the ```config.json```file is in the same directory as ```clear.py```

Then, you have to edit the config based on your accounts and system configuration. The proccess of doing that is covered in the Setup section

# Setup
The installation proccess is very simple. You have to press the green "Code" button at the top of the page, then press "Download ZIP" in the pop-up menu, unzip the folder wherever you want and proceed to the next step. The name of the folder doesnt matter and can be change, but its highly recommended for it to have english characters only to avoid any potential issues. The folder should containt 2 main files, it's ```config.json``` and ```clear.py``` which is the program itself, you can also use ```run.ps1``` to run the program by just double clicking it

Changes are have to made to the config file in order for the program to work. The config file already comes with the program and as specified earlier, should be called ```config.json```. The content of the file should look something like this but without the comments:

```jsonc
{
"accounts": [ 
    // list of all your accounts where you want to clear the cache, use only full /folder name (e.g ROBLOXCORPORATION.ROBLOX.username_5x0a1b2c...)
        "ROBLOXCORPORATION.ROBLOX.username_5x0a1b2b23r2r2",
    ],

    // folders to clean inside of LocalState (cache & stuff), approximate weights(sounds: 500MB - ∞, logs: up to 100 MB, http(not recommended, might reset client settings): up to 2GB)
    "cacheToClean": [
        "sounds",
        "logs"
    ],

    "username": "yourname", // your account name in Windows (if you dont have an offline account, use the first word that you see in the start menu, if that gives you an error, go to "C:\Users" in the explorer and whatever is not Default and Public is your username)
    "clearTemp": true, // wether or not the program is gonna clear your local temp folder or not
    "createLogs": true, // allow program to create logs inside of logs folder in the current directory for debugging.
    "clearDelay": 30 // how long should the program wait before each cleaning in seconds (not recommended making lower than 10 secs)
}
```

The first option you should modify is the ```accounts``` table. In here, you should list all the accounts where you want the cache to be cleared, to get the list of all of your accounts, you need to press ```WIN + R``` on your keyboard and type ```%localappdata%``` in the field of the new popup program. Then, you will be met with an explorer window with your local AppData folder opened. Locate a folder called ```Packages``` there, open it, and scroll down until you see the word ```ROBLOXCORPORATION.ROBLOX...```. All of the folders that start with that name are your UWP instances, and now you have to copy their names (right click rename, then do ctrl + A, ctrl + C and hit Escape), include them in double qoutes the next line after the word "account" (just like its shown in the example above), and comma at the end of the line and do this for every account.

Then you have change the ```username``` to your Windows username, its explained in the example above.

And that's it. You can change some other options there, its documented what they all do, but its not necessary tho.

# Running
As said before, you need Python to run the program. You can either double click the run.ps1 file (if it opens notepad, do right click and then ```Open with PowerShell```, if it instantly crahses it means you have scirpts disabled, so do the other metod), or you can do shift + right click on the folder in the explorer, the press ```Open PowerShell window here``` and then in the new window type ```py clear.py``` and that's it! Enjoy the program.
