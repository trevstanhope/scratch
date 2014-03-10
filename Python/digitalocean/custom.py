import httplib

class DigitalOcean:
    
    
    def __init__(self, api=None, client=None):
        self.api=api
        self.client=client

    def create(self, client=self.client, api=self.client, image=None, name=None, region=None, size=None, backup_active=False):
        conn = httplib.HTTPSConnection("api.digitalocean.com")
        request = '/droplets/new?client_id=' + client + '&api_key=' + api + '&name=' + name + '&size_id=' + size + '&image_id=' + image + '&region_id=' + region
        conn.request("GET", request)
        r1 = conn.getresponse()
        print r1.status, r1.reason, r1.read()
    
    def images(self, client=None, api=None):
        conn = httplib.HTTPSConnection("api.digitalocean.com")
        request = '/images?client_id=' + client + '&api_key=' + api
        conn.request("GET", request)
        resp = conn.getresponse()
        print resp.status, resp.reason, resp.read()

    def regions(self, client=None, api=None):
        conn = httplib.HTTPSConnection("api.digitalocean.com")
        request = '/regions?client_id=' + client + '&api_key=' + api
        conn.request("GET", request)
        resp = conn.getresponse()
        return resp.read()
    
    def 

if __name__ == '__main__':
    root = DigitalOcean()
#    root.images(
#        client='c4de22b97cecd2bbf65c61b9e15dfee5',
#        api='cc7edd986a44936d610bda74ad059d00'
#    )
#    root.regions(
#        client='c4de22b97cecd2bbf65c61b9e15dfee5',
#        api='cc7edd986a44936d610bda74ad059d00'
#    )
    root.create(
        client='c4de22b97cecd2bbf65c61b9e15dfee5',
        api='cc7edd986a44936d610bda74ad059d00',
        image='12573',
        name='temp',
        region='4',
        size='66',
        backup_active=False
    )
    

