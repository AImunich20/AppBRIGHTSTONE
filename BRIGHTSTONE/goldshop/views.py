import requests
from django.http import JsonResponse


def goldprice_api(request):

    url = "https://api.chnwt.dev/thai-gold-api/latest"

    try:
        res = requests.get(url, timeout=5)
        data = res.json()

        buy = data["response"]["price"]["gold_bar"]["buy"]
        sell = data["response"]["price"]["gold_bar"]["sell"]

        update_date = data["response"]["update_date"]
        update_time = data["response"]["update_time"]

        return JsonResponse({
            "buy": buy,
            "sell": sell,
            "update_date": update_date,
            "update_time": update_time
        })

    except Exception as e:

        print("API ERROR:", e)

        return JsonResponse({
            "buy": "-",
            "sell": "-",
            "update_date": "-",
            "update_time": "-"
        })