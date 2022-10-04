from django.http import HttpResponse
from . import functions

ID = functions.jsonData['ID']
PWD = functions.jsonData['PWD']
serverAddr =functions.jsonData['serverAddr']

def ready(request):
    TransData = dict()
    
    #########################################
    # 아래 데이터는 고정값입니다. 변경하지 마세요 #
    #########################################
    
    TransData['TXTYPE'] = 'ITEMSEND'
    TransData['SERVICE'] = 'UAS'
    TransData['AUTHTYPE'] = '36'
    
    
    ############### 필 수 사 항 ###############
    # ID : 다날에서 제공해드린 ID ( function 파일 참조)
    # PWD : 다날에서 제공해드린 PWD ( function 파일 참조)
    # TARGETURL : 인증 완료 시 이동할 페이지의 FULL URL
    ##########################################
    
    TransData['CPID'] = ID
    TransData['CPPWD'] = PWD
    TransData['TARGETURL'] = serverAddr + functions.jsonData['TargetURL']
    
    ############### 선 택 사 항 ###############
    # USERID : 사용자 USERID
    # ORDERID : CP 주문번호
    ##########################################
    
    # TransData['USERID'] = functions.jsonData['USERID']
    # TransData['ORDERID'] = functions.jsonData['ORDERID']
    
    
    ##########################################
    # CPCGI 에 HTTP POST 로 전달되는 데이터
    ##########################################
    
    
    ############### 필 수 사 항 ###############
	# BgColor      : 인증 페이지 Background Color 설정
	# BackURL      : 에러 발생 및 취소 시 이동 할 페이지의 FULL URL
	# IsCharSet	: charset 지정( deault:EUC-KR, UTF-8 )
    ##########################################
    
    ByPassValue = dict() 
    
    ByPassValue["BgColor"] = "00"
    ByPassValue["BackURL"] = serverAddr + functions.jsonData['BackURL']
    ByPassValue["IsCharSet"] = functions.jsonData['IsCharSet'] if 'IsCharSet' in functions.jsonData else 'EUC-KR'
    
    ############### 선 택 사 항 ###############
    
    # ByPassValue["ByBuffer"] = functions.jsonData['ByBuffer']
    # ByPassValue["ByAnyName"] = functions.jsonData['ByAnyName']
    
    
    ##########################################
    # 가맹점 인증 후 TID 전송, 본인인증 창 호출하기
    ########################################## 
    
    Res = functions.CallTrans(TransData, True);
    
    if( Res['RETURNCODE'] == "0000"):
        Out = """
        <head>
        <meta http-equiv="X-UA-Compatible" content="IE=edge"/>
        <meta http-equiv="Content-Type" content="text/html; charset=euc-kr" />
        </head>
        <body>
            <form name="Ready" action="https://wauth.teledit.com/Danal/WebAuth/Web/Start.php" method="post">
                """ + functions.MakeFormInput(Res, ["RETURNCODE", "RETURNMSG"]) + functions.MakeFormInput(ByPassValue) + f"""
            </form>
            <script Language="JavaScript">
                document.Ready.submit();
            </script>
        </body>

        """
        
        return HttpResponse(Out, content_type='text/html; charset=euc-kr')
    else :        
    	return HttpResponse("Error on Ready Step. <br>RETURNCODE: "+ Res['RETURNCODE'] + "<br>RETURNMSG: " + Res['RETURNMSG'])