import digitalocean


client = 'c4de22b97cecd2bbf65c61b9e15dfee5'
api = 'cc7edd986a44936d610bda74ad059d00'

# Sample droplet
droplet = digitalocean.Droplet(
    client_id=client,
    api_key=api,
    name='temp',
    region_id=4, # New York,
    image_id=12573,
    size_id=66, # 512MB,
    backup_active=False
)
#droplet.create()

# Events for current droplet
events = droplet.get_events()
for event in events:
    event.load()
    print event.percentage

# Shutdown all droplets
manager = digitalocean.Manager(client_id=client, api_key=api)
my_droplets = manager.get_all_droplets()
for droplet in my_droplets:
    droplet.shutdown()

# Destory droplets
manager = digitalocean.Manager(client_id=client, api_key=api)
my_droplets = manager.get_all_droplets()
for droplet in my_droplets:
    print droplet
    droplet.destroy()
