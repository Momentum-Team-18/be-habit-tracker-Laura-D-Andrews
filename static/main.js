let submitRecord = document.querySelector('#submitRecord')
let recordNumber = document.querySelector('#recordNumber')


submitRecord.addEventListener('click', (event) => {
    recordAdd = 1
    recordNumber.value+=recordAdd
    console.log(recordAdd)
})