from app import app

if __name__=="__main__":
    with open("allium.cfg") as config_file:
        for line in config_file:
            if line.find('SSL_ENABLED') != -1:
                ssl_enabled = line.split('"')[1::2][0]
            if line.find('HOST') != -1:
                host = line.split('"')[1::2][0]

            if line.find('PORT') != -1:
                port = line.split('"')[1::2][0]

    if ((ssl_enabled == 'True') or (ssl_enabled=='adhoc')):
        import ssl
        if ssl_enabled==True:
            context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
            context.load_cert_chain('ssl/web.crt', 'ssl/web.key')
            app.run(port=port, host=host, ssl_context=context)
        else:
            context = 'adhoc'
            app.run(port=port, host=host, ssl_context=context)

    elif ssl_enabled=='adhoc':
        print("adhoc")
        context='adhoc'
        app.run(port=port,host=host,ssl_context=context)
    else:
        app.run(port=port, host=host)
else:
    exit