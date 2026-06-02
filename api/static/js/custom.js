


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');





let form = document.querySelector(".submit-form")
let input = document.querySelector("#input_value")

let heading = document.querySelector("#main-header")
let bot_container = document.querySelector(".bot-feature-container")
let container = document.querySelector(".container-fluid-2")
let spinner = document.querySelector(".spinner-main")

form.addEventListener("submit", submitForm)




async function postJSON(data) {
    spinner.style.display = "flex"
    const url = "/chat/"
    try {
      const response = await fetch(url, {
        method: "POST", // or 'PUT'
        headers: {
          "Content-Type": "application/json",
          'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(data),
      });
  
      const result = await response.json();




    console.log(result);

    console.log("ADDING MESSAGE TO CHAT");  

      

      

      heading.style.display = "none"
      bot_container.style.display = "none"
      spinner.style.display = "none"
      container.innerHTML += `<div class="chat-container">
      <div class="user-chat-container">
          <div class="user-pic"><i class="fa-solid fa-circle-user"></i></div>
          <div class="user-message">${data.message}</div>
      </div>
      <div class="bot-chat-container">
          <div class="bot-icon"><i class="fa-solid fa-robot"></i></div>
          <div class="bot-response">${result.response}</div>
      </div>
</div>`

    container.scrollTop = container.scrollHeight;

    input.value = "";
    

  
      

    } catch (error) {
  spinner.style.display = "none";

  container.innerHTML += `
  <div class="chat-container">
      <div class="bot-chat-container">
          <div class="bot-icon">
              <i class="fa-solid fa-robot"></i>
          </div>
          <div class="bot-response">
              Sorry, AI service is temporarily unavailable.
          </div>
      </div>
  </div>`;

  console.error("Error:", error);
}
}

function submitForm(e){
    e.preventDefault()
    let message = input.value
    const data = { message: message };
    postJSON(data);

}