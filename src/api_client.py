import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_data(self, endpoint):
        """
        Realiza una petición GET a la API.
        
        :param endpoint: El endpoint específico de la API (por ejemplo, '/users')
        :return: Los datos en formato JSON si la respuesta es exitosa.
        :raises: requests.exceptions.HTTPError si la petición falla.
        """
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url)
        response.raise_for_status()  # Levanta un error si la respuesta fue errónea (status code 4xx/5xx)
        return response.json()

    def post_data(self, endpoint, data):
        """
        Envía datos a la API usando el método POST.
        
        :param endpoint: El endpoint específico de la API (por ejemplo, '/users')
        :param data: Un diccionario con los datos a enviar en la petición POST.
        :return: Los datos en formato JSON si la respuesta es exitosa.
        :raises: requests.exceptions.HTTPError si la petición falla.
        """
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, json=data)
        response.raise_for_status()  # Levanta un error si la respuesta fue errónea (status code 4xx/5xx)
        return response.json()

    def put_data(self, endpoint, data):
        """
        Actualiza datos en la API usando el método PUT.
        
        :param endpoint: El endpoint específico de la API (por ejemplo, '/users/1')
        :param data: Un diccionario con los datos a enviar en la petición PUT.
        :return: Los datos en formato JSON si la respuesta es exitosa.
        :raises: requests.exceptions.HTTPError si la petición falla.
        """
        url = f"{self.base_url}{endpoint}"
        response = requests.put(url, json=data)
        response.raise_for_status()  # Levanta un error si la respuesta fue errónea (status code 4xx/5xx)
        return response.json()

    def delete_data(self, endpoint):
        """
        Elimina datos en la API usando el método DELETE.
        
        :param endpoint: El endpoint específico de la API (por ejemplo, '/users/1')
        :return: Un mensaje de confirmación si la respuesta es exitosa.
        :raises: requests.exceptions.HTTPError si la petición falla.
        """
        url = f"{self.base_url}{endpoint}"
        response = requests.delete(url)
        response.raise_for_status()  # Levanta un error si la respuesta fue errónea (status code 4xx/5xx)
        return {"message": "Resource deleted successfully"}
