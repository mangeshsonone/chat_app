from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class MyWebsocketConsumer(WebsocketConsumer):
    def connect(self):
        print('connected..')
        self.accept()
        print("channel layer",self.channel_layer)
        print("channel layer",self.channel_name)
        async_to_sync (self.channel_layer.group_add)(
            'room1',
            self.channel_name
        )



    def receive(self,text_data=None,bytes_data=None):
        print('message recieve from client',text_data)
        print(type(text_data))
        data=json.loads(text_data)
        mesage=data['msg']

        if self.scope['user'].is_authenticated:
            async_to_sync(self.channel_layer.group_send)(
                'room1',
                {
                    'type':'chat.message',
                    'message':mesage,
                    'user':str(self.scope['user'])
                }
            )
        else:
            self.send(text_data=json.dumps({
            "msg": "Login Required"
      
        }))
        
    def chat_message(self,event):
        print('event',event)
        # user=str(self.scope['user'])
        # print(user)
        self.send(text_data=json.dumps({
            'msg':event['message'],
            'user':event['user']
        }))

    def disconnect(self,close_code):
        print('disconnected')