script = '{"d":{"messageId":"%(msg_id)s",' \
                     '"traceId":"0000000000","oa":"%(oa)s",' \
                     '"prefixOa":"","da":"qa_chatapp","prefixDa":"",' \
                     '"acc":"%(api_key)s","appId":null,"msg":"%(chatapp_body)s",' \
                     '"media":"","content":"text","host":"CPQ.QA.Scripts",' \
                     '"srcIp":null,"cost":"0.02","internalCost":"0.002","price":"0.00050000",' \
                     '"internalPrice":"","currency":"","country":"%(country)s","product":"19",' \
                     '"type":"MO","msgType":"%(msgType)s","@version":"1",' \
                     '"anonymized":"false","@timestamp":"%(timestamp)s","moProviderLatencyMs":"",' \
                     '"moLatencyMs":"", "@date":"%(date)s","status":"%(status)s","deliveredDate":"%(zdate)s"' \
                     ',"aggregateId": "%(aggregateId)s","billingContentType": "template_charged"},' \
                     '"quotedPriceAttributes": { ' \
                        '"pricingModel": "NBP", ' \
                        '"conversationId": "532b57b5f6e63595ccd74c6010e5c5c7",'\
                        '"category": "user_initiated"'\
                        '},'\
                     '"topic": "event_chatapp_mo_anonymized","datacenter":"lon2"}\n' % {
                         "status":status,
                         "msgType": msgType,
                         "country": country,
                         "msg_id": msg_id,
                         "oa": oa,
                         "api_key": api_key,
                         "date": date,
                         "zdate": submittedDate,
                         "timestamp": timestamp,
                         "chatapp_body": CHATAPP_MO_BODY,
                         "aggregateId": aggregateId}

