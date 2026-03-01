# Prompt String Selector 説明書

## 1. 概要
Prompt String Selector は、ComfyUI でのプロンプト管理を効率化・視覚化するためのカスタムノードセットです。
大量のプロンプトを「キャラクター」「画風」「衣装」などのカテゴリごとにテキストファイルで管理し、それらを ID やスイッチによって動的に制御・統合することを目的としています。

## 2. インストールと構成
ComfyUIの`custom_nodes` フォルダ内で以下のコマンドを実行してください。
```
git clone https://github.com/itom0717/ComfyUI-Prompt-String-Selector.git
```

### ディレクトリ構成
```
ComfyUI-Prompt-String-Selector/
├── __init__.py             # ノードの登録・マッピング管理
├── core_lib.py             # 共通ロジック
├── config.json             # データパス設定（任意）
├── node_aggregator10.py    # プロンプト統合ノード（入力10）
├── node_aggregator20.py    # プロンプト統合ノード（入力20）
├── node_prompt_switch5.py  # IDによる分岐スイッチノード（入力5）
├── node_prompt_switch10.py # IDによる分岐スイッチノード（入力10）
├── node_prompt_switch20.py # IDによる分岐スイッチノード（入力20）
├── node_id_selector.py     # 数値入力・メモ用ノード
├── (その他各カテゴリの .py ファイル)
└── data/                   # プロンプトファイルを格納するフォルダ
     ├── negative/          # ネガティブプロンプト用
     ├── art_style/         # 画質スタイルプロンプト用
     ├── background/        # 背景プロンプト用
     ├── camera/            # カメラワークプロンプト用
     ├── character/         # キャラクタープロンプト用
     ├── clothing1/         # 衣装プロンプト用1（春）
     ├── clothing2/         # 衣装プロンプト用2（夏）
     ├── clothing3/         # 衣装プロンプト用3（秋）
     ├── clothing4/         # 衣装プロンプト用4（冬）
     ├── emotion/           # 表情プロンプト用
     ├── extra1/            # その他プロンプト用1
     ├── extra2/            # その他プロンプト用2
     ├── extra3/            # その他プロンプト用3
     ├── extra4/            # その他プロンプト用4
     ├── extra5/            # その他プロンプト用5
     ├── pose1/             # ポーズプロンプト用1
     ├── pose2/             # ポーズプロンプト用2
     ├── season/            # 季節プロンプト用
     └── time/              # 時間帯プロンプト用
```

## 3. config.json の設定 (オプション)
データフォルダを外部（OneDriveや別ドライブ等）に置きたい場合は、config.json を作成して絶対パスを指定してください。
```
{
    "data_path": "C:\\Users\\YourName\\OneDrive\\AI_Data\\data"
}
```
* Windowsパスの \\ は \\\\ と二重に記述してください。

## 3. データの作成ルール
各カテゴリのフォルダ内には、プロンプトを記述した .txt ファイルを1つ以上配置します。
* ファイル一つ一つがプルダウンの選択項目となります。
* ファイル名の拡張子を除いた部分がプルダウンの選択項目で表示されます。
* ファイル名：
   01_normal_eyes.txt のように、「2桁の数字 + アンダーバー」 で始めてください。
* IDの認識：
   ファイル名の先頭の数字が、ノードから出力される id (INT) として処理されます。
* コメント機能：
   ファイル内で // または /* ... */ を使用すると、その部分は出力から除外されます。

## 4. ノード一覧と機能
### 4-1. 各種セレクター系
各フォルダ内のテキストファイル一覧を選択し、ファイルの内容 (text) と番号 (id) を出力します。

| 対応ノード | カテゴリ |
|:----|:---|
| Art Style | 画質スタイル |
| Character |  キャラクター |
| Emotion | 表情 |
| Pose 1 | ポーズ1 |
| Pose 2 | ポーズ2 |
| Clothing 1 | 衣装プロンプト用1（春） | 
| Clothing 2 | 衣装プロンプト用2（夏） |
| Clothing 3 | 衣装プロンプト用3（秋） |
| Clothing 4 | 衣装プロンプト用4（冬） |
| Season | 季節 |
| Time | 時間帯 |
| Background | 背景 |
| Camera | カメラワーク |
| Extra 1 | その他1 |
| Extra 2 | その他2 |
| Extra 3 | その他3 |
| Extra 4 | その他4 |
| Negative | ネガティブプロンプト |

* custom_input：
  プルダウンでこれを選択すると、ノード内のテキストボックスに書いた内容が優先出力されます。

### 4-2. 数値選択
任意の数値を出力します。
| 対応ノード |
|:----|
| ID Select  |

* メモ欄はワークフロー内の自分用備忘録として機能します。

### 4-3. プロンプト選択
ID 入力に基づき、接続された text_01～ のいずれかの入力を切り替えて出力します。

| 対応ノード | 入力ノード数 |
|:----|----:|
| Prompt Switch (5) |5|
| Prompt Switch (10) |10|
| Prompt Switch (20) |20|

* 未接続のピンが選択された場合は、空の文字列を出力します。

### 4-4. プロンプト連結
入力されたプロンプトを1つに連結して出力します。
| 対応ノード | 入力ノード数 |
|:----|----:|
| Aggregator (10) |10|
| Aggregator (20) |10|

* 未接続のピンは無視します。
* 各プロンプトの間に自動でカンマが挿入されます。


## Licence
* MIT  
    * see LICENSE.txt

## Author

[itom0717](https://github.com/itom0717)
