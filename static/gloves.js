function f(){
  fetch('/main/api_gl?categorie=glove').then(res=>res.json()).then(json=>{
     
    json.data.forEach(glove => {
        document.getElementById("elmdr1").innerHTML +=
        
        `
        <div class="card">
            <div id="circle"></div>
            <div class="imgBx">
                <img src="${glove.image_url}">
            </div>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <h2 class ="ht">${glove.name}</h2>
            <p class ="pt">${glove.reference} <BR>
                <STRONG>${glove.price}</STRONG>
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






