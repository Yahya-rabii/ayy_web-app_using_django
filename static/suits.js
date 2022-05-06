function f(){
  fetch('/main/api_gl?categorie=suit').then(res=>res.json()).then(json=>{
     
    json.data.forEach(suits => {
        document.getElementById("elmdr1").innerHTML +=
        
        `
        <div class="card">
            <div id="circle"></div>
            <div class="imgBx">
                <img src="${suits.image_url}">
            </div>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <h2>${suits.name}</h2>
            <p>${suits.reference} <BR>
                <STRONG>${suits.price}</STRONG>
            </p>
            <div class="content">
                <a href="/main/mysite">BUY IT</a>
            </div>
        </div>
        `
    });
  })
}

window.addEventListener("load",f)






