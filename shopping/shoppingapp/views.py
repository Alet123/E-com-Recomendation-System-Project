from re import sub
import re
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
import json
import MySQLdb

db=MySQLdb.connect("localhost","root","","dbshopping")
c=db.cursor()

######################################################################
#                                                                    #
#                                                                    #
#                           COMMON                                   #
#                                                                    #
#                                                                    #
######################################################################
######################################################################
#                           LOAD INDEX PAGE
######################################################################
def index(request):
    return render(request,"index.html")
######################################################################
#                           LOAD LOGIN PAGE
######################################################################
def login(request):
    msg=""
    if(request.POST):
        email=request.POST.get("txtEmail")
        pwd=request.POST.get("txtPassword")
        s="select count(*) from tbllogin where uname='"+email+"'"
        c.execute(s)
        i=c.fetchone()
        if(i[0]>0):
            s="select * from tbllogin where uname='"+email+"'"
            c.execute(s)
            i=c.fetchone()
            if(i[1]==pwd):
                request.session['email'] = email
                if(i[3]=="1"):
                    if(i[2]=="admin"):
                        return HttpResponseRedirect("/adminhome")
                    elif(i[2]=="customer"):
                        s="select * from tblregistration where email='"+email+"'"
                        c.execute(s)
                        d=c.fetchone()
                        request.session['id']=d[0]
                        return HttpResponseRedirect("/customerhome")
                    
                elif(i[3]=="inactive"):
                    msg="Your registration is incomplete. Please register"
                else:
                    msg="You are not authenticated to login"
            else:
                msg="Incorrect password"
        else:
            msg="User doesnt exist"
    return render(request,"commonlogin.html",{"msg":msg})
######################################################################
#                   LOAD  REGISTRATION PAGE
######################################################################
def registration(request):
    msg=""
    if(request.POST):
        name=request.POST['txtName']
        email=request.POST['txtEmail']
        contact=request.POST['txtContact']
        pwd=request.POST['txtPassword']        
        s="insert into tblregistration (name,contact,email) values('"+name+"','"+contact+"','"+email+"')"
        print(s)
        try:
            c.execute(s)
        except:
            msg="Sorry registration error"
        else:
            s="insert into tbllogin (uname,pwd,utype,status) values('"+email+"','"+pwd+"','customer','1')"
            try:
                c.execute(s)
                db.commit()
            except:
                msg="Sorry some error occured"
            else:
                msg="Registration successfull."
    return render(request,"commonregister.html",{"msg":msg})

######################################################################
#                                                                    #
#                                                                    #
#                           ADMIN                                    #
#                                                                    #
#                                                                    #
######################################################################
######################################################################
#                           LOAD INDEX PAGE
######################################################################
def adminhome(request):
    return render(request,"adminhome.html")
######################################################################
#                      LOAD CATEGORY PAGE
######################################################################
def admincategory(request):
    msg=""
    if(request.POST):
        name=request.POST['txtCategory']
        s="insert into tblcategory (category) values('"+name+"')"
        try:
            c.execute(s)
            db.commit()
        except:
            msg="Sorry some error occured"
        else:
            msg="Category added"
    s="select * from tblcategory"
    c.execute(s)
    data=c.fetchall()
    return render(request,"admincategory.html",{"msg":msg,"data":data})
def updatecategory(request):
    msg=""
    cid=request.GET.get("id")
    if(request.POST):
        name=request.POST['txtCategory']
        s="update tblcategory set category='"+name+"' where catid='"+cid+"'"
        try:
            c.execute(s)
            db.commit()
        except:
            msg="Sorry some error occured"
        else:
            msg="Category updated"
    s="select * from tblcategory where catid='"+cid+"'"
    c.execute(s)
    category=c.fetchall()
    s="select * from tblcategory"
    c.execute(s)
    data=c.fetchall()
    return render(request,"adminupdatecategory.html",{"msg":msg,"data":data,"category":category})
def deletecategory(request):
    msg=""
    cid=request.GET.get("id")
    s="delete from tblcategory where catid='"+cid+"'"
    c.execute(s)
    db.commit()
    return HttpResponseRedirect("/admincategory")
######################################################################
#                      LOAD SUBCATEGORY PAGE
######################################################################
def adminsubcategory(request):
    msg=""
    s="select * from tblcategory"
    c.execute(s)
    category=c.fetchall()
    if(request.POST):
        catid=request.POST['cat']
        name=request.POST['txtSubcategory']
        s="insert into tblsubcategory (catid,subcategory) values('"+catid+"','"+name+"')"
        try:
            c.execute(s)
            db.commit()
        except:
            msg="Sorry some error occured"
        else:
            msg="Subcategory added"
    s="select tblsubcategory.*,tblcategory.category from tblcategory,tblsubcategory where tblcategory.catid=tblsubcategory.catid"
    c.execute(s)
    data=c.fetchall()
    return render(request,"adminsubcategory.html",{"msg":msg,"data":data,"category":category})
def updatesubcategory(request):
    msg=""
    cid=request.GET.get("id")
    if(request.POST):
        name=request.POST['txtSubcategory']
        s="update tblsubcategory set subcategory='"+name+"' where subid='"+cid+"'"
        try:
            c.execute(s)
            db.commit()
        except:
            msg="Sorry some error occured"
        else:
            msg="Subcategory updated"
    s="select tblsubcategory.*,tblcategory.category from tblcategory,tblsubcategory where tblcategory.catid=tblsubcategory.catid and subid='"+cid+"'"
    c.execute(s)
    category=c.fetchall()
    s="select tblsubcategory.*,tblcategory.category from tblcategory,tblsubcategory where tblcategory.catid=tblsubcategory.catid"
    c.execute(s)
    data=c.fetchall()
    return render(request,"adminupdatesubcategory.html",{"msg":msg,"data":data,"category":category})
def deletesubcategory(request):
    msg=""
    cid=request.GET.get("id")
    s="delete from tblsubcategory where subid='"+cid+"'"
    c.execute(s)
    db.commit()
    return HttpResponseRedirect("/adminsubcategory") 
######################################################################
#                      LOAD BRAND PAGE
######################################################################
def adminbrand(request):
    msg=""
    if(request.POST):
        name=request.POST['txtCategory']
        s="insert into tblbrand (brand) values('"+name+"')"
        try:
            c.execute(s)
            db.commit()
        except:
            msg="Sorry some error occured"
        else:
            msg="Brand added"
    s="select * from tblbrand"
    c.execute(s)
    data=c.fetchall()
    return render(request,"adminbrand.html",{"msg":msg,"data":data})
def updatebrand(request):
    msg=""
    cid=request.GET.get("id")
    if(request.POST):
        name=request.POST['txtCategory']
        s="update tblbrand set brand='"+name+"' where bid='"+cid+"'"
        try:
            c.execute(s)
            db.commit()
        except:
            msg="Sorry some error occured"
        else:
            msg="Brand updated"
    s="select * from tblbrand where bid='"+cid+"'"
    c.execute(s)
    category=c.fetchall()
    s="select * from tblbrand"
    c.execute(s)
    data=c.fetchall()
    return render(request,"adminupdatebrand.html",{"msg":msg,"data":data,"category":category})
def deletebrand(request):
    msg=""
    cid=request.GET.get("id")
    s="delete from tblbrand where bid='"+cid+"'"
    c.execute(s)
    db.commit()
    return HttpResponseRedirect("/adminbrand")   
######################################################################
#                      LOAD PRODUCT PAGE
######################################################################
def adminproduct(request):
    msg=""
    s="select * from tblcategory"
    c.execute(s)
    category=c.fetchall()
    s="select * from tblbrand"
    c.execute(s)
    brand=c.fetchall()
    if(request.POST):
        bid=request.POST['brand']
        print(bid)
        subid=request.POST['subcat']
        s="select subid from tblsubcategory where subcategory='"+subid+"'"
        c.execute(s)
        d=c.fetchone()
        subid=d[0]
        product=request.POST['txtProduct']
        producdesct=request.POST['txtDesc']
        rate=request.POST['txtRate']
        img=request.FILES["txtFile"]
        fs=FileSystemStorage()
        filename=fs.save(img.name,img)
        uploaded_file_url=fs.url(filename)
        s="insert into tblproduct (subid,bid,product,description,rate,img) values('"+str(subid)+"','"+str(bid)+"','"+product+"','"+producdesct+"','"+str(rate)+"','"+uploaded_file_url+"')"
        print(s)
        try:
            c.execute(s)
            db.commit()
        except:
            msg="Sorry some error occured"
        else:
            msg="Product added"
    s="select tblproduct.*,tblsubcategory.subcategory,tblcategory.category,tblbrand.brand from tblcategory,tblsubcategory,tblproduct,tblbrand where tblcategory.catid=tblsubcategory.catid and tblproduct.bid=tblbrand.bid and tblproduct.subid=tblsubcategory.subid"
    c.execute(s)
    data=c.fetchall()
    return render(request,"adminproduct.html",{"msg":msg,"data":data,"category":category,"brand":brand})
def deleteproduct(request):
    msg=""
    cid=request.GET.get("id")
    s="delete from tblproduct where pid='"+cid+"'"
    c.execute(s)
    db.commit()
    return HttpResponseRedirect("/adminproduct") 
def getsub(request):
    y=request.GET.get("id")
    print(y)
    s="select subcategory from tblsubcategory where catid='"+str(y)+"'"
    c.execute(s)
    data=c.fetchall()
    print(data)
    jsonStr = json.dumps(data)
    print(jsonStr)
    return HttpResponse(jsonStr)
######################################################################
#                      LOAD ORDER PAGE
######################################################################
def adminorders(request):
    s="select tblproduct.pid,tblproduct.product,tblcart.rate,tblproduct.img,tblregistration.name,tblcart.status from tblproduct,tblcart,tblregistration where tblproduct.pid=tblcart.pid and tblcart.rid=tblregistration.rid"
    c.execute(s)
    data=c.fetchall()
    return render(request,"adminorders.html",{"data":data})
######################################################################
#                                                                    #
#                                                                    #
#                           CUSTOMER                                 #
#                                                                    #
#                                                                    #
######################################################################
######################################################################
#                      LOAD CUSTOMER HOME PAGE
######################################################################
def customerhome(request):
    rid=request.session['id']
    s="select tblproduct.*,tblsubcategory.subcategory,tblcategory.category,tblbrand.brand from tblcategory,tblsubcategory,tblproduct,tblbrand where tblcategory.catid=tblsubcategory.catid and tblproduct.bid=tblbrand.bid and tblproduct.subid=tblsubcategory.subid order by tblproduct.pid desc limit 5"
    c.execute(s)
    data=c.fetchall()
    recomend=[]
    recent=[]
    if weighted_recommendation():
        recomend=weighted_recommendation()
    if recently_viewed(rid):
        recent=recently_viewed(rid)
    if most_selling():
        mostselling=most_selling()
    return render(request,"customerhome.html",{"data":data,"recomend":recomend,"recent":recent,"mostselling":mostselling})
######################################################################
#                      LOAD CUSTOMER ALL PRODUCTS PAGE
######################################################################
def customerallproducts(request):
    rid=request.session['id']
    s="select tblproduct.*,tblsubcategory.subcategory,tblcategory.category,tblbrand.brand from tblcategory,tblsubcategory,tblproduct,tblbrand where tblcategory.catid=tblsubcategory.catid and tblproduct.bid=tblbrand.bid and tblproduct.subid=tblsubcategory.subid order by tblproduct.pid desc"
    c.execute(s)
    data=c.fetchall()
    return render(request,"customerallproducts.html",{"data":data})
######################################################################
#                      LOAD PRODUCT DETAILS PAGE
######################################################################
def customerviewproduct(request):
    pid=request.GET.get("id")
    rid=request.session['id']
    s="insert into tblview(rid,vdate,pid) values('"+str(rid)+"',(select sysdate()),'"+str(pid)+"')"
    c.execute(s)
    db.commit()
    s="select * from tblproduct where pid='"+pid+"'"
    c.execute(s)
    data=c.fetchall()
    rate=data[0][5]
    # print(rate)
    s="select avg(rating) from tblreview where pid='"+str(pid)+"'"
    c.execute(s)
    d=c.fetchone()
    rating=d[0]
    s="select tblregistration.name,tblreview.feedback from tblregistration,tblreview where tblregistration.rid=tblreview.rid and tblreview.pid='"+str(pid)+"'"
    c.execute(s)
    feedback=c.fetchall()
    if 'cart' in request.POST:
        s="insert into tblcart(rid,pid,cdate,qty,rate,status) values('"+str(rid)+"','"+str(pid)+"',(select sysdate()),'1','"+str(rate)+"','In cart')"
        try:
            c.execute(s)
            db.commit()
        except:
            pass
        else:
            return HttpResponseRedirect("/customercart")
    if 'review' in request.POST:
        return HttpResponseRedirect("/customerreview?id="+str(pid)+"&rating=0")
    return render(request,"customerviewproduct.html",{"data":data,"rating":rating,"feedback":feedback})
######################################################################
#                      LOAD CUSTOMER CART PAGE
######################################################################
def customercart(request):
    rid=request.session['id']
    s="select tblproduct.pid,tblproduct.product,tblcart.rate,tblproduct.img from tblproduct,tblcart where tblproduct.pid=tblcart.pid and tblcart.rid='"+str(rid)+"' and tblcart.status='In cart'"
    c.execute(s)
    data=c.fetchall()
    if request.POST:
        return HttpResponseRedirect("/payment")
    return render(request,"customercart.html",{"data":data})
######################################################################
#                      PAYMENT PAGE
######################################################################
def payment(request):
    rid=request.session['id']
    s="select sum(rate) from tblcart where rid='"+str(rid)+"'"
    c.execute(s)
    d=c.fetchone()
    amt=d[0]
    if request.POST:
        s="update tblcart set status='purchased',cdate=(select sysdate()) where rid='"+str(rid)+"'"
        c.execute(s)
        db.commit()
        return HttpResponseRedirect("/customerhome")
    return render(request,"payment.html",{"amt":amt})
######################################################################
#                      LOAD CUSTOMER REVIEW PAGE
######################################################################
def customerreview(request):
    pid=request.GET.get("id")
    rid=request.session['id']
    rating=request.GET.get("rating")
    s="select count(*) from tblreview where pid='"+str(pid)+"' and rid='"+str(rid)+"'"
    c.execute(s)
    d=c.fetchone()
    if d[0]>0:
        return HttpResponseRedirect("/customerviewproduct?id="+str(pid))
    if request.POST:
        feedback=request.POST['txtfeedback']
        s="insert into tblreview(rid,pid,rdate,feedback,rating) values('"+str(rid)+"','"+str(pid)+"',(select sysdate()),'"+feedback+"','"+rating+"')"
        try:
            c.execute(s)
            db.commit()
        except:
            pass
        else:
            return HttpResponseRedirect("/customerhome")
    return render(request,"customerreview.html",{"rating":rating,"id":pid})
######################################################################
#                      WEIGHTED RECOMMENDATION
######################################################################
def weighted_recommendation():
    pid=[]
    rating={}
    
    s="select pid from tblproduct"
    c.execute(s)
    d=c.fetchall()
    for i in d:
        pid.append(i[0])
    print(pid)

    for i in pid:
        s="select count(*) from tblreview where pid='"+str(i)+"'"
        c.execute(s)
        d=c.fetchone()
        if d[0]>0:
            s1="select avg(rating) from tblreview where pid='"+str(i)+"'"
            c.execute(s1)
            d1=c.fetchone()
            if d1[0]>2:
                rating[i]=int(d1[0])
    print(rating)

    import operator
    data=dict(sorted(rating.items(), key=operator.itemgetter(1),reverse=True))

    from itertools import islice
    
    def take(n, iterable):
        return list(islice(iterable, n))
    
    n_items = take(5, data.items())
    
    items=[]
    for i in n_items:
        s="select * from tblproduct where pid='"+str(i[0])+"'"
        c.execute(s)
        d=c.fetchone()
        items.append(d)
    print(items)
    return items
######################################################################
#                      RECENTLY VIEWED PRODUCT
######################################################################
def recently_viewed(rid):
    items=[]

    s="select count(*) from tblview where rid='"+str(rid)+"'"
    c.execute(s)
    d=c.fetchone()
    if d[0]>0:
        s="select distinct(pid) from tblview where rid='"+str(rid)+"' order by vid desc limit 5 "
        c.execute(s)
        data=c.fetchall()
        
        for i in data:
            s="select * from tblproduct where pid='"+str(i[0])+"'"
            c.execute(s)
            d=c.fetchone()
            items.append(d)
        print(items)
    return items

######################################################################
#                      MOST SOLD PRODUCT
######################################################################
def most_selling():
    items=[]

    s="select pid,count(pid) from tblcart group by pid order by count(pid) desc"
    c.execute(s)
    purchasecount=c.fetchall()

    
    
    for i in purchasecount:
        s="select * from tblproduct where pid='"+str(i[0])+"'"
        c.execute(s)
        d=c.fetchone()
        items.append(d)

        
    return items[:5]
######################################################################
#                      LOAD CUSTOMER ORDER PAGE
######################################################################
def customerorders(request):
    rid=request.session['id']
    s="select tblcart.cartid,tblproduct.product,tblcart.rate,tblproduct.img,tblcart.status,tblcart.cdate from tblproduct,tblcart where tblproduct.pid=tblcart.pid and tblcart.rid='"+str(rid)+"' and tblcart.status='purchased'"
    c.execute(s)
    data=c.fetchall()
    return render(request,"customerorders.html",{"data":data})