# querySfmcDE.py

import FuelSDK as f
import time
import json
import requests
import config
import os, ssl
import argparse


def get_access_token():

    # requestToken
    token_url = "https://auth.exacttargetapis.com/v1/requestToken"
    headers = {'content-type': 'application/json'}
    token_data = {"clientId": config.clientid, "clientSecret": config.clientsecret}

    response = requests.post(token_url, json=token_data, headers=headers)

    token = json.loads(response.text)

    # print("access token =" + str(token['accessToken']))
    return str(token['accessToken'])


def get_auth_token():

    # request token
    auth_token = 'Bearer ' + get_access_token()  # Bearer Token
    # print("auth_token = " + auth_token)
    return str(auth_token)


def get_subscriberkey(EmailAddress):


    headers = {'content-type': 'application/json',
               'Authorization': get_auth_token()}
    if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
        ssl._create_default_https_context = ssl._create_unverified_context

    debug = False
    stubObj = f.ET_Client(False, debug)

    row = f.ET_DataExtension_Row()
    row.auth_stub = stubObj

    # define DE List
    # deList = list()
    # deList = ['DE_order_confirm']
    # deList = ['DE_order_confirm', 'DE_password_reset', 'DE_password_changed',
    #               'DE_pdt_print_ready', 'DE_pdt_proof_ready', 'DE_photo_share_receiver',
    #               'DE_photo_share_sender', 'DE_share_project_receiver']
    # nameOfDE = 'DE_password_reset'
    # loop over DE list

    de = 'DE_SF_USER_D'

    row.CustomerKey = str(de)

    row.props = ["USERID"]

    # set search filter
    row.search_filter = {'Property': 'CURR_EMAIL_ADDRESS',
                         'SimpleOperator': 'equals', 'Value': EmailAddress}
    getResponse = row.get()

    data = dict()
    #

    if len(getResponse.results) > 0:
        data = {
            "name": getResponse.results[0].Properties.Property[0].Name,
            "value": getResponse.results[0].Properties.Property[0].Value
        }
    else:
        data = {"Message": str(getResponse.results)}

    return data

    # print('Retrieve Status: ' + str(getResponse.status))
    # print('Code: ' + str(getResponse.code))
    # print('Message: ' + str(getResponse.message))
    # print('MoreResults: ' + str(getResponse.more_results))
    # print('RequestID: ' + str(getResponse.request_id))
    # print('Results Length: ' + str(len(getResponse.results)))
    # print('Results: ' + str(getResponse.results))


def get_de_row(EmailAddress):

    headers = {'content-type': 'application/json',
               'Authorization': get_auth_token()}
    if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
        ssl._create_default_https_context = ssl._create_unverified_context

    debug = False
    stubObj = f.ET_Client(False, debug)

    row = f.ET_DataExtension_Row()
    row.auth_stub = stubObj

    # define DE List
    de = 'SentEvent'

    row.CustomerKey = str(de)

    # get columns in the DE and append to row props

    # row.props = getDeColumns(nameOfDE)
    row.props = ["TriggeredSendCustomerKey", 'EmailAddress']

    # correlationID from method param
    # correlationID = 'a3e3227f-b8e8-40f2-b5e2-9e899147e2d1'

    SubscriberKey = get_subscriberkey(EmailAddress).get('value')

    print("SubscriberKey = %s" % SubscriberKey)

    # set search filter
    row.search_filter = {'Property': 'SubscriberKey',
                 'SimpleOperator': 'equals', 'Value': SubscriberKey}

    # start_time = time.time()

    getResponse = row.get()

    data = list()

    if len(getResponse.results) > 0:
        record_found = True

        for response in getResponse.results[0].Properties.Property:
            for property in response:
                data.append(property,)
                # https://stackoverflow.com/questions/13761054/more-pythonic-way-to-format-a-json-string-from-a-list-of-tuples
                data = '{{{}}}'.format(','.join(['{}:{}'.format(json.dumps(k), json.dumps(v)) for k, v in data]))
    else:
        data = {"Message": str(getResponse.results)}

    return data


def check():
  return {"status": "working"}



# if __name__ == '__main__':
#     correlationID = 'a3e3227f-b8e8-40f2-b5e2-9e899147e2d1'
#     get_de_row(correlationID)
