from behave import given, when, then
import requests


@given(u'I set base REST API url and headers correctly')
def setupClient(context):
    context.baseURL = context.config.userdata.get("baseURL", "url")
    context.headers = {"token": context.config.userdata.get("accessToken", "token"), "content-type": "application/json"}


@given(u'I Set posts api endpoint to tatics endpoint')
def setTaticsURL(context):
    context.url = "adaccount/" + context.config.userdata.get("AccountId", "0") + "/tactic"


@when(u'set the body of request to contents of the {fileName}')
def setBodyFromFile(context, fileName):
    f = open("./data/" + fileName, "r")
    context.body = f.read()


@when(u'perfrom post')
def PerfromPost(context):
    context.resp = requests.post(context.baseURL+context.url, json=context.body, headers=context.headers)
    print(context.resp.json())


@then(u'I receive valid HTTP response code as {code}')
def validateResponseCode(context, code):
    assert str(context.resp.status_code) == code


@then(u'validate error is {errCode}')
def validateResponseErrorCode(context, errCode):
    assert str(context.resp.json()["error"]) == errCode


@then(u'Extract Message')
def step_impl(context):
    print(context.resp.json()["message"])
