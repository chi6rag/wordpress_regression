from appium import webdriver


def before_all(context):
    desired_capabilities = {}
    desired_capabilities['platformName'] = 'Android'
    desired_capabilities['automationName'] = 'Appium'
    desired_capabilities['platformVersion'] = '5.1'
    desired_capabilities['deviceName'] = 'Nexus 5'
    desired_capabilities['app'] = '/Users/chi6rag/workspace/talks/pydelhi_05032016/spikes/wordpress_regression/apks/wordpress_android.apk'
    context.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)


def before_scenario(context, scenario):
    context.driver.reset()


def after_all(context):
    print("Executing after all")
    context.driver.close_app
