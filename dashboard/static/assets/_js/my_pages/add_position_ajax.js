$(document).ready(function () {
    $('#position-form').on('submit', function (e) {
        e.preventDefault();
        $.ajax({
            url: $(this).data('url'),
            type: 'POST',
            data: $(this).serialize(),
            success: function (data) {
                // Add new row to positions table
                let table = $('#positions-table tbody')
                table.append('<tr><td>' + data.position_name + '</td></td>')

                // Add the position to positions select
                let newOption = new Option(data.position_name, data.position_id, true, true);
                $('#positions-select').append(newOption).trigger('change')

                let newCard = `
                    <div class="col-sm-6 col-md-4  col-xl-3 ">
                        <div class="block block-rounded mb-0 h-100">
                            <div class="block-content block-content-full d-flex justify-content-between align-items-center flex-grow-1">
                                <div class="me-3">
                                    <p class="fs-lg fw-bold mb-0">
                                        ${data.position_name}
                                    </p>
                                    <p class="text-muted mb-0">
                                        0 Employee
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                `;
                $('#positions-list').append(newCard)
            },
            error: function (xhr, status, error) {
                alert('Error: ' + error)
            }
        })
    })
})