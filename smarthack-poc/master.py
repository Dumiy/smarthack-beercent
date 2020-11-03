from bs4 import BeautifulSoup
from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
import pyodbc
from sphinx.util import requests
import json
import modules.top_phones as phones
import modules.techspot as tech
from flask_cors import CORS, cross_origin


#from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


driver="{SQL Server Native Client 11.0}"
server="smarthack2020server.database.windows.net"
database="Smarthack2020SearchDB"
username="beercent"
Pwd="Password01!"
#pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+Pwd+";Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36'}

category = ["smartphone","smartwatch",'laptop','mouse',"telefon",'headphones']

positive_wrds = ['absolutely', 'accepted', 'acclaimed', 'accomplish', 'accomplishment', 'achievement', 'action', 'active', 'admire', 'adorable', 'adventure', 'affirmative', 'affluent', 'agree', 'agreeable', 'amazing', 'angelic', 'appealing', 'approve', 'aptitude', 'attractive', 'awesome', 'beaming', 'beautiful', 'believe', 'beneficial', 'bliss', 'bountiful', 'bounty', 'brave', 'bravo', 'brilliant', 'bubbly', 'calm', 'celebrated', 'certain', 'champ', 'champion', 'charming', 'cheery', 'choice', 'classic', 'classical', 'clean', 'commend', 'composed', 'congratulation', 'constant', 'cool', 'courageous', 'creative', 'cute', 'dazzling', 'delight', 'delightful', 'distinguished', 'divine', 'earnest', 'easy', 'ecstatic', 'effective', 'effervescent', 'efficient', 'effortless', 'electrifying', 'elegant', 'enchanting', 'encouraging', 'endorsed', 'energetic', 'energized', 'engaging', 'enthusiastic', 'essential', 'esteemed', 'ethical', 'excellent', 'exciting', 'exquisite', 'fabulous', 'fair', 'familiar', 'famous', 'fantastic', 'favorable', 'fetching', 'fine', 'fitting', 'flourishing', 'fortunate', 'free', 'fresh', 'friendly', 'fun', 'funny', 'generous', 'genius', 'genuine', 'giving', 'glamorous', 'glowing', 'good', 'gorgeous', 'graceful', 'great', 'green', 'grin', 'growing', 'handsome', 'happy', 'harmonious', 'healing', 'healthy', 'hearty', 'heavenly', 'honest', 'honorable', 'honored', 'hug', 'idea', 'ideal', 'imaginative', 'imagine', 'impressive', 'independent', 'innovate', 'innovative', 'instant', 'instantaneous', 'instinctive', 'intellectual', 'intelligent', 'intuitive', 'inventive', 'jovial', 'joy', 'jubilant', 'keen', 'kind', 'knowing', 'knowledgeable', 'laugh', 'learned', 'legendary', 'light', 'lively', 'lovely', 'lucid', 'lucky', 'luminous', 'marvelous', 'masterful', 'meaningful', 'merit', 'meritorious', 'miraculous', 'motivating', 'moving', 'natural', 'nice', 'novel', 'now', 'nurturing', 'nutritious', 'okay', 'one', 'one-hundred percent', 'open', 'optimistic', 'paradise', 'perfect', 'phenomenal', 'pleasant', 'pleasurable', 'plentiful', 'poised', 'polished', 'popular', 'positive', 'powerful', 'prepared', 'pretty', 'principled', 'productive', 'progress', 'prominent', 'protected', 'proud', 'quality', 'quick', 'quiet', 'ready', 'reassuring', 'refined', 'refreshing', 'rejoice', 'reliable', 'remarkable', 'resounding', 'respected', 'restored', 'reward', 'rewarding', 'right', 'robust', 'safe', 'satisfactory', 'secure', 'seemly', 'simple', 'skilled', 'skillful', 'smile', 'soulful', 'sparkling', 'special', 'spirited', 'spiritual', 'stirring', 'stunning', 'stupendous', 'success', 'successful', 'sunny', 'super', 'superb', 'supporting', 'surprising', 'terrific', 'thorough', 'thrilling', 'thriving', 'tops', 'tranquil', 'transformative', 'transforming', 'trusting', 'truthful', 'unreal', 'unwavering', 'up', 'upbeat', 'upright', 'upstanding', 'valued', 'vibrant', 'victorious', 'victory', 'vigorous', 'virtuous', 'vital', 'vivacious', 'wealthy', 'welcome', 'well', 'whole', 'wholesome', 'willing', 'wonderful', 'wondrous', 'worthy', 'wow', 'yes', 'yummy', 'zeal', 'zealous','abundenta', 'acceptare', 'acord', 'actiune', 'activ', 'activare', 'acuratete', 'adaptabilitate', 'adaugare', 'admirabil', 'admiratie', 'adorabil', 'adorare', 'afectiune', 'afirmare', 'afirmatie', 'agilitate', 'agreabil', 'ajutor', 'alegere', 'altruism', 'ambitie', 'amuzament', 'anticipare', 'apartenenta', 'apartinut', 'apreciat', 'apreciata', 'apreciere', 'apreciez', 'aprobare', 'aprobat', 'aprobata', 'armonie', 'armonioasa', 'armonios', 'asertivitate', 'asigura', 'atentie', 'a-tipasa', 'atotputernic', 'atotstiutor', 'autenticitate', 'autocontrol', 'autonomie', 'avantaj', 'aventura', 'accepta', 'actiona', 'activa', 'adauga', 'admira', 'adora', 'afirma', 'ajutat', 'apartine', 'aproba','beatifica', 'beatitudine', 'benedictiune', 'benefica', 'beneficiat', 'beneficiata', 'beneficiati', 'beneficiu', 'bine', 'bineaisosit', 'bineaivenit', 'bineatisosit', 'bineativenit', 'binemeritat', 'binecuvantare', 'binecuvantat', 'binecuvantata', 'binecuvantati', 'binefacere', 'binevoitoare', 'blagoslovenie', 'blagoslovire', 'blandete', 'bliliant', 'bogat', 'bogata', 'bogati', 'bogatie', 'bravo', 'bucurata', 'bucurie', 'bucuros', 'bun', 'bunatate', 'bunavestire', 'bunavointa', 'beneficia', 'binecuvanta', 'sebucura','calm', 'capabil', 'capabilitate', 'caritate', 'certitudine', 'ceruri', 'cinste', 'cinstire', 'cinstit', 'cinstita', 'claritate', 'colaborare', 'compasiune', 'competenta', 'comunicare', 'comunitate', 'concentrare', 'conexiune', 'confort', 'consecventa', 'consolidare', 'consolidat', 'consolidata', 'constientizare', 'constientizat', 'constientizata', 'constiinciozitate', 'constiinta', 'construire', 'construita', 'continua', 'continuitate', 'contributie', 'control', 'convingatoare', 'convingere', 'cooperare', 'corai', 'corectitudine', 'creare', 'creat', 'creata', 'creatie', 'creativitate', 'credinta', 'curaj', 'curajoasa', 'curajos', 'curajosi', 'curatenie', 'curatire', 'curatit', 'curatita', 'curiozitate', 'curtoazie', 'cinsti', 'consolida', 'constientiza', 'construit', 'crea', 'crede', 'curati','datorie', 'decent', 'delicat', 'delicatete', 'delicios', 'demnitate', 'deplina', 'desavarsire', 'desavarsit', 'desavarsita', 'descoperire', 'desfat', 'desfatari', 'desfatat', 'desfatata', 'detasare', 'determinare', 'devotament', 'dinamica', 'dinamice', 'directie', 'disciplina', 'discretie', 'distractie', 'diversitate', 'divin', 'divinitate', 'dobandire', 'dobandit', 'dobandita', 'dorinta', 'dorit', 'dragoste', 'drept', 'dreptate', 'duh', 'duhovnicesc', 'dumnezeu', 'desavarsi', 'dobandi', 'tedesfata','echilibru', 'educatie', 'eficacitate', 'eficient', 'eficienta', 'egalitate', 'eleganta', 'emotie', 'empatie', 'emulare', 'energie', 'entuziasm', 'entuziasmat', 'entuziasmata', 'entuziast', 'etern', 'euforie', 'evlavie', 'exaltare', 'excelent', 'excelenta', 'experienta', 'expertiza', 'explorare', 'expresivitate', 'exprimare', 'exprimat', 'extraordinar', 'exuberant', 'exprima', 'seentuziasma', 'seexprima','fabulos', 'faima', 'familie', 'fantastic', 'fericire', 'fericit', 'fericita', 'fericiti', 'fiabilitate', 'fidelitate', 'flexibilitate', 'floare', 'focus', 'forta', 'frumos', 'frumosa', 'frumosi', 'frumusete', 'seferici','genera', 'generoasa', 'generos', 'generozitate', 'genial', 'genius', 'gratiat', 'gratiata', 'gratiati', 'gratie', 'gratia','har', 'harnic', 'harnica', 'harnici', 'harnicie', 'hortarata', 'hotarat', 'hotarati', 'harnici', 'sehotari','idee', 'iertare', 'iertat', 'iertata', 'iertati', 'imaginatie', 'imbarbatare', 'imbogatire', 'imbogatit', 'imbogatita', 'imbogatiti', 'imbunatatire', 'impacare', 'impartialitate', 'impreuna', 'improspatat', 'improspatata', 'improspateaza', 'imputernicire', 'imputernicit', 'inaltare', 'inaltat', 'inaltata', 'inaltpreasfintit', 'incantare', 'incredere', 'incredereinsine', 'incredibil', 'increzatoare', 'increzator', 'incurajare', 'independenta', 'individualism', 'indrazneala', 'indraznet', 'indumnezeire', 'infatisare', 'infinit', 'influenta', 'informativ', 'infrumusetare', 'ingaduinta', 'ingaduitoare', 'ingaduitor', 'ingeniozitate', 'inima', 'inimoasa', 'inimos', 'inovare', 'inovat', 'inovatie', 'inspirat', 'inspirata', 'inspiratie', 'insufletit', 'intampinare', 'intampinat', 'intampinata', 'intarire', 'intarit', 'intarita', 'integritate', 'inteleasa', 'intelegere', 'intelepciune', 'inteles', 'inteligenta', 'intensitate', 'intentie', 'interes', 'interesant', 'interesanta', 'interesanti', 'interior', 'intimitate', 'intrajutorare', 'intrupare', 'intuitie', 'intuitiv', 'intuitiva', 'inventivitate', 'investitie', 'inviere', 'irezistibil', 'iubire', 'iubit', 'iubita', 'iubitoare', 'iubitor', 'izvoritoare', 'ierta', 'imbarbata', 'imbogati', 'improspata', 'inalta', 'incuraja', 'indrazni', 'inova', 'inspira', 'intampina', 'intari', 'intui', 'investi', 'iubi', 'seimbogati', 'seincrede', 'seiubi','lauda', 'laudabil', 'laudat', 'liber', 'libera', 'liberi', 'libertate', 'lider', 'limpede', 'logic', 'loial', 'loiala', 'loiali', 'loialitate', 'longevitate', 'lucioasa', 'lucios', 'lucire', 'lucrator', 'lumina', 'luminat', 'luminata', 'lux', 'luci', 'lumina','magic', 'magnific', 'maimult', 'maiestate', 'mandrie', 'mangaiat', 'mangaiata', 'mangaiere', 'mantuire', 'mantuit', 'mantuita', 'mantuitor', 'mantuitorul', 'marinimie', 'maririiluidumnezeu', 'marit', 'marturie', 'maturitate', 'merit', 'meritat', 'mila', 'milostenie', 'minunat', 'minunata', 'minune', 'miracol', 'miraculoasa', 'miraculos', 'miruit', 'moderatie', 'modestie', 'moralitate', 'motivare', 'motivat', 'motivata', 'motivatie', 'multe', 'multumesc', 'multumire', 'multumiri', 'multumit', 'multumita', 'mangaia', 'mantui', 'motiva', 'multumi', 'semantui', 'seminuna','mie', 'maririiluidumnezeu', 'marit', 'marturie', 'maturitate', 'merit', 'meritat', 'mila', 'milostenie', 'minunat', 'minunata', 'minune', 'miracol', 'miraculoasa', 'miraculos', 'miruit', 'moderatie', 'modestie', 'moralitate', 'motivare', 'motivat', 'motivata', 'motivatie', 'multe', 'multumesc', 'multumire', 'multumiri', 'multumit', 'multumita', 'mangaia', 'mantui', 'motiva', 'multumi', 'semantui', 'seminuna', 'nadejde', 'nascatoarededumnezeu', 'neasemanat', 'neasemuit', 'neinfricat', 'nelimitat', 'nemarginit', 'nerezistent', 'nerezistenta', 'nirvana', 'nobil', 'nobilare', 'nobilat', 'nobilata', 'nonviolenta', 'omagial', 'omenia', 'onoare', 'oportunitate', 'optimism', 'optimist', 'optimista', 'ordine', 'organizare', 'orientare', 'original', 'originalitate', 'ospitalitate', 'pace', 'paradis', 'pasionat', 'pasionata', 'pasiune', 'perfect', 'perfecta', 'perfectiune', 'perseverenta', 'placere', 'placut', 'plenitudine', 'plinatate', 'plus', 'pocainta', 'politete', 'pot', 'potential', 'pozitiv', 'pozitiva', 'pozitivi', 'pozitivitate', 'practic', 'preafericit', 'preamarire', 'preamarit', 'preasfintit', 'precizie', 'pregatire', 'prezenta', 'prieten', 'prietena', 'prietenie', 'prietenos', 'proactiv', 'proactiva', 'proactivitate', 'progres', 'prolific', 'prosperitate', 'prudenta', 'punctualitate', 'pur', 'puritate', 'putere', 'puternic', 'puternica', 'pacifica', 'preamari', 'preasfinti', 'prosperasacru', 'salvare', 'satisfacere', 'satisfactie', 'satisfacut', 'securitate', 'seninatate', 'sensibilitate', 'sentiment', 'serenitate', 'servi', 'sfant', 'sfanta', 'sfantulduh', 'sfintiiparinti', 'sfintit', 'siguranta', 'simpatie', 'simplificare', 'simplitate', 'simplu', 'sinceritate', 'sine', 'sistematizare', 'slava', 'slavdumnezeiasca', 'spera', 'speranta', 'spirit', 'splendid', 'spori', 'sporire', 'spornica', 'stabilitate', 'stiut', 'straluci', 'stralucire', 'stralucit', 'stralucita', 'suflet', 'suprem', 'sustine', 'sustinut', 'fiseren', 'sti', 'stralucitact', 'tandrete', 'tare', 'tatal', 'tenace', 'tenacitate', 'toleranta', 'traditie', 'trambita', 'trezire', 'trezit', 'trezita', 'triumfatoare', 'triumfator', 'fitolerant', 'trezi', 'uimitor', 'uman', 'umor', 'unic', 'unire', 'unitate', 'usor', 'usurare', 'usurinta', 'util', 'utile', 'utilizare', 'valid', 'validare', 'validat', 'valoare', 'valori', 'valoroase', 'varietate', 'verificare', 'verosimil', 'verosimilitate', 'vesel', 'veselie', 'vesnicie', 'viabil', 'vibrant', 'victorie', 'vigilent', 'vigilenta', 'virtuoasa', 'virtuos', 'virtute', 'vitalitate', 'viu', 'vivace', 'vointa', 'voios', 'voiosie', 'vulnerabilitate']

negative_wrds =  ['abysmal', 'adverse', 'alarming', 'angry', 'annoy', 'anxious', 'apathy', 'appalling', 'atrocious', 'awful', 'bad', 'banal', 'barbed', 'belligerent', 'bemoan', 'beneath', 'boring', 'broken', 'callous', "can't", 'clumsy', 'coarse', 'cold', 'cold-hearted', 'collapse', 'confused', 'contradictory', 'contrary', 'corrosive', 'corrupt', 'crazy', 'creepy', 'criminal', 'cruel', 'cry', 'cutting', 'damage', 'damaging', 'dastardly', 'dead', 'decaying', 'deformed', 'deny', 'deplorable', 'depressed', 'deprived', 'despicable', 'detrimental', 'dirty', 'disease', 'disgusting', 'disheveled', 'dishonest', 'dishonorable', 'dismal', 'distress', "don't", 'dreadful', 'dreary', 'enraged', 'eroding', 'evil', 'fail', 'faulty', 'fear', 'feeble', 'fight', 'filthy', 'foul', 'frighten', 'frightful', 'gawky', 'ghastly', 'grave', 'greed', 'grim', 'grimace', 'gross', 'grotesque', 'gruesome', 'guilty', 'haggard', 'hard', 'hard-hearted', 'harmful', 'hate', 'hideous', 'homely', 'horrendous', 'horrible', 'hostile', 'hurt', 'hurtful', 'icky', 'ignorant', 'ignore', 'ill', 'immature', 'imperfect', 'impossible', 'inane', 'inelegant', 'infernal', 'injure', 'injurious', 'insane', 'insidious', 'insipid', 'jealous', 'junky', 'lose', 'lousy', 'lumpy', 'malicious', 'mean', 'menacing', 'messy', 'misshapen', 'missing', 'misunderstood', 'moan', 'moldy', 'monstrous', 'naive', 'nasty', 'naughty', 'negate', 'negative', 'never', 'no', 'nobody', 'nondescript', 'nonsense', 'not', 'noxious', 'objectionable', 'odious', 'offensive', 'old', 'oppressive', 'pain', 'perturb', 'pessimistic', 'petty', 'plain', 'poisonous', 'poor', 'prejudice', 'questionable', 'quirky', 'quit', 'reject', 'renege', 'repellant', 'reptilian', 'repugnant', 'repulsive', 'revenge', 'revolting', 'rocky', 'rotten', 'rude', 'ruthless', 'sad', 'savage', 'scare', 'scary', 'scream', 'severe', 'shocking', 'shoddy', 'sick', 'sickening', 'sinister', 'slimy', 'smelly', 'sobbing', 'sorry', 'spiteful', 'sticky', 'stinky', 'stormy', 'stressful', 'stuck', 'stupid', 'substandard', 'suspect', 'suspicious', 'tense', 'terrible', 'terrifying', 'threatening', 'ugly', 'undermine', 'unfair', 'unfavorable', 'unhappy', 'unhealthy', 'unjust', 'unlucky', 'unpleasant', 'unsatisfactory', 'unsightly', 'untoward', 'unwanted', 'unwelcome', 'unwholesome', 'unwieldy', 'unwise', 'upset', 'vice', 'vicious', 'vile', 'villainous', 'vindictive', 'wary', 'weary', 'wicked', 'woeful', 'worthless', 'wound', 'yell', 'yucky', 'zero',"abisal","advers","prost","revoltator","ciudat","jignitor","vechi","urat","lipsa","imperfect","slab","defectuos","esueaza","rau","lipsit"]


app = FlaskAPI(__name__)
CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'
sql_connection_string =""""Driver={ODBC Driver 13 for SQL Server};"
                      "Server=tcp:smarthack2020server.database.windows.net,1433;"
                      "Database=Smarthack2020SearchDB;"
                      "Uid=beercent;Pwd={Password01!};"
                      "Encrypt=yes;"
                       "TrustServerCertificate=no;"
                        "Connection Timeout=30;"
                        """


query_one  = """USE [Smarthack2020SearchDB]

INSERT INTO [dbo].[review_list]
           ([product_name]
           ,[review_list]
           ,[link_provider]
           ,[category]
           ,[device])
"""

query_two = """
SELECT [review_list]
  FROM [dbo].[review_list]
  WHERE 
"""
#conn = pyodbc.connect(sql_connection_string)
def Sort(sub_li):
    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of
    # sublist lambda has been used
    sub_li.sort(key=lambda x: x[1],reverse=True)
    return sub_li

key_words = {'ieftin':['cheap','affordable','bargain','steal','low-cost','economical','resonable'],'profesional':['skillful','competent','efficient','experienced','licensed','qualified','expert','bun','best'],'munca':['office','job','work','station','service','duty','performant'],'joc':['gaming','fun','pro']}

def get_data_search(query):
    conn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + Pwd + ";Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
    cursor = conn.cursor()
    dev = None
    query = query.lower()
    output,links =  phones.search_string_top(query)
    print(len(output))
    print(len(links))
    for (x,y),link in zip(output.items(),links):
        cur = conn.cursor()
        product= x
        url = link
        categ = "top"
        for s in category:
            if s in query:
                dev = s
        if dev is None:
            dev = "other"
        for rev in  y:
            review = rev.replace("'","")
            adding_string =query_one +  "VALUES ""('" + product +"', '"+  review+"','"+url+"','"+categ+"','"+dev+"');"+ "\n"
            print(adding_string)
            cur.execute(adding_string)
            cur.commit()
        cur.close()
    return "done"


@app.route("/top/<query>", methods=['POST'])
def src(query):
    if request.method == 'POST':
        json = request.get_json()
        query = json['query']
        conn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + Pwd + ";Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
        cursor = conn.cursor()
        dev = None
        query = query.lower()
        output,links =  phones.search_string_top(query)
        print(len(output))
        print(len(links))
        for (x,y),link in zip(output.items(),links):
            cur = conn.cursor()
            product= x
            url = link
            categ = "top"
            for s in category:
                if s in query:
                    dev = s
            if dev is None:
                dev = "other"
            for rev in  y:
                review = rev.replace("'","")
                adding_string =query_one +  "VALUES ""('" + product +"', '"+  review+"','"+url+"','"+categ+"','"+dev+"');"+ "\n"
                print(adding_string)
                cur.execute(adding_string)
                cur.commit()
            cur.close()
        return "done"

@app.route("/techradar", methods=['GET'])
def techradar():
    """
    List or create notes.
    """
    # if request.method == 'POST':
    #     print(query)
    #     note = str(request.data.get('text', ''))
    #     print(note)
    #
    #     output = phones.search_string_top("phone")
    #     print(output)
    if request.method == 'GET':
        print('started techradar')
        conn = pyodbc.connect(
            'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + Pwd + ";Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
        cursor = conn.cursor()
        dev = None
        output, links = tech.tech_news_best_phones()
        print(len(output))
        print(len(links))
        for (x, y), link in zip(output.items(), links):
            cur = conn.cursor()
            product = x
            url = link
            categ = "top-prod"
            dev = "smartphone"
            if dev is None:
                dev = "other"
            for rev in y:
                review = rev.replace("'", "")
                adding_string = query_one + "VALUES ""('" + str(product) + "', '" + str(review) + "','" + str(url) + "','" + str(categ) + "','" + str(dev) + "');" + "\n"
                print(adding_string)
                cur.execute(adding_string)
                cur.commit()
            cur.close()
        return "done"

    #return [note_repr(idx) for idx in sorted(notes.keys())]
@app.route("/find/", methods=['POST'])
@cross_origin()
def find():
    """
    List or create notes.
    """
    # if request.method == 'POST':
    #     print(query)
    #     note = str(request.data.get('text', ''))
    #     print(note)
    #
    #     output = phones.search_string_top("phone")
    #     print(output)

    if request.method == 'POST':
        out = request.get_json()
        first_key = out['first_key']
        type = out['type']
        temp = type
        if type.lower() == "iphone":
            type="Apple"
        key_word = out['key_word']
        if len(key_word.split(" ")) == 1:
            print('started search in db')
            #search = search.split(" ")
            conn = pyodbc.connect(
                'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + Pwd + ";Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
            cursor = conn.cursor()
            query_string = query_two + " [dbo].[review_list].[device] = '" + first_key.lower() + "' AND [dbo].[review_list].[product_name] = '" + type.title()+"' ;"
            print(query_string)
            cur = conn.cursor()
            cur.execute(query_string)
            records = cur.fetchall()

            review_list = []
            for row in records:
                row = row[0]
                if key_word in row or key_word in row.lower():
                    review_list.append(row)
                if key_word in key_words.keys():
                    for x in key_words[key_word]:
                        if x in row:
                            review_list.append(row)
                else:
                    for x in key_words.values():
                        if key_word in x:
                            for y in x:
                                if y in row:
                                    review_list.append(row)

            if len(review_list)  == 0:
                get_data_search(first_key + " " + type + " " + "review")
                get_data_search(first_key + " " + type + " " + key_word )
                get_data_search(first_key + " " + type + " " + key_word+ "review")
                cur.execute(query_string)
                records = cur.fetchall()
                for row in records:
                    row = row[0]
                    if key_word in row or key_word in row.lower():
                        review_list.append(row)
        if len(key_word.split(" ")) > 1:
            print('started search in db')
            # search = search.split(" ")
            key_word = key_word.split(" ")
            conn = pyodbc.connect(
                'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + Pwd + ";Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
            cursor = conn.cursor()
            query_string = query_two + " [dbo].[review_list].[device] = '" + first_key.lower() + "' AND [dbo].[review_list].[product_name] = '" + type.title() + "' ;"
            print(query_string)
            cur = conn.cursor()
            cur.execute(query_string)
            records = cur.fetchall()

            review_list = []
            for row in records:
                row = row[0]
                for key in key_word:
                    if key in row or key in row.lower():
                        review_list.append(row)
                    if key in key_words.keys():
                        for x in key_words[key]:
                            if x in row:
                                review_list.append(row)
                else:
                    for x in key_words.values():
                        for key in key_word:
                            if key in x:
                                for y in x:
                                    if y in row:
                                        review_list.append(row)
            if len(review_list) == 0:
                if type(key_word) == "string":
                    get_data_search(first_key + " " + type + " " + "review")
                    get_data_search(first_key + " " + type + " " + key_word)
                    get_data_search(first_key + " " + type + " " + key_word + "review")
                    cur.execute(query_string)
                    records = cur.fetchall()
                    for row in records:
                        row = row[0]
                        if key_word in row or key_word in row.lower():
                            review_list.append(row)
                else:
                    for x in key_word:
                        get_data_search(first_key + " " + type + " " + "review")
                        get_data_search(first_key + " " + type + " " + x)
                        get_data_search(first_key + " " + type + " " + x + "review")
                        cur.execute(query_string)
                        records = cur.fetchall()
                        for row in records:
                            row = row[0]
                            if x in row or x in row.lower():
                                review_list.append(row)
        review_list= set(review_list)
        key_word = ' '.join(key_word)
        print(key_word)
        #print(review_list)
        print(type)
        positivity = 0
        negative = 0
        text_perf = []
        review = []
        if type == "Apple":
            type = "iphone"
        #analyser = SentimentIntensityAnalyzer()
        for x in review_list:
            iphone = None
            phone = None
            if len(x) >50:
                lista = x.lower().split(" ")
                lower = x.lower()
                if type.lower() in lower:
                    phone = lower[lower.find(type.lower()):lower.find(type.lower()) + 15]
                else:
                    if "iphone" in lower:
                        iphone = lower[lower.find("iphone"):lower.find("iphone") + 5]
                        phone = None
                    if "samsung galaxy" in lower:
                        iphone = None
                    phone = lower[lower.find("samsung galaxy"):lower.find("samsung galaxy")+22]
                for pos in positive_wrds:
                    pos = pos.lower()
                    positivity += lista.count(pos)
                for neg in negative_wrds:
                    neg = neg.lower()
                    negative = lista.count(neg)
                if iphone is None:
                    text_perf.append([phone,positivity-negative])
                    review.append(x)
                if phone is None:
                    text_perf.append([iphone,positivity-negative])
                    review.append(x)
                elif iphone is None and phone is None:
                    pass
        text_perf = Sort(text_perf)
        print(text_perf)
            # if type.lower() + " " + key_word.lower() in x.lower():
            #     print(x[x.find(type.title()+" "+key_word):x.find(type.title()+" "+key_word)])
            #     smh = x[x.find(type.title()+" "+key_word):x.find( type.title()+" "+key_word)]
        max = text_perf[0][1]
        if max == 0 or max is None:
            max = 1
        for i in range(0,len(text_perf)):
            text_perf[i][1] = text_perf[i][1] / max
            text_perf[i][1]*=10
        rev_dict = {}
        for x in text_perf:
            if x[0] in rev_dict:
                rev_dict[x[0]].append(x[1])
            else:
                rev_dict[x[0]] = [x[1]]

        for item1,item2 in rev_dict.items():
            if len(item2) !=1:
                rev_dict[item1] = sum(item2) / len(item2)
            else:
                rev_dict[item1] = item2[0]
        y = json.dumps(rev_dict)
        cur.close()
        return y
@app.route("/")
@cross_origin()
def helloWorld():
  return "Hello, cross-origin-world!"

if __name__ == "__main__":
    #application()
    app.run(debug=True)