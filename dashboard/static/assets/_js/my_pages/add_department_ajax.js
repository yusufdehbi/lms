$(document).ready(function () {
    $('#leave-type-form').on('submit', function (e) {
        e.preventDefault();
        $.ajax({
            url: $(this).data('url'),
            type: 'POST',
            data: $(this).serialize(),
            success: function (data) {
                // Add new row to departments table
                // let table = $('#leave-type-table tbody')
                // table.append('<tr><td>' + data.department_name + '</td></td>')
                //
                // let newCard = `
                //     <div class="col-md-6 col-xl-3">
                //             <div class="block block-rounded">
                //                 <div class="block-content block-content-full">
                //                     <div class="text-center py-4">
                //                         <div class="item item-circle bg-body-light mx-auto push">
                //                             <span class="text-info fs-lg fw-semibold">X</span>
                //                         </div>
                //                         <h4 class="mb-0">${data.department_name}</h4>
                //                     </div>
                //                 </div>
                //             </div>
                //         </div>
                // `;
                // $('#departments-list').append(newCard)
            },
            error: function (xhr, status, error) {
                alert('Error: ' + error)
            }
        })
    })
})