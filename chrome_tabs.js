#!/usr/bin/env osascript -l JavaScript

const app = Application.currentApplication()
app.includeStandardAdditions = true

const folder = app.chooseFolder({
    withPrompt: "Select Save Location",
    defaultLocation: Path("/Users/tandav/Desktop"),
})

console.log(folder)
//document
// Result: Path("/Users/yourUserName/Documents/ImportantDoc.pages")


//console.log()

//const chrome = Application('Google Chrome')
//chrome.chooseFolder()
//const currentTab = chrome.windows[0].activeTab()
//console.log(currentTab.url())
//console.log(currentTab.title())


// console.log(chrome.windows.length)
// for (let i = 0; i < chrome.windows.length; i++) {
//     console.log(i)
//     let tab = chrome.windows[i].activeTab()
//     console.log(tab.title())
//     // console.log(chrome.windows[i].activeTab())
// }

// chrome.windows.forEach(x => console.log(x.activeTab().title()))

// currentTab.execute({javascript: 'alert("Hello")'})

// run from Terminal: 
// osascript -l JavaScript myscript.js


// let safari = Application('Google Chrome')


// const RESET = '\033[0m'
// const GREEN = '\033[32;1m'
// const URL = '\033[34;2m'
// const RED = '\033[31;1m'

// let tabs = ''


// for (let i = 0; i < safari.windows.length; i++) {
//     console.log(RED, '================ ' + 'window ' + i +  ' ================')
//     tabs += '<h1>Window ' + i + '</h1>\n'
//     tabs += '<ul>\n'
//     for (let j = 0; j < safari.windows[i].tabs.length; j++) {
//         let tab_name = safari.windows[i].tabs[j].name()
//         let tab_url  = safari.windows[i].tabs[j].url()
//         let tab = ''
//         tab += '<li>'
//         hostname = /^(?:\w+\:\/\/)?([^\/]+)(.*)$/.exec(tab_url)[1] // todo: make it more beautiful 
//         tab += '<img align="center" src="https://s2.googleusercontent.com/s2/favicons?domain=' + hostname + '">'
//         tab += '<a href="' + tab_url + '">'
//         tab += tab_name
//         tab += '</a></li>\n'
//         tabs += tab
//         console.log(GREEN, tab_name)
//         console.log(URL, tab_url)
//         console.log(RESET)
//     }
//     tabs += '</ul>\n\n\n'
// }


// var app = Application.currentApplication()
// app.includeStandardAdditions = true

// fileStr = $.NSString.alloc.initWithUTF8String(tabs)
// fileStr.writeToFileAtomicallyEncodingError( '/Users/tandav/Desktop/tabs.html', true, $.NSUTF8StringEncoding, $() )

// //app.doShellScript('echo' + tabs +  '> /Users/tandav/Desktop/1.txt')
// //app.displayAlert(tabs)
// //alert(tabs)
