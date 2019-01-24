def Mail_Message(date,action_time,latit,long,depth,strength,city):
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title></title>
    </head>
    <body>
    
    <div style="width: 300px; border: 4px solid black; background-color: rgb(237, 237, 237);">
    
        <p style="text-align: center; font-size: 19px;"><b>Depreme Ait Bilgiler</b></p>
        <hr style="height: 1px; background-color: black; border-color:black">
        <div style="margin-left: 6px">
            <p><b>Tarih:</b>  """ + date + """</p>
            <p><b>Saat:</b>  """ + action_time + """</p>
            <p><b>Derinlik:</b>  """ + depth + """ km</p>
            <p><b>Büyüklük:</b>  """ + strength + """</p>
            <p><b>Şehir:</b>  """ + city + """</p>
            <p><b>Haritalarda:  </b> <a href='https://www.google.com/maps/place/""" + latit + '+' + long + """'>Google Maps</a></p>
        </div>
    
    </div>
    
    </body>
    </html>
    """
