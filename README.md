## Salesforce Marekting Cloud Data Extension Query API
Enables you to query data extensions in [Salesforce Marketing Cloud](https://www.salesforce.com/products/marketing-cloud/overview/) using any column(s) from the data extension.

BuiltWith:
`
Flask & Swagger UI
`

**Available endpoints:**

## Swagger UI
`http://0.0.0.0:5000/apidocs/`



## Check
`curl 'http://0.0.0.0:5000/check'`

```json
{
    "status": "success",
    "message": "service is operating normally.",
    "data": []
}
```
## Error handler

`curl 'http://0.0.0.0:5000/<random_text>'
`

```json
{"status": "error", "message": "Resource not found. Please check URL. Did you mean "/sfmc/sends/<emailType>/<correlationId> ?", "data": []}
```

## Query Data Extension

`curl 'http://0.0.0.0:5000/sfmc/sends/password_reset/TEST-GUID'`

```json
{
    "status": "success",
    "message": "1 result(s) returned by Salesforce",
    "data": [
        {
            "name": "correlationId",
            "value": "TEST-GUID"
        },
        {
            "name": "EmailAddress",
            "value": "mohapsat@gmail.com"
        },
        {
            "name": "SubscriberKey",
            "value": "001"
        },
        {
            "name": "emailType",
            "value": "password_reset"
        },
        {
            "name": "uid",
            "value": "001"
        },
        {
            "name": "timestamp_DT",
            "value": "12/28/2018 8:28:47 PM"
        }
    ]
}
```