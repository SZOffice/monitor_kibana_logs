# -*- coding: utf-8 -*-
  
from selenium import webdriver
import time, os

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
DesiredCapabilities.INTERNETEXPLORER["ignoreProtectedModeSettings"] = True
  
def capture(config, url, pix_w=1200, pix_h=1500, output_dir=".", save_fn="capture"):
  chromedriver = config["chromedriver"]
  iedriver = config["iedriver"]
  ie32driver = config["ie32driver"]
  firefoxdriver = config["firefoxdriver"]
  firefox32driver = config["firefox32driver"]
  os.environ["webdriver.chrome.driver"] = chromedriver
  os.environ["webdriver.ie.driver"] = ie32driver#iedriver
  os.environ["webdriver.firefox.driver"] = firefoxdriver
  
  #browser = webdriver.Chrome(chromedriver) # Get local session of chrome
  #browser = webdriver.Ie(iedriver) # Get local session of ie
  print(firefoxdriver)
  browser = webdriver.Firefox(executable_path=firefoxdriver)
  browser.set_window_size(pix_w, pix_h)
  browser.get(url) # Load page
 
  browser.execute_script("""
    (function () {
      var y = 0;
      var step = 100;
      window.scroll(0, 0);
  
      function f() {
        if (y < document.body.scrollHeight) {
          y += step;
          window.scroll(0, y);
          setTimeout(f, 50);
        } else {
          window.scroll(0, 0);
          document.title += "scroll-done";
        }
      }
  
      setTimeout(f, 1000*20);
    })();
  """)
  
  for i in range(30):
    if "scroll-done" in browser.title:
      break
    time.sleep(1)
    
  save_path = '%s/%s.png' % (output_dir, save_fn) 
  browser.save_screenshot(save_path)
  browser.close()
  
if __name__ == "__main__":
  
  webdriver = {
    "chromedriver": "D:\Sycee\monitor_kibana_jobsdb_rc_error\webdrivers\chromedriver.exe",
    "iedriver": "D:\Sycee\monitor_kibana_jobsdb_rc_error\webdrivers\IEDriverServer.exe",
    "ie32driver": "D:\Sycee\monitor_kibana_jobsdb_rc_error\webdrivers\IEDriverServer_x32.exe",
    "firefoxdriver": "D:\Sycee\monitor_kibana_jobsdb_rc_error\webdrivers\geckodriver.exe"  
  }
  capture(webdriver, "http://kibana.jobsdb.com/_plugin/kibana/app/kibana#/dashboard/dc1cd5f0-60c2-11e9-a745-5d98f3f08996?embed=true&_g=(refreshInterval:(display:Off,pause:!f,value:0),time:(from:now-7d,mode:quick,to:now))&_a=(filters:!(),options:(darkTheme:!f),panels:!((col:1,id:'5e65e9d0-60c2-11e9-a745-5d98f3f08996',panelIndex:2,row:1,size_x:12,size_y:8,type:visualization)),query:(query_string:(analyze_wildcard:!t,query:'*')),title:'Sycee%20Dashboard',uiState:())", output_dir="./logs/screenshots")