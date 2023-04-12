import requests


def generer_bilde(tekst, apiKey):
    url = "https://api.openai.com/v1/images/generations"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + apiKey,
    }
    body = {
        "prompt": tekst,
        "n": 2,
        "size": "1024x1024"
    }

    response = requests.post(url, headers=headers, json=body)
    data = response.json()
    print(data)
    return [i["url"] for i in data["data"]]


def generer_svar_davinci3(tekst, apiKey):
    url = "https://api.openai.com/v1/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + apiKey,
    }
    body = {
        "model": "text-davinci-003",
        "prompt": tekst,
        "max_tokens": 800,
        "temperature": 0.2,
        "n": 1
    }

    response = requests.post(url, headers=headers, json=body)
    data = response.json()
    return data["choices"][0]["text"]


def generer_svar_chatGPT3(tekst, apiKey):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + apiKey,
    }
    body = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": tekst}]
    }

    response = requests.post(url, headers=headers, json=body)
    data = response.json()
    return data["messages"][0]["message"]["content"]


# Eksempel på bruk:

API_KEY = "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" # Finn din egen på https://platform.openai.com/account/api-keys
print(generer_bilde("Sandvikas IT-klasse malt av Munch", API_KEY))
print(generer_svar_davinci3("Skriv en cocktail med disse oppskriftene: eggehvite, bringebær, rom, sukker", API_KEY))