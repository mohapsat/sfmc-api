from flask import Flask
from flask_restful import Resource, Api
import FuelSDK as f
import os
import ssl
import config
import json
import requests


app = Flask(__name__)
api = Api(app)


class sfmc(Resource):

    def get(self, emailType, correlationId):

        # requestToken
        token_url = "https://auth.exacttargetapis.com/v1/requestToken"
        headers = {'content-type': 'application/json'}
        token_data = {"clientId": config.clientid, "clientSecret": config.clientsecret}

        response = requests.post(token_url, json=token_data, headers=headers)

        token = json.loads(response.text)

        # print("access token =" + str(token['accessToken']))
        access_token = str(token['accessToken'])

        # request token
        auth_token = 'Bearer ' + access_token  # Bearer Token
        # print("auth_token = " + auth_token)

        # SSL context verification

        if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
            ssl._create_default_https_context = ssl._create_unverified_context

        debug = False
        stubObj = f.ET_Client(False, debug)

        if emailType.lower() == 'password_reset':

            row = f.ET_DataExtension_Row()
            row.auth_stub = stubObj

            nameOfDE = emailType.lower()
            row.CustomerKey = nameOfDE

            # TODO: get columns in the DE and append to row props
            # row.props = getDeColumns(nameOfDE)
            row.props = ["correlationId", 'EmailAddress', 'SubscriberKey',
                         'emailType', 'uid']

            # correlationId = 'PASS_RESET_TEST_001'

            # set search filter
            row.search_filter = {'Property': 'correlationId',
                                 'SimpleOperator': 'equals', 'Value': correlationId}

            getResponse = row.get()

            data = list()
            data_dict = {}

            records_found = len(getResponse.results)

            if records_found > 0:

                results = getResponse.results
                for i, j in enumerate(results):
                    # print("%s-%s"%(i,j))
                    for p, q in enumerate(j.Properties.Property):
                        # print(("%s-%s-%s"%(i,p,q)))
                        print("{\"name\": %s, \"value\": %s}" % (q.Name, q.Value))
                        data_dict.update({"name": q.Name, "value": q.Value})
                        data.append(data_dict.copy())

                response = {"status": 'success',
                            "message": 'Search results returned by Salesforce',
                            "data": data}

            else:

                data = []

                response = {"status": 'success',
                            "message": 'No records found',
                            "data": data}

            pass

        elif emailType.lower() == 'order_confirm':

            row = f.ET_DataExtension_Row()
            row.auth_stub = stubObj

            nameOfDE = emailType.lower()
            row.CustomerKey = nameOfDE

            # TODO: get columns in the DE and append to row props
            # row.props = getDeColumns(nameOfDE)
            row.props = ["correlationId", 'EmailAddress', 'SubscriberKey',
                         'emailType', 'uid']

            # correlationId = 'PASS_RESET_TEST_001'

            # set search filter
            row.search_filter = {'Property': 'correlationId',
                                 'SimpleOperator': 'equals', 'Value': correlationId}

            getResponse = row.get()

            data = list()
            data_dict = {}

            records_found = len(getResponse.results)

            if records_found > 0:

                results = getResponse.results
                for i, j in enumerate(results):
                    # print("%s-%s"%(i,j))
                    for p, q in enumerate(j.Properties.Property):
                        # print(("%s-%s-%s"%(i,p,q)))
                        print("{\"name\": %s, \"value\": %s}" % (q.Name, q.Value))
                        data_dict.update({"name": q.Name, "value": q.Value})
                        data.append(data_dict.copy())

                response = {"status": 'success',
                            "message": 'Search results returned by Salesforce',
                            "data": data}

            else:

                data = []

                response = {"status": 'success',
                            "message": 'No records found',
                            "data": data}

            pass

        elif emailType.lower() == 'password_changed':

            row = f.ET_DataExtension_Row()
            row.auth_stub = stubObj

            nameOfDE = emailType.lower()
            row.CustomerKey = nameOfDE

            # TODO: get columns in the DE and append to row props
            # row.props = getDeColumns(nameOfDE)
            row.props = ["correlationId", 'EmailAddress', 'SubscriberKey',
                         'emailType', 'uid']

            # correlationId = 'PASS_RESET_TEST_001'

            # set search filter
            row.search_filter = {'Property': 'correlationId',
                                 'SimpleOperator': 'equals', 'Value': correlationId}

            getResponse = row.get()

            data = list()
            data_dict = {}

            records_found = len(getResponse.results)

            if records_found > 0:

                results = getResponse.results
                for i, j in enumerate(results):
                    # print("%s-%s"%(i,j))
                    for p, q in enumerate(j.Properties.Property):
                        # print(("%s-%s-%s"%(i,p,q)))
                        print("{\"name\": %s, \"value\": %s}" % (q.Name, q.Value))
                        data_dict.update({"name": q.Name, "value": q.Value})
                        data.append(data_dict.copy())

                response = {"status": 'success',
                            "message": 'Search results returned by Salesforce',
                            "data": data}

            else:

                data = []

                response = {"status": 'success',
                            "message": 'No records found',
                            "data": data}

            pass

        elif emailType.lower() == 'pdt_print_ready':

            row = f.ET_DataExtension_Row()
            row.auth_stub = stubObj

            nameOfDE = emailType.lower()
            row.CustomerKey = nameOfDE

            # TODO: get columns in the DE and append to row props
            # row.props = getDeColumns(nameOfDE)
            row.props = ["correlationId", 'EmailAddress', 'SubscriberKey',
                         'emailType', 'uid']

            # correlationId = 'PASS_RESET_TEST_001'

            # set search filter
            row.search_filter = {'Property': 'correlationId',
                                 'SimpleOperator': 'equals', 'Value': correlationId}

            getResponse = row.get()

            data = list()
            data_dict = {}

            records_found = len(getResponse.results)

            if records_found > 0:

                results = getResponse.results
                for i, j in enumerate(results):
                    # print("%s-%s"%(i,j))
                    for p, q in enumerate(j.Properties.Property):
                        # print(("%s-%s-%s"%(i,p,q)))
                        print("{\"name\": %s, \"value\": %s}" % (q.Name, q.Value))
                        data_dict.update({"name": q.Name, "value": q.Value})
                        data.append(data_dict.copy())

                response = {"status": 'success',
                            "message": 'Search results returned by Salesforce',
                            "data": data}

            else:

                data = []

                response = {"status": 'success',
                            "message": 'No records found',
                            "data": data}

            pass

        elif emailType.lower() == 'pdt_proof_ready':

            row = f.ET_DataExtension_Row()
            row.auth_stub = stubObj

            nameOfDE = emailType.lower()
            row.CustomerKey = nameOfDE

            # TODO: get columns in the DE and append to row props
            # row.props = getDeColumns(nameOfDE)
            row.props = ["correlationId", 'EmailAddress', 'SubscriberKey',
                         'emailType', 'uid']

            # correlationId = 'PASS_RESET_TEST_001'

            # set search filter
            row.search_filter = {'Property': 'correlationId',
                                 'SimpleOperator': 'equals', 'Value': correlationId}

            getResponse = row.get()

            data = list()
            data_dict = {}

            records_found = len(getResponse.results)

            if records_found > 0:

                results = getResponse.results
                for i, j in enumerate(results):
                    # print("%s-%s"%(i,j))
                    for p, q in enumerate(j.Properties.Property):
                        # print(("%s-%s-%s"%(i,p,q)))
                        print("{\"name\": %s, \"value\": %s}" % (q.Name, q.Value))
                        data_dict.update({"name": q.Name, "value": q.Value})
                        data.append(data_dict.copy())

                response = {"status": 'success',
                            "message": 'Search results returned by Salesforce',
                            "data": data}

            else:

                data = []

                response = {"status": 'success',
                            "message": 'No records found',
                            "data": data}

            pass

        elif emailType.lower() == 'photo_share_receiver':

            row = f.ET_DataExtension_Row()
            row.auth_stub = stubObj

            nameOfDE = emailType.lower()
            row.CustomerKey = nameOfDE

            # TODO: get columns in the DE and append to row props
            # row.props = getDeColumns(nameOfDE)
            row.props = ["correlationId", 'EmailAddress', 'SubscriberKey',
                         'emailType', 'uid']

            # correlationId = 'PASS_RESET_TEST_001'

            # set search filter
            row.search_filter = {'Property': 'correlationId',
                                 'SimpleOperator': 'equals', 'Value': correlationId}

            getResponse = row.get()

            data = list()
            data_dict = {}

            records_found = len(getResponse.results)

            if records_found > 0:

                results = getResponse.results
                for i, j in enumerate(results):
                    # print("%s-%s"%(i,j))
                    for p, q in enumerate(j.Properties.Property):
                        # print(("%s-%s-%s"%(i,p,q)))
                        print("{\"name\": %s, \"value\": %s}" % (q.Name, q.Value))
                        data_dict.update({"name": q.Name, "value": q.Value})
                        data.append(data_dict.copy())

                response = {"status": 'success',
                            "message": 'Search results returned by Salesforce',
                            "data": data}

            else:

                data = []

                response = {"status": 'success',
                            "message": 'No records found',
                            "data": data}

            pass


        elif emailType.lower() == 'photo_share_sender':

            row = f.ET_DataExtension_Row()
            row.auth_stub = stubObj

            nameOfDE = emailType.lower()
            row.CustomerKey = nameOfDE

            # TODO: get columns in the DE and append to row props
            # row.props = getDeColumns(nameOfDE)
            row.props = ["correlationId", 'EmailAddress', 'SubscriberKey',
                         'emailType', 'uid']

            # correlationId = 'PASS_RESET_TEST_001'

            # set search filter
            row.search_filter = {'Property': 'correlationId',
                                 'SimpleOperator': 'equals', 'Value': correlationId}

            getResponse = row.get()

            data = list()
            data_dict = {}

            records_found = len(getResponse.results)

            if records_found > 0:

                results = getResponse.results
                for i, j in enumerate(results):
                    # print("%s-%s"%(i,j))
                    for p, q in enumerate(j.Properties.Property):
                        # print(("%s-%s-%s"%(i,p,q)))
                        print("{\"name\": %s, \"value\": %s}" % (q.Name, q.Value))
                        data_dict.update({"name": q.Name, "value": q.Value})
                        data.append(data_dict.copy())

                response = {"status": 'success',
                            "message": 'Search results returned by Salesforce',
                            "data": data}

            else:

                data = []

                response = {"status": 'success',
                            "message": 'No records found',
                            "data": data}

            pass

        elif emailType.lower() == 'share_project_receiver':

            row = f.ET_DataExtension_Row()
            row.auth_stub = stubObj

            nameOfDE = emailType.lower()
            row.CustomerKey = nameOfDE

            # TODO: get columns in the DE and append to row props
            # row.props = getDeColumns(nameOfDE)
            row.props = ["correlationId", 'EmailAddress', 'SubscriberKey',
                         'emailType', 'uid']

            # correlationId = 'PASS_RESET_TEST_001'

            # set search filter
            row.search_filter = {'Property': 'correlationId',
                                 'SimpleOperator': 'equals', 'Value': correlationId}

            getResponse = row.get()

            data = list()
            data_dict = {}

            records_found = len(getResponse.results)

            if records_found > 0:

                results = getResponse.results
                for i, j in enumerate(results):
                    # print("%s-%s"%(i,j))
                    for p, q in enumerate(j.Properties.Property):
                        # print(("%s-%s-%s"%(i,p,q)))
                        print("{\"name\": %s, \"value\": %s}" % (q.Name, q.Value))
                        data_dict.update({"name": q.Name, "value": q.Value})
                        data.append(data_dict.copy())

                response = {"status": 'success',
                            "message": 'Search results returned by Salesforce',
                            "data": data}

            else:

                data = []

                response = {"status": 'success',
                            "message": 'No records found',
                            "data": data}

            pass

        elif emailType.lower() == 'share_project_sender':

            row = f.ET_DataExtension_Row()
            row.auth_stub = stubObj

            nameOfDE = emailType.lower()
            row.CustomerKey = nameOfDE

            # TODO: get columns in the DE and append to row props
            # row.props = getDeColumns(nameOfDE)
            row.props = ["correlationId", 'EmailAddress', 'SubscriberKey',
                         'emailType', 'uid']

            # correlationId = 'PASS_RESET_TEST_001'

            # set search filter
            row.search_filter = {'Property': 'correlationId',
                                 'SimpleOperator': 'equals', 'Value': correlationId}

            getResponse = row.get()

            data = list()
            data_dict = {}

            records_found = len(getResponse.results)

            if records_found > 0:

                results = getResponse.results
                for i, j in enumerate(results):
                    # print("%s-%s"%(i,j))
                    for p, q in enumerate(j.Properties.Property):
                        # print(("%s-%s-%s"%(i,p,q)))
                        print("{\"name\": %s, \"value\": %s}" % (q.Name, q.Value))
                        data_dict.update({"name": q.Name, "value": q.Value})
                        data.append(data_dict.copy())

                response = {"status": 'success',
                            "message": 'Search results returned by Salesforce',
                            "data": data}

            else:

                data = []

                response = {"status": 'success',
                            "message": 'No records found',
                            "data": data}

            pass

        elif emailType.lower() == 'ship_confirm':

            row = f.ET_DataExtension_Row()
            row.auth_stub = stubObj

            nameOfDE = emailType.lower()
            row.CustomerKey = nameOfDE

            # TODO: get columns in the DE and append to row props
            # row.props = getDeColumns(nameOfDE)
            row.props = ["correlationId", 'EmailAddress', 'SubscriberKey',
                         'emailType', 'uid']

            # correlationId = 'PASS_RESET_TEST_001'

            # set search filter
            row.search_filter = {'Property': 'correlationId',
                                 'SimpleOperator': 'equals', 'Value': correlationId}

            getResponse = row.get()

            data = list()
            data_dict = {}

            records_found = len(getResponse.results)

            if records_found > 0:

                results = getResponse.results
                for i, j in enumerate(results):
                    # print("%s-%s"%(i,j))
                    for p, q in enumerate(j.Properties.Property):
                        # print(("%s-%s-%s"%(i,p,q)))
                        print("{\"name\": %s, \"value\": %s}" % (q.Name, q.Value))
                        data_dict.update({"name": q.Name, "value": q.Value})
                        data.append(data_dict.copy())

                response = {"status": 'success',
                            "message": 'Search results returned by Salesforce',
                            "data": data}

            else:

                data = []

                response = {"status": 'success',
                            "message": 'No records found',
                            "data": data}

            pass

        elif emailType.lower() == 'welcome':

            row = f.ET_DataExtension_Row()
            row.auth_stub = stubObj

            nameOfDE = emailType.lower()
            row.CustomerKey = nameOfDE

            # TODO: get columns in the DE and append to row props
            # row.props = getDeColumns(nameOfDE)
            row.props = ["correlationId", 'EmailAddress', 'SubscriberKey',
                         'emailType', 'uid']

            # correlationId = 'PASS_RESET_TEST_001'

            # set search filter
            row.search_filter = {'Property': 'correlationId',
                                 'SimpleOperator': 'equals', 'Value': correlationId}

            getResponse = row.get()

            data = list()
            data_dict = {}

            records_found = len(getResponse.results)

            if records_found > 0:

                results = getResponse.results
                for i, j in enumerate(results):
                    # print("%s-%s"%(i,j))
                    for p, q in enumerate(j.Properties.Property):
                        # print(("%s-%s-%s"%(i,p,q)))
                        print("{\"name\": %s, \"value\": %s}" % (q.Name, q.Value))
                        data_dict.update({"name": q.Name, "value": q.Value})
                        data.append(data_dict.copy())

                response = {"status": 'success',
                            "message": 'Search results returned by Salesforce',
                            "data": data}

            else:

                data = []

                response = {"status": 'success',
                            "message": 'No records found',
                            "data": data}

            pass

        elif emailType.lower() == 'new_prospect_request':

            row = f.ET_DataExtension_Row()
            row.auth_stub = stubObj

            nameOfDE = emailType.lower()
            row.CustomerKey = nameOfDE

            # TODO: get columns in the DE and append to row props
            # row.props = getDeColumns(nameOfDE)
            row.props = ["correlationId", 'EmailAddress', 'SubscriberKey',
                         'emailType', 'uid']

            # correlationId = 'PASS_RESET_TEST_001'

            # set search filter
            row.search_filter = {'Property': 'correlationId',
                                 'SimpleOperator': 'equals', 'Value': correlationId}

            getResponse = row.get()

            data = list()
            data_dict = {}

            records_found = len(getResponse.results)

            if records_found > 0:

                results = getResponse.results
                for i, j in enumerate(results):
                    # print("%s-%s"%(i,j))
                    for p, q in enumerate(j.Properties.Property):
                        # print(("%s-%s-%s"%(i,p,q)))
                        print("{\"name\": %s, \"value\": %s}" % (q.Name, q.Value))
                        data_dict.update({"name": q.Name, "value": q.Value})
                        data.append(data_dict.copy())

                response = {"status": 'success',
                            "message": 'Search results returned by Salesforce',
                            "data": data}

            else:

                data = []

                response = {"status": 'success',
                            "message": 'No records found',
                            "data": data}

            pass

        return response


class check(Resource):
    def get(self):
        return {'status': 'Services are operating normally.'}


api.add_resource(check, '/check')
api.add_resource(sfmc, '/sfmc/sends/<string:emailType>/<string:correlationId>')

if __name__ == '__main__':
    app.run(host='0.0.0.0')  # Turn off for PROD
