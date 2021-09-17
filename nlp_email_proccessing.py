import imaplib
import email
from email.header import decode_header
import os
import re
import nltk
from nltk.corpus import stopwords
from nltk.data import find
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
import smtplib, ssl
from geotext import GeoText
from nltk.util import pr
from uszipcode import SearchEngine
import  pandas
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sqlite3


s=""
sfrom=""
mail_body=""""""
receiver_email =""

email_status=0

pri=""

to_address=""
from_address=""

datee=""



username = "ntr4d6@gmail.com"
password = "Ntr91337"



code=0

p=[]
a=[]
mail_data=""


def clean(text):
  
    return "".join(c if c.isalnum() else "_" for c in text)



imap = imaplib.IMAP4_SSL("imap.gmail.com")

imap.login(username, password)


status, messages = imap.select("INBOX",readonly=False)

N = 1

messages = int(messages[0])

try:

    for i in range(messages, messages-N, -1):
        variable_for_i=i


        try:
            
            res, msg = imap.fetch(str(i), "(RFC822)")
            for response in msg:
                if isinstance(response, tuple):
                    
                    msg = email.message_from_bytes(response[1])
                    
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                       
                        subject = subject.decode(encoding)
              

                    From, encoding = decode_header(msg.get("From"))[0]
                    if isinstance(From, bytes):
                        From = From.decode(encoding)
                    print("Subject:", subject)
                    datee=decode_header(msg["Date"])[0][0]
                    print(datee)


                    print("""\n\n\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n\n""")
                    s+=subject

                    sfrom+=From

                    receiver_email =sfrom[sfrom.find("<")+1:sfrom.find(">")]
                   
                    if msg.is_multipart():
                       
                        for part in msg.walk():
                            
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))
                            try:


                                body = part.get_payload(decode=True).decode()
                            except:
                                pass
                            if content_type == "text/plain" and "attachment" not in content_disposition:
                               
                                print(body)
                                print("""\n\n\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n\n""")
                                mail_body+=body
                            elif "attachment" in content_disposition:
                         
                                filename = part.get_filename()
                                if filename:
                                    folder_name = clean(subject)
                                    if not os.path.isdir(folder_name):
                                       
                                        os.mkdir(folder_name)
                                    filepath = os.path.join(folder_name, filename)
                                   
                                    open(filepath, "wb").write(part.get_payload(decode=True))
                    else:
                      
                        content_type = msg.get_content_type()
                        
                        body = msg.get_payload(decode=True).decode()
                        if content_type == "text/plain":
                            
                            print(body)
                            print("""\n\n\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n\n""")
        

            """________________________________________________________________________________________________________________________
            __________________________________________________________________________________________________________________________"""




            cities=["coloumbus","savannah","williston","minneapolis","frazee","kansas","sedalia","quincy","lincoln","fowlerville","columbus","brookeville","detroit","flint","holly","cuyahoga","omaha"]
            pincodes=["29853","65301","62305","68524","48836","43217","45309","48507","48442"]


            """_______________________________________________________________________________________________________________________
            ___________________________________________________________________________________________________________________________"""



            subject_string=string = s.replace('\r', '').replace('\n', ' ')
            print(subject_string)

            print("""\n\n\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n\n""")



            """_______________________________________________________________________________________________________________________
            ___________________________________________________________________________________________________________________________"""




            resu = re.findall(r'\w+', subject_string)



            new1=""""""
            for i in resu:
                new1+=i+" "

            print(new1)
            print("""\n\n\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n\n""")




            """_______________________________________________________________________________________________________________________
            ___________________________________________________________________________________________________________________________"""


            stop_words = stopwords.words('english')


            stop_words.append("hello")




            stop_words = set(stopwords.words('english')) - set(['again', 'once',"from","to","40,000-42,000"])

            wordlemmator=WordNetLemmatizer()

            texts=new1.lower()

            x={"requried","much","Hello","hello","HELLO","hi","HI","Hi"}

  
            tokenized_words=(word_tokenize(texts))
           

            filtered_tokenized_words=[]
            for i in tokenized_words:
                if i.isalnum():
                    filtered_tokenized_words.append(i)    
       
       
            stopwords_filtered_tokenized_words=[]
            for word in filtered_tokenized_words:
                if not word in stop_words :
                    if not word in x:
                        stopwords_filtered_tokenized_words.append(word)

            print(stopwords_filtered_tokenized_words)
       

            wordss=[]
            for i in stopwords_filtered_tokenized_words:
                wordss.append((wordlemmator.lemmatize(i,pos="v")))
            print(wordss)

            print("""\n\n\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n\n""")




            """_______________________________________________________________________________________________________________________
            ___________________________________________________________________________________________________________________________"""






            """-------------------------------------------------------------------------------------------------------------------
            _____________________________________________________________________________________________________________________
                                                                
                                                                MAIL BODY
            ______________________________________________________________________________________________________________________

            ----------------------------------------------------------------------------------------------------------------------"""






            my_string=string = mail_body.replace('\r', '').replace('\n', ' ')
            print(my_string)

            print("""\n\n\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n\n""")




            """_______________________________________________________________________________________________________________________
            ___________________________________________________________________________________________________________________________"""




            res = re.findall(r'\w+', my_string)


            new=""""""
            for i in res:
                new+=i+" "

            print(new)
            print("""\n\n\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n\n""")




            """_______________________________________________________________________________________________________________________
            ___________________________________________________________________________________________________________________________"""






            text=new.lower()

            x={"requried","much","Hello","hello","HELLO","hi","HI","Hi"}

            #word tokenization
            tokenized_word=(word_tokenize(text))

            #filtering the input with puntuations
            filtered_tokenized_word=[]
            for i in tokenized_word:
                if i.isalnum():
                    filtered_tokenized_word.append(i)    
                    
            #removing the stop words
            stopwords_filtered_tokenized_word=[]
            for word in filtered_tokenized_word:
                if not word in stop_words :
                    if not word in x:
                        stopwords_filtered_tokenized_word.append(word)

            print(stopwords_filtered_tokenized_word)
            print("""these are the stop words""")
       





            """_____________________________________________________________________________________________________________________"""

            w=[]

            words=[]
            for i in stopwords_filtered_tokenized_word:
                # w.append((wordlemmator.lemmatize(i,pos="v")))
                w.append(i)

            indi=0

            for i in range(len(w)):
                if w[i]=="thank" or w[i]=="thanks" or w[i]=="regards":
                    indi+=i
                    words=w[:indi]
                    break
            

            
                    

            print(words)

            print("""\n\n\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n\n""")




            """_______________________________________________________________________________________________________________________
            ___________________________________________________________________________________________________________________________"""





            check=[]

            for i in range(len(wordss)):
                if wordss[i] in cities:
                    check.append(wordss[i])

            if len(check)==2:
                print("ok this is in the subject")

                if ("from" in wordss ) and ("to" in wordss ) :
                    index_from=wordss.index("from")
                    index_for_to=wordss.index("to")

                    if index_from > index_for_to:
                        lis_for_from=wordss[index_from:]
                        lis_for_to=wordss[index_for_to:index_from]

                        for i in range(len(lis_for_from)):
                            if lis_for_from[i] in pincodes:
                                p.append(lis_for_from[i])

                            if lis_for_from[i] in cities:
                                a.append(lis_for_from[i])

                        for i in range(len(lis_for_to)):
                            if lis_for_to[i] in pincodes:
                                if len(p)==1:
                                    p.append(lis_for_to[i])
                                if len(p)==0:
                                    p.append("")
                                    p.append(lis_for_to[i])
                            if lis_for_to[i] in cities:
                                if len(a)==1:
                                    a.append(lis_for_to[i])
                                if len(a)==0:
                                    a.append("")
                                    a.append(lis_for_to[i])
                            
                    print(a)
                    print(p)



                    if ("from" in wordss ) and ("to" in wordss ) :
                        index_from=wordss.index("from")
                        index_for_to=wordss.index("to")

                        if index_from < index_for_to:
                            lis_for_from=wordss[index_from:index_for_to]
                            lis_for_to=wordss[index_for_to:]

                            for i in range(len(lis_for_from)):
                                if lis_for_from[i] in pincodes:
                                    p.append(lis_for_from[i])

                                if lis_for_from[i] in cities:
                                    a.append(lis_for_from[i])

                            for i in range(len(lis_for_to)):
                                if lis_for_to[i] in pincodes:
                                    if len(p)==1:
                                        p.append(lis_for_to[i])
                                    if len(p)==0:
                                        p.append("")
                                        p.append(lis_for_to[i])
                                if lis_for_to[i] in cities:
                                    if len(a)==1:
                                        a.append(lis_for_to[i])
                                    if len(a)==0:
                                        a.append("")
                                        a.append(lis_for_to[i])

                        print(a)
                        print(p)


                    """___________________________________________________________________________________________________________________________________________________________________________________"""


                elif "to" in wordss:
                    index_to=wordss.index("to")
                    print("this is for the word in case to subject")
                    list_upto_to=wordss[:index_to]
                    rlist_upto_to=list_upto_to[::-1]

                    list_after_to=wordss[index_to:]

                    for i in range(len(rlist_upto_to)):
                        if rlist_upto_to[i] in pincodes:
                            p.append(rlist_upto_to[i])
                        if rlist_upto_to[i] in cities:
                            a.append(rlist_upto_to[i])

                    for i in range(len(list_after_to)):
                        if list_after_to[i] in pincodes:
                            if len(p)==1:
                                p.append(list_after_to[i])
                            if len(p)==0:
                                p.append("")
                                p.append(list_after_to[i])

                        if list_after_to[i] in cities:
                            if len(a)==1:
                                a.append(list_after_to[i])
                            if len(a)==0:
                                a.append("")
                                a.append(list_after_to[i])

                else:
                    pi=[]
                    ad=[]

                    indexes_of_from_and_to=[]

                    for i in range(len(wordss)):
                        if wordss[i] in cities:
                            ad.append(wordss[i])
                            indexes_of_from_and_to.append(wordss.index(wordss[i]))

                    from_pin=wordss[:indexes_of_from_and_to[1]]
                    to_pin=wordss[indexes_of_from_and_to[1]:]

                    for i in range(len(from_pin)):
                        if from_pin[i] in pincodes:
                            pi.append(from_pin[i])
                    for i in range(len(to_pin)):
                        if to_pin[i] in pincodes:
                            if len(pi)==1:
                                pi.append(to_pin[i])
                            if len(pi)==0:
                                pi.append("")
                                pi.append(to_pin[i])


                    p=pi
                    a=ad
                if len(a)==2:
                    pass
                if len(a)==0 or len(a)==1:
                    p=[]
                    a=[]

                
            print(a)
            print(p)

            if len(a)==0:
                if len(words)!=0:
                    print("ok this is in the body of the mail")

                if ("from" in words ) and ("to" in words) :
                    index_from=words.index("from")
                    index_for_to=words.index("to")

                    if index_from > index_for_to:
                        lis_for_from=words[index_from:]
                        lis_for_to=words[index_for_to:index_from]

                        for i in range(len(lis_for_from)):
                            if lis_for_from[i] in pincodes:
                                p.append(lis_for_from[i])

                            if lis_for_from[i] in cities:
                                a.append(lis_for_from[i])

                        for i in range(len(lis_for_to)):
                            if lis_for_to[i] in pincodes:
                                if len(p)==1:
                                    p.append(lis_for_to[i])
                                if len(p)==0:
                                    p.append("")
                                    p.append(lis_for_to[i])
                            if lis_for_to[i] in cities:
                                if len(a)==1:
                                    a.append(lis_for_to[i])
                                if len(a)==0:
                                    a.append("")
                                    a.append(lis_for_to[i])
                            
                    print(a)
                    print(p)



                    if ("from" in words ) and ("to" in words ) :
                        index_from=words.index("from")
                        index_for_to=words.index("to")

                        if index_from < index_for_to:
                            lis_for_from=words[index_from:index_for_to]
                            lis_for_to=words[index_for_to:]

                            for i in range(len(lis_for_from)):
                                if lis_for_from[i] in pincodes:
                                    p.append(lis_for_from[i])

                                if lis_for_from[i] in cities:
                                    a.append(lis_for_from[i])

                            for i in range(len(lis_for_to)):
                                if lis_for_to[i] in pincodes:
                                    if len(p)==1:
                                        p.append(lis_for_to[i])
                                    if len(p)==0:
                                        p.append("")
                                        p.append(lis_for_to[i])
                                if lis_for_to[i] in cities:
                                    if len(a)==1:
                                        a.append(lis_for_to[i])
                                    if len(a)==0:
                                        a.append("")
                                        a.append(lis_for_to[i])

                        print(a)
                        print(p)


                    """___________________________________________________________________________________________________________________________________________________________________________________"""


                elif "to" in words:
                
                    index_to=words.index("to")
                    print("this is for the word in case to")
                    list_upto_to=words[:index_to]
                    rlist_upto_to=list_upto_to[::-1]

                    list_after_to=words[index_to:]

                    fla=0
                    
                    for i in range(len(list_after_to)):
                        if list_after_to[i] in cities:
                            fla+=1
                            break
                        
                    if fla==1:

                        for i in range(len(rlist_upto_to)):
                            if rlist_upto_to[i] in pincodes:
                                p.append(rlist_upto_to[i])
                            if rlist_upto_to[i] in cities:
                                a.append(rlist_upto_to[i])

                        for i in range(len(list_after_to)):
                            if list_after_to[i] in pincodes:
                                if len(p)==1:
                                    p.append(list_after_to[i])
                                if len(p)==0:
                                    p.append("")
                                    p.append(list_after_to[i])

                            if list_after_to[i] in cities:
                                if len(a)==1:
                                    a.append(list_after_to[i])
                                if len(a)==0:
                                    a.append("")
                                    a.append(list_after_to[i])
                    else:
                        pi=[]
                        ad=[]

                        indexes_of_from_and_to=[]

                        for i in range(len(words)):
                            if words[i] in cities:
                                ad.append(words[i])
                                indexes_of_from_and_to.append(words.index(words[i]))
                                print(indexes_of_from_and_to)

                        from_pin=wordss[:indexes_of_from_and_to[1]]
                        to_pin=words[indexes_of_from_and_to[1]:]

                        for i in range(len(from_pin)):
                            if from_pin[i] in pincodes:
                                pi.append(from_pin[i])
                        for i in range(len(to_pin)):
                            if to_pin[i] in pincodes:
                                if len(pi)==1:
                                    pi.append(to_pin[i])
                                if len(pi)==0:
                                    pi.append("")
                                    pi.append(to_pin[i])


                        p=pi
                        a=ad
                    if len(a)==2:
                        pass
                    if len(a)==0 or len(a)==1:
                        p=[]
                        a=[]
                        

                else:
                    pi=[]
                    ad=[]
                    print(words)
                    print(words)
                    indexes_of_from_and_to=[]

                    for i in range(len(words)):
                        if words[i] in cities:
                            ad.append(words[i])
                            indexes_of_from_and_to.append(words.index(words[i]))
                    

                    from_pin=words[:indexes_of_from_and_to[1]]
                    to_pin=words[indexes_of_from_and_to[1]:]

                    for i in range(len(from_pin)):
                        if from_pin[i] in pincodes:
                            pi.append(from_pin[i])
                    for i in range(len(to_pin)):
                        if to_pin[i] in pincodes:
                            if len(pi)==1:
                                pi.append(to_pin[i])
                            if len(pi)==0:
                                pi.append("")
                                pi.append(to_pin[i])


                    p=pi
                    a=ad
                if len(a)==2:
                    pass
                if len(a)==0 or len(a)==1:
                    p=[]
                    a=[]

                
            print(a)
            print(p)


            print("""++++++++++++++++++++++++++++++++++++++++++ Final values ++++++++++++++++++++++++++++++++++++""")

            print(a)
            print(p)
            if len(a)==0:
                raise TypeError()

        except:
            imap.store(str(variable_for_i), '-FLAGS', '\Seen')
            code=1

            dae=datee[6:17]
            print(dae)
            print(code)
            admin_mail="thrinath.narahari@gmail.com"

        
            dollar="The Email From "+receiver_email+" is not answerable marking the email from "+receiver_email+" as UNREAD  ENGINE FAILURE"
            port = 587  
            smtp_server = "smtp.gmail.com"
            username = "ntr4d6@gmail.com"


            txt=""+dollar
            

            message = """Subject: {}\n\n{}""".format(s, txt)


            context = ssl.create_default_context()
            with smtplib.SMTP(smtp_server, port) as server:
                server.ehlo()  
                server.starttls(context=context)
                server.ehlo()  
                server.login(username, password)
                server.sendmail(username, admin_mail, message)
            
            email_status=1


            

            con = sqlite3.connect('db.sqlite3')

            cursorObj = con.cursor()

            


            dae=datee[5:16]
            print(dae)
            print(len(dae))


            m=""
            y=dae[7:]
            d=dae[:2]


            if dae[3:6]=="Sep":
                m="09"
                print("kkk")

            t=y+"-"+m+"-"+d
            print(t)

            from_=receiver_email
            to_=username
            subject_=s
            date_=t
            body_=body
            status_="0"
            result_="ENGINE FAIL"
            res_body_=dollar
            if len(s)==0:
                subject_="--NONE--"




            



            dat="1999-10-09"
            data = [(from_,to_,subject_,date_,status_,result_,res_body_)]

            cursorObj.executemany("INSERT INTO aoo1_page(From_Address_t, To_Address_t,Subject_t,date_of_email_t,status_t,result_t,response_Body_t) VALUES(?,?,?,?,?,?,?)", data)

            con.commit()


                

        
        if code!=1:

            try:


                def city_zip(value):
                    engine = SearchEngine()
                    zipcodes = engine.by_city(city=value,returns=1000)

                    us_zip_codes=[]
                    for zipcode in zipcodes:
                        us_zip_codes.append(zipcode.zipcode)
                    print(us_zip_codes)
                    return us_zip_codes[0]
                
                if len(p)==0:
                    add_1=a[0]
                    add_2=a[1]
                    p.append(city_zip(add_1))
                    p.append(city_zip(add_2))


                if len (p)==1:
                    add_1=a[1]
                    p.append(city_zip(add_1))


                if len (p)==2:
                    if len(p[0])==0:
                        add_1=a[0]
                        p[0]=city_zip(add_1)
                    
                print(a)
                print(p)



                zip_tuple=(int(p[0]),int(p[1]))

                data=pandas.read_excel("Final_CHKD_RateBook_Columbus_2021-7-20.xlsx")

                
                zip_dict={(int(data_row["STARTING ZIP"]),int(data_row["ZIP"])):data_row for (index,data_row) in data.iterrows()}

                for i in range(len(zip_dict)):
                    if zip_tuple in zip_dict:
                        price=zip_dict[zip_tuple]
                            # p+="$"+str(price["01-08-2021"])
                        pri+=str(round(price["PRICE"]))
                        to_address=str(price["DESTINATION CITY"])
                        from_address=str(price["STARTING CITY"])

                        break
                    else:raise Exception()
                print(pri)

                

            except:
                imap.store(str(variable_for_i), '-FLAGS', '\Seen')
                
                code=2

                dae=datee[6:17]
                print(dae)
                print(code)


                dae=datee[6:17]
                print(dae)
                print(code)
                admin_mail="thrinath.narahari@gmail.com"

            
                dollar="The Email From "+receiver_email+" is not answerable marking the email from "+receiver_email+" as UNREAD Data Error"
                port = 587  
                smtp_server = "smtp.gmail.com"
                username = "ntr4d6@gmail.com"
                

                txt=""+dollar
                message = """Subject: {}\n\n{}""".format(s, txt)



                context = ssl.create_default_context()
                with smtplib.SMTP(smtp_server, port) as server:
                    server.ehlo()  
                    server.starttls(context=context)
                    server.ehlo()  
                    server.login(username, password)
                    server.sendmail(username, admin_mail, message)
                email_status=2

                con = sqlite3.connect('db.sqlite3')

                cursorObj = con.cursor()

                

        

                dae=datee[5:16]
                print(dae)
                print(len(dae))


                m=""
                y=dae[7:]
                d=dae[:2]


                if dae[3:6]=="Sep":
                    m="09"
                    print("kkk")

                t=y+"-"+m+"-"+d
                print(t)

                from_=receiver_email
                to_=username
                subject_=s
                date_=t
                body_=body
                status_="0"
                result_="DATA NOT FOUND"
                res_body_=dollar

                if len(s)==0:
                    subject_="--NONE--"




                



                dat="1999-10-09"
                data = [(from_,to_,subject_,date_,status_,result_,res_body_)]

                cursorObj.executemany("INSERT INTO aoo1_page(From_Address_t, To_Address_t,Subject_t,date_of_email_t,status_t,result_t,response_Body_t) VALUES(?,?,?,?,?,?,?)", data)

                con.commit()
        





    print(code)



    if code==0:

        mail_data=(str(from_address)+"   "+"  to  "+"   "+str(to_address)+"  "+"$"+str(pri)+" "+"  "+"35% "+"+ FST")
        dollar=mail_data
        port = 587  
        smtp_server = "smtp.gmail.com"
        username = "ntr4d6@gmail.com"
        

        message = """Subject: {}\n\n
        Thanks for reaching out.  Calhoun Truck Lines appreciates your business.



        Your rate is listed below, after you have had a chance to review 
        please let us know how we can further assist or feel free to send your DO to columbus@calhountrucklines.com for scheduling and confirmation.


        

        Please see our rate below  :{}

        $75      Chassis Split/Positioning

        $35     Chassis rental/day OR $150 Tri-axle charge for 20 s over 38,500lbs.

        $50     Overweight

        $80     per hour after 1 free hour

        $150    Pre-Pull/Rail-Depot Return Delay

        $50/day storage for CSX and Norfolk Southern

        Max weight is 44,000#

        $350 for 45 day Overweight Permit  Exports only

        Max OW 57,000# for 20 & 40 containers  Exports Only

        ***Please note this quote is valid for 30 days for accessorial and dray rates and must be included in the DO/WO, or a copy of the email quote must be attached.  FSC is subject to change bi-weekly in accordance with the Midwest average for diesel""".format(s, dollar)
        

        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  
            server.starttls(context=context)
            server.ehlo()  
            server.login(username, password)
            server.sendmail(username, receiver_email, message)




            con = sqlite3.connect('db.sqlite3')

            cursorObj = con.cursor()

            

            

            dae=datee[5:16]
            print(dae)
            print(len(dae))


            m=""
            y=dae[7:]
            d=dae[:2]


            if dae[3:6]=="Sep":
                m="09"
                print("kkk")

            t=y+"-"+m+"-"+d
            print(t)

            from_=receiver_email
            to_=username
            subject_=s
            date_=t
            body_=body
            status_="1"
            result_="SUCESS"
            res_body_=dollar

            if len(s)==0:
                subject_="--NONE--"




            



            dat="1999-10-09"
            data = [(from_,to_,subject_,date_,status_,result_,res_body_)]

            cursorObj.executemany("INSERT INTO aoo1_page(From_Address_t, To_Address_t,Subject_t,date_of_email_t,status_t,result_t,response_Body_t) VALUES(?,?,?,?,?,?,?)", data)

            con.commit()



    print(code)
    imap.close()
    imap.logout()



finally:
    if email_status ==0:


        dollar="DATA INSUFFICIENT"
        port = 587  
        smtp_server = "smtp.gmail.com"
        username = "ntr4d6@gmail.com"
        receiver_email =sfrom[sfrom.find("<")+1:sfrom.find(">")]

        txt="""
        Thanks for reaching out.  Calhoun Truck Lines appreciates your business.



        Your rate is listed below, after you have had a chance to review 
        please let us know how we can further assist or feel free to send your DO to columbus@calhountrucklines.com for scheduling and confirmation.


        

        Please see our rate below  :



        {}



        $75      Chassis Split/Positioning

        $35     Chassis rental/day OR $150 Tri-axle charge for 20 s over 38,500lbs.

        $50     Overweight

        $80     per hour after 1 free hour

        $150    Pre-Pull/Rail-Depot Return Delay

        $50/day storage for CSX and Norfolk Southern

        Max weight is 44,000#

        $350 for 45 day Overweight Permit  Exports only

        Max OW 57,000# for 20 & 40 containers  Exports Only

        ***Please note this quote is valid for 30 days for accessorial and dray rates and must be included in the DO/WO, or a copy of the email quote must be attached.  FSC is subject to change bi-weekly in accordance with the Midwest average for diesel***
        """.format(dollar)


        message = """Subject: {}\n\n{}""".format(s, txt)

        


        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  
            server.starttls(context=context)
            server.ehlo()  
            server.login(username, password)
            server.sendmail(username, "thrinath.narahari@gmail.com", message)


        con = sqlite3.connect('db.sqlite3')

        cursorObj = con.cursor()

        

        

        dae=datee[5:16]
        print(dae)
        print(len(dae))


        m=""
        y=dae[7:]
        d=dae[:2]


        if dae[3:6]=="Sep":
            m="09"
            print("kkk")

        t=y+"-"+m+"-"+d
        print(t)

        from_=receiver_email
        to_=username
        subject_=s
        date_=t
        body_=body
        status_="1"
        result_="SUCESS"
        res_body_=dollar

        if len(s)==0:
            subject_="--NONE--"


        dat="1999-10-09"
        data = [(from_,to_,subject_,date_,status_,result_,res_body_)]

        cursorObj.executemany("INSERT INTO aoo1_page(From_Address_t, To_Address_t,Subject_t,date_of_email_t,status_t,result_t,response_Body_t) VALUES(?,?,?,?,?,?,?)", data)

        con.commit()

    