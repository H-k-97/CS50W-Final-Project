document.addEventListener('DOMContentLoaded',function(){

    load_patients(1)

    document.querySelector('#serbtn').addEventListener('click',function(){
        let ins = document.querySelector('#serach').value
        if (ins != ''){

            serach(1,ins)
        
        let back_main = document.querySelector('.input-group-append')
        let btn = document.createElement('button')
        btn.classList.add('btn')
        btn.classList.add('btn-outline-success')
        btn.innerHTML = 'Back'
        back_main.appendChild(btn)
        btn.addEventListener('click',function(){
            load_patients(1)
            back_main.removeChild(btn)
            document.querySelector('#serach').value = ''
        })

    }

    });


});



function load_patients(num){
    document.querySelector('.main-table').innerHTML = '';
    document.querySelector('.section').innerHTML = '';
    fetch(`/allpatients?page=${num}`,{
        method:'GET',
    })
    .then(res => res.json())
    .then(data => {
        let main = document.querySelector('.main-table')
        let table = document.createElement('table')
        table.classList.add('table')
        table.classList.add('table-striped')
        table.classList.add('table-dark')
        table.classList.add('table-hover')
        main.appendChild(table)
        let thead = document.createElement('thead')
        table.appendChild(thead)
        let tr = document.createElement('tr')
        tr.innerHTML = 
        `
            
            <th scope="col">id</th>
            <th scope="col">Photo</th>
            <th scope="col">Name</th>
            <th scope="col">Gender</th>
            <th scope="col">Blood Type</th>
            <th scope="col">Phone</th>
           
        `
        thead.appendChild(tr)
        data.patients.forEach(data => {

        let thead2 = document.createElement('thead')
        table.appendChild(thead2)
        let tr2 = document.createElement('tr')
        tr2.innerHTML =`
        
        <th scope="row">${data.id}</th>
        <td><img style="border-radius: 50px;" src="${data.image}" alt="patient" width="50" height="50"></td>
        <td><a href="patient/p/${data.id}">${data.name} </a></td>
        <td>${data.gender}</td>
        <td>${data.blood_group}</td>
        <td>${data.phone}</td>
        
        `
        thead2.appendChild(tr2)

        });

        let pag = document.querySelector('.section')
        let ul = document.createElement('ul')
        ul.classList.add('pagination')
        ul.classList.add('justify-content-center')
        pag.appendChild(ul)

        for (num =1 ; num <= data.num_pages ; num++){
        let li = document.createElement('li')
        li.classList.add('page-item')
        li.innerHTML = `<a class="page-link" href="#" onclick="load_patients(${num})">${num}</a>`
        ul.appendChild(li)
        

        }
        
    })

}


function serach(num,ins){
    document.querySelector('.main-table').innerHTML = '';
    document.querySelector('.section').innerHTML = '';



    fetch(`/patient/${ins}`,{ method:'GET' })
    .then(res => res.json())
    .then(data => {
        let main = document.querySelector('.main-table')
        let table = document.createElement('table')
        table.classList.add('table')
        table.classList.add('table-striped')
        table.classList.add('table-dark')
        table.classList.add('table-hover')
        main.appendChild(table)
        let thead = document.createElement('thead')
        table.appendChild(thead)
        let tr = document.createElement('tr')
        tr.innerHTML = 
        `
            <th scope="col">id</th>
            <th scope="col">Photo</th>
            <th scope="col">Name</th>
            <th scope="col">Gender</th>
            <th scope="col">Blood Type</th>
            <th scope="col">Phone</th>
        `
        thead.appendChild(tr)
        data.patients.forEach(data => {

        let thead2 = document.createElement('thead')
        table.appendChild(thead2)
        let tr2 = document.createElement('tr')
        tr2.innerHTML =`
        <th scope="row">${data.id}</th>
        <td><img style="border-radius: 50px;" src="${data.image}" alt="patient" width="50" height="50"></td>
        <td><a href="patient/p/${data.id}">${data.name} </a></td>
        <td>${data.gender}</td>
        <td>${data.blood_group}</td>
        <td>${data.phone}</td>
        
        `
        thead2.appendChild(tr2)

        });


    })
}