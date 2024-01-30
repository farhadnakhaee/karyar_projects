import requests


class DigikalaAPIs:
    def __init__(self):
        self.BASE_URL_API = "https://about.digikala.com/api/v1/dsb/report1401/chapters/"
        self.apis = self.get_apis()

    def request(self, URL: str):
        response = requests.get(URL)
        data = response.json()
        return data, response.status_code

    def get_apis(self):
        data, status_code = self.request(self.BASE_URL_API)
        slugs = [item['slug'] for item in data['results']]
        apis = [f"{self.BASE_URL_API}{slug}" for slug in slugs]
        return apis

    def get_section(self, user_url: str):
        temp = user_url.split('/')
        slug = temp[-2]
        for api in self.apis:
            if api.endswith(slug):
                data, status_code = self.request(api)

                if status_code == 200:
                    for section in data['sections']:
                        if section['html_id'] == temp[-1][1:]:
                            return section


if __name__ == "__main__":
    user_url = "https://about.digikala.com/reports/digikala1401/digikala-customers/#aiv-per-category"
    digi = DigikalaAPIs()
    print(digi.get_section(user_url))