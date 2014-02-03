requests = Request.FromProxyLog()
for request in requests:
 if request.Method == "POST":
  requestBody = request.Body
  if requestBody.Has("authenticity_token"):
   print "Looks Like RoR is being used check for CSRF",request.FullUrl,requestBody.RawGetNames()
   print "**********************************************************************"
