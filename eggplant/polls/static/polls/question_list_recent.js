// Display all poll questions or only the recent ones

// This is the script tag used in the html file.
// <!--The script is not working.-->
// <!--script defer src="{% static 'polls/question_list_recent.js' %}"-->
// <!--/script-->

// We make a POST request using the fetch() API, setting
// the FormData object as the request body.
// the post and the data is correct,
// the data is not displayed or returned correctly.
// But the button can work properly.
console.log("Display all question or recent ones only");
const form = document.querySelector("#id_recent_form");
const submitBtn = document.querySelector("#id_recent_btn");
const recentBox = document.querySelector("#id_recent_box");

const form_handler = "/polls/question_list_recent/";

// post data of the form
async function post_data(){
  // associate the FormData object with the form element
  const form_data = new FormData(form);
  const body = { method: "POST", body: "form_data"};
  const request = new Request(form_handler, body);
  try {
    const response = await fetch (request);
    console.log(await response);
  } catch(e) {
    console.error(e);
  }
}
// Take over form submission
// The first time the checkbox is clicked,
// display recent can work.
// After that its value always remains at "on".
form.addEventListener("change", (event) => {
  //event.preventDefault();
  data = event.formData;
  console.log(data);
  //post_data();
  form.requestSubmit(submitBtn);
});

// Using another method: HTMLFormElement.requestSubmit
// form.addEventListener("change", (event)=>{
//   form.requestSubmit();
// });

// Using formdata event
/****************
form.addEventListener("submit", (event)=>{
  // on form submission, prevent default
  event.preventDefault();

  // Do something before the actual submission
  console.log("formdata fired");
  //const data = event.formData;
  const data = event.FormData;
  console.log(data);
  //for (const value of data.values()) {
    //console.log(value);
  //}
  
  // Submit the data via fetch
  const body = { method: "POST", body: "form_data"};
  const request = new Request(form_handler, body);
  //fetch(request);
  form.requestSubmit(submitBtn);
});
***********************************/