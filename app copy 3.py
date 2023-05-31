from flask import Flask, request, send_from_directory,url_for
from twilio.twiml.messaging_response import MessagingResponse, Body, Media, Message
import responses as response

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/media/<path:path>')
def send_media(path):
    return send_from_directory('media', path)


def templates_sub_menu():

    print('The templates sub menu has been called')
    msg = request.form.get('Body')
    resp = MessagingResponse()
    resp.message(response.Templates)

    #if msg == 'a':
    message = Message()
    message.body('VPN Template')
    message.media(url_for('send_media',path=''))
    resp.append(message)

    if msg == 'b':
        message = Message()
        message.body('Survey Template')
        message.media(url_for('send_media',path=''))
        resp.append(message)

        
    print('The sub menu code has executed')
    return str(resp)




@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message"""
    #Fetch the message
    msg = request.form.get('Body')

    # Create reply


    resp = MessagingResponse()
    

    if msg == "Hello":
        resp.message("You said: {}".format(response.Welcome_msg))

    elif msg == "1":
        message = Message()
        message.body('')
        message.media(url_for('send_media',path=''))
        #https://3a38-197-221-253-164.eu.ngrok.io

        resp.append(message)

    elif msg == "2":
        resp.message("{}".format(response.Templates))
        templates_sub_menu()

        #message = Message()
       # message.body('VPN Template')
       # message.media(url_for('send_media',path='Econet_Client _ VPN template Site_to_Site.xlsx'))
        # resp.append(message)
    
    elif msg =="a":
        templates_sub_menu()
        
    elif msg == "3":
        message = Message()
        message.body('Survey Template')
        message.media(url_for('send_media',path=''))
        resp.append(message)
        

    elif msg == "4":
        message = Message()
        message.body('VPN Workflow Diagram')
        message.media(url_for('send_media',path=''))
        resp.append(message)

    
    elif msg == "5":
        message = Message()
        message.body('Connectivity Notes')
        message.media(url_for('send_media',path=''))
        resp.append(message)


    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)