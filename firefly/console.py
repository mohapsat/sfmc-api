import FuelSDK as f
import os
import ssl


if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

debug = False
stubObj = f.ET_Client(False, debug)

row = f.ET_DataExtension_Row()
row.auth_stub = stubObj

# loop over DE list
# deList = list()
# nameOfDE = '_SENT'
nameOfDE = 'password_reset'
# nameOfDE = 'DE_password_changed'
# nameOfDE = 'DE_order_confirm'
# nameOfDE = 'DE_password_reset'


row.CustomerKey = nameOfDE

# TODO: get columns in the DE and append to row props
# row.props = getDeColumns(nameOfDE)
row.props = ["correlationId", 'EmailAddress']

# correlationID from method param
correlationId = 'PASS_RESET_TEST_001'
# correlationId = 'correlationID_test_009'  # pass changed

# EmailAddress = 'kurt.becker@pinpoint-corp.com'

# set search filter
row.search_filter = {'Property': 'correlationId',
                     'SimpleOperator': 'equals', 'Value': correlationId}

getResponse = row.get()

print('Retrieve Status: ' + str(getResponse.status))
print('Code: ' + str(getResponse.code))
print('Message: ' + str(getResponse.message))
print('MoreResults: ' + str(getResponse.more_results))
print('RequestID: ' + str(getResponse.request_id))
print('Results Length: ' + str(len(getResponse.results)))
print('Results: ' + str(getResponse.results))

