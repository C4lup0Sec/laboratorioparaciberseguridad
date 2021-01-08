from bs4 import BeautifulSoup
import requests


def get_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

def wiki():
    soup = get_soup("https://en.wikipedia.org/wiki/List_of_states_of_Mexico")
    tr= soup.table.find_all('tr')
    for row in tr:
        cols = row.find_all('td')
        t = [ele.text.strip() for ele in cols]
        print(f"{t}")

def google_images():
    soup = get_soup("https://www.google.com/search?q=perros&sxsrf=ALeKk02jGsCChitxcd1n9i8fZNIA8H2y0A:1602915634703&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiwoIuI_rrsAhUKCKwKHYTdBI4Q_AUoAXoECAQQAw&biw=1280&bih=662")
    images = soup.find_all('img')
    t = [{'src':image.get('src'), 'alt': image.get('alt')} for image in images]
    print(f"{t}")

def transparencia_uanl():
    soup = get_soup("http://transparencia.uanl.mx/remuneraciones_mensuales/bxd.php?pag_act=1&id_area_form=2305&mya_det=082020")
    tr= soup.find_all("table")[2].find_all('t')
    for row in tr:
         cols = row.find_all('td')
         t = [ele.text.strip() for ele in cols]
         print(f"{t}")


#ejemplo usado       "ftp.ntua.gr/stats/"
if __name__ == '__main__':
    url = input("Ingrese la URL: ")
# Capturamos el hml de la pagina web y creamos un objeto Response
    r  = requests.get("http://" +url)
    data = r.text
    print ("")
# Creamos el objeto soup y le pasamos lo capturado con request
    soup = BeautifulSoup(data, 'lxml')
# Capturamos el titulo de la página y luego lo mostramos
# Lo que hace BeautifulSoup es capturar lo que esta dentro de la etiqueta title de la url
    titulo = soup.title.text
    print ("El titulo de la pagina es: " + titulo)
    print ("")
# Buscamos todas etiquetas HTML (a) y luego imprimirmos todo lo que viene despues de "href"
    for link in soup.find_all('a'):
        print(link.get('href'))

