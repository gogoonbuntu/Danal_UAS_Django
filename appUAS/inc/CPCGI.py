from django.http import HttpResponse

from . import functions

def cpcgi(request):
    TransData = dict()
    
    if(request.method == 'POST'):
        TID = request.POST["TID"]
        
    TransData["TXTYPE"] = "CONFIRM"
    TransData["TID"] = TID
    TransData["CONFIRMOPTION"] = str(functions.jsonData['CONFIRMOPTION'])
    TransData["IDENOPTION"] = str(functions.jsonData['IDENOPTION'])

    if (TransData["CONFIRMOPTION"] == 1):
        TransData['CPID'] = functions.ID
        TransData['ORDERID'] = functions.jsonData['ORDERID']

    Res = functions.CallTrans(TransData, False)

    if( Res["RETURNCODE"] == "0000" ):	
        ##################################
        # 결제 성공에 대한 작업
        ##################################
        return HttpResponse('Success!<br>'+functions.Map2Str(TransData)+functions.Map2Str(Res))
    else:
        ##################################
        # 결제 실패에 대한 작업
        ##################################
        return HttpResponse('Error!!!<br>'+functions.Map2Str(TransData)+functions.Map2Str(Res))
