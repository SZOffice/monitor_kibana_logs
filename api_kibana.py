# -*- coding: utf-8 -*-
import json, requests, time, urllib
import config
import helpers.logger_helper as logger_helper
logger = logger_helper.mylog('api_kibana').getlog()

def search_kibana(querystring = None, post_data = None):
    search_url = config.kibana_jobsdb_search

    #print(data)
    try:
        header = {
            "kbn-name": "kbn-name",
            'kbn-version': "5.3.2",
        }
        res = requests.post(url=search_url, params=querystring, data=post_data, headers = header, verify = False)
        
        if res.status_code == 200:
            list_res = json.loads(res.text)
            #logger.info(list_res)
            return list_res
        else:
            error_msg = "JobsDB Kibana search response failed, response code = %s method: %s " %(res.status_code, search_url)        
            logger.info(error_msg)
    except Exception as ex:
        logger.info('***** Failed to call kibana search {0}!'.format(search_url), ex)
    return None

def get_report():
    report_result = {
        "RC": [], "Login":[], "EmpJobs": [], "EmpMyCandidates": []
    }
    pay_load = '''
{
    "size": 0,
    "query": {
        "query_string": {
            "query": "%s",
            "fields": ["URL"]
        }
    },
    "aggs": {
        "group_by_expDate": {
        	"filter": {
        		"range": {
        			"expDate": {
        				"from": "now-30m"
        			}
        		}
        	},
            "aggs": {
                "all_tags": {
                    "terms": {
                        "field": "loggingCountry.raw"
                    }
                }
            }
        }
    }
}'''
    dic_query = config.dic_query
    for key in dic_query.keys():
        #print(pay_load % (query))
        logger.info("get for: %s" % dic_query[key])
        response_data = search_kibana({"uri":"logstash-%2A/_search"}, pay_load % (dic_query[key]))
        if response_data != None:
            report_result[key] = response_data["aggregations"]["group_by_expDate"]["all_tags"]["buckets"]
        else:            
            logger.info("None")
    logger.info(report_result)
    return report_result


if __name__ == "__main__":
    pay_load = '''
{
    "size": 0,
    "query": {
        "query_string": {
            "query": "empjobs.mvc AND rms.jobsdb.co.th",
            "fields": ["URL"]
        }
    },
    "aggs": {
        "group_by_expDate": {
        	"filter": {
        		"range": {
        			"expDate": {
        				"from": "now-2h"
        			}
        		}
        	},
            "aggs": {
                "all_tags": {
                    "terms": {
                        "field": "loggingCountry.raw"
                    }
                }
            }
        }
    }
}'''
    #response_data = search_kibana({"uri":"logstash-%2A/_search"}, pay_load)
    #if response_data != None:
        #logger.info(response_data["aggregations"]["group_by_expDate"]["all_tags"]["buckets"])

    #logger.info(get_report())
    result = {'RC': [{'key': 'HK', 'doc_count': 453}, {'key': 'TH', 'doc_count': 449}, {'key': 'SA_JobSearchService', 'doc_count': 1}], 'Login': [{'key': 'HK', 'doc_count': 16}, {'key': 'TH', 'doc_count': 5}], 'EmpJobs': [{'key': 'HK', 'doc_count': 8}, {'key': 'TH', 'doc_count': 1}], 'EmpMyCandidates': [{'key': 'HK', 'doc_count': 5}, {'key': 'TH', 'doc_count': 5}]}
    for key in result.keys():
        print(key)
        for record in result[key]:
            if record["doc_count"] > 20:
                print(record["key"])
                print(record["doc_count"])