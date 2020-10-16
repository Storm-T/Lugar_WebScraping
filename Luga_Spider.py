# spider pour récuperer toutes les pages du site de Lugar
# et les stocker

import scrapy  # importation de la bibliothèque scrapy


class LugarSpider(scrapy.spiders): # Création du spider 
    name = "lugar"                 # Nom du spider

    def start_requests(self):             # Fonction de spécification des URL de départ
        url = 'http://www.lugarsalr.com'  # URL de depart

        for url in url:  # Création d'une boucle pour parcourir tous les liens se trouvants dans le site de départ
            yield scrapy.Request(url=url, callback=self.parse)   

    def parse(self, response):                       # Tâche a effectuer sur les pages explorées
        page = response.css('title::text').getall()  # Récupération du titre de la page visitée
        filename = f'lugar-{page}.html'              # Définition du titre du fichier de page précédé de "lugar-"
        with open(filename, 'wb') as f:              # Ouverture du fichier pour enregistrer le contenu de la page
            f.write(response.body)                   # Enregistrement
        self.log(f'saved file {filename}')           # Sauvegarde du fichier dans le log d'exploration du spider
