from startup import StartUp
from app.core.constants.app_metadata import APP_PORT

def main() -> None:
    StartUp().buid().run(port = APP_PORT)

if __name__ == "__main__":
    main()