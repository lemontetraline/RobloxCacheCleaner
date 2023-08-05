import shutil, logging, os, json, time

# Config #
with open("config.json") as config_file:
    config = json.loads(config_file.read())

user = config["username"]
localappdata = f"C:\\Users\\{user}\\AppData\\Local"

# Main #
def log(message):
    if config["createLogs"]:
        logging.info(message)
    else:
        print(message)

def clear_cache(dir_name):
    for account in config["accounts"]:
        account_dir = os.path.join(localappdata, f"Packages\\{account}")
        
        try:
            shutil.rmtree(os.path.join(account_dir, f"LocalState\\{dir_name}"))

            log(f"The cache of {account} of type {dir_name} was successfully cleared.")
        except OSError as err:
            error_type = "" # insane shit to check what error is that
            if str(err).find("cannot find") > 0:
                error_type = "was already removed (cleared)."
            elif str(err).find("being used") > 0:
                error_type = "Roblox is currently opened and the folder is used."

            error_message = f"The cache of {account} of type {dir_name} cannot be removed because {error_type}"
            log(error_message)

def clear_temp():
    temp_dir = os.path.join(localappdata, "Temp")

    for filename in os.listdir(temp_dir):
        file = os.path.join(temp_dir, filename)
        
        try:
            if os.path.isfile(file):
                os.remove(file)
            else:
                shutil.rmtree(file) # if its a directory despite being called file
        except OSError as _:
            pass

    log("Temp cleared")

def main():
    print("RobloxCacheCleaner by Lemon4K")

    if not config["username"]:
        print("Fatal error, no username was specified, please specify it in config.json file and read the README.md")
        return

    if config["createLogs"]:
        if not os.path.exists("./logs"):
            os.mkdir("logs")
        
        logging.basicConfig(
            filename="logs/latest.log",
            format='%(asctime)s %(message)s',
            level=logging.INFO,
            datefmt='%Y-%m-%d %H:%M:%S')

    if len(config["accounts"]) <= 0:
        print("No account names were specified, cannot proceed!")
        return

    print("Successfully initalised, starting clear")
    log("Starting")

    while True:
        if config["clearTemp"]:
            clear_temp()

        for dir in config["cacheToClean"]:
            clear_cache(dir)

        log("------------------------------")

        time.sleep(config["clearDelay"])
        

if __name__ == "__main__": # unnecessary, but i still gonna work good
    main()
