import os
import openai
openai.api_key = os.environ["OPENAI_API_KEY"]

text_input = input()

prompt = """
下の文章から都道府県名や市区町村名に対してエンティティリンキングを行なってください

text:'''{text_input}'''

一例として

text: 「根室本線は北海道の滝川駅から帯広、釧路を経て根室駅を結ぶJR北海道の路線です。このうち釧路駅から根室駅までの区間は「花咲線」の愛称で呼ばれています。観光シーズンには札幌からのリゾート列車が多数運行されます。キハ283系の車体は、ブルーとグリーンに丹頂鶴の赤を組み合わせ北海道らしさを演出しています.」

では
北海道-都道府県-北海道 https://ja.wikipedia.org/wiki/北海道
帯広-市-帯広市 https://ja.wikipedia.org/wiki/帯広市
釧路-市-釧路市 https://ja.wikipedia.org/wiki/釧路市
根室-市-根室市 https://ja.wikipedia.org/wiki/根室市
札幌-市-札幌市 https://ja.wikipedia.org/wiki/札幌市
となります。

この際、市区町村名と都道府県名だけに対してエンティティリンキングを行うことに注意してください。



"""

res = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    max_tokens=1024,
    temperature=0.6,  
    stop=["###"]
)

print(res.choices[0].text)