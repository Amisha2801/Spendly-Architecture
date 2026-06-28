import requests

# This Service layer is responsible for communication with external currency API.
# This class abstracts third-party integration from the controller.

class CurrencyAPIService:
    # This function fetches real-time exchange rate.
    def get_exchange_rate(self, base_currency="USD", target_currency="CAD") -> float:
        url = f"https://open.er-api.com/v6/latest/{base_currency}"

        try:
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()

                if data["result"] == "success":
                    return data["rates"][target_currency]

            return 1.0  # it returns fallback valueif API fails

        except Exception:
            return 1.0
        