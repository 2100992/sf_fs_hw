const p = $('p');
const vdsinaURL = new URL('http://94.103.94.54:8000/words');
const sfSSEURL = new URL('https://sf-pyw.mosyag.in/sse/stream');
const vdsevtSource = new EventSource(vdsinaURL);
const sfevetSource = new EventSource(sfSSEURL);


const header = new Headers({
    'Access-Control-Allow-Credentials': true, 
    'Access-Control-Allow-Origin': '*'
})

sfevetSource.onopen = event => {
    console.log(event)
    }
  
    sfevetSource.onerror = error => {
        sfevetSource.readyState ? console.error("EventSource failed: ", error) : null;
    };
  
    sfevetSource.onmessage = message => {
        console.log(message.data)
  }