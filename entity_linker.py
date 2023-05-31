import os
import openai
openai.api_key = os.environ["OPENAI_API_KEY"]

text_input = input("文章を入力してください")
print("API受付しました")
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "下の文章から都道府県名や市区町村名に対してエンティティリンキングを行なってください\
         出力は 単語-属性-固有名詞 wikipediaのリンク  のようにしてください\
            text: 「根室本線は北海道の滝川駅から帯広、釧路を経て根室駅を結ぶJR北海道の路線です。このうち釧路駅から根室駅までの区間は「花咲線」の愛称で呼ばれています。\
            観光シーズンには札幌からのリゾート列車が多数運行されます。キハ283系の車体は、ブルーとグリーンに丹頂鶴の赤を組み合わせ北海道らしさを演出しています.」"},
        {"role": "assistant", "content": "北海道-都道府県-北海道 https://ja.wikipedia.org/wiki/北海道\
        帯広-市-帯広市 https://ja.wikipedia.org/wiki/帯広市\
        釧路-市-釧路市 https://ja.wikipedia.org/wiki/釧路市\
        根室-市-根室市 https://ja.wikipedia.org/wiki/根室市\
        札幌-市-札幌市 https://ja.wikipedia.org/wiki/札幌市"},
        {"role": "user", "content": f"{text_input}に対して上のようにエンティティリンキングを行なってください。この際、属性が都道府県名と市町村名であるもののみ対象であることに気をつけてください\
         出力結果は\
        帯広-市-帯広市 https://ja.wikipedia.org/wiki/帯広市\
        釧路-市-釧路市 https://ja.wikipedia.org/wiki/釧路市\
        根室-市-根室市 https://ja.wikipedia.org/wiki/根室市\
        札幌-市-札幌市 https://ja.wikipedia.org/wiki/札幌市    のように読みやすいように改行してください"}     
    ],
    temperature=0
)
result = response.choices[0]["message"]["content"].strip()
print(result)
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": f"{result}に対して読みやすいように改行をおこなって出力してください。 駅や路線名、建築物,人物名などは除外してください wikipediaのリンクは表示してください"} 
    ],
    temperature=0
)

print(response.choices[0]["message"]["content"].strip())

