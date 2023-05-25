import requests


def APIpaw(nome,content):
    username = 'grimo04'
    token = 'f44a48c5f1b4aa6a873e7c6036c577cb679d5c95'
    path="/home/grimo04/bot/"+nome
    response = requests.post(
        f'https://www.pythonanywhere.com/api/v0/user/{username}/files/path{path}'.format(
            username=username
        ),
        headers={'Authorization': f'Token {token}'.format(token=token)},
        files={"content": content}
    )
    if response.status_code == 200 or response.status_code == 201:
        return
    else:
        print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))


                
        

def upload():
    try:
        response = requests.get("https://www.mise.gov.it/images/exportCSV/anagrafica_impianti_attivi.csv")
        APIpaw("impianti.csv",response.content)
        response = requests.get("https://www.mise.gov.it/images/exportCSV/prezzo_alle_8.csv")
        APIpaw("prezzi.csv",response.content)
        return "fatto"
    except Exception as e:
        return f"error: {e.args[0]}"
    
    
