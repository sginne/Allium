from app import app
if __name__=="__main__":
    with open("allium.cfg") as config_file:
        for line in config_file:
            if line.find('SSL_ENABLED') != -1:
                ssl_enabled = line.split('"')[1::2][0]

    print (template_name)
    app.run(port=8080)
else:
    exit