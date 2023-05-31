# VSCode を用いたエンティティリンキング

vscode を用いてテキストの中の都道府県名と市町村名にエンティティリンキングを行う







##　使い方

1. 作成したレポジトリをローカル環境（PC）上に clone する。

2.  clone したローカル環境下に　.devcontainer/devcontainer.envのファイルを作り
```
OPENAI_API_KEY=自分のAPI Key
```
を書き込む 

 3. .devcontainer/devcontainer.jsonに
```
"runArgs": ["--env-file", ".devcontainer/devcontainer.env"]
```
を書き込む   

4. このままだと.devcontainer/devcontainer.env もpushされてしまうので.gitignoreに
```
*.env
```
を書き込む

### 注意
.gitignore に書き込む前に .devcontainer/devcontainer.envをadd するとignoreされないので注意


5. ローカルのレポジトリで vscode を開く

```
code ディレクトリ
```

6. vscode 左下の `><` こんなアイコンをクリックして `Reopen in container` を選択して、python が実行可能なコンテナ内で vscode を開く

7. vscode でentity_linker.py を実行した後、ターミナル内に好きな文章を入力する

8. 結果が
```
三郷市-市
三郷市
https://ja.wikipedia.org/wiki/三郷市

埼玉県-都道府県
埼玉県
https://ja.wikipedia.org/wiki/埼玉県

東京都-都道府県
東京都
https://ja.wikipedia.org/wiki/東京都

千葉県-都道府県
千葉県
https://ja.wikipedia.org/wiki/千葉県
```
のように出力される


