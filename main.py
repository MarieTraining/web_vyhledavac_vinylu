from flask import Flask, render_template, request, make_response
from tabulka import Tabulka 
from cookie_manager import Cookie_Manager

app = Flask(__name__, static_url_path='/static')
@app.route("/")
def home():  
    hledany_vyraz = request.args.get("hledany_vyraz")
    try:
        list_of_cookies = Cookie_Manager('cookie_hledane_vyrazy').get_cookie(hledany_vyraz)
        if hledany_vyraz is None:hledany_vyraz = ""
        tabulka4 = Tabulka().random_detail()
        tabulka5 = Tabulka().mostly_searched(list_of_cookies)
        if tabulka5 is None:tabulka5 = []
        response = make_response(render_template("home.html", hledany_vyraz=hledany_vyraz, tabulka4=tabulka4, list_of_cookies=list_of_cookies, tabulka5=tabulka5))
        Cookie_Manager('cookie_hledane_vyrazy').set_cookie(response, list_of_cookies)
        return response
    except:
        return render_template("home.html")

@app.route("/oprojektu")    
def oprojektu():  
        return render_template("oprojektu.html")   

@app.route("/vyhledani")    
def vyhledani(): 
    try:
        hledany_vyraz = request.args.get("hledany_vyraz")
        list_of_cookies = Cookie_Manager('cookie_hledane_vyrazy').get_cookie(hledany_vyraz) 
        tabulka= Tabulka().print_table()
        tabulka3 =Tabulka().search_table(hledany_vyraz)
        response = make_response(render_template("vyhledani.html", hledany_vyraz=hledany_vyraz, tabulka=tabulka,tabulka3=tabulka3, list_of_cookies=list_of_cookies))
        #response.set_cookie('cookie_hledane_vyrazy', json.dumps(list_of_cookies))
        Cookie_Manager('cookie_hledane_vyrazy').set_cookie(response, list_of_cookies)
        return response
   
    except:
        return render_template("vyhledani.html")  
    
@app.route("/detail")
def detail():
    hledany_vyraz = request.args.get("hledany_vyraz")
    IDdeska = request.args.get('IDdeska')
    try:
        tabulka5 = Tabulka().detail(IDdeska)
        return render_template("detail.html", tabulka5=tabulka5, hledany_vyraz=hledany_vyraz, IDdeska=IDdeska)
    except:
        return render_template("detail.html")
Tabulka().exit()

if __name__ == "__main__":
    app.run()
    