function f(){
  fetch('/main/api_gl?categorie=helmet').then(res=>res.json()).then(json=>{
     
    json.data.forEach(helmets => {
        document.getElementById("elmdr1").innerHTML +=
        
        `
        <div class="card">
            <div id="circle"></div>
            <div class="imgBx">
                <img src="${helmets.image_url}">
            </div>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <h2 class="ht">${helmets.name}</h2>
            <p class="pt">${helmets.reference} <BR>
                <STRONG>${helmets.price}</STRONG>
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






