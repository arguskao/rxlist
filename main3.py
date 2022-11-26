from datetime import datetime
from flask import Flask, flash, request,  redirect, url_for, render_template
from deta import Deta  
from model_cock import *


today=f'{datetime.now().year}'+"."+f'{datetime.now().month}'+"."+f'{datetime.now().day}_'
deta = Deta("c04wvyhi_ecBAX3odCitDT5jLAg88UXf7vNEpEfGu")
drive = deta.Drive("photo")


app = Flask(__name__)
app.secret_key =  b'_5#y2L"F4Q8z\n\xec]/'            # 設置密鑰 
#app.config['MAX_CONTENT_LENGTH'] = 50 * 1024  * 1024  # 上傳檔最大50MB

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif','JPG','PNG','JPEG'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in  ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    if 'filename' not in request.files:            # 如果表單的「檔案」欄位沒有'filename'
        flash('沒有上傳檔案')
        return redirect(url_for('index'))
    file = request.files['filename']               # 取得上傳的檔案 
    if file.filename == '':                        # 若上傳的檔名是空白的… 
        flash('請選擇要上傳的影像')                   # 發出快閃訊息 
        return redirect(url_for('index'))          # 令瀏覽器跳回首頁 
    if file and allowed_file(file.filename):       # 確認有檔案且副檔名在允許之列
        telphone=request.form.get('phone')
        drive.put(today+f'{telphone}.'+file.filename, file)
        flash('影像上傳完畢！手機號碼就可以用來查詢。')
        add=f"INSERT INTO clinic7 VALUES (DEFAULT,'{telphone}','{datetime.now()}','收到，準備包藥中',DEFAULT,0)"
        cur.execute(add)
        conn.commit()
        return render_template('success.html')
    else:
        flash('僅允許上傳png, jpg, jpeg和gif影像檔')
        return redirect(url_for('index'))   # 令瀏覽器跳回首頁
    

@app.route("/query",methods=['GET','POST'])
def form():
    return render_template('query.html')
    
@app.route("/submit", methods=['POST'])
def submit():
    ans = request.values['tel']
    sql='SELECT * from clinic7 where tel=f"{ans}"'
    book= cur.execute(sql)
    if book.count()==0:
        reply="手機號碼輸入錯誤！"             
    else:
        Mode=f"{book.mode}"    
        print("book")
    return render_template('submit.html',**locals())


@app.route("/prize")
def prize():
    return render_template('prize.html')

if __name__ == "__main__":
    app.run()



