function f(){
  fetch('/main/api_gl?categorie=boot').then(res=>res.json()).then(json=>{
     
    json.data.forEach(boots => {
        document.getElementById("elmdr1").innerHTML +=
        
        `
        <div class="card">
            <div id="circle"></div>
            <div class="imgBx">
                <img src="${boots.image_url}">
            </div>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <h2 class="ht">${boots.name}</h2>
            <p class="pt">${boots.reference} <BR>
                <STRONG>${boots.price}</STRONG>
            </p>
            <div class="contentx">
                <a href="/main/mysite">BUY IT</a>
            </div>
        </div>
        `
    });
  })
}

window.addEventListener("load",f)






