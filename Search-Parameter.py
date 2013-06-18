#author "PK"

vals = ["23771","True","true","False","false"] #Enter the Value to be Searched

def gety(req):
 for params in req.Query.GetNames():
  for val in vals:
   if req.Query.GetAll(params)[0] == val:
    print "URL = ",req.FullUrl,req.Method,"Request ID: ",req.LogId
    
def puty(req):
 for param in req.Body.RawGetNames():
  for val in vals:
   if req.Body.GetAll(param)[0] == val:
    print "URL = ",req.FullUrl,req.Method,"Request ID: ",req.LogId
   

for i in range(1,Config.LastProxyLogId):
 req = Request.FromProxyLog(i)
 if req.Method == "GET": 
  gety(req)
 elif req.Method == "POST":
  puty(req)
