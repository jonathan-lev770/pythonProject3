import uuid
from datetime import datetime, timedelta
from random import randint

start_date_raw = datetime.utcnow() - timedelta(days=30)
default_start_time = str(start_date_raw.strftime('%H:%M:%S'))
default_start_day = str(start_date_raw.strftime('%Y-%m-%d'))
default_start_date = str(default_start_day) + "T" + str(default_start_time) + "+0000"

old_start_date = "2017-06-01T14:10:11+0000"
old_end_date = "2017-09-15T14:10:11+0000"

end_date_raw = datetime.utcnow() + timedelta(days=2)
default_end_time = str(end_date_raw.strftime('%H:%M:%S'))
default_end_day = str(end_date_raw.strftime('%Y-%m-%d'))
default_end_date = str(default_end_day) + "T" + str(default_end_time) + "+0000"
submittedDate = str(default_end_day) + "T" + str(default_end_time) + ".000Z"



def voice_cdr(api_key, number, country, productClass="tts", topic="event_tts_call_anonymized"):
    """
    Builds test voice (tts) CDR and pushes it into Kafka qa1_ test topic, that eventually
    leads to insertion into Google Cloud Datastore
    :param api_key: User's api_key i.e. account_id
    :param number: Target msisdn (number) to generate a request
    :return: Generated unique message_id
    :developer: alexander.fokin
    """
    uid = uuid.uuid4()
    msg_id = "{}-{}-{}-{}-{}".format(uid.hex[:8], uid.hex[:4], uid.hex[:4], uid.hex[:4],
                                     uid.hex[:12])
    now = datetime.utcnow() + timedelta(days=int(0))
    date = now.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + '+0000'
    timestamp = int(now.timestamp())
    script = '{"d":{"@class":"com.nexmo.voice.core.cache.VoiceContext",' \
             '"@date":"%(date)s",' \
             '"@timestamp":"%(timestamp)s","acc":"%(api_key)s","backend":"VOXEO",' \
             '"callDate":"%(date)s","callDuration":"1998","callRetries":"0",' \
             '"cost":"0.06660000","costPrefix":"44","country":"%(country)s","direction":"out",' \
             '"duration":"2","end":"%(date)s","forceSender":"null",' \
             '"from":"null","gw":"ibasis","host":"CPQ.QA.Scripts",' \
             '"id":"%(id)s","minUnit":"6","net":"23420","pdd":"0",' \
             '"price":"0.60000000","product":"5","productClass":"%(productClass)s","reason":"200",' \
             '"reasonDesc":"The call was successful.","recurringUnit":"6",' \
             '"requestIp":"10.136.125.54","routingSeq":"1416305884",' \
             '"sessionId":"%(id)s",' \
             '"start":"%(date)s","status":"ok","superHubAcc":"null",' \
             '"text":"Random text on create a callt jdelbkkwrzz9y2yny5zi7tndmmhzm03ukwduf.",' \
             '"to":"%(number)s","totalCost":"0.00222000","totalPrice":"0.02000000","unit":"6",' \
             '"voice":"en-us-female"},"topic":"%(topic)s"}\n' % {"id": msg_id,
                                             "productClass": productClass,
                                             "country": country,
                                             "number": number,
                                             "api_key": api_key,
                                             "date": date,
                                             "timestamp": timestamp,
                                             "topic": topic}
    return script, msg_id


def outbound_voice_cdr(api_key, number, country, productClass="tts", topic="event_sip_outbound_anonymized"):
    """
    Builds test voice (tts) CDR and pushes it into Kafka qa1_ test topic, that eventually
    leads to insertion into Google Cloud Datastore
    :param api_key: User's api_key i.e. account_id
    :param number: Target msisdn (number) to generate a request
    :return: Generated unique message_id
    :developer: alexander.fokin
    """
    uid = uuid.uuid4()
    msg_id = "{}-{}-{}-{}-{}".format(uid.hex[:8], uid.hex[:4], uid.hex[:4], uid.hex[:4],
                                     uid.hex[:12])


    now = datetime.utcnow() + timedelta(days=int(0))
    date = now.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + '+0000'
    timestamp = int(now.timestamp())
    script = '{"d":{"@class":"com.nexmo.voice.core.cache.VoiceContext",' \
             '"@date":"%(date)s",' \
             '"@timestamp":"%(timestamp)s","acc":"%(api_key)s","backend":"VOXEO",' \
             '"callDate":"%(date)s","callDuration":"1998","callRetries":"0",' \
             '"cost":"0.06660000","costPrefix":"44","country":"%(country)s","direction":"out",' \
             '"duration":"3","end":"%(date)s","forceSender":"null",' \
             '"from":"null","gw":"ibasis","host":"CPQ.QA.Scripts",' \
             '"id":"%(id)s","minUnit":"6","net":"23420","pdd":"0",' \
             '"price":"0.60000000","product":"5","productClass":"%(productClass)s","reason":"200",' \
             '"reasonDesc":"The call was successful.","recurringUnit":"6",' \
             '"requestIp":"10.136.125.54","routingSeq":"1416305884",' \
             '"sessionId":"%(id)s",' \
             '"start":"%(date)s","status":"ok","superHubAcc":"null",' \
             '"text":"Kafka insertion test",' \
             '"to":"%(number)s","totalCost":"0.00222000","totalPrice":"0.02000000","unit":"6",' \
             '"voice":"en-us-female"},"topic":"%(topic)s"}\n' % {"id": msg_id,
                                             "productClass": productClass,
                                             "country": country,
                                             "number": number,
                                             "api_key": api_key,
                                             "date": date,
                                             "timestamp": timestamp,
                                             "topic": topic}
    return script, msg_id


def inbound_voice_cdr(api_key, number, country, productClass="tts",topic="event_sip_inbound_anonymized"):
    """
    Builds test voice (tts) CDR and pushes it into Kafka qa1_ test topic, that eventually
    leads to insertion into Google Cloud Datastore
    :param api_key: User's api_key i.e. account_id
    :param number: Target msisdn (number) to generate a request
    :return: Generated unique message_id
    :developer: alexander.fokin
    """
    uid = uuid.uuid4()
    msg_id = "{}-{}-{}-{}-{}".format(uid.hex[:8], uid.hex[:4], uid.hex[:4], uid.hex[:4],
                                     uid.hex[:12])


    now = datetime.utcnow() + timedelta(days=int(0))
    date = now.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + '+0000'
    timestamp = int(now.strftime('%S')) * 1000
    script = '{"d":{"@class":"com.nexmo.voice.core.cache.VoiceContext",' \
             '"@date":"%(date)s",' \
             '"@timestamp":"%(timestamp)s","acc":"%(api_key)s","backend":"VOXEO",' \
             '"callDate":"%(date)s","callDuration":"1998","callRetries":"0",' \
             '"cost":"0.06660000","costPrefix":"44","country":"%(country)s","direction":"in",' \
             '"duration":"1","end":"%(date)s","forceSender":"null",' \
             '"from":"%(number)s","gw":"ibasis","host":"CPQ.QA.Scripts",' \
             '"id":"%(id)s","minUnit":"6","net":"23420","pdd":"0",' \
             '"price":"0.60000000","product":"5","productClass":"%(productClass)s","reason":"200",' \
             '"reasonDesc":"The call was successful.","recurringUnit":"6",' \
             '"requestIp":"10.136.125.54","routingSeq":"1416305884",' \
             '"sessionId":"%(id)s",' \
             '"start":"%(date)s","status":"ok","superHubAcc":"null",' \
             '"text":"Kafka insertion test",' \
             '"to":"18669010242","totalCost":"0.00222000","totalPrice":"0.02000000","unit":"6",' \
             '"voice":"en-us-female"},"topic":"%(topic)s"}\n' % {"id": msg_id,
                                             "productClass": productClass,
                                             "country": country,
                                             "number": number,
                                             "api_key": api_key,
                                             "date": date,
                                             "timestamp": timestamp,
                                             "topic":topic}
    return script, msg_id

def hlr_cdr(api_key, product, number, country, lookupType, topic="event_hlr_requests_anonymized"):
    """
    Builds test Number Insight (HLR) CDR and pushes it into Kafka qa1_ test topic, that eventually
    leads to insertion into Google Cloud Datastore
    :param api_key: User's api_key i.e. account_id
    :param number: Target msisdn (number) to generate a request
    :return: Generated unique message_id
    :developer: alexander.fokin
    """
    uid = uuid.uuid4()
    msg_id = "{}-{}-{}-{}-{}".format(uid.hex[:8], uid.hex[:4], uid.hex[:4], uid.hex[:4], uid.hex[:12])
    now = datetime.utcnow() + timedelta(days=int(0))
    date = now.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + '+0000'
    timestamp = int(now.strftime('%S')) * 1000
    prefix = number[:6]
    script = '{"d":{"@class":"Core","@date":"%(date)s",' \
             '"@timestamp":"%(timestamp)s","acc":"%(api_key)s","ackLat":"501",' \
             '"anonymized":"false","callback":"","callerName":"unknown",' \
             '"callerSubscriptionType":"unknown","callerType":"unknown","campaign":"",' \
             '"clientIpAddress":"10.136.125.54","cost":"999","country":"%(country)s",' \
             '"dateSubmitted":"%(date)s","err":"Success",' \
             '"firstName":"unknown","forceHandler":"null","forcePrice":"","handler":"dummy",' \
             '"handlerTrxId":"","host":"CPQ.QA.Scripts",' \
             '"id":"%(id)s","internalAcc":"","ip":"",' \
             '"ipCity":"London","ipCountry":"%(country)s","ipMatchLevel":"mismatch",' \
             '"ipWarnings":"anon_proxy","lastName":"unknown",' \
             '"lookupType":"%(lookupType)s",' \
             '"msisdn":"%(number)s","net":"-unknown-","netDerived":"false","netType":"mobile",' \
             '"ported":"assumed_ported","prefixMsisdn":"%(prefix)s","price":"0.00050000",' \
             '"product":"%(product)s","productClass":"","reachable":"reachable","ref":"",' \
             '"responseCode":"0","roaming":"true","roamingCountry":"IT","roamingNet":"22205",' \
             '"routingRuleSeq":"1429278393","subscriberId":"","subscriberStatus":"",' \
             '"super":"true","valid":"valid","accountPricingGroup":"", "masterAccount":"", ' \
             '"masterAccountPricingGroup":"", "networkName":"AT,T"},"topic":"%(topic)s"}\n' % {"id": msg_id,
                                                                       "country": country,
                                                                       "number": number,
                                                                       "api_key": api_key,
                                                                       "date": date,
                                                                       "prefix": prefix,
                                                                       "timestamp": timestamp,
                                                                       "product": product,
                                                                       "lookupType": lookupType,
                                                                       "topic": topic}

    return script, msg_id


def verify_cdr(api_key,number,country,pricingModel,topic="event_verify_verify_anonymized"):
    """
    Builds test Verify CDR and pushes it into Kafka qa1_ test topic, that eventually
    leads to insertion into Google Cloud Datastore
    :param api_key: User's api_key i.e. account_id
    :param number: Target msisdn (number) to generate a request
    :return: Generated unique message_id
    :developer: alexander.fokin
    """
    uid = uuid.uuid4()
    msg_id = "{}{}{}".format('1b', uid.hex[:26], '8306')
    now = datetime.utcnow() + timedelta(days=int(0))
    date = now.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + '+0000'
    timestamp = int(now.strftime('%S')) * 1000
    date_wout_seconds = now.strftime('%Y-%m-%d %H:%M:%S')
    prefix = number[:6]
    script = '{"d":{"@class":"Core","@date":"%(date)s",' \
             '"@timestamp":"%(timestamp)s","acc":"%(api_key)s","app":"",' \
             '"brand":"NexmoQA","callbackUrl":"null","callbacks":' \
             '[{"callbacks":[{"callbackId":"0A000001000278F0","cost":"1",' \
             '"dateReceived":"%(date_wout_seconds)s","status":"accepted","type":"DLR"}],' \
             '"date":"%(date_wout_seconds)s","eventId":"0A000001000278F0","type":"DLR"}],' \
             '"channel":"API","checkCount":"1","checks":[{"code":"0457",' \
             '"date_received":"%(date_wout_seconds)s","ip_address":"","status":"VALID"}],' \
             '"codeLength":"4","cost":"1","countryCode":"%(country)s","currency":"EUR",' \
             '"dateFinalized":"%(date)s",' \
             '"dateSubmitted":"%(date)s","eventCount":"1",' \
             '"firstCodeSent":"%(date)s",' \
             '"id":"%(id)s",' \
             '"lastCodeSent":"%(date)s","locale":"en-us","network":"23420",' \
             '"number":"%(number)s","numberType":"MOBILE","prefixNumber":"%(prefix)s",' \
             '"price":"0.05000000","product":"NUMBER-VERIFY","productClass":"",' \
             '"pushEventCount":"0","requestIp":"10.136.125.54","sender":"verify",' \
             '"smsEventCount":"1","status":"SUCCESS","tracingContext":' \
             '{"requestId":"%(id)s"},"ttsEventCount":"0",' \
             '"workflowId":"40","pricingModel":"%(pricingModel)s"}, "fqdn":"test.host","topic":"%(topic)s"}\n' % {"id": msg_id,
                                        "pricingModel": pricingModel,
                                        "country": country,
                                        "number": number,
                                        "api_key": api_key,
                                        "date": date,
                                        "date_wout_seconds": date_wout_seconds,
                                        "prefix": prefix,
                                        "timestamp": timestamp,
                                        "topic": topic}
    return script, msg_id


def sms_mo_cdr(api_key, number, country, topic="event_hub_all-mo_anonymized"):
    """
    Builds test SMS MO CDR and pushes it into Kafka qa1_ test topic, that eventually
    leads to insertion into Google Cloud Datastore
    :param api_key: User's api_key i.e. account_id
    :param number: Target msisdn (number) to generate a request
    :return: Generated unique message_id
    :developer: alexander.fokin
    """
    uid = uuid.uuid4()
    msg_id = "{}{}{}".format('0', uid.hex, '1A')
    now = datetime.utcnow() + timedelta(days=int(0))
    date = now.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + '+0000'
    timestamp = int(now.strftime('%S')) * 1000
    script = '{"d":{"type":"MO","product":"SMS","productClass":"","hub":"hub1",' \
             '"host":"CPQ.QA.Scripts","acc":' \
             '"%(api_key)s","sysType":"null(0x00)","accountPricingGroup":"","ref":"null",' \
             '"accountRef":"","app":"",' \
             '"channel":"NONE","superChannel":"NONE","gw":"qa1-qa2",' \
             '"gwTarget":"qa1-qa22-target1","cdrUuid":"%(id)s","gwId":' \
             '"3","oa":"1497055241","da":"%(number)s","udh":"","udhi":"false",' \
             '"msg":"%(sms_body)s","country":"%(country)s"' \
             ',"net":"US-UNKNOWN","tariff":"null","sessionId":"null",' \
             '"serviceType":"null","delivered":"false",' \
             '"resp":"-","final":"expired","reason":"expired_in_queue",' \
             '"received":"%(date)s",' \
             '"moPrice":"0.013500000","hlrLookupCost":"0.0011","moCost":"0.00135000","moKeyword":"NEXMO","dcs":"0",' \
             '"senderCountry":"US","replyToMtId":' \
             '"null","loopback":"false","routingRuleSeq":"0","mwi":"0",' \
             '"kickback":"0.00000000","ackLat":"0",' \
             '"totalLat":"86436020","@timestamp":"%(timestamp)s",' \
             '"@date":"%(date)s","@class":' \
             '"MO-Deliverer"},"transitFeeCost":"0.09","status":"ok",' \
             '"masterAccountPricingGroup":"", "net":"", "networkType":"", ' \
             '"networkName":"AT&T","topic":"%(topic)s"}\n' % {"country": country,
                                      "id": msg_id,
                                      "number": number,
                                      "api_key": api_key,
                                      "date": date,
                                      "timestamp": timestamp,
                                      "sms_body": SMS_MO_CDR_BODY,
                                      "topic": topic}
    msg_id = str(msg_id)
    return script, msg_id


def sms_mt_cdr(api_key, number, country, productClass="", topic="event_connector_mt_anonymized"):
    """
    Builds test SMS MT CDR and pushes it into Kafka qa1_ test topic, that eventually
    leads to insertion into Google Cloud Datastore
    :param api_key: User's api_key i.e. account_id
    :param number: Target msisdn (number) to generate a request
    :return: Generated unique message_id
    :developer: alexander.fokin
    """
    uid = uuid.uuid4()
    msg_id = "{}{}{}".format('0', uid.hex, '1A')
    super_hub_msg_id = '0A00000' + str(randint(111111111, 999999999))
    now = datetime.utcnow() + timedelta(days=int(0))
    date = now.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + '+0000'
    timestamp = int(now.strftime('%S')) * 1000
    prefix = number[:6]
    script = '{"d":{"@class":"MT-Deliverer","@date":"%(date)s",' \
             '"@timestamp":"%(timestamp)s","acc":"%(api_key)s","accountPricingGroup":"",' \
             '"accountRef":"","accountRoutingGroup":"","ackLat":"0","anonymized":"false","app":"",' \
             '"channel":"SMPP","clientIpAddress":"10.134.79.92","country":"%(country)s",' \
             '"customDlrCallback":"null","da":"%(number)s","dcs":"0","delivered":"true",' \
             '"final":"submitted","forceNet":"false","forceRoute":"false","gatewaysToAvoid":"",' \
             '"gw":"clx","gwId":"000075B1","gwTarget":"null","hlrLookupCost":"0.00",' \
             '"hlrLookupPrice":"0.0","host":"CPQ.QA.Scripts","hub":"clx","cdrUuid":"%(id)s",' \
             '"loopback":"false","messageClass":"",' \
             '"msg":"%(sms_body)s","msgLengthBytes":"50",' \
             '"msgLengthChars":"50","mwi":"0","net":"23420","oa":"447475540248","pid":"0",' \
             '"prefixDa":"%(prefix)s","priceCap":"","priceCapAllParts":"","product":"SMS",' \
             '"productClass":"%(productClass)s","randomizedSenderInDlr":"false",' \
             '"reason":"-Delivered Successfully-","received":"%(date)s",' \
             '"ref":"null","remainingBalance":"46.67000000","replaceIfPresent":"0","resp":"0",' \
             '"respReq":"false","routeCost":"0","routingRuleSeq":"9999999999999999",' \
             '"routingTargetGroup":"null","serviceType":"null","sessionId":"null","srr":"255",' \
             '"submissionPrice":"1.000000","superChannel":"HTTP","superHubAcc":"smpp",' \
             '"superHubMsgId":"%(super_hub_msg_id)s","superReceived":"%(date)s",' \
             '"sysType":"hub0","tariff":"null","terminatedLocally":"false","totalLat":"11",' \
             '"transitFeeCost":"0.00","transitFeePrice":"0.0","trustTokens":"","type":"MT","udh":"",' \
             '"udhi":"false","validityPeriod":"null","masterAccountPricingGroup":"", ' \
             '"networkType":"", "networkName":"AT&T"},"topic":"%(topic)s"}\n' % {
                 "productClass": productClass,
                 "country": country,
                 "id": msg_id,
                 "prefix": prefix,
                 "number": number,
                 "api_key": api_key,
                 "date": date,
                 "timestamp": timestamp,
                 "super_hub_msg_id": super_hub_msg_id,
                 "sms_body": SMS_MT_CDR_BODY,
                 "topic": topic}
    msg_id = str(msg_id)
    return script, msg_id


def subscription_cdr(api_key, details, productId, country, action, topic="event_subscription_subscription"):
    """
    Builds test Subscription CDR and pushes it into Kafka qa1_ test topic, that eventually
    leads to insertion into Google Cloud Datastore
    :param api_key: User's api_key i.e. account_id
    :param details: Subscription detail
    :return: Generated subscription id
    """
    sub_uid = uuid.uuid4()
    subscription_id = "{}-{}-{}-{}-{}".\
        format(sub_uid.hex[:8], sub_uid.hex[:4], sub_uid.hex[:4], sub_uid.hex[:4], sub_uid.hex[:12])
    cyc_uid = uuid.uuid4()
    cycle_id = "{}-{}-{}-{}-{}". \
        format(sub_uid.hex[:8], cyc_uid.hex[:4], cyc_uid.hex[:4], cyc_uid.hex[:4], cyc_uid.hex[:12])
    now = datetime.utcnow() + timedelta(days=int(0))
    date = now.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + '+0000'
    timestamp = int(now.timestamp())
    script = '{"d":{"@class":"SubscriptionEngine","@date":"%(date)s",' \
             '"@timestamp":"%(timestamp)s","acc":"%(api_key)s", "instance":"", "host":"CPQ.QA.Scripts", "action":"%(action)s", ' \
             '"subscriptionId":"%(subscriptionId)s", "cycleId":"%(cycleId)s", "productId":"%(productId)s", "resourceFeature":"", ' \
             '"resourceType":"", "country":"%(country)s", "details":"%(details)s", "price":"0.60000000", "cost":"0.02", "reason":"", ' \
             '"dateSubscriptionStarted":"", "totalPaidSinceStartOfSubscription":""}, "topic":"%(topic)s"}\n' % {
                 "country": country,
                 "productId": productId,
                 "api_key": api_key,
                 "date": date,
                 "timestamp": timestamp,
                 "subscriptionId": subscription_id,
                 "cycleId": cycle_id,
                 "details": details,
                 "action": action,
                 "topic": topic}

    print(cycle_id)
    return script, cycle_id


def chatapp_mo(api_key, oa, country, status, msgType,  z_date=False, aggregateId=''):
    """
    Builds test Chatapp(Messages) MO CDR and pushes it into Kafka qa1_ test
    topic, that eventually
    leads to insertion into Google Cloud Datastore
    :param api_key: User's api_key i.e. account_id
    :param oa: chatapp source id
    :return: Generated unique message_id
    :developer: yannick.lambruschi
    """
    print(aggregateId)
    uid = uuid.uuid4()
    msg_id = "{}{}{}".format('0', uid.hex, '1A')
    now = datetime.utcnow() + timedelta(days=int(0))
    date = now.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + '+0000'
    timestamp = int(now.timestamp())
    if z_date == True:
        date = now.isoformat()[:-3] + 'Z'
    if status == "delivered":
        if msgType == "whatsapp":
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
                     '"conversationId": "532b57b5f6e63595ccd74c6010e5c5c7",' \
                     '"category": "user_initiated"' \
                     '},' \
                     '"topic": "event_chatapp_mo_anonymized","datacenter":"lon2"}\n' % {
                         "status": status,
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
        else:
            script = '{"datacenter":"lon2","topic": "event_chatapp_mo_anonymized","d":{"messageId":"%(msg_id)s",' \
                 '"traceId":"0000000000","oa":"%(oa)s",' \
                 '"prefixOa":"","da":"qa_chatapp","prefixDa":"",' \
                 '"acc":"%(api_key)s","appId":null,"msg":"%(chatapp_body)s",' \
                 '"media":"","content":"text","host":"CPQ.QA.Scripts",' \
                 '"srcIp":null,"cost":"0.02","internalCost":"0.002","price":"0.00050000",' \
                 '"internalPrice":"","currency":"","country":"%(country)s","product":"19",' \
                 '"type":"MO","msgType":"%(msgType)s","@version":"1",'\
                 '"anonymized":"false","@timestamp":"%(timestamp)s","moProviderLatencyMs":"",' \
                 '"moLatencyMs":"", "@date":"%(date)s","status":"%(status)s","deliveredDate":"%(zdate)s"}}\n' % {
                     "status":status,
                     "msgType": msgType,
                     "country": country,
                     "msg_id": msg_id,
                     "oa": oa,
                     "api_key": api_key,
                     "date": date,
                     "zdate": submittedDate,
                     "timestamp": timestamp,
                     "chatapp_body": CHATAPP_MO_BODY}
    elif status == "submitted":
        script = '{"datacenter":"lon2","topic": "event_chatapp_mo_anonymized","d":{"messageId":"%(msg_id)s",' \
             '"traceId":"0000000000","oa":"%(oa)s",' \
             '"prefixOa":"","da":"qa_chatapp","prefixDa":"",' \
             '"acc":"%(api_key)s","appId":null,"msg":"%(chatapp_body)s",' \
             '"media":"","content":"text","host":"CPQ.QA.Scripts",' \
             '"srcIp":null,"cost":"0.02","internalCost":"0.002","price":"0.00050000",' \
             '"internalPrice":"","currency":"","country":"%(country)s","product":"19",' \
             '"type":"MO","msgType":"%(msgType)s","@version":"1",' \
             '"anonymized":"false","@timestamp":"%(timestamp)s","moProviderLatencyMs":"",' \
             '"moLatencyMs":"", "@date":"%(date)s","status":"%(status)s","submittedDate":"%(zdate)s"}}\n' % {
                 "status":status,
                 "msgType": msgType,
                 "country": country,
                 "msg_id": msg_id,
                 "oa": oa,
                 "api_key": api_key,
                 "date": date,
                 "zdate": submittedDate,
                 "timestamp": timestamp,
                 "chatapp_body": CHATAPP_MO_BODY}
    return script, msg_id


def chatapp_mt(api_key, oa, country, status, msgType, z_date=False, aggregateId=''):
    """
    Builds test Chatapp(Messages) MO CDR and pushes it into Kafka qa1_ test
    topic, that eventually
    leads to insertion into Google Cloud Datastore
    :param api_key: User's api_key i.e. account_id
    :param oa: chatapp source id
    :return: Generated unique message_id
    :developer: yannick.lambruschi
    """
    uid = uuid.uuid4()
    msg_id = "{}{}{}".format('0', uid.hex, '1A')
    now = datetime.utcnow() + timedelta(days=int(0))
    date = now.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + '+0000'
    timestamp = int(now.timestamp())
    if z_date == True:
        date = now.isoformat()[:-3] + 'Z'
    if status == "delivered":
        if msgType == "whatsapp":
            script = '{"d":{"messageId":"%(msg_id)s",' \
                     '"traceId":"0000000000","oa":"%(oa)s",' \
                     '"prefixOa":"","da":"qa_chatapp","prefixDa":"",' \
                     '"acc":"%(api_key)s","appId":null,"msg":"%(chatapp_body)s",' \
                     '"media":"","content":"text","host":"CPQ.QA.Scripts",' \
                     '"srcIp":null,"cost":"0.02","internalCost":"0.002","price":"0.00050000",' \
                     '"internalPrice":"","currency":"","country":"%(country)s","product":"19",' \
                     '"type":"MT","msgType":"%(msgType)s","@version":"1",' \
                     '"anonymized":"false","@timestamp":"%(timestamp)s",' \
                     '"@date":"%(date)s","status":"%(status)s","deliveredDate":"%(zdate)s",' \
                     '"aggregateId": "%(aggregateId)s","billingContentType": "template_charged"},' \
                     '"topic": "event_chatapp_dr_anonymized","datacenter":"lon2"}\n' % {
                         "status":status,
                         "msgType": msgType,
                         "country": country,
                         "msg_id": msg_id,
                         "oa": oa,
                         "api_key": api_key,
                         "date": date,
                         "zdate": date,
                         "timestamp": timestamp,
                         "chatapp_body": CHATAPP_MO_BODY,
                         "aggregateId": aggregateId}
        else:
            script = '{"datacenter":"lon2","topic": "event_chatapp_dr_anonymized","d":{"messageId":"%(msg_id)s",' \
                 '"traceId":"0000000000","oa":"%(oa)s",' \
                 '"prefixOa":"","da":"qa_chatapp","prefixDa":"",' \
                 '"acc":"%(api_key)s","appId":null,"msg":"%(chatapp_body)s",' \
                 '"media":"","content":"text","host":"CPQ.QA.Scripts",' \
                 '"srcIp":null,"cost":"0.02","internalCost":"0.002","price":"0.00050000",' \
                 '"internalPrice":"","currency":"","country":"%(country)s","product":"19",' \
                 '"type":"MT","msgType":"%(msgType)s","@version":"1",' \
                 '"anonymized":"false","@timestamp":"%(timestamp)s",' \
                 '"@date":"%(date)s","status":"%(status)s","deliveredDate":"%(zdate)s"}}\n' % {
                     "status":status,
                     "msgType": msgType,
                     "country": country,
                     "msg_id": msg_id,
                     "oa": oa,
                     "api_key": api_key,
                     "date": date,
                     "zdate": submittedDate,
                     "timestamp": timestamp,
                     "chatapp_body": CHATAPP_MO_BODY}

    elif status == "submitted":
        script = '{"datacenter":"lon2","topic": "event_chatapp_dr_anonymized","d":{"messageId":"%(msg_id)s",' \
             '"traceId":"0000000000","oa":"%(oa)s",' \
             '"prefixOa":"","da":"qa_chatapp","prefixDa":"",' \
             '"acc":"%(api_key)s","appId":null,"msg":"%(chatapp_body)s",' \
             '"media":"","content":"text","host":"CPQ.QA.Scripts",' \
             '"srcIp":null,"cost":"0.02","internalCost":"0.002","price":"0.00050000",' \
             '"internalPrice":"","currency":"","country":"%(country)s","product":"19",' \
             '"type":"MT","msgType":"%(msgType)s","@version":"1",' \
             '"anonymized":"false","@timestamp":"%(timestamp)s",' \
             '"@date":"%(date)s","status":"%(status)s","submittedDate":"%(zdate)s"}}\n' % {
                 "status":status,
                 "msgType": msgType,
                 "country": country,
                 "msg_id": msg_id,
                 "oa": oa,
                 "api_key": api_key,
                 "date": date,
                 "zdate": submittedDate,
                 "timestamp": timestamp,
                 "chatapp_body": CHATAPP_MO_BODY}
    return script, msg_id

def final_connector(api_key,country, topic="event_connector_final-states_anonymized"):
    uid = uuid.uuid4()
    msg_id = "{}{}{}".format('0', uid.hex, '1A')
    now = datetime.utcnow() + timedelta(days=int(0))
    date = now.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + '+0000'
    timestamp = int(now.strftime('%S')) * 1000
    script = '{"d":{"accountPricingGroup": "","@class": "STATE-ENGINE","gwId": "-none-","country":"%(country)s","transitFeeCost": "0.0001","prefixMsisdn": "20102149","gw": "mobiletulip-direct","gwErrorCode": "0","intGenerated": "true","errorCode": "0","host": "CPQ.QA.Scripts","masterAccountPricingGroup": "","dateSubmitted": "%(date)s","accountRef": "","cdrUuid":"%(id)s","state": "DELIVRD","networkType": "mobile","superHubMsgId": "1500000053C918B5","transitFeePrice": "0","acc": "%(api_key)s","submissionPrice": "0.05350000","dateClosed": "%(date)s","hub": "mobiletulip","masterAcc": "","@date": "%(date)s","net": "60202","networkName": "Vodafone","product": "SMS"},"offset": 1307881657,"type": "log","source": "/home/logconverter/runtime/json/connector/mobiletulip/final-states.2019.08.21.log","datacenter": "wdc4","@timestamp": "%(timestamp)s","lsUuid": "6411b86d-3173-4350-8cfd-36e2514fef92","time_diff": 4.823544936,"beat": {"hostname": "con4","version": "5.4.1+nexmo","name": "con4"},"fqdn": "test.host", "topic":"%(topic)s"}\n'% {
                 "country": country,
                 "id": msg_id,
                 "api_key": api_key,
                 "date": date,
                 "timestamp": timestamp,
                 "topic": topic}

    return script, msg_id

def sip_outbound(api_key,country, productClass="sip", topic='event_sip_outbound_anonymized'):
    uid = uuid.uuid4()
    msg_id = "{}{}{}".format('0', uid.hex, '1A')
    now = datetime.utcnow() + timedelta(days=int(0))
    date = now.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + '+0000'
    script = '{"lsUuid": "%(id)s","fqdn": "ass1.wdc4.internal","d": {"leg2Id": "%(id)s@sip.nexmo.com","status": "ANSWER","country":"%(country)s","cost": "0.00020000","callOrigin": "","acc": "%(api_key)s","prefixTo": "1919709","accountPricingGroup": "","callDate": "%(date)s","minUnit": "6","prefixFrom": "1910208","totalCost": "0.00000667","host": "CPQ.QA.Scripts","direction": "out","net": "","prefixForcedSender": "","totalPrice": "0.00011667","reason": "200","sessionId": "6fe339de-0788-4149-94ef-5e2f0ed64add","networkType": "MOBILE","callDuration": "2000","price": "0.00350000","costPrefix": "1919709","end": "%(date)s","recurringUnit": "6","@date": "%(date)s","start": "%(date)s","requestIp": "","overridePrice": "null","routingSeq": "173598286224604","callTermination": "pstn","leg1Id": "%(id)s","sipDestAttempt": "1#1","networkName": "TEST","pdd": "1662","masterAccountPricingGroup": "","from": "19102084936","forceSender": "null","productClass": "%(productClass)s","gw": "vonage-prem","reasonDesc": "The call was successful.","@class": "com.nexmo.voice.core.cache.VoiceContext","to": "19197098586","id":"%(id)s","unit": "6","duration": "2","gwAttempt": "1#2","product": "5","gws": "vonage-prem,idt","superHubAcc": "null"}, "topic":"%(topic)s"}\n' % {
        "productClass": productClass,
        "country": country,
        "id": msg_id,
        "api_key": api_key,
        "date": date,
        "topic": topic}
    return script, msg_id


def sip_inbound(api_key,country, topic="event_sip_inbound_anonymized"):
    uid = uuid.uuid4()
    msg_id = "{}{}{}".format('0', uid.hex, '1A')
    now = datetime.utcnow() + timedelta(days=int(0))
    date = now.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + '+0000'
    timestamp = int(now.strftime('%S')) * 1000
    script = '{"@version": "1","offset": 20513588,"@timestamp": "%(timestamp)s","time_diff": 11.575543,"beat": {"hostname": "ass3","version": "5.4.1+nexmo","name": "ass3"},"lsUuid": "%(id)s","fqdn": "ass3.wdc4.internal","source": "","d": {"leg2Id": "%(id)s@sip.nexmo.com","status": "ANSWER","country":"%(country)s","cost": "0.0000333","callOrigin": "pstn","acc": "%(api_key)s","prefixTo": "1647477","accountPricingGroup": "","callDate": "%(date)s","minUnit": "6","prefixFrom": "1647982","totalCost": "0.000667","host": "CPQ.QA.Scripts","direction": "in","net": "TEST","prefixForcedSender": "","totalPrice": "0.00013167","reason": "200","sessionId": "4aca7f4fbadb9684297273881090a922","networkType": "MOBILE","callDuration": "1000","price": "0.00790000","rerouteAddress": "12049090742","costPrefix": "null","end": "%(date)s","recurringUnit": "6","@date": "%(date)s","start": "%(date)s","callRetries": "0","requestIp": "","overridePrice": "null","routingSeq": "173598286160707","callTermination": "","leg1Id": "%(id)s@69.59.231.70","sipDestAttempt": "1#1","networkName": "TEST","masterAccountPricingGroup": "","from": "16479824521","forceSender": "null","productClass": "sip","gw": "vonage","reasonDesc": "The call was successful.","@class": "com.nexmo.voice.core.cache.VoiceContext","to": "16474772450","id":"%(id)s","unit": "6","duration": "1","product": "5","gws": "vonage","superHubAcc": "null"}, "topic":"%(topic)s"}'% {
                 "country": country,
                 "id": msg_id,
                 "api_key": api_key,
                 "date": date,
                 "timestamp": timestamp,
                 "topic": topic}

    return script, msg_id

def ipLegMsg_cdr(api_key,currency,topic):
    uid = uuid.uuid4()
    msg_id = "{}{}{}".format('0', uid.hex, '1A')
    con_id = "CON-" + str("{}{}{}".format('0', uid.hex, '1A'))
    user_id = "USR-" + str("{}{}{}".format('0', uid.hex, '1A'))
    now = datetime.utcnow() + timedelta(days=int(0))
    date = now.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    timestamp = int(now.strftime('%S')) * 1000
    script = '{"@timestamp": "%(timestamp)s","d":{"@timestamp": "%(timestamp)s", "@version": "1.7","acc": "%(api_key)s","applicationId": "d7dfe4a5-2493-4f0f-8d1b-3d81317b027d","clientRef": "","contentType": "text","conversationId": "%(con_id)s","cost": "0.00002","creationDate": "%(timestamp)s","id": "%(id)s","messageId": 7,"messageSequenceNumber": 0,"price": "0.00000000","priceCurrency": "%(currency)s","product": 27,"productClass": "stitch","requestId": "%(id)s%(id)s","totalPrice": "1.0000012","traceId": "sub_sent_different_text_to_conversation_--_@1.2__%(id)s","type": "cs:ip-messaging:new","userId": "%(user_id)s"}, "topic":"%(topic)s"}'% {
                 "id": msg_id,
                 "con_id": con_id,
                 "api_key": api_key,
                 "timestamp": date,
                 "currency": currency,
                 "user_id": user_id,
                 "topic": topic}
    return script, msg_id

def ipLegCall_cdr(api_key,currency, topic):
    uid = uuid.uuid4()
    msg_id = "{}{}{}".format('0', uid.hex, '1A')
    con_id = "CON-" + str("{}{}{}".format('0', uid.hex, '1A'))
    user_id = "USR-" + str("{}{}{}".format('0', uid.hex, '1A'))
    now = datetime.utcnow() + timedelta(days=int(0))
    date = now.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    timestamp = int(now.strftime('%S')) * 1000
    script = '{"@timestamp": "%(timestamp)s","d":{"@timestamp": "%(timestamp)s", "@version": "1.7","acc": "%(api_key)s","applicationId": "41ccf54e-bb3a-42df-b128-35db9494443f","clientRef": "","conversationId": "%(con_id)s","cost": "0.0002","costCurrency": "EUR","duration": 38,"endDate": "%(timestamp)s","host": "CPQ.QA.Scripts","id": "%(id)s","jitterBurstRate": 1,"jitterLossRate": 0,"jitterMaxVar": 20.459999,"jitterMinVar": 0.22,"legId": "15cb13bd-b613-4df2-894b-334cbabf5bf7","mos": 4.49,"packetLossPerc": 0.111049,"price": "0.01000000","priceCurrency": "%(currency)s","product": 26,"productClass": "stitch","requestId": "%(id)s%(id)s","srcIp": "11.22.33.44","startDate": "%(timestamp)s","terminationStatus": 200,"terminationStatusReason": "Call answered","totalCost": 0,"totalPrice": "0.0063333","traceId": "%(id)s","type": "cs:ip-audio:end","userId": "%(user_id)s"}, "topic":"%(topic)s"}'% {
                 "id": msg_id,
                 "con_id": con_id,
                 "api_key": api_key,
                 "timestamp": date,
                 "currency": currency,
                 "user_id": user_id,
                 "topic": topic}
    return script, msg_id
    
def custom_event_cdr(api_key, product, productClass,currency, topic="event_ted_cs-custom-event-new"):
    uid = uuid.uuid4()
    msg_id = "{}{}{}".format('0', uid.hex, '1A')
    con_id = "CON-" + str("{}{}{}".format('0', uid.hex, '1A'))
    user_id = "USR-" + str("{}{}{}".format('0', uid.hex, '1A'))
    now = datetime.utcnow() + timedelta(days=int(0))
    date = now.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    timestamp = int(now.timestamp())
    script = '{"@timestamp":"%(timestamp)s","d":{"@timestamp":"%(timestamp)s","@version":"1.7","acc":"%(api_key)s","applicationId":"ea52fde9-e4a7-4fb9-a524-30c669908559","clientRef":"","contentLength":2,"conversationId":"%(con_id)s","cost":"0.00002","creationDate":"%(timestamp)s","id":"%(id)s","nexmoService":"","price":"0.005","priceCurrency":"EUR","product":"%(product)s","productClass":"%(productClass)s","requestId":"%(id)s","resourceId":"%(con_id)s","totalPrice":"0.150","traceId":"CPQ_customEvent_name@QASystems","type":"cs:custom-event:new"}, "topic":"%(topic)s"}'% {
                 "id": msg_id,
                 "con_id": con_id,
                 "api_key": api_key,
                 "timestamp": date,
                 "currency": currency,
                 "user_id": user_id,
                 "product": product,
                 "productClass": productClass,
                 "topic": topic}
    
    return script, msg_id

def websocket_cdr(api_key,currency,duration, topic="event_ted_websocket-call-done"):
    msg_id = str(uuid.uuid4())
    leg_id = str(uuid.uuid4())
    now = datetime.utcnow() + timedelta(days=int(0))
    start_time = now - timedelta(seconds=(int(duration)))
    date = now.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + '+0000'
    start_date = start_time.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + '+0000'
    timestamp = int(now.timestamp())
    duration = int(duration)
    script = '{"@timestamp":"%(timestamp)s","d":{"@date":"%(date)s","@timestamp":"%(timestamp)s","@version":"1.0","acc":"%(api_key)s","duration":%(duration)s,"endDate":"%(date)s","id":"%(id)s","legId":"%(leg_id)s","price":"0.0040000","priceCurrency":"%(currency)s","product":"34","productClass":"WEBSOCKET-CALL","srcIp":"","startDate":"%(start_date)s","terminationStatus":"200","terminationStatusReason":"Call answered, terminated by FS, []","totalPrice":"0.0024000","traceId":"%(id)s","type":"websocket-call:done","websocketURL":"ws://63.33.178.222:5221/socket"}, "topic":"%(topic)s"}'% {
        "id": msg_id,
        "leg_id": leg_id,
        "api_key": api_key,
        "currency": currency,
        "timestamp": timestamp,
        "start_date": start_date,
        "duration":duration,
        "date": date,
        "topic": topic}

    return script, msg_id


def asr_cdr(api_key,duration,currency, topic="event_ted_asr-done_anonymized"):
    msg_id = str(uuid.uuid4())
    asr_id = str(uuid.uuid4())
    now = datetime.utcnow() + timedelta(days=int(0))
    start_time = now - timedelta(seconds=(int(duration)))
    date = now.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + '+0000'
    start_date = start_time.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + '+0000'
    timestamp = int(now.timestamp())
    duration = int(duration)
    script = '{"@timestamp":"%(timestamp)s","to":"447425248855","d":{"@date":"%(date)s","@timestamp":"%(timestamp)s","@version":"1.0","acc":"%(api_key)s","applicationId":"","asrId":"%(asr_id)s","callId":"%(asr_id)s","callStartDate":"%(start_date)s","clientIpAddress":"","direction":"outbound","duration":%(duration)s,"endDate":"%(date)s","event":"asr-done","extCallId":"","from":"443456015450","gateway":"","id":"%(id)s","maxLength":"7200000","mixerId":"%(asr_id)s","nodeId":"ffs7.lon1.internal","parentRequestId":"%(asr_id)s","price":"0.0040000","priceCurrency":"%(currency)s","product":"25","productClass":"ASR","recordingId":"%(asr_id)s","requestId":"%(asr_id)s","ringTimeout":"60000","startDate":"%(start_date)s","status":"ok","timeoutReason":"start_timeout","to":"447425248855","totalPrice":"0.0024000","traceId":"%(asr_id)s","type":"asr:done","anonymized":"true"}, "topic":"%(topic)s"}'% {
        "id": msg_id,
        "asr_id": asr_id,
        "api_key": api_key,
        "currency": currency,
        "timestamp": timestamp,
        "start_date": start_date,
        "duration":duration,
        "date": date,
        "topic": topic}

    return script, msg_id

def reports_sync_api_cdr(api_key, currency, country, duration, topic="event_ted_reports-sync"):
    duration = int(duration)
    msg_id = str(uuid.uuid4())
    req_id = str(uuid.uuid4())
    now = datetime.utcnow() + timedelta(days=int(0))
    start_time = now - timedelta(seconds=(duration))
    end_date = now.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + '+0000'
    start_date = start_time.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + '+0000'
    timestamp = int(now.timestamp() * 1000)

    script = '{"@timestamp": "%(start_date)s", "d": { "@date": "%(start_date)s", "@timestamp": "%(timestamp)s",' \
             ' "acc": "%(api_key)s", "accountId": "%(api_key)s", "callerServiceId": "CUSTOMER_EXTERNAL", "charged": "true",' \
             ' "endpointType": "PUBLIC", "finishedAt": %(timestamp)s, "id": "%(id)s", "internal": "false", ' \
             '"itemsWritten": 1, "jobType": "SYNC_JOB_FROM_ID", "masterAccount": "%(api_key)s", "numberOfSubAccounts": "0",' \
             ' "price": "0.0000000", "priceCurrency": "%(currency)s", "product": 33, "receivedAt": %(timestamp)s, ' \
             '"reportsVersionEnum": "TWO", "requestParams": { "account_id": "%(api_key)s", "direction": "outbound",' \
             ' "id": "15000000F05763CB", "include_message": "true", "include_subaccounts": "false", "product": "SMS",' \
             ' "show_concatenated": "true" }, "requestedProduct": "SMS", "selfLink": "https://api.nexmo.com/v2/reports/' \
             'records?account_id=8c402049&product=SMS&direction=outbound&id=15000000F05763CB&show_concatenated=true&' \
             'include_message=true", "status": "SUCCESS", "totalPrice": "0.01", "traceId": "%(id)s", "tracingContext": ' \
             '{ "clientCountry": "%(country)s", "clientIpAddress": "176.248.255.120", "requestId": "%(req_id)s", "traceId": "%(id)s" },' \
             ' "type": "reports" }, "topic": "%(topic)s"}'% {
                "id": msg_id,
                "req_id": req_id,
                "api_key": api_key,
                "currency": currency,
                "timestamp": timestamp,
                "start_date": start_date,
                "end_date": end_date,
                "country": country,
                "topic": topic}
    return script, msg_id


def reports_async_api_cdr(api_key, currency, country, duration, topic="event_ted_reports-async"):
    duration = int(duration)
    msg_id = str(uuid.uuid4())
    req_id = str(uuid.uuid4())
    now = datetime.utcnow() + timedelta(days=int(0))
    start_time = now - timedelta(seconds=(duration))
    end_date = now.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + '+0000'
    start_date = start_time.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + '+0000'
    timestamp = int(now.timestamp() * 1000)
    script ='{"@timestamp": "%(start_date)s", "d": {"@date": "%(start_date)s","@timestamp": "%(timestamp)s",' \
            '"acc": "%(api_key)s","accountId": "%(api_key)s","attempts": 0,"callerServiceId": "CUSTOMER_EXTERNAL",' \
            '"charged": "true","downloadURL": "https://api.nexmo.com/v3/media/5e29bc72-67f8-4189-b9a8-ec729f85159c",' \
            '"endpointType": "PUBLIC","fileID": "5e29bc72-67f8-4189-b9a8-ec729f85159c","finishedAt": %(timestamp)s,' \
            '"id": "%(id)s","internal": "false","itemsWritten": 34,"jobType": "ASYNC_JOB","masterAccount": "%(api_key)s",' \
            '"numberOfSubAccounts": "0","price": "0.0000000","priceCurrency": "%(currency)s","product": 33,' \
            '"receivedAt": %(timestamp)s,"reportsVersion": 2,"reportsVersionEnum": "TWO","requestParams": ' \
            '{"account_id": "%(api_key)s","date_end": "%(end_date)s","date_start": "%(start_date)s","direction": "outbound",' \
            '"include_message": "false","include_subaccounts": "false","product": "SMS","show_concatenated": "false"},' \
            '"requestedProduct": "SMS","selfLink": "https://api.nexmo.com/v2/reports/ri3p58f-86206231-8bfc-4098-ad39-9593428a9cc7",' \
            '"serviceId": "reports","startedAt": %(timestamp)s,"status": "SUCCESS","totalPrice": "0.01","traceId": "%(id)s",' \
            '  "tracingContext": {"clientCountry": "%(country)s", "clientIpAddress": "1.2.3.4", "requestId": "%(req_id)s",' \
            ' "traceId": "%(id)s"},  "type": "reports"},  "topic": "%(topic)s"}'% {
                                "id": msg_id,
                                "req_id": req_id,
                                "api_key": api_key,
                                "currency": currency,
                                "timestamp": timestamp,
                                "start_date": start_date,
                                "end_date": end_date,
                                "country": country,
                                "topic": topic}
    return script, msg_id

SMS_MT_CDR_BODY = 'Test GDS MT CDRs.'
SMS_MO_CDR_BODY = 'Test GDS MO CDRs.'
CHATAPP_MO_BODY = 'QA test chatapp message'


details = 'SC:BG:359889855690'