from behave import given, when, then
import requests
import helper.rw_csv as csv
from helper.log import custom_logger as log

log = log()
log.info("*******************************************NEW RUN*********************************************************")



@given(u'I set base REST API url and headers correctly')
def setup_baseurl(context):
    context.baseURL = context.config.userdata.get("base_url", "url")
    context.headers = {"token": context.config.userdata.get("access_token", "token"),
                       "content-type": "application/json"}
    context.account_id = context.config.userdata.get("account_id", "1001")
    log.info(f"Base URL set to : {context.baseURL}")
    log.info(f"Headers set to : {context.headers}")
    log.info(f"account_id set to : {context.account_id}")


@given(u'Execute test case {testcase_id}')
def get_testcase_data(context, testcase_id):
    context.testcase_id = testcase_id
    context.row = csv.read_csv(testcase_id, key="row")
    try:
        # Check if CSV file returned any error
        if context.row["error"]: raise context.row["error_msg"]
    except Exception as e:
        # If the error is not raised for "error" key not in row (context.row["error"]) log and raise error message
        if "error" not in str(e):
            log.exception(e)
            raise e
    log.info(f'<{context.testcase_id}> - CSV File row data: {context.row}')


@given(u'I Set posts api endpoint to Step 1 endpoint')
def step1_endpoint(context):
    context.endpoint = f"adaccount/{context.account_id}/tactic"
    log.info(f"<{context.testcase_id}> - Endpoint set to : {context.endpoint}")


@when(u'set the body of request')
def set_body(context):
    # Get body code from CSV file row
    context.body = context.row["Test Data"]
    log.info(f"<{context.testcase_id}> - Body set to: {context.body}")
    # log.debug(f"context.body :type{type(context.body)}, plain {context.body}, str:{str(context.body)}")
    # if context.body == "": raise Exception("There is no data in body")


@when(u'perfrom post')
def perform_post(context):
    log.info(f"<{context.testcase_id}> - Performing post")
    context.response = requests.post(context.baseURL + context.endpoint, data=context.body, headers=context.headers)
    log.info(f'<{context.testcase_id}> - POST Response: {context.response.json()}')



@then(u'Validate HTTP response code')
def validate_response_code(context):
    # Get response code from CSV file
    context.response_code = context.row["Expected status code"]
    # csv.read_csv(context.testcase_id, key="Expected status code")
    log.info(f"<{context.testcase_id}> - Actule Response Code: {context.response.status_code}")
    log.info(f"<{context.testcase_id}> - Expected Response Code: {context.response_code}")
    assert str(context.response.status_code) == context.response_code, \
        log.exception(f"<{context.testcase_id}> - Actule Response Code({context.response.status_code})does not "
                      f"matches Expected Response Code({context.response_code})")


@then(u'Validate error')
def validate_response_error(context):
    # Get err_code from CSV file
    err_code = context.row["Error"]
    context.a_err_code = context.response.json()["error"]
    # csv.read_csv(context.testcase_id, key="Error")
    log.info(f'<{context.testcase_id}> - Actule Error Code: {context.a_err_code}')
    log.info(f'<{context.testcase_id}> - Expected Error Code: {err_code}')
    assert str(context.response.json()["error"]).lower() == err_code.lower(), \
        log.exception(
            f'<{context.testcase_id}> - Actule Error Code ({context.response.json()["error"]}'
            f' does not matches Expected Error Code ({err_code})')


@then(u'Extract tactic Id')
def get_tactic_id(context):
    context.tactic_id = context.response.json()["data"]["id"]
    print(f'<{context.testcase_id}> - Tactic Id: {context.tactic_id}')
    log.info(f'<{context.testcase_id}> - Tactic Id: {context.tactic_id}')


@then(u'validate if is status {status}')
def validate_status(context, status):
    context.status = context.response.json()["data"]["status"]
    log.info(f'<{context.testcase_id}> - Tactic status: {context.status}')
    assert str(context.status).lower() == status.lower(), \
        log.exception(
            f'<{context.testcase_id}> - Actule Tactic status ({context.status}'
            f' does not matches Expected Error Code ({status})')


@then(u'delete the tactic')
def del_tactic(context):
    if not context.a_err_code:
        get_tactic_id(context)
        # context.tactic_id = context.response.json()["data"]["id"]
        context.del_response = requests.delete(
            context.baseURL + f"adaccount/{context.account_id}/tactic/{context.tactic_id}", headers=context.headers)
        log.info(f'<{context.testcase_id}> - DELETE Response: {context.del_response.json()}')
    else:
        log.info(f'<{context.testcase_id}> - DELETE Response: Tactic was not created.')


@then(u'Validate if  "date_schedule" parameter accepts {date_schedule}')
def validate_date_schedule(context, date_schedule):
    context.date_schedule = context.response.json()["data"]["tactic_json"]["date_schedule"]
    log.info(f'<{context.testcase_id}> - date_schedule status: {context.date_schedule}')
    assert str(context.date_schedule).lower() == date_schedule.lower(), \
        log.exception(
            f'<{context.testcase_id}> - Actual Tactic date_schedule ({context.date_schedule}'
            f' does not matches Expected Error Code ({date_schedule})')
