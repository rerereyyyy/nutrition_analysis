# 栄養分析アプリ
このアプリは、ユーザーが入力した食材と分量に基づいて、カロリーや主要な栄養素の情報をリアルタイムで提供するアプリケーション

## 主な機能
- 食材と分量を入力するとカロリー、タンパク質、脂肪、炭水化物を計算
- 食材データはEdaman API を使用して取得

## 使用技術
- Python 3.9
- Flask 2.0
- Edamam Nutrition Analysis API
- HTML/CSS

## セットアップ
1. リポジトリをクローンします
```bash
git clone https://github.com/username/nutrition_analysis_app.git
cd nutrition_analysis_app
```

2. 仮想環境を作成し、必要なパッケージをインストール
```bash
python3 -m venv venv
source venv/bin/active
pip install -r requirements.txt
```

3. .envファイルを作成し、APIキーを設定


EDAMAM_API_KEY=your_api_key


EDAMAM_API_ID=your_app_id

4. アプリケーションを起動
```bash
python app.py
```

## 使用方法
1. ブラウザで`http://127.0.0.1:5000`にアクセス
2. 材料と分量をフォームに入力して、「分析する」ボタンをクリック
3. 栄養分析結果が表示される
