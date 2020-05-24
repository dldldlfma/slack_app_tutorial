dialog = {
  "callback_id": "g_test_0",
  "title": "그로스팀 실험 템플릿",
  "submit_label": "Submit",
  "state": "Limo",
  "elements": [
    {
      "type": "text",
      "label": "실험 제목",
      "name": "test_name"
    },
    {
      "type": "textarea",
      "label": "실험 배경",
      "name": "test_background"
    },
    {
      "type": "text",
      "label": "실험의 핵심 가설",
      "name": "test_hypothesis"
    },
    {
      "type": "text",
      "label": "실험이 성공하면 어떤 지표가 변하는가?",
      "name": "test_key_point"
    },
    {
      "type": "textarea",
      "label": "실험이 실패할경우, 어떤 지표를 미리 추적해야 배움을 얻을수 있을까?",
      "name": "test_fail_backup"
    },
    {
      "type": "text",
      "label": "타겟 오디언스",
      "name": "test_target"
    },
    {
      "type": "textarea",
      "label": "실험에 필요한 기능",
      "name": "test_requirements"
    }
  ]
}

alp_dialog = {
  "callback_id": "ryde-46e2b0",
  "title": "Alp-Redmine Prj Builder",
  "submit_label": "Submit",
  "state": "Limo",
  "elements": [
    {
      "type": "text",
      "label": "프로젝트 명",
      "name": "text_0"
    },
    {
      "type": "textarea",
      "label": "프로젝트 설명",
      "name": "text_1"
    },
    {
      "type": "textarea",
      "label": "라벨2",
      "name": "text_2"
    },
    
  ]
}

alp_modals={
	"type": "modal",
	"title": {
		"type": "plain_text",
		"text": "My App",
		"emoji": True
	},
	"submit": {
		"type": "plain_text",
		"text": "제출",
		"emoji": True
	},
	"close": {
		"type": "plain_text",
		"text": "취소",
		"emoji": True
	},
	"blocks": [
		{
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"action_id": "sl_input",
				"placeholder": {
					"type": "plain_text",
					"text": "Placeholder text for single-line input"
				}
			},
			"label": {
				"type": "plain_text",
				"text": "Label"
			},
			"hint": {
				"type": "plain_text",
				"text": "Hint text"
			}
		},
		{
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"action_id": "ml_input",
				"multiline": True,
				"placeholder": {
					"type": "plain_text",
					"text": "Placeholder text for multi-line input"
				}
			},
			"label": {
				"type": "plain_text",
				"text": "Label"
			},
			"hint": {
				"type": "plain_text",
				"text": "Hint text"
			}
		}
	]
}