import requests
import json
import sys

BASE_URL = "https://api.ce-cotoha.com/api/dev/nlp/"

# アクセストークンを取得する関数
# Function to get the access token.
# 获取访问令牌的函数
def auth(client_id, client_secret):
	token_url = "https://api.ce-cotoha.com/v1/oauth/accesstokens"
	headers = {
			"Content-Type": "application/json",
			"charset": "UTF-8"
	}

	data = {
			"grantType": "client_credentials",
			"clientId": client_id,
			"clientSecret": client_secret
	}

	r = requests.post(token_url,
										headers=headers,
										data=json.dumps(data))

	return r.json()["access_token"]

# 形態素解析する関数
# Function for morphological analysis.
# 形态学分析功能
def parse(sentence, access_token):
	base_url = BASE_URL

	headers = {
			"Content-Type": "application/json",
			"charset": "UTF-8",
			"Authorization": "Bearer {}".format(access_token)
	}
	
	data = {
			"sentence": sentence,
			"type": "default"
	}
	
	r = requests.post(base_url + "v1/parse",
										headers=headers,
										data=json.dumps(data))
	return r.json()

# ひらがなを削除する関数
# Function to delete hiragana.
# 删除平假名的功能
def hira_to_blank(str):
    return "".join(["" if ("ぁ" <= ch <= "ん") else ch for ch in str])

if __name__ == "__main__":
	envjson = open('env.json', 'r')
	json_load = json.load(envjson)
	CLIENT_ID = json_load["client_id"]
	CLIENT_SECRET = json_load["client_secret"]

	document = "私は明日、伊豆大島に行きたい"
	args = sys.argv
	if len(args) >= 2:
		document = str(args[1])

	access_token = auth(CLIENT_ID, CLIENT_SECRET)
	parse_document = parse(document, access_token)
	print(parse_document)
	result_list = list()
	for chunks in parse_document['result']:
			for token in chunks["tokens"]:
					# 形態素解析結果に置き換えルールを適用する
					if (token["pos"] != "連用助詞" 
					and token["pos"] != "引用助詞" 
					and token["pos"] != "終助詞" 
					and token["pos"] != "接続接尾辞" 
					and token["pos"] != "動詞活用語尾"):
							if token["pos"] == "動詞接尾辞" and '終止' in token["features"]:
									if ("する" in token["lemma"]) or ("ます" in token["lemma"]):
											prime = "也"
									elif "たい" in token["lemma"]:
											prime = "希望"
									elif token['lemma'] != 'ない':
											prime = "了"
									else:
											prime = "実行"
							else:
									prime = token["form"]

							if token['lemma'] == '私':
									prime = '我'

							if (token['lemma'] == '君' or token['lemma'] == 'あなた' or token['lemma'] == 'お前'):
									prime = '你'

							if len(token["features"]) != 0:
									if "SURU" in token["features"][0] :
											prime = "実行"
									elif "連体" in token['features'][0]:
											prime = "的"
									elif "疑問符" in token["features"][0]:
											prime = "如何?"

							result_list.append(hira_to_blank(prime))

	print(''.join(result_list))
