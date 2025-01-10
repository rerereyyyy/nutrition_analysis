import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='urllib3')
from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

#.env から各種情報を取得
API_KEY = os.getenv('EDAMAM_API_KEY')
APP_ID = os.getenv('EDAMAM_API_ID')
NUTRITION_API_URL = os.getenv('NUTRITION_API_URL')

@app.route('/', methods=['GET','POST'])
def index():
    nutrition_result = None
    if request.method == 'POST':
        #フォームから材料リストを取得
        ingredients = request.form.get('ingredients')
        
        #入力された材料をリストに分割してから送信
        ingredients_list = [ingredient.strip() for ingredient in ingredients.split(';')]
        
        #APIに送信するためのデータ
        ingredients_data = {
            "ingr":ingredients_list
        }
        
        #APIリクエストのパラメータ
        params = {
            "app_id":APP_ID,
            "app_key":API_KEY
        }
        
        #POSTリクエストを送信
        response = requests.post(NUTRITION_API_URL, json=ingredients_data, params=params)
        
        if response.status_code == 200:
            data = response.json()
            if data:
                nutrition_result = {
                    'calories':data.get('calories','N/A'),
                    'protein':data.get('protein','N/A'),
                    'carbohydrates':data.get('carbohydrates','N/A'),
                    'fat':data.get('fat','N/A')
                }
        else:
            print(f"Error: {response.status_code}, {response.text}")
            nutrition_result = {'error':'栄養分析に失敗しました'}
            
    return render_template('index.html',result=nutrition_result)

if __name__ == '__main__':
    app.run(debug=True)