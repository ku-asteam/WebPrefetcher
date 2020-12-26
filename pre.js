/* Functions */
const delay = ms => new Promise(res => setTimeout(res, ms));

async function navigate_with_target(driver, url, target) {
  // Initialize the target window
  await driver.executeScript(`window.open("about:blank", "${target}");`);
  if (target == '_blank') { // target == '_self' or '_blank'
    windows = await driver.getAllWindowHandles();
    await driver.switchTo().window(windows[windows.length -1]);
  }

  // Navigate to the URL and return the window handle in control
  await driver.executeScript(`window.location.href = "${url}";`);
  return await driver.getWindowHandle();
}

/* Main part */
module.exports = async function(context, commands) {  
  // context: options, log, index, storageManager, selenium.webdriver, selenium.driver
  // commands: navigate(URL), measure.start(URL), measure.start(URL,alias), measure.start(), measure.start(alias), measure.stop()
  const jsonObj = JSON.parse(context.options.my.param);

  // Start this prescript
  context.log.info('Starting the preScript of pre.js');

  // Do prefetching by the specified type
  if (jsonObj.type == 'none') {
    context.log.info('No prefetching specified; Skip this prescript');
  } else if (jsonObj.type == 'prefetch') {  // prefetch(not enough time) & predict (not always right answer)
    context.log.info('Prefetch lisetd URLs as the given scenario');

    // Load inputs
    var urls = jsonObj.predict_urls;
    var timeForPrefetch = jsonObj.t_prefetch;             // in ms
    var timeForPredict = jsonObj.t_predict;               // in ms
    var totalWaitTime = timeForPrefetch - timeForPredict; // in ms
    context.log.info('Inputs loaded: ' + urls.length + ' URLs [' + urls + '] (' + timeForPrefetch + ' - ' + timeForPredict + ' = ' + totalWaitTime + 'ms)');

    // Initialize the main window
    const driver = context.selenium.driver;
    mainWindow = await navigate_with_target(driver, 'about:blank', '_self'); // main window
    baseUri = await driver.executeScript(`return window.document.baseURI;`);
    context.log.info('Main window: ' + baseUri + ' (' + mainWindow + ')');

    // Navigate to each URL in the pre-specified list
    var start = new Date().getTime();
    for (var i=0; i < urls.length; i++) {
      ret = await navigate_with_target(driver, urls[i], '_blank');
      //baseUri = await driver.executeScript(`return window.document.baseURI;`);
      //context.log.info('Window ' + (i+1) + ': ' + baseUri + ' (' + ret + ')');
    }
    
    // Wait and clear all windows other than the main window
    while ( (new Date().getTime() - start) < totalWaitTime) {;}
    windows = await driver.getAllWindowHandles();
    for (var i=0; i < windows.length; i++) {
      if (windows[i] == mainWindow) {
        continue;
      }
      await driver.switchTo().window(windows[i]);
      await driver.close();
    }
    await driver.switchTo().window(mainWindow);
    context.log.info('After prefetching (partial & predict): ' + (new Date().getTime() - start) + ' ms');
  } else if(jsonObj.type == 'prefetchcorrect'){ // prefetch (not enough time) & correct (always right answer)
    context.log.info('Prefetch only the answer URL within the limited time as the given scenario');

    // Load inputs
    var urls = new Array(jsonObj.answer_url);
    var timeForPrefetch = jsonObj.t_prefetch;             // in ms
    var timeForPredict = jsonObj.t_predict;               // in ms
    var totalWaitTime = timeForPrefetch - timeForPredict; // in ms
    context.log.info('Inputs loaded: ' + urls.length + ' URLs [' + urls + '] (' + timeForPrefetch + ' - ' + timeForPredict + ' = ' + totalWaitTime + 'ms)');

    // Initialize the main window
    const driver = context.selenium.driver;
    mainWindow = await navigate_with_target(driver, 'about:blank', '_self'); // main window
    baseUri = await driver.executeScript(`return window.document.baseURI;`);
    context.log.info('Main window: ' + baseUri + ' (' + mainWindow + ')');

    // Navigate to each URL in the pre-specified list
    var start = new Date().getTime();
    for (var i=0; i < urls.length; i++) {
      ret = await navigate_with_target(driver, urls[i], '_blank');
      //baseUri = await driver.executeScript(`return window.document.baseURI;`);
      //context.log.info('Window ' + (i+1) + ': ' + baseUri + ' (' + ret + ')');
    }
    
    // Wait and clear all windows other than the main window
    while ( (new Date().getTime() - start) < totalWaitTime) {;}
    windows = await driver.getAllWindowHandles();
    for (var i=0; i < windows.length; i++) {
      if (windows[i] == mainWindow) {
        continue;
      }
      await driver.switchTo().window(windows[i]);
      await driver.close();
    }
    await driver.switchTo().window(mainWindow);
    context.log.info('After prefetching (partial & correct): ' + (new Date().getTime() - start) + ' ms');
  } else if (jsonObj.type == 'complete') {  // complete (always enough time) & complete (always right answer)
    context.log.info('Prefetch the correct URL only');

    // Navigate to the answer URL and wait until completed
    const driver = context.selenium.driver;
    mainWindow = await navigate_with_target(driver, jsonObj.answer_url, '_self'); // main window
    var initialized = false;
    while (!initialized) {
      ret = await driver.executeScript(`return [window.document.baseURI, window.document.body, window.document.readyState];`);
      if (ret[0] != 'about:blank' && ret[1] != null && ret[2] == 'complete') {
        initialized = true;
      }
    }
    context.log.info('Navigation completed: ' + ret[0]);
  } else {
    context.log.info('ERROR: invalid prefetching type');
  }

  // Finish this prescript
  context.log.info('Finishing the preScript of pre.js');
}
