# VSCode を用いたエンティティリンキング

vscode を用いてテキストの中の都道府県名と市町村名にエンティティリンキングを行う
### 使い方

1. 作成したレポジトリをローカル環境（PC）上に clone する。
1. ローカルのレポジトリで vscode を開く

```
code ディレクトリ
```

3. vscode 左下の `><` こんなアイコンをクリックして `Reopen in container` を選択して、python が実行可能なコンテナ内で vscode を開く

4. vscode でentity_linker.py を実行した後、ターミナル内に好きな文章を入力する

5. 結果が
```
埼玉県-都道府県-埼玉県 https://ja.wikipedia.org/wiki/埼玉県        三郷市-市-三郷市 https://ja.wikipedia.org/wiki/三郷市
```
のように出力される


