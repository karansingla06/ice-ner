import logging
import ast
import requests
from pydash import get
import datetime
from ice_commons.data.dl.manager import ProjectManager, TestRunsManager, TestDataManager

logger = logging.getLogger(__name__)

project_manager = ProjectManager()
test_data_manager = TestDataManager()
test_run_manager = TestRunsManager()


def get_predict_api_url(req):
    relative_uri = "/api/parse/predict"
    url = req.url
    return url.replace(req.relative_uri, relative_uri)


def validate(serviceid, predict_url):
    test_data = test_data_manager.fetch_by_serviceid(serviceid)
    cases_passed = []
    doc = {'serviceid': serviceid}
    utterances = get(test_data, "utterances", [])
    report_list = []
    for item in utterances:  # test cases one by one
        report = {}
        prediction = {}
        text = get(item, "utterance", "")
        report['utterance'] = text
        test_data_intent = get(item, 'intent', '')
        report['intent'] = test_data_intent
        test_data_tags = get(item, "tags", [])
        report['tags'] = test_data_tags
        response = requests.post(url=predict_url, json={'serviceid': serviceid, 'text': text},
                                 headers={'Content-type': 'application/json'})
        predict_results = ast.literal_eval(response.content)
        entities = get(predict_results, "entities", [])

        predicted_intent = predict_results['intent']['top_intent']
        prediction['intent'] = predicted_intent
        prediction['tags'] = entities

        if str(test_data_intent).upper() == str(predicted_intent).upper():
            res = []
            for tag in test_data_tags:  # tags in single test case
                flag = 0
                for entity in entities:  # check single tag doc presence in predict results
                    if entity['entity'].upper() == tag['entity'].upper():
                        if int(entity['start']) == int(tag['start']) and int(entity['end']) == int(tag['end']):
                            flag = 1
                            break

                res.append(flag)
            logger.info(res)

            if res.count(1) == len(test_data_tags):
                cases_passed.append(1)
                prediction['run_status'] = "pass"
            else:
                cases_passed.append(0)
                prediction['run_status'] = "fail"
        else:
            cases_passed.append(0)
            prediction['run_status'] = "fail"
        report['prediction'] = prediction
        report_list.append(report)

    logger.info(cases_passed)
    total_pass = 0
    if len(cases_passed) != 0:
        total_pass = float((cases_passed.count(1) * 100) / len(cases_passed))
    test_run_doc = {"run_score": total_pass, "run_time": datetime.datetime.now(),
                    "utterances": [x for x in report_list]}
    test_run_manager.update_config_by_service_id(serviceid, test_run_doc)

    query = {
        "serviceid": serviceid
    }
    config = project_manager.find_model(query)
    document = {}
    if config is not None:
        document = {
            "$set": {
                "ner.status": ProjectManager.STATUS_VALIDATED,
                "ner.status_message": "Validation completed successfully.",
                "ir.status": ProjectManager.STATUS_VALIDATED,
                "ir.status_message": "Validation completed successfully."
            }
        }
    project_manager.update_config(query, document)
