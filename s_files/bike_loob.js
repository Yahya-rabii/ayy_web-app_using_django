function f(){
  fetch('/main/api_gl?categorie=bikelube').then(res=>res.json()).then(json=>{
     
    json.data.forEach(bl => {
        document.getElementById("elmdr1").innerHTML +=
        
        `
        <div class="card">
            <div id="circle"></div>
            <div class="imgBx">
                <img src="${bl.image_url}">
            </div>
            <br>
            <br>
            <br>

            <h2 class="ht">${bl.name}</h2>
            <p class ="pt">${bl.reference} <BR>

                <STRONG>${bl.price}</STRONG>
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






