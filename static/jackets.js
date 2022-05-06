function f(){
  fetch('/main/api_gl?categorie=jacket').then(res=>res.json()).then(json=>{
     
    json.data.forEach(jackets => {
        document.getElementById("elmdr1").innerHTML +=
        
        `
        <div class="card">
            <div id="circle"></div>
            <div class="imgBx">
                <img src="${jackets.image_url}">
            </div>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <h2>${jackets.name}</h2>
            <p>${jackets.reference} <BR>
                <STRONG>${jackets.price}</STRONG>
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






