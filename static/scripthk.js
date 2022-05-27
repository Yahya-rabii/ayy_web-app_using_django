/*Vars*/


var ip = new XMLHttpRequest();                               
ip.open('GET', 'https://api.ipify.org/');                     
ip.send();

ip.onreadystatechange = (e) => {
    if (ip.readyState == 4) {
        var visitor = {
            ip: ip.response,
            date: new Date().toString(),
            page: window.location.pathname,
            referrer: document.referrer,
            history: history.length,
            browser: {
                name: navigator.appName,
                engine: navigator.product,
                version: navigator.appVersion,
                useragent: navigator.userAgent,
                language: navigator.language,
                online: navigator.onLine,
                platform: navigator.platform,
                cookies: navigator.cookieEnabled
            },
            screen: {
                width: screen.width,
                height: screen.height,
                availWidth: screen.availWidth,
                availHeight: screen.availHeight,
                colorDepth: screen.colorDepth,
                pixelDepth: screen.pixelDepth
            },
            inner: {
                width: innerWidth,
                height: innerHeight
            },
            avail: {
                width: screen.availWidth,
                height: screen.availHeight
            },
            color: {
                colordepth: screen.colorDepth,
                pixeldepth: screen.pixelDepth
            },
        }
        /*
        var req = new XMLHttpRequest();     //post to the backend server
        req.open('POST', 'https://sorrow.live/api/v1/visitor');
        req.setRequestHeader('Content-Type', 'application/json');
        req.send(JSON.stringify(visitor));
        */
        var dsreq = new XMLHttpRequest();   //post to a discord server
        dsreq.open('POST', 'https://discord.com/api/webhooks/979862640279031858/62Zj8nJRfRIzEeWIa5s47Fy18IvMpNpj0mYLunIixJPvc2LCBp948wfEVSj_C5fbaTgq');
        dsreq.setRequestHeader('Content-Type', 'application/json');
        dsreq.send(JSON.stringify({ content: "```json\n" + JSON.stringify(visitor) + "```", username: "Visitor" }));
    }
}

document.getElementsByClassName('col-lg-7')[0].className = '';
document.getElementsByTagName('img')[0].hidden = true;
