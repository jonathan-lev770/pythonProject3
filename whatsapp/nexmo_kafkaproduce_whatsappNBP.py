from kafka import KafkaProducer, KafkaConsumer
import threading
from reports_service_helper_whatsappNBP import *
import boto3
import json
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError
from time import sleep

region = 'us-east-1'
this_script_server = ['bssrating-bs1.bssva0.qa.vonagenetworks.net:9092','bssrating-bs2.bssva0.qa.vonagenetworks.net:9092']
number = '+18669010242'
consumer = KafkaConsumer(bootstrap_servers=this_script_server,
                         auto_offset_reset='earliest',
                         consumer_timeout_ms=1000, api_version=(2, 3, 0))

producer = KafkaProducer(bootstrap_servers=this_script_server, api_version=(2, 3, 0))
print(producer)
print("Starting Kafka flow")
productId_list = ["dedicated-selected-shortcode", "dedicated-random-shortcode", "single-short-code","single-voice-long-code", "single-long-code", "single-voice-tollfree-long-code","single-sms-tollfree-long-code", "single-long-code-custom", "single-long-code-custom-bulk", "eu-dedicated-random-shortcode", "single-keyword-short-code"]
#country_list = ["AD","AE","AF","AG","AI","AL","AM","AO","AR","AS","AT","AU","AW","AZ","BA","BB","BD","BE","BF","BG","BH","BI","BJ","BM","BN","BO","BR","BS","BT","BW","BY","BZ","CA","CD","CF","CG","CH","CI","CK","CL","CM","CN","CO","CR","CV","CY","CZ","DE","DJ","DK","DM","DO","DZ","EC","EE","EG","ES","ET","FI","FJ","FM","FO","FR","GA","GB","GD","GE","GH","GI","GL","GM","GN","GQ","GR","GT","GW","GY","HK","HN","HR","HT","HU","ID","IE","IL","IN","IQ","IS","IT","JM","JO","JP","KE","KG","KH","KM","KN","KR","KW","KY","KZ","LA","LB","LC","LI","LK","LR","LS","LT","LU","LV","LY","MA","MC","MD","ME","MG","MK","ML","MM","MN","MO","MQ","MR","MS","MT","MU","MV","MW","MX","MY","MZ","NA","NC","NE","NG","NI","NL","NO","NP","NR","NZ","OM","PA","PE","PF","PG","PH","PK","PL","PM","PR","PT","PW","PY","QA","RE","RO","RS","RU","RW","SA","SB","SC","SD","SE","SG","SI","SK","SL","SM","SN","SO","SR","SS","ST","SV","SZ","TC","TD","TG","TH","TJ","TL","TM","TN","TO","TR","TT","TW","TZ","UA","UG","US","UY","UZ","VC","VE","VG","VI","VN","VU","WS","XK","YE","ZA","ZM","ZW"]
deliv_list = ["whatsapp", "viber_service_msg"]
country_list = ["GB"]
api_key_list = ["JL_1.29"]
product_list = ["PRODUCT_HLR_LOOKUP_FORMAT","HLR-LOOKUP-LIGHT","HLR-LOOKUP"]
action_list = ["NEW-SUBSCRIPTION", "SUBSCRIPTION-CYCLE", "CANCEL-SUBSCRIPTION"]

cdr_list = []
error_list = []

details = 'SC:BG:359889855690'

##countries: "AD", "AF", "DE", "DJ", "GB", "PE", "SY", "US", "CW","RU","KR","KP","CD","CG","SG"
# qa servers: ['kafka4.fra2.internal:9092','kafka5.fra2.internal:9092','kafka6.fra2.internal:9092']
# dev servers: this_script_server = ['b-1.vrater-bssva0-dev.zulw9g.c6.kafka.us-east-1.amazonaws.com:9092','b-2.vrater-bssva0-dev.zulw9g.c6.kafka.us-east-1.amazonaws.com:9092']
# qa oss servers: this_script_server =  ['b-1.bssrating-bssva0-qa.racatl.c16.kafka.us-east-1.amazonaws.com:9092','b-2.bssrating-bssva0-qa.racatl.c16.kafka.us-east-1.amazonaws.com:9092']

def nexmo_flow():
    for API_KEY in api_key_list:
        for country in country_list:
            for productId in productId_list:
                for action in action_list:
                    try:
                        record, msg_id = subscription_cdr(API_KEY, details, productId, country, action)
                        msg_id = "NEXMO_" + str(msg_id)
                        print(record)
                        print("Sending " + str(productId) + " subscription record to event_subscription_subscription")

                        producer.send('event_subscription_subscription', bytes(record, 'utf-8'))
                        cdr_list.append(msg_id)
                        print("Producer record sent")
                    except Exception as e:
                        try:
                            error_list.append(msg_id)
                        except Exception as e:
                            pass
                        print(e)
                        print("ERROR sending subscription record with productId " + str(productId))

            # other CDRs
            try:
                print("SMS MT CDR -> event_connector_mt_anonymized")
                record, msg_id = sms_mt_cdr(API_KEY, number, country)
                #print(record)
                msg_id = "NEXMO_" + str(msg_id)
                producer.send('event_connector_mt_anonymized', bytes(record, 'utf-8'))
                cdr_list.append(msg_id)
                print("Producer record sent")
            except Exception as e:
                try:
                    error_list.append(msg_id)
                except Exception as e:
                    pass
                print("ERROR sending SMS Outbound Record -> event_connector_mt_anonymized")
            try:
                print("SMS MT CDR -> event_hub_core-mt_anonymized ")
                record, msg_id = sms_mt_cdr(API_KEY, number, country, productClass="", topic="event_hub_core-mt_anonymized")
                msg_id = "NEXMO_" + str(msg_id)
                producer.send('event_hub_core-mt_anonymized', bytes(record, 'utf-8'))
                cdr_list.append(msg_id)
                print("Producer record sent")
            except Exception as e:
                try:
                    error_list.append(msg_id)
                except Exception as e:
                    pass
                print("ERROR sending SMS MT CDR -> event_hub_core-mt_anonymized")

            try:
                print("SMS MT CDR -> event_connector_mt_anonymized")
                record, msg_id = sms_mt_cdr(API_KEY, number, country, productClass="verify")
                msg_id = "NEXMO_" + str(msg_id)
                producer.send('event_connector_mt_anonymized', bytes(record, 'utf-8'))
                cdr_list.append(msg_id)
                print("Producer record sent")
            except Exception as e:
                try:
                    error_list.append(msg_id)
                except Exception as e:
                    pass
                print("ERROR sending SMS Outbound Record -> event_connector_mt_anonymized")
            try:
                print("Duplicate SMS MT CDR -> event_connector_mt_anonymized")
                record, msg_id = sms_mt_cdr(API_KEY, number, country, productClass="verify")
                producer.send('event_connector_mt_anonymized', bytes(record, 'utf-8'))

                msg_id = "NEXMO_" + str(msg_id)
                producer.send('event_connector_mt_anonymized', bytes(record, 'utf-8'))
                cdr_list.append(msg_id)
                print("Producer record sent")
            except Exception as e:
                try:
                    print(e)
                    error_list.append(msg_id)
                except Exception as e:
                    pass
                print("ERROR sending SMS Outbound Record -> event_connector_mt_anonymized")

            try:
                print("SMS MT PRODUCT CLASS VERIFY CDR -> event_hub_core-mt_anonymized ")
                record, msg_id = sms_mt_cdr(API_KEY, number, country, productClass="verify", topic="event_hub_core-mt_anonymized")
                msg_id = "NEXMO_" + str(msg_id)
                producer.send('event_hub_core-mt_anonymized', bytes(record, 'utf-8'))
                cdr_list.append(msg_id)
                print("Producer record sent")
            except Exception as e:
                try:
                    error_list.append(msg_id)
                except Exception as e:
                    pass
                print("ERROR sending SMS MT PRODUCT CLASS VERIFY CDR -> event_hub_core-mt_anonymized")


            try:
                print("SMS MO CDR")
                record, msg_id = sms_mo_cdr(API_KEY, number, country)
                #print(record)
                msg_id = "NEXMO_" + str(msg_id)
                producer.send('event_hub_all-mo_anonymized', bytes(record, 'utf-8'))
                cdr_list.append(msg_id)
                print("Producer record sent")
            except Exception as e:
                try:
                    error_list.append(msg_id)
                except Exception as e:
                    pass
                print("ERROR sending SMS Inbound CDR")

            try:
                print("Verify Request CDR 0")
                record, msg_id = verify_cdr(API_KEY, number, country, "0")
                msg_id = "NEXMO_" + str(msg_id)
                producer.send('event_verify_verify_anonymized', bytes(record, 'utf-8'))
                cdr_list.append(msg_id)
                print("Producer record sent")
            except Exception as e:
                try:
                    error_list.append(msg_id)
                except Exception as e:
                    pass
                print("ERROR sending Verify CDR 0")

            try:
                print("Verify Request CDR 1")
                record, msg_id = verify_cdr(API_KEY, number, country, "1")
                msg_id = "NEXMO_" + str(msg_id)
                producer.send('event_verify_verify_anonymized', bytes(record, 'utf-8'))
                cdr_list.append(msg_id)
                print("Producer record sent")
            except Exception as e:
                try:
                    error_list.append(msg_id)
                except Exception as e:
                    pass
                print("ERROR sending Verify CDR 1")

            try:
                print("Verify Conversion record")
                record, msg_id = verify_cdr(API_KEY, number, country, "2")
                msg_id = "NEXMO_" + str(msg_id)
                producer.send('event_verify_verify_anonymized', bytes(record, 'utf-8'))
                cdr_list.append(msg_id)
                print("Producer record sent - TTS record -> TTS record -> event_tts_call_anonymized")
            except Exception as e:
                try:
                    error_list.append(msg_id)
                except Exception as e:
                    pass
                print("ERROR sending Verify Conversion CDR")
            for product in product_list:
                lookupType_list = ["carrier,type,valid,ported,reachable,roaming,subscriber","carrier,type,valid,ported,reachable,roaming,subscriber,cnam"]
                for lookupType in lookupType_list:
                    try:
                        print("HLR CDR")
                        record, msg_id = hlr_cdr(API_KEY, product, number, country, lookupType)
                        msg_id = "NEXMO_" + str(msg_id)
                        producer.send('event_hlr_requests_anonymized', bytes(record, 'utf-8'))
                        cdr_list.append(msg_id)
                        print("Producer record sent")
                    except Exception as e:
                        print(e)
                        try:
                            error_list.append(msg_id)
                        except Exception as e:
                            print(e)
                            pass
                        print("ERROR sending HLR (Number Insight) CDR")

            oa = "1497055241"
            msgType = "viber_service_msg"
            try:
                print("Chatapp MO " + str(msgType))
                record, msg_id = chatapp_mo(API_KEY, oa, country, "delivered", msgType)
                msg_id = "NEXMO_" + str(msg_id) + "_delivered"
                producer.send('event_chatapp_mo_anonymized' , bytes(record, 'utf-8'))
                cdr_list.append(msg_id)
                print("Producer record sent")
            except Exception as e:
                try:
                    error_list.append(msg_id)
                except Exception as e:
                    pass
                print("ERROR sending standard Chatapp inbound type " + str(msgType))

            try:
                print("Chatapp MT " + str(msgType))
                record, msg_id = chatapp_mt(API_KEY, oa, country, "delivered", msgType)
                msg_id = "NEXMO_" + str(msg_id) + "_delivered"
                producer.send('event_chatapp_dr_anonymized', bytes(record, 'utf-8'))
                cdr_list.append(msg_id)
                print("Producer record sent")
            except Exception as e:
                try:
                    error_list.append(msg_id)
                except Exception as e:
                    pass
                print("ERROR sending standard Chatapp outbound type " + str(msgType))
            oa = "1497055241"
            msgType = "whatsapp"
            aggregateId = API_KEY
            print(aggregateId)
            try:
                print("Chatapp MO " + str(msgType))
                #chatapp_mo(api_key, oa, country, status, msgType,  z_date=False, aggregateId=''):
                record, msg_id = chatapp_mo(API_KEY, oa, country, "delivered", msgType, False, aggregateId)
                print(record)
                wa_fee_msg_id = "NEXMO_" + str(msg_id) + "_delivered_whatsapp_whatsapp_fee"
                vfee_msg_id = "NEXMO_" + str(msg_id) + "_delivered_whatsapp_vonage_fee"
                producer.send('event_chatapp_mo_anonymized' , bytes(record, 'utf-8'))
                cdr_list.append(wa_fee_msg_id)
                cdr_list.append(vfee_msg_id)
                print("Producer record sent")
            except Exception as e:
                print(e)
                try:
                    error_list.append(msg_id)
                except Exception as e:
                    pass
                print("ERROR sending standard Chatapp inbound type " + str(msgType))

            try:
                print("Chatapp MT " + str(msgType))
                #chatapp_mt(api_key, oa, country, status, msgType, z_date=False, aggregateId='')
                record, msg_id = chatapp_mt(API_KEY, oa, country, "delivered", msgType, False, aggregateId)
                print(record)
                wa_fee_msg_id = "NEXMO_" + str(msg_id) + "_delivered_whatsapp_whatsapp_fee"
                vfee_msg_id = "NEXMO_" + str(msg_id) + "_delivered_whatsapp_vonage_fee"
                producer.send('event_chatapp_dr_anonymized', bytes(record, 'utf-8'))
                cdr_list.append(wa_fee_msg_id)
                cdr_list.append(vfee_msg_id)
                print("Producer record sent")
            except Exception as e:
                print(e)
                try:
                    error_list.append(msg_id)
                except Exception as e:
                    pass
                print("ERROR sending standard Chatapp outbound type " + str(msgType))

            msgType = "mms"
            try:
                print("Chatapp MO " + str(msgType))
                record, msg_id = chatapp_mo(API_KEY, oa, country, "submitted", msgType)
                msg_id = "NEXMO_" + str(msg_id) + "_submitted"
                producer.send('event_chatapp_mo_anonymized', bytes(record, 'utf-8'))
                cdr_list.append(msg_id)
                print("Producer record sent")
            except Exception as e:
                try:
                    error_list.append(msg_id)
                except Exception as e:
                    pass
                print("ERROR sending standard Chatapp inbound type " + str(msgType))

            try:
                print("Chatapp MT " + str(msgType))
                record, msg_id = chatapp_mt(API_KEY, oa, country, "submitted", msgType)
                msg_id = "NEXMO_" + str(msg_id) + "_submitted"
                producer.send('event_chatapp_dr_anonymized', bytes(record, 'utf-8'))
                cdr_list.append(msg_id)
                print("Producer record sent")
            except Exception as e:
                try:
                    error_list.append(msg_id)
                except Exception as e:
                    pass
                print("ERROR sending standard Chatapp outbound type " + str(msgType))

            oa = "1497055241"
            msgType = "viber_service_msg"
            try:
                print("Chatapp MO " + str(msgType))
                record, msg_id = chatapp_mo(API_KEY, oa, country, "delivered", msgType, True)
                msg_id = "NEXMO_" + str(msg_id) + "_delivered"
                producer.send('event_chatapp_mo_anonymized' , bytes(record, 'utf-8'))
                cdr_list.append(msg_id)
                print("Producer record sent")
            except Exception as e:
                try:
                    error_list.append(msg_id)
                except Exception as e:
                    pass
                print("ERROR sending standard Chatapp inbound type " + str(msgType))

            try:
                print("Chatapp MT " + str(msgType))
                record, msg_id = chatapp_mt(API_KEY, oa, country, "delivered", msgType, True)
                msg_id = "NEXMO_" + str(msg_id) + "_delivered"
                producer.send('event_chatapp_dr_anonymized', bytes(record, 'utf-8'))
                cdr_list.append(msg_id)
                print("Producer record sent")
            except Exception as e:
                try:
                    error_list.append(msg_id)
                except Exception as e:
                    pass
                print("ERROR sending standard Chatapp outbound type " + str(msgType))
            oa = "1497055241"
            msgType = "whatsapp"
            aggregateId = API_KEY
            try:
                print("Chatapp MO " + str(msgType))
                record, msg_id = chatapp_mo(API_KEY, oa, country, "delivered", msgType, True, aggregateId)
                wa_fee_msg_id = "NEXMO_" + str(msg_id) + "_delivered_whatsapp_whatsapp_fee"
                vfee_msg_id = "NEXMO_" + str(msg_id) + "_delivered_whatsapp_vonage_fee"
                producer.send('event_chatapp_mo_anonymized' , bytes(record, 'utf-8'))
                cdr_list.append(wa_fee_msg_id)
                cdr_list.append(vfee_msg_id)
                print("Producer record sent")
            except Exception as e:
                print(e)
                try:
                    error_list.append(msg_id)
                except Exception as e:
                    pass
                print("ERROR sending standard Chatapp inbound type " + str(msgType))

            try:
                print("Chatapp MT " + str(msgType))
                record, msg_id = chatapp_mt(API_KEY, oa, country, "delivered", msgType, True, aggregateId)
                wa_fee_msg_id = "NEXMO_" + str(msg_id) + "_delivered_whatsapp_whatsapp_fee"
                vfee_msg_id = "NEXMO_" + str(msg_id) + "_delivered_whatsapp_vonage_fee"
                producer.send('event_chatapp_dr_anonymized', bytes(record, 'utf-8'))
                cdr_list.append(wa_fee_msg_id)
                cdr_list.append(vfee_msg_id)
                print("Producer record sent")
            except Exception as e:
                print(e)
                try:
                    error_list.append(msg_id)
                except Exception as e:
                    pass
                print("ERROR sending standard Chatapp outbound type " + str(msgType))

            msgType = "mms"
            try:
                print("Chatapp MO " + str(msgType))
                record, msg_id = chatapp_mo(API_KEY, oa, country, "submitted", msgType, True)
                msg_id = "NEXMO_" + str(msg_id) + "_submitted"
                producer.send('event_chatapp_mo_anonymized', bytes(record, 'utf-8'))
                cdr_list.append(msg_id)
                print("Producer record sent")
            except Exception as e:
                try:
                    error_list.append(msg_id)
                except Exception as e:
                    pass
                print("ERROR sending standard Chatapp inbound type " + str(msgType))

            try:
                print("Chatapp MT " + str(msgType))
                record, msg_id = chatapp_mt(API_KEY, oa, country, "submitted", msgType, True)
                msg_id = "NEXMO_" + str(msg_id) + "_submitted"
                producer.send('event_chatapp_dr_anonymized', bytes(record, 'utf-8'))
                cdr_list.append(msg_id)
                print("Producer record sent")
            except Exception as e:
                try:
                    error_list.append(msg_id)
                except Exception as e:
                    pass
                print("ERROR sending standard Chatapp outbound type " + str(msgType))

            try:
                print("Final connector states record")
                record, msg_id = final_connector(API_KEY, country)
                msg_id = "NEXMO_" + str(msg_id)
                producer.send('event_connector_final-states_anonymized', bytes(record, 'utf-8'))
                cdr_list.append(msg_id)
                print("Producer record sent")
            except Exception as e:
                try:
                    error_list.append(msg_id)
                except Exception as e:
                    pass
                print("ERROR sending Final Connector States record")

            try:
                print("Sip inbound record")
                record, msg_id = sip_inbound(API_KEY, country)
                msg_id = "NEXMO_" + str(msg_id)
                print(record)
                producer.send('event_sip_inbound_anonymized', bytes(record, 'utf-8'))
                cdr_list.append(msg_id)
                print("Producer record sent")
            except Exception as e:
                try:
                    error_list.append(msg_id)
                except Exception as e:
                    pass
                print("ERROR sending SIP Inbound Record")

            try:
                print("Sip outbound record -> event_sip_outbound_anonymized")
                record, msg_id = sip_outbound(API_KEY, country)
                msg_id = "NEXMO_" + str(msg_id)
                print(record)
                producer.send('event_sip_outbound_anonymized', bytes(record, 'utf-8'))
                cdr_list.append(msg_id)
                print("Producer record sent -> Sip outbound record -> event_sip_outbound_anonymized")
            except Exception as e:
                try:
                    error_list.append(msg_id)
                except Exception as e:
                    pass
                print("ERROR sending SIP Outbound Record")

            try:
                print("Sip outbound verify record -> event_sip_outbound_anonymized")
                record, msg_id = sip_outbound(API_KEY, country, productClass="verify")
                msg_id = "NEXMO_" + str(msg_id)
                print(record)
                producer.send('event_sip_outbound_anonymized', bytes(record, 'utf-8'))
                cdr_list.append(msg_id)
                print("Producer record sent -> Sip outbound record -> event_sip_outbound_anonymized")
            except Exception as e:
                try:
                    error_list.append(msg_id)
                except Exception as e:
                    pass
                print("ERROR sending SIP Outbound Record")

            try:
                print("TTS record -> event_tts_call_anonymized")
                record, msg_id = voice_cdr(API_KEY, number, country)
                msg_id = "NEXMO_" + str(msg_id)
                producer.send('event_tts_call_anonymized', bytes(record, 'utf-8'))
                cdr_list.append(msg_id)
                print("Producer record sent - TTS record -> TTS record -> event_tts_call_anonymized")
            except Exception as e:
                try:
                    error_list.append(msg_id)
                except Exception as e:
                    pass
                print("ERROR sending TTS record -> TTS record -> event_tts_call_anonymized")

            try:
                print("TTS record verify -> event_tts_call_anonymized")
                record, msg_id = voice_cdr(API_KEY, number, country, productClass="verify")
                msg_id = "NEXMO_" + str(msg_id)
                producer.send('event_tts_call_anonymized', bytes(record, 'utf-8'))
                cdr_list.append(msg_id)
                print("Producer record sent - TTS record -> TTS record -> event_tts_call_anonymized")
            except Exception as e:
                try:
                    error_list.append(msg_id)
                except Exception as e:
                    pass
                print("ERROR sending TTS record -> TTS record -> event_tts_call_anonymized")
            for productClass in ["api","sip","psip"]:
                try:
                    print("Outbound voice cdr: " + str(productClass))
                    record, msg_id = outbound_voice_cdr(API_KEY, number, country, productClass=productClass)
                    msg_id = "NEXMO_" + str(msg_id)
                    print(record)
                    producer.send('event_sip_outbound_anonymized', bytes(record, 'utf-8'))
                    cdr_list.append(msg_id)
                    print("Outbound voice cdr: " + str(productClass) + " -> event_sip_outbound_anonymized")
                except Exception as e:
                    try:
                        error_list.append(msg_id)
                    except Exception as e:
                        pass
                    print("ERROR sending voice cdr: " + str(productClass) + " -> event_sip_outbound_anonymized")

                try:
                    print("Inbound voice cdr: " + str(productClass))
                    record, msg_id = inbound_voice_cdr(API_KEY, number, country, productClass=productClass)
                    msg_id = "NEXMO_" + str(msg_id)
                    print(record)
                    producer.send('event_sip_inbound_anonymized', bytes(record, 'utf-8'))
                    cdr_list.append(msg_id)
                    print("Inbound voice cdr: " + str(productClass) + " -> event_sip_inbound_anonymized")
                except Exception as e:
                    try:
                        error_list.append(msg_id)
                    except Exception as e:
                        pass
                    print("ERROR sending voice cdr: " + str(productClass) + " -> event_sip_inbound_anonymized")
            try:
                print("IP Leg Record to event_ted_ip-audio-end_anonymized")
                record, msg_id = ipLegCall_cdr(API_KEY,"EUR","event_ted_ip-audio-end_anonymized")
                msg_id = "NEXMO_" + str(msg_id)
                producer.send('event_ted_ip-audio-end_anonymized', bytes(record, 'utf-8'))
                cdr_list.append(msg_id)
                print("Producer record sent IP Leg Record to event_ted_ip-audio-end_anonymized")
            except Exception as e:
                print(e)
                try:
                    error_list.append(msg_id)
                except Exception as e:
                    pass
                print("ERROR sending IP Leg Record to event_ted_ip-audio-end_anonymized")

            try:
                print("IP Leg Record to event_ted_ip-messaging-new")
                record, msg_id = ipLegMsg_cdr(API_KEY,"EUR","event_ted_ip-messaging-new")
                msg_id = "NEXMO_" + str(msg_id)
                producer.send('event_ted_ip-messaging-new', bytes(record, 'utf-8'))
                cdr_list.append(msg_id)
                print("Producer record sent IP Leg Record to event_ted_ip-messaging-new")
            except Exception as e:
                print(e)
                try:
                    error_list.append(msg_id)
                except Exception as e:
                    pass
                print("ERROR sending IP Leg Record to event_ted_ip-messaging-new")
            try:
                 print("Custom Event Record to event_ted_cs-custom-event-new")
                 record, msg_id = custom_event_cdr(API_KEY, 29, "stitch","EUR")
                 msg_id = "NEXMO_" + str(msg_id)
                 producer.send('event_ted_cs-custom-event-new', bytes(record, 'utf-8'))
                 cdr_list.append(msg_id)
                 print("Producer record sent Custom Event Record to event_ted_cs-custom-event-new")
            except Exception as e:
                 try:
                     error_list.append(msg_id)
                 except Exception as e:
                     pass
                 print("ERROR sending Custom Event Record to event_ted_cs-custom-event-new")
            try:
                 print("Websocket Record to event_ted_websocket-call-done")
                 record, msg_id = websocket_cdr(API_KEY,"EUR",30)
                 msg_id = "NEXMO_" + str(msg_id)
                 producer.send('event_ted_websocket-call-done', bytes(record, 'utf-8'))
                 cdr_list.append(msg_id)
                 print("Producer record sent Websocket Record to event_ted_websocket-call-done")
            except Exception as e:
                 try:
                     error_list.append(msg_id)
                 except Exception as e:
                     pass
                 print("ERROR sending Websocket Record to event_ted_websocket-call-done")
            try:
                 print("ASR Record to event_ted_asr-done_anonymized")
                 record, msg_id = asr_cdr(API_KEY,30,"EUR")
                 msg_id = "NEXMO_" + str(msg_id)
                 producer.send('event_ted_asr-done_anonymized', bytes(record, 'utf-8'))
                 cdr_list.append(msg_id)
                 print("Producer record sent ASR Record to event_ted_asr-done_anonymized")
            except Exception as e:
                 try:
                     error_list.append(msg_id)
                 except Exception as e:
                     pass
                 print("ERROR sending ASR Record to event_ted_asr-done_anonymized")
            try:
                print("Reports Sync CDR to event_ted_reports-sync")
                record, msg_id = reports_sync_api_cdr(API_KEY, "EUR", country, 2)
                print(record)
                msg_id = "NEXMO_" + str(msg_id)
                producer.send('event_ted_reports-sync', bytes(record, 'utf-8'))
                cdr_list.append(msg_id)
                print("Producer record sent Reports Sync CDR to event_ted_reports-sync")
            except Exception as e:
                print(e)
                try:
                    error_list.append(msg_id)
                except Exception as e:
                    print("ERROR!")
                    print(e)
                    pass
                print("ERROR sending Reports Sync CDR to event_ted_reports-sync")

            try:
                print("Reports Async CDR to event_ted_reports-async")
                record, msg_id = reports_async_api_cdr(API_KEY, "EUR", country, 2)
                print(record)
                msg_id = "NEXMO_" + str(msg_id)
                producer.send('event_ted_reports-async', bytes(record, 'utf-8'))
                cdr_list.append(msg_id)
                print("Producer record sent Reports Async CDR to event_ted_reports-async")
            except Exception as e:
                print(e)
                try:
                    error_list.append(msg_id)
                except Exception as e:
                    print("ERROR!")
                    print(e)
                    pass
                print("ERROR sending Reports Async CDR to event_ted_reports-async")

    producer.flush()
    print("Producer flushed")


Threads = []

for i in range(1):
    Thread = threading.Thread(target=nexmo_flow)
    Threads.append(Thread)
    Thread.start()
for Thread in Threads:
    Thread.join()

producer.close()
print("Producer closed")

print(cdr_list)

def dynamo_query(table, key, value, region, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name=region)
    table = dynamodb.Table(table)
    try:
        response = table.query(
            KeyConditionExpression=Key(key).eq(value)
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Items']

def dynamo_verification(cdr_list, region):
    for cid in cdr_list:
        print(cid)
        try:
            items = dynamo_query("vusage-qa6-usage-history", "originId", cid, region)
            for v in items:
                agg_key = v['aggregateKey']
                print(agg_key)
                agg_values = v['aggregatedValues']
                cdr = json.loads(v['cdr'])
                #print(cdr)
                try:
                    ratingFilters = cdr["ratedCdrs"][0]["costDetails"]["ratingFilters"]
                    rates=cdr["ratedCdrs"][0]["costDetails"]["rates"]
                    filters = [ratingFilters[k] for k in iter(ratingFilters)]
                    for r in filters:
                        rpid = r["RatingPlanID"]
                    units = [rates[u] for u in iter(rates)]
                except Exception as e:
                        print("Error parsing ratedCdrs field:")
                        print(e)

                price = agg_values["amount"]
                rated_price = agg_values["ratedPrice"]
                orig_price = agg_values["originalPrice"]
                cost = agg_values["cost"]

                frmt_price = "{}".format(price)
                frmt_rp = "{}".format(rated_price)
                frmt_op = "{}".format(orig_price)
                frmt_cost = "{}".format(cost)


                print("Price: " + str(frmt_price))
                print("Rated price: " + str(frmt_rp))
                print("Original price: " + str(frmt_op))
                print("Cost: " + str(frmt_cost))
        except Exception as e:
            print(e)
            print("ERROR during Dynamo verification of cdr " + str(cid) + "!!")
print("Beginning 5 minute wait...")
sleep(300)
print("Beginning verification...")
dynamo_verification(cdr_list, region)