  $(document).ready(function() {
        $('#position-form').on('submit', function(e) {
            e.preventDefault();
            $.ajax({
                url: $(this).data('url'),
                type: 'POST',
                data: $(this).serialize(),
                success: function(data) {
                    // Add new row to positions table
                    let table = $('#positions-table tbody')
                    table.append('<tr><td>' + data.position_name + '</td></td>')

                    // Add the position to positions select
                    let newOption = new Option(data.position_name, data.position_id, true, true);
                    $('#positions-select').append(newOption).trigger('change')
                },
                error: function(xhr, status, error) {
                    alert('Error: ' + error)
                }
            })
        })
    })