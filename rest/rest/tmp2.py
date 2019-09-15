import json


out_dic = {}
out_dic['message'] = '224×224サイズ以上の画像データが対象です。'
out_dic['result'] = '入力が正しくないため、分類処理ができませんでした。'
out_dic['status'] = '200'
print(json.dumps(out_dic, ensure_ascii=False, indent=2))
