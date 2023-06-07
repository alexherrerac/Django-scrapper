import requests
from lxml import etree
from bs4 import BeautifulSoup

# Listas que guardan los resultados obtenidos del scraping
nombre = list()
universidad = list()
ciudad = list()
profesion = list()
threads = list()

def limpiar():
    nombre.clear()
    universidad.clear() 
    ciudad.clear()  
    profesion.clear()

# Hace la transformacion de los nombres al formato requerido para la busqueda
def transform_name(nombre: str):
    nombres = nombre.split(" ")
    if len(nombres) == 3:
        nombre = nombres[1].capitalize() + "+" + nombres[2].capitalize() + "%2C+" + nombres[0].capitalize()
    elif len(nombres) == 4:
        nombre = nombres[2].capitalize() + "+" + nombres[3].capitalize() + "%2C+" + nombres[0].capitalize() + "+" + nombres[1].capitalize()
    elif len(nombres) == 2:
        nombre = nombres[1].capitalize() + "%2C+" + nombres[0].capitalize()
    return nombre

def transform_name2(nombre: str):
    nombres = nombre.split(" ")
    if len(nombres) == 3:
        nombre = nombres[2].capitalize() + "%2C+" + nombres[0].capitalize() + "+" + nombres[1].capitalize()
    if len(nombres) == 4:
        nombre = nombres[2].capitalize() + "-" + nombres[3].capitalize() + "%2C+" + nombres[0].capitalize() + "+" + nombres[1].capitalize()
    return nombre

# Hace la busqueda de la profesion de cada nombre ingresado, con la url 
# proporcionada al encontrar el objeto con el nombre de la persona 
def carrera_catolica(direccion: str):
    try:
        res = requests.get(direccion, timeout=2)
        soup = BeautifulSoup(res.content, "html.parser")
        dom = etree.HTML(str(soup))
        carrera = dom.xpath("//tr[last()]/td[@class='metadataFieldValue']/a")[0].text
    except:
        carrera = "Pregrado"
    return carrera[5:].replace(",", "")

def carreras_andes(direccion: str):
    try:
        res = requests.get(direccion, timeout=2)
        soup = BeautifulSoup(res.content, "html.parser")
        dom = etree.HTML(str(soup))
        carrera = dom.xpath("//ul[@class='breadcrumb hidden-xs']/li[last()-1]/a")[0].text
    except:
        carrera = "Pregrado"
    return carrera.replace(",", "")

def carreras_udea(direccion: str):
    try:
        res = requests.get(direccion, timeout=2)
        soup = BeautifulSoup(res.content, "html.parser")
        dom = etree.HTML(str(soup))
        papa = dom.xpath("//td[@class='metadataFieldValue']/a")[0].text
    except:
        papa = "Pregrado"
    return papa.replace(",", "")

def carreras_li(direccion: str):
    try:
        res = requests.get(direccion, timeout=2)
        soup = BeautifulSoup(res.content, "html.parser")
        dom = etree.HTML(str(soup))
        carrera = dom.xpath("//ul[@class='ds-referenceSet-list']/li/a")[0].text
    except:
        carrera = "Pregrado"
    return carrera.replace(",", "")


def scraper_politecnico(name: str):
    buscar = transform_name(name)
    try:
        url = "https://alejandria.poligran.edu.co/browse?type=author&value=" + buscar
        res = requests.get(url, timeout=2)
        soup = BeautifulSoup(res.content, "html.parser")
        if soup.find("li", class_="ds-artifact-item odd"):
            enlace = soup.find("h4", class_="artifact-title").find("a", href=True).get("href")
            ruta = "https://alejandria.poligran.edu.co" + enlace
            profesion.append(carreras_li(ruta))
            nombre.append(name)
            universidad.append("Politécnico Grancolombiano")
            ciudad.append("Bogotá")
    except:
        print("Fallo politecnico")

def scraper_distrital(name: str):
    buscar = transform_name(name)
    try:
        url = "https://repository.udistrital.edu.co/handle/11349/24/browse?type=author&value=" + buscar
        res = requests.get(url, timeout=2)
        soup = BeautifulSoup(res.content, "html.parser")
        if soup.find("li", class_="ds-artifact-item odd"):
            enlace = soup.find("h4", class_="artifact-title").find("a", href=True).get("href")
            ruta = "https://repository.udistrital.edu.co" + enlace
            profesion.append(carreras_li(ruta))
            nombre.append(name)
            universidad.append("Universidad Distrital Francisco José de Caldas")
            ciudad.append("Bogotá")
    except:
        print("Fallo distrital")

def scraper_cvlac(name: str):
    buscar = name.replace("ñ", "n").upper()
    try:
        url = "https://sba.minciencias.gov.co/Buscador_HojasDeVida/BuscadorIFindIt/busqueda?q=" + buscar + "&pagenum=1&start=0&type=load&lang=es"
        res = requests.get(url, timeout=2)
        soup = BeautifulSoup(res.content, "html.parser")
        resultado = soup.find("div", class_="contentResult")
        if resultado.find("a", class_="link_res fontColor titlesSized").text.strip() == buscar:
            if resultado.find("div", class_="listaInterna"):
                profesion.append(resultado.find("div", class_="listaInterna").text.strip().capitalize())
            else:
                profesion.append("Investigador")
            nombre.append(name)
            universidad.append("Universidad")
            ciudad.append("Colombia")
    except:
        print("Falla cvlac")

def scraper_nacional(name: str):
    buscar = transform_name(name)
    try:
        url = "https://repositorio.unal.edu.co/discover?filtertype_1=author&filter_relational_operator_1=equals&filter_1=" + buscar
        res = requests.get(url, timeout=2)
        soup = BeautifulSoup(res.content, "html.parser")
        if soup.find("div", class_="row ds-artifact-item"):
            enlace = soup.find("div", class_="col-sm-9 artifact-description").find("a", href=True).get("href")
            ruta = "https://repositorio.unal.edu.co" + enlace
            profesion.append(carreras_li(ruta))
            nombre.append(name)
            universidad.append("Universidad Nacional")
            ciudad.append("Bogotá")
    except:
        print("Falla nacional")

def scraper_javeriana(name: str):
    buscar = transform_name(name)
    try:
        url = "https://repository.javeriana.edu.co/browse?type=author&value=" + buscar
        res = requests.get(url, timeout=2)
        soup = BeautifulSoup(res.content, "html.parser")
        if soup.find("li", class_="ds-artifact-item odd"):
            enlace = soup.find("h4", class_="artifact-title").find("a", href=True).get("href")
            ruta = "https://repository.javeriana.edu.co" + enlace
            profesion.append(carreras_li(ruta))
            nombre.append(name)
            universidad.append("Universidad Javeriana")
            ciudad.append("Bogotá")
    except:
        print("Fallo javeriana")

def scraper_utp(name: str):
    buscar = transform_name(name)
    try:
        url = "http://repositorio.utp.edu.co/dspace/handle/11059/1/browse?value=" + buscar + "&type=author"
        res = requests.get(url, timeout=2)
        soup = BeautifulSoup(res.content, "html.parser")
        if soup.find("li", class_="ds-artifact-item odd"):
            enlace = soup.find("h4", class_="artifact-title").find("a", href=True).get("href")
            ruta = "http://repositorio.utp.edu.co" + enlace
            profesion.append(carreras_li(ruta))
            nombre.append(name)
            universidad.append("Universidad Tecnologica de Pereira")
            ciudad.append("Pereira")
    except:
        print("Fallo utp")

def scraper_unad(name: str):
    buscar = transform_name(name)
    try:
        url = "https://repository.unad.edu.co/browse?type=author&value=" + buscar
        res = requests.get(url, timeout=2)
        soup = BeautifulSoup(res.content, "html.parser")
        if soup.find("li", class_="ds-artifact-item odd"):
            enlace = soup.find("h4", class_="artifact-title").find("a", href=True).get("href")
            ruta = "https://repository.unad.edu.co" + enlace
            profesion.append(carreras_li(ruta))
            nombre.append(name)
            universidad.append("Universidad Nacional Abierta")
            ciudad.append("Bogotá")
    except:
        print("Fallo unad")

def scraper_udea(name: str):
    buscar = transform_name(name)
    try:
        url = "https://bibliotecadigital.udea.edu.co/browse?type=author&value=" + buscar
        res = requests.get(url, timeout=2)
        soup = BeautifulSoup(res.content, "html.parser")
        if soup.find("div", class_="panel panel-primary"):
            enlace = soup.select('td[headers="t2"]')[0].find("a", href=True).get("href")
            ruta = "https://bibliotecadigital.udea.edu.co" + enlace
            profesion.append(carreras_udea(ruta))
            nombre.append(name)
            universidad.append("Universidad de Antioquia")
            ciudad.append("Medellin")
    except:
        print("Fallo antioquia")

def scraper_ulibre(name: str):
    buscar = transform_name(name)
    try:
        url = "https://repository.unilibre.edu.co/browse?type=author&value=" + buscar
        res = requests.get(url, timeout=2)
        soup = BeautifulSoup(res.content, "html.parser")
        if soup.find("li", class_="ds-artifact-item odd"):
            enlace = soup.find("h4", class_="artifact-title").find("a", href=True).get("href")
            ruta = "https://repository.unilibre.edu.co" + enlace
            profesion.append(carreras_li(ruta))
            nombre.append(name)
            universidad.append("Universidad Libre")
            ciudad.append("Bogotá")
    except:
        print("Fallo libre")

def scraper_ucatolica(name: str):
    buscar = transform_name(name)
    buscar2 = transform_name2(name)
    try:
        for i in buscar, buscar2:
            url = "https://repository.ucatolica.edu.co/handle/10983/29/browse?type=author&value=" + i
            res = requests.get(url, timeout=2)
            soup = BeautifulSoup(res.content, "html.parser")
            if soup.find("div", class_="panel panel-primary"):
                enlace = soup.find("td", class_="evenRowOddCol").find("a", href=True).get("href")
                ruta = "https://repository.ucatolica.edu.co" + enlace
                profesion.append(carrera_catolica(ruta))
                nombre.append(name)
                universidad.append("Universidad Católica")
                ciudad.append("Bogotá")
    except:
        print("Fallo catolica")

def scraper_eafit(name: str):
    buscar = transform_name(name)
    try:
        url = "https://repository.eafit.edu.co/discover?filtertype=author&filter_relational_operator=equals&filter=" + buscar
        res = requests.get(url, timeout=2)
        soup = BeautifulSoup(res.content, "html.parser")
        if soup.find("div", class_="row ds-artifact-item"):
            enlace = soup.find("div", class_="col-sm-9 artifact-description").find("a", href=True).get("href")
            ruta = "https://repository.eafit.edu.co" + enlace
            profesion.append(carreras_li(ruta))
            nombre.append(name)
            universidad.append("Universidad EAFIT")
            ciudad.append("Medellin")
    except:
        print("Fallo eafit")

def scraper_andes(name: str):
    buscar = transform_name(name)
    try:
        url = "https://repositorio.uniandes.edu.co/discover?filtertype_0=author&filter_relational_operator_0=equals&filter_0=" + buscar
        res = requests.get(url, timeout=2)
        soup = BeautifulSoup(res.content, "html.parser")
        if soup.find("div", class_="row ds-artifact-item"):
            enlace = soup.find("div", class_="col-sm-12 artifact-description").find("a", href=True).get("href")
            ruta = "https://repositorio.uniandes.edu.co" + enlace
            profesion.append(carreras_andes(ruta))
            nombre.append(name)
            universidad.append("Universidad de los Andes")
            ciudad.append("Bogotá")
    except:
        print("Fallo andes")

def scraper_univalle(name: str):
    buscar = transform_name(name)
    try:
        url = "https://bibliotecadigital.univalle.edu.co/browse?type=author&value=" + buscar
        res = requests.get(url, timeout=2)
        soup = BeautifulSoup(res.content, "html.parser")
        if soup.find("li", class_="ds-artifact-item odd"):
            enlace = soup.find("h4", class_="artifact-title").find("a", href=True).get("href")
            ruta = "https://bibliotecadigital.univalle.edu.co/" + enlace
            profesion.append(carreras_li(ruta))
            nombre.append(name)
            universidad.append("Universidad del Valle")
            ciudad.append("Cali")
    except:
        print("Fallo univalle")

def scraper_santotomas(name: str):
    buscar = transform_name(name)
    try:
        url = "https://repository.usta.edu.co/browse?type=author&value=" + buscar
        res = requests.get(url, timeout=2)
        soup = BeautifulSoup(res.content, "html.parser")
        if soup.find("li", class_="ds-artifact-item odd"):
            enlace = soup.find("h4", class_="artifact-title").find("a", href=True).get("href")
            ruta = "https://repository.usta.edu.co" + enlace
            profesion.append(carreras_li(ruta))
            nombre.append(name)
            universidad.append("Universidad Santo Tomás")
            ciudad.append("Bogotá")
    except:
        print("Falla santo tomas")

def scraper_cundinamarca(name: str):
    buscar = transform_name(name)
    try:
        url = "https://repositorio.ucundinamarca.edu.co/browse?type=author&value=" + buscar
        res = requests.get(url, timeout=2)
        soup = BeautifulSoup(res.content, "html.parser")
        if soup.find("li", class_="ds-artifact-item odd"):
            enlace = soup.find("h4", class_="artifact-title").find("a", href=True).get("href")
            ruta = "https://repositorio.ucundinamarca.edu.co" + enlace
            profesion.append(carreras_li(ruta))
            nombre.append(name)
            universidad.append("Universidad de Cundinamarca")
            ciudad.append("Bogotá")
    except:
        print("Fallo cundinamarca")

def scraper_uan(name: str):
    buscar = transform_name(name)
    try:
        url = "http://repositorio.uan.edu.co/simple-search?filterquery=" + buscar + "&filtername=author&filtertype=equals"
        res = requests.get(url, timeout=2)
        soup = BeautifulSoup(res.content, "html.parser")
        if soup.find("div", class_="panel panel-info"):
            enlace = soup.select('td[headers="t2"]')[0].find("a", href=True).get("href")
            ruta = "http://repositorio.uan.edu.co" + enlace
            profesion.append(carreras_udea(ruta))
            nombre.append(name)
            universidad.append("Universidad Antonio Nariño")
            ciudad.append("Bogota")
    except:
        print("Falla uan")

def scraper_santander(name: str):
    buscar = transform_name(name)
    try:
        url = "https://repositorio.udes.edu.co/browse?type=author&value=" + buscar + "&value_lang=spa"
        res = requests.get(url, timeout=2)
        soup = BeautifulSoup(res.content, "html.parser")
        if soup.find("div", class_="panel panel-primary"):
            profesion.append("Pregrado")
            nombre.append(name)
            universidad.append("Universidad de Santander")
            ciudad.append("Bucaramanga")
    except:
        print("Falla santander")

def scraper_militar(name: str):
    buscar = transform_name(name)
    try:
        url = "https://repository.unimilitar.edu.co/browse?type=author&value=" + buscar
        res = requests.get(url, timeout=2)
        soup = BeautifulSoup(res.content, "html.parser")
        if soup.find("li", class_="ds-artifact-item odd"):
            enlace = soup.find("h4", class_="artifact-title").find("a", href=True).get("href")
            ruta = "https://repository.unimilitar.edu.co" + enlace
            profesion.append(carreras_li(ruta))
            nombre.append(name)
            universidad.append("Universidad Militar Nueva Granada")
            ciudad.append("Bogotá")
    except:
        print("Fallo u militar")

paginas = [scraper_politecnico, scraper_distrital, scraper_cvlac, scraper_nacional, scraper_javeriana,
scraper_utp, scraper_unad, scraper_udea, scraper_ulibre, scraper_ucatolica, scraper_eafit, scraper_andes, 
scraper_univalle, scraper_santotomas, scraper_cundinamarca, scraper_uan, scraper_santander, scraper_militar]