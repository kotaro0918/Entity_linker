import os
import openai
openai.api_key = os.environ["OPENAI_API_KEY"]
sample_input=" 根室本線は北海道の滝川駅から帯広、釧路を経て根室駅を結ぶＪＲ北海道の路線です。\
    このうち釧路駅から根室駅までの区間は「花咲線」の愛称で呼ばれています。観光シーズンには札幌から\
    のリゾート列車が多数運行されます。キハ283系の車体は、ブルーとグリーンに丹頂鶴の赤を組み合わせ北海道らしさを演出しています"
sample_result='''
{"都道府県名": "北海道","市区町村名": ["滝川市", "帯広市", "釧路市", "根室市", "札幌市"]}'''
sampel_linking='''{"北海道-都道府県-北海道":"https://ja.wikipedia.org/wiki/北海道",
"帯広-市-帯広市": "https://ja.wikipedia.org/wiki/帯広市",
"釧路-市-釧路市": "https://ja.wikipedia.org/wiki/釧路市",
"根室-市-根室市": "https://ja.wikipedia.org/wiki/根室市",
"札幌-市-札幌市": "https://ja.wikipedia.org/wiki/札幌市",}'''
text_input = input("文章を入力してください")
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"system","content":"あなたは与えられた文章の中から都道府県名と市区町村名を抜き出してJSON形式で出力するエージェントです。\
         なかった場合はnullを返してください."},
        {"role":"user", "content":sample_input},
        {"role":"assistant","content":sample_result},
        {"role":"user", "content": text_input}
    ],
    temperature =0
)
print(response.choices[0]["message"]["content"].strip())
entity_json=response.choices[0]["message"]["content"].strip()
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"system", "content":"あなたは入力された都道府県名と市町村名に対して関連するウィキペディア\
         のページを出力するエージェントです。入力、出力ともにJSON形式で行われます。出力はJSON形式です"},
        {"role":"user", "content":sample_result},
        {"role":"assistant","content":sampel_linking},
        {"role":"user", "content":entity_json}
    ],
    temperature=0
)
print(response.choices[0]["message"]["content"].strip())