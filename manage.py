from flask_script import Manager, Server

try:
    from .. import SET_UP
except ImportError or ModuleNotFoundError:
    import sys
    sys.path.append("..")
    from app import SET_UP

flask_app = SET_UP() # create flask instance
app_manager  = Manager(flask_app)

app_manager.add_command("runserver", Server()) # start app

if __name__ == "__main__":
    app_manager.run()