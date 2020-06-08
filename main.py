import os
import json

from flask import Flask, request, make_response
from pprint import pprint
from dialog_templete import dialog

from slack import WebClient
from slack.errors import SlackApiError


token = os.environ['SLACK_BOT_TOKEN'] #From, OS environment variable 
slack_client = WebClient(token=token)

app = Flask(__name__)

def event_handler(event_type, slack_event):
    if event_type =="app_mention":
        channel = slack_event["event"]["channel"]
        text = slack_event["event"]['text']
        text = text.replace("<@U011S1YGX1B>","")
        text = text[1:]
        try:
            text = text.split(",")
        except:
            pass

        response=slack_client.chat_postMessage(channel=channel,text="Hello")
            
        return make_response("앱 멘션 메시지가 보내졌습니다.",200,)

    message = "[%s] 이벤트 핸들러를 찾을 수 없습니다. " %event_type
    return make_response(message, 200, {"X-Slack-No-Retry"})


@app.route("/slack", methods=["GET", "POST"])
def hears():
    slack_event = json.loads(request.data)
    if "challenge" in slack_event:
        return make_response(slack_event["challenge"], 200,
                             {"content_type": "application/json"})

    if "event" in slack_event:
        event_type = slack_event["event"]["type"]
        return event_handler(event_type, slack_event)
    return make_response("슬랙 요청에 이벤트가 없습니다.", 404, {"X-Slack-No-Retry":1})


@app.route("/slack/project", methods=["GET", "POST"])
def sug_hears():
    slack_event = request.values
    
    dialog["callback_id"] = slack_event['user_id'] + "g_test_0"
    open_dialog=slack_client.dialog_open(dialog=dialog,trigger_id=slack_event["trigger_id"])
    
    print(open_dialog)

    return make_response("", 200, {"X-Slack-No-Retry":1})


@app.route("/slack/interaction", methods=["GET", "POST"])
def interaction_hears():
    slack_event = request.values
    submitted_info = json.loads(slack_event['payload'])
        
    if(submitted_info['type'] == "dialog_submission"):
        send_test_templete(submitted_info)
        pprint(submitted_info['channel'])
        response=slack_client.chat_postMessage(channel=submitted_info['channel']['name'],text="Redmine에 데이터 전송 완료")
        """
         return값에 메세지가 들어가면 submit 이후에 dialog box가 자동으로 사라지지 않음
         return으로 아무것도 주지말고 200만 줘야함
        """
        return make_response("", 200)
    

    #modal은 view로 받는데 view_submission type을 따로 줘야된다
    if(submitted_info['type'] == "view_submission"):
        send_test_templete(submitted_info)
        response=slack_client.chat_postMessage(channel=submitted_info['channel']['name'],text="Redmine에 데이터 전송 완료")
        return make_response("", 200)
    
    return make_response("unexpected input in interaction state", 404, {"X-Slack-No-Retry":1})

def send_test_templete(submit_info):
    """
    특정 부분(spreadsheet, Redmine, Asana, Slack 등등)에 데이터를 보낼 코드를 작성
    """
    print("Send data")


@app.route("/", methods=["GET", "POST"])
def index():
    return "Hello World!"

if __name__ == "__main__":
    app.run('0.0.0.0', port=8080)