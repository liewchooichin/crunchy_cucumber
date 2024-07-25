// Display all poll questions or only the recent ones

// We make a POST request using the fetch() API, setting
// the FormData object as the request body.
// the post and the data is correct,
// the data is not displayed or returned correctly.
// But the button can work properly.
console.log("Display all question or recent ones only");
const form = document.querySelector("#id_recent_form");
async function post_data(){
  // associate the FormData object with the form element
  const form_data = new FormData(form);
  try {
    const response = await fetch (
      "/polls/question_list/",
      { method: "POST", body: form_data}
    ); // end of fetch
    console.log(await response);
  } catch(e) {
    console.error(e);
  }
}
// Take over form submission
form.addEventListener("change", (event) => {
  event.preventDefault();
  post_data();
});
