import os
import json
from slacker import Slacker
from flask import Flask, request, make_response
from pprint import pprint
from dialog_templete import dialog

#이제 하나씩 slack-client로 변환시켜야 할듯
from slack import WebClient
from slack.errors import SlackApiError



token = os.environ['SLACK_BOT_TOKEN'] #From, OS environment variable 
slack = Slacker(token)
slack_client = WebClient(token=token)

app = Flask(__name__)

def get_answer():
    return "안녕하세요."

def event_handler(event_type, slack_event):
    if event_type =="app_mention":
        channel = slack_event["event"]["channel"]
        #pprint(slack_event)
        #pprint(dir(slack_event))
        #print(slack_event["event"]['text'])
        #print(slack_event["event"]['blocks'][0])
        #print(slack_event)

        text = slack_event["event"]['text']
        text = text.replace("<@U011S1YGX1B>","")
        text = text[1:]
        try:
            text = text.split(",")
        except:
            pass

        #slack.chat.post_message(channel, text)
        #slack.chat.post_message(channel, tutorial)
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


@app.route("/slack/g_test", methods=["GET", "POST"])
def sug_hears():
    slack_event = request.values
    #slack_other = request.data
    """
    print("\n\n----request.values----\n")
    print(slack_event)

    print("\n\n----request.data----")
    print(slack_other)

    print("\n\n----pprint(dir(request))----")
    pprint(dir(request))
    """

    dialog["callback_id"] = slack_event['user_id'] + "g_test_0"
    open_dialog=slack.dialog.open(dialog,slack_event["trigger_id"])
    print(open_dialog)

    return make_response("", 200, {"X-Slack-No-Retry":1})

@app.route("/slack/interaction", methods=["GET", "POST"])
def interaction_hears():
    slack_event = request.values
    #slack_event = json.loads(request.data)
    #print("\n\n----request.values----\n")
    #print(slack_event)
    submitted_info = json.loads(slack_event['payload'])
    #pprint(submitted_info)
    pprint(submitted_info)


    
    if(submitted_info['type'] == "dialog_submission"):
        send_test_templete(submitted_info)
        submitted_data = setup_submit_data(submitted_info)
        print("post_message")       
        slack.chat.post_message(submitted_info['channel']['name'],submitted_data)
        """
         return값에 어떤 메세지가 들어가면 submit 이후에 dialog box가 자동으로 사라지지 않음
         위 코드를 보면
         return make_response("interaction command", 200, {"X-Slack-No-Retry":1})

         이렇게 되어 있는데 

         "interaction command" 때문에 자동으로 안꺼진거임 

         무조건 아무것도 주지말고 200만 줘야됨
        """
        return make_response("", 200)
    
    #return make_response("setup in interaction state", 200, {"X-Slack-No-Retry":1})
    return make_response("unexpected input in interaction state", 404, {"X-Slack-No-Retry":1})

def send_test_templete(submit_info):
    print("Send data")

def setup_submit_data(submitted_info):
    text = "===:heart:그로스팀 아이디어 제출 결과:heart:===\n" +\
           "*>실험 제목* " + submitted_info["submission"]["test_name"] + "\n\n" +\
            \
           "*>실험 배경* " + submitted_info["submission"]["test_background"] + "\n\n" +\
            \
           "*>실험의 핵심가설* " + submitted_info["submission"]["test_hypothesis"] + "\n\n" + \
            \
           "*>실험이 성공하면 어떤 지표가 변하는가?*  " + submitted_info["submission"]["test_key_point"] + "\n\n" + \
           \
           "*>실험 실험이 실패할경우, 어떤 지표를 미리 추적해야 배움을 얻을 수 있을까?* " + submitted_info["submission"]["test_fail_backup"] + "\n\n" + \
           \
           "*>타겟 오디언스* " + submitted_info["submission"]["test_target"] + "\n\n" + \
           \
           "*>실험에 필요한 기능* " + submitted_info["submission"]["test_requirements"] + "\n\n" + \
           "==============================\n"
    return text

@app.route("/", methods=["GET", "POST"])
def index():
    return "Hello World!"

if __name__ == "__main__":
    app.run('0.0.0.0', port=8080)