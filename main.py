from controllers.spendly_controller import SpendlyController
from views.spendly_view import SpendlyView
from colorama import Fore


def main():
    controller = SpendlyController()
    view = SpendlyView(controller)
    view.run()


if __name__ == "__main__":
    try:
        main()
    # Catching KeyboardInterrupt to allow graceful exit when user presses any key to avoid any errors or abrupt termination.
    except KeyboardInterrupt:
        print(Fore.RED + "\n\nUser requested to exit the Program. Exiting safely... Goodbye!\n")
        