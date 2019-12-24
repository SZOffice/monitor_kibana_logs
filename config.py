
webdriver = {
    "chromedriver": "D:\Sycee\monitor_kibana_jobsdb_rc_error\webdrivers\chromedriver.exe",
    "iedriver": "D:\Sycee\monitor_kibana_jobsdb_rc_error\webdrivers\IEDriverServer.exe",
    "ie32driver": "D:\Sycee\monitor_kibana_jobsdb_rc_error\webdrivers\IEDriverServer_x32.exe",
    "firefoxdriver": "D:\Sycee\monitor_kibana_jobsdb_rc_error\webdrivers\geckodriver-0.26-win64.exe",
    "firefox32driver": "D:\Sycee\monitor_kibana_jobsdb_rc_error\webdrivers\geckodriver-0.26-win32.exe"
}

slack = {
    "token": '****',
    "channel": "C80G17TM1"     #rc_monitor: C80G17TM1;     test-api: CAF8QRX4N
}

dic_query = {
    "RC": "'rms.jobsdb.com' OR 'rms.jobsdb.co.id' OR 'rms.jobsdb.co.th'",
    "Login": "'login.mvc' AND ('rms.jobsdb.com' OR 'rms.jobsdb.co.id' OR 'rms.jobsdb.co.th')",
    "EmpJobs": "'empjobs.mvc' AND ('rms.jobsdb.com' OR 'rms.jobsdb.co.id' OR 'rms.jobsdb.co.th')",
    "EmpMyCandidates": "'empmycandidates.mvc' AND ('rms.jobsdb.com' OR 'rms.jobsdb.co.id' OR 'rms.jobsdb.co.th')"
}

email = {'from_addr': 'ifelse01@126.com', 'receivers': ['miragelu@seekasia.com']}

kibana_jobsdb = "http://kibana.jobsdb.com/"
kibana_jobsdb_dashboard_rc_error = "http://kibana.jobsdb.com/_plugin/kibana/app/kibana#/dashboard/dc1cd5f0-60c2-11e9-a745-5d98f3f08996?embed=true&_g=(refreshInterval:(display:Off,pause:!f,value:0),time:(from:now-24h,mode:quick,to:now))&_a=(filters:!(),options:(darkTheme:!f),panels:!((col:1,id:'5e65e9d0-60c2-11e9-a745-5d98f3f08996',panelIndex:2,row:1,size_x:12,size_y:8,type:visualization)),query:(query_string:(analyze_wildcard:!t,query:'*')),title:'Sycee+Dashboard',uiState:())"
kibana_jobsdb_search = "http://kibana.jobsdb.com/_plugin/kibana/api/console/proxy"
kibana_jobsdb_query="http://kibana.jobsdb.com/_plugin/kibana/app/kibana#/discover?_g=(refreshInterval:(display:Off,pause:!f,value:0),time:(from:now-30m,mode:quick,to:now))&_a=(columns:!(_source),index:'logstash-*',interval:auto,query:(query_string:(analyze_wildcard:!t,query:'{0}')),sort:!(expDate,desc))"

baseline_error_rc = 600
baseline_error_action = 30

screentshot_path = r"./logs/screenshots/"
